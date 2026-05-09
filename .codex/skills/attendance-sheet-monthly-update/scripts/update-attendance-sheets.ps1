[CmdletBinding()]
param(
    [Parameter(Mandatory = $true)]
    [string]$FolderPath,

    [Parameter(Mandatory = $true)]
    [int]$Year,

    [Parameter(Mandatory = $true)]
    [int]$FromMonth,

    [Parameter(Mandatory = $true)]
    [int]$ToMonth,

    [string]$RosterChangesJson
)

Set-StrictMode -Version Latest
$ErrorActionPreference = "Stop"

function Get-TrimmedText {
    param(
        [Parameter(Mandatory = $true)]
        $Cell
    )

    return ([string]$Cell.Text).Trim()
}

function Get-TitleSuffix {
    return ([string][char]0x7B7E) + ([string][char]0x5230) + ([string][char]0x8868)
}

function Get-MonthToken {
    param(
        [Parameter(Mandatory = $true)]
        [int]$YearValue,
        [Parameter(Mandatory = $true)]
        [int]$MonthValue
    )

    $yearChar = [string][char]0x5E74
    $monthChar = [string][char]0x6708
    return "{0}{1}{2}{3}{4}" -f $YearValue, $yearChar, $MonthValue, $monthChar, (Get-TitleSuffix)
}

function Find-TitleCell {
    param(
        [Parameter(Mandatory = $true)]
        $Worksheet,
        [Parameter(Mandatory = $true)]
        [string]$FromText
    )

    $usedRange = $Worksheet.UsedRange
    $maxRows = [Math]::Min($usedRange.Rows.Count, 5)
    $maxCols = [Math]::Min($usedRange.Columns.Count, 5)

    for ($row = 1; $row -le $maxRows; $row++) {
        for ($col = 1; $col -le $maxCols; $col++) {
            $cell = $Worksheet.Cells.Item($row, $col)
            $text = Get-TrimmedText -Cell $cell
            if ($text -and $text.Contains($FromText)) {
                return $cell
            }
        }
    }

    throw "Title cell containing '$FromText' was not found."
}

function Find-FooterRow {
    param(
        [Parameter(Mandatory = $true)]
        $Worksheet
    )

    $usedRange = $Worksheet.UsedRange
    for ($row = 6; $row -le $usedRange.Rows.Count; $row++) {
        $serialText = Get-TrimmedText -Cell $Worksheet.Cells.Item($row, 2)
        if (-not $serialText) {
            continue
        }
        $serialNumber = 0
        if (-not [int]::TryParse($serialText, [ref]$serialNumber)) {
            return $row
        }
    }

    throw "Footer row was not found."
}

function Get-CurrentNames {
    param(
        [Parameter(Mandatory = $true)]
        $Worksheet,
        [Parameter(Mandatory = $true)]
        [int]$StartRow,
        [Parameter(Mandatory = $true)]
        [int]$EndRow,
        [Parameter(Mandatory = $true)]
        [int]$NameColumn
    )

    $names = New-Object 'System.Collections.Generic.List[string]'
    for ($row = $StartRow; $row -le $EndRow; $row++) {
        $name = Get-TrimmedText -Cell $Worksheet.Cells.Item($row, $NameColumn)
        if ($name) {
            [void]$names.Add($name)
        }
    }
    return $names
}

function Normalize-StringArray {
    param($Value)

    if ($null -eq $Value) {
        return @()
    }

    if ($Value -is [string]) {
        $trimmed = $Value.Trim()
        if ($trimmed) {
            return @($trimmed)
        }
        return @()
    }

    $result = @()
    foreach ($item in $Value) {
        if ($null -eq $item) {
            continue
        }
        $trimmed = ([string]$item).Trim()
        if ($trimmed) {
            $result += $trimmed
        }
    }
    return $result
}

function ConvertTo-Hashtable {
    param($Value)

    if ($null -eq $Value) {
        return $null
    }

    if ($Value -is [System.Collections.IDictionary]) {
        $result = @{}
        foreach ($key in $Value.Keys) {
            $result[[string]$key] = ConvertTo-Hashtable -Value $Value[$key]
        }
        return $result
    }

    if ($Value -is [System.Management.Automation.PSCustomObject]) {
        $result = @{}
        foreach ($property in $Value.PSObject.Properties) {
            $result[$property.Name] = ConvertTo-Hashtable -Value $property.Value
        }
        return $result
    }

    if ($Value -is [System.Collections.IEnumerable] -and -not ($Value -is [string])) {
        $items = @()
        foreach ($item in $Value) {
            $items += ConvertTo-Hashtable -Value $item
        }
        return $items
    }

    return $Value
}

function Apply-RosterChanges {
    param(
        [Parameter(Mandatory = $true)]
        [System.Collections.Generic.List[string]]$Names,
        $ChangeSet
    )

    if ($null -eq $ChangeSet) {
        return $Names
    }

    $removeValue = $null
    $addValue = $null
    if ($ChangeSet -is [System.Collections.IDictionary]) {
        if ($ChangeSet.Contains("remove")) {
            $removeValue = $ChangeSet["remove"]
        }
        if ($ChangeSet.Contains("add")) {
            $addValue = $ChangeSet["add"]
        }
    }
    else {
        $removeValue = $ChangeSet.remove
        $addValue = $ChangeSet.add
    }

    $removeNames = Normalize-StringArray -Value $removeValue
    foreach ($student in $removeNames) {
        while ($Names.Remove($student)) { }
    }

    $addNames = Normalize-StringArray -Value $addValue
    foreach ($student in $addNames) {
        if (-not $Names.Contains($student)) {
            [void]$Names.Add($student)
        }
    }

    return $Names
}

function Write-NamesBack {
    param(
        [Parameter(Mandatory = $true)]
        $Worksheet,
        [Parameter(Mandatory = $true)]
        [System.Collections.Generic.List[string]]$Names,
        [Parameter(Mandatory = $true)]
        [int]$StartRow,
        [Parameter(Mandatory = $true)]
        [int]$EndRow,
        [Parameter(Mandatory = $true)]
        [int]$NameColumn
    )

    $capacity = $EndRow - $StartRow + 1
    if ($Names.Count -gt $capacity) {
        throw "Roster length $($Names.Count) exceeds template capacity $capacity."
    }

    $index = 0
    for ($row = $StartRow; $row -le $EndRow; $row++) {
        if ($index -lt $Names.Count) {
            $Worksheet.Cells.Item($row, $NameColumn).Value2 = $Names[$index]
        } else {
            $Worksheet.Cells.Item($row, $NameColumn).Value2 = ""
        }
        $index++
    }
}

if (-not (Test-Path -LiteralPath $FolderPath)) {
    throw "Folder does not exist: $FolderPath"
}

$resolvedFolder = (Resolve-Path -LiteralPath $FolderPath).Path
$fromText = Get-MonthToken -YearValue $Year -MonthValue $FromMonth
$toText = Get-MonthToken -YearValue $Year -MonthValue $ToMonth

$rosterChanges = @{}
if ($RosterChangesJson) {
    if (-not (Test-Path -LiteralPath $RosterChangesJson)) {
        throw "Roster change file does not exist: $RosterChangesJson"
    }
    $rosterJsonText = [System.IO.File]::ReadAllText($RosterChangesJson, [System.Text.Encoding]::UTF8)
    $rosterRaw = $rosterJsonText | ConvertFrom-Json
    $rosterChanges = ConvertTo-Hashtable -Value $rosterRaw
}

$excelFiles = Get-ChildItem -LiteralPath $resolvedFolder -Filter *.xlsx -File | Sort-Object Name
if (-not $excelFiles) {
    throw "No .xlsx files were found in: $resolvedFolder"
}

$excel = $null
try {
    $excel = New-Object -ComObject Excel.Application
    $excel.Visible = $false
    $excel.DisplayAlerts = $false

    foreach ($file in $excelFiles) {
        $workbook = $null
        $worksheet = $null
        try {
            $workbook = $excel.Workbooks.Open($file.FullName)
            $worksheet = $workbook.Worksheets.Item(1)

            $titleCell = Find-TitleCell -Worksheet $worksheet -FromText $fromText
            $oldTitle = [string]$titleCell.Value2
            $titleCell.Value2 = $oldTitle.Replace($fromText, $toText)

            $footerRow = Find-FooterRow -Worksheet $worksheet
            $startRow = 6
            $endRow = $footerRow - 1
            $nameColumn = 3

            $currentNames = Get-CurrentNames -Worksheet $worksheet -StartRow $startRow -EndRow $endRow -NameColumn $nameColumn
            $changeSet = $null
            if ($rosterChanges.ContainsKey($file.Name)) {
                $changeSet = $rosterChanges[$file.Name]
            }
            $updatedNames = Apply-RosterChanges -Names $currentNames -ChangeSet $changeSet
            Write-NamesBack -Worksheet $worksheet -Names $updatedNames -StartRow $startRow -EndRow $endRow -NameColumn $nameColumn

            $workbook.Save()
            Write-Host ("[OK] {0} -> {1} | roster count: {2}" -f $file.Name, $toText, $updatedNames.Count)
        }
        finally {
            if ($workbook) {
                $workbook.Close($false)
            }
            if ($worksheet) {
                [void][System.Runtime.InteropServices.Marshal]::ReleaseComObject($worksheet)
            }
            if ($workbook) {
                [void][System.Runtime.InteropServices.Marshal]::ReleaseComObject($workbook)
            }
        }
    }
}
finally {
    if ($excel) {
        $excel.Quit()
        [void][System.Runtime.InteropServices.Marshal]::ReleaseComObject($excel)
    }
    [GC]::Collect()
    [GC]::WaitForPendingFinalizers()
}
