param(
    [Parameter(Mandatory = $true)]
    [string]$EditorialDir
)

$ErrorActionPreference = 'Stop'

function Get-ProblemPdfName {
    param(
        [Parameter(Mandatory = $true)]
        [string]$FileName
    )

    $match = [regex]::Match($FileName, '^([a-z0-9]+)_([a-z0-9]+)\.editorial\.md$', 'IgnoreCase')
    if(-not $match.Success){
        throw "Unexpected editorial file name: $FileName"
    }

    return (([string]$match.Groups[2].Value).ToUpperInvariant() + '.pdf')
}

function Get-ContestId {
    param(
        [Parameter(Mandatory = $true)]
        [System.IO.FileInfo[]]$Files
    )

    $contestIds = @()
    foreach($file in $Files){
        $match = [regex]::Match($file.Name, '^([a-z0-9]+)_([a-z0-9]+)\.editorial\.md$', 'IgnoreCase')
        if(-not $match.Success){
            throw "Unexpected editorial file name: $($file.Name)"
        }
        $contestIds += $match.Groups[1].Value.ToLower()
    }

    $uniqueIds = @($contestIds | Select-Object -Unique)
    if($uniqueIds.Count -ne 1){
        throw "Expected exactly one contest id, got: $($uniqueIds -join ', ')"
    }

    return [string]($uniqueIds | Select-Object -First 1)
}

$resolvedEditorialDir = (Resolve-Path $EditorialDir).Path
$md2pdf = Get-Command md2pdf.cmd -ErrorAction SilentlyContinue
if(-not $md2pdf){
    $md2pdf = Get-Command md2pdf -ErrorAction SilentlyContinue
}
if(-not $md2pdf){
    throw 'md2pdf command not found in PATH.'
}

$files = Get-ChildItem -Path $resolvedEditorialDir -File |
    Where-Object { $_.Name -match '^[a-z0-9]+_[a-z0-9]+\.editorial\.md$' } |
    Sort-Object Name

if(-not $files){
    throw "No editorial markdown files found in $resolvedEditorialDir"
}

$contestId = Get-ContestId -Files $files
$contestUpper = ([string]$contestId).ToUpperInvariant()
$combinedMarkdownName = "$contestId.editorials.md"
$combinedPdfName = "$contestUpper-editorials.pdf"
$combinedMarkdownPath = Join-Path $resolvedEditorialDir $combinedMarkdownName

$parts = @()
$parts += "# $contestUpper 题解合集"
foreach($file in $files){
    $text = (Get-Content -Path $file.FullName -Raw -Encoding UTF8).Trim()
    if([string]::IsNullOrWhiteSpace($text)){
        continue
    }
    if($parts.Count -gt 1){
        $parts += '<div style="page-break-after: always;"></div>'
    }
    $parts += $text
}

$combinedText = ($parts -join "`r`n`r`n") + "`r`n"
Set-Content -Path $combinedMarkdownPath -Value $combinedText -Encoding UTF8

Push-Location $resolvedEditorialDir
try {
    foreach($file in $files){
        & $md2pdf.Source $file.Name --output-dir .
        if($LASTEXITCODE -ne 0){
            throw "md2pdf failed for $($file.Name)"
        }

        $generatedPdf = Join-Path $resolvedEditorialDir ($file.BaseName + '.pdf')
        $finalPdf = Join-Path $resolvedEditorialDir (Get-ProblemPdfName -FileName $file.Name)
        if(Test-Path $finalPdf){
            Remove-Item -Path $finalPdf -Force
        }
        Move-Item -Path $generatedPdf -Destination $finalPdf -Force
        Write-Output ("PDF " + (Split-Path $finalPdf -Leaf))
    }

    & $md2pdf.Source $combinedMarkdownName --output-dir .
    if($LASTEXITCODE -ne 0){
        throw "md2pdf failed for $combinedMarkdownName"
    }

    $generatedCombinedPdf = Join-Path $resolvedEditorialDir ($contestId + '.editorials.pdf')
    $finalCombinedPdf = Join-Path $resolvedEditorialDir $combinedPdfName
    if(Test-Path $finalCombinedPdf){
        Remove-Item -Path $finalCombinedPdf -Force
    }
    Move-Item -Path $generatedCombinedPdf -Destination $finalCombinedPdf -Force
    Write-Output ("MD " + $combinedMarkdownPath)
    Write-Output ("PDF " + $finalCombinedPdf)
}
finally {
    Pop-Location

    $localTmpDir = Join-Path $resolvedEditorialDir '.tmp'
    if(Test-Path $localTmpDir){
        Remove-Item -Path $localTmpDir -Recurse -Force
    }
}
