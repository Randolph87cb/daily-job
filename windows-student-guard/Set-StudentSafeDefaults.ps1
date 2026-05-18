[CmdletBinding(SupportsShouldProcess = $true)]
param(
    [switch]$ApplyToDefaultUser,
    [switch]$RestartExplorer,
    [ValidateRange(1, 20)]
    [int]$MouseSpeed = 10,
    [string]$CursorScheme = "Windows Black (large)",
    [switch]$SkipDisplayResolution
)

Set-StrictMode -Version Latest
$ErrorActionPreference = "Stop"

Add-Type -TypeDefinition @"
using System;
using System.Runtime.InteropServices;

public static class StudentSafeNativeMethods
{
    public const uint SPI_SETCURSORS = 0x0057;
    public const uint SPI_SETMOUSESPEED = 0x0071;
    public const uint SPIF_UPDATEINIFILE = 0x0001;
    public const uint SPIF_SENDCHANGE = 0x0002;

    public const int CDS_UPDATEREGISTRY = 0x00000001;
    public const int DISP_CHANGE_SUCCESSFUL = 0;
    public const uint DM_BITSPERPEL = 0x00040000;
    public const uint DM_PELSWIDTH = 0x00080000;
    public const uint DM_PELSHEIGHT = 0x00100000;
    public const uint DM_DISPLAYFREQUENCY = 0x00400000;

    [StructLayout(LayoutKind.Sequential, CharSet = CharSet.Unicode)]
    public struct DEVMODE
    {
        private const int CCHDEVICENAME = 32;
        private const int CCHFORMNAME = 32;

        [MarshalAs(UnmanagedType.ByValTStr, SizeConst = CCHDEVICENAME)]
        public string dmDeviceName;
        public ushort dmSpecVersion;
        public ushort dmDriverVersion;
        public ushort dmSize;
        public ushort dmDriverExtra;
        public uint dmFields;
        public int dmPositionX;
        public int dmPositionY;
        public uint dmDisplayOrientation;
        public uint dmDisplayFixedOutput;
        public short dmColor;
        public short dmDuplex;
        public short dmYResolution;
        public short dmTTOption;
        public short dmCollate;

        [MarshalAs(UnmanagedType.ByValTStr, SizeConst = CCHFORMNAME)]
        public string dmFormName;

        public ushort dmLogPixels;
        public uint dmBitsPerPel;
        public uint dmPelsWidth;
        public uint dmPelsHeight;
        public uint dmDisplayFlags;
        public uint dmDisplayFrequency;
        public uint dmICMMethod;
        public uint dmICMIntent;
        public uint dmMediaType;
        public uint dmDitherType;
        public uint dmReserved1;
        public uint dmReserved2;
        public uint dmPanningWidth;
        public uint dmPanningHeight;
    }

    [DllImport("user32.dll", CharSet = CharSet.Unicode, SetLastError = true)]
    public static extern bool SystemParametersInfoW(uint uiAction, uint uiParam, IntPtr pvParam, uint fWinIni);

    [DllImport("user32.dll", CharSet = CharSet.Unicode)]
    public static extern int ChangeDisplaySettingsW(ref DEVMODE devMode, int flags);
}
"@

function Write-Step {
    param(
        [string]$Message
    )

    Write-Host ("[{0}] {1}" -f (Get-Date -Format "HH:mm:ss"), $Message)
}

function Test-IsAdministrator {
    $identity = [Security.Principal.WindowsIdentity]::GetCurrent()
    $principal = New-Object Security.Principal.WindowsPrincipal($identity)
    return $principal.IsInRole([Security.Principal.WindowsBuiltInRole]::Administrator)
}

function Ensure-RegistryPath {
    param(
        [Parameter(Mandatory = $true)]
        [string]$Path
    )

    if (-not (Test-Path -LiteralPath $Path)) {
        New-Item -Path $Path -Force | Out-Null
    }
}

function Ensure-Directory {
    param(
        [Parameter(Mandatory = $true)]
        [string]$Path
    )

    if (-not (Test-Path -LiteralPath $Path)) {
        New-Item -ItemType Directory -Path $Path -Force | Out-Null
    }
}

function Convert-RegistryValueForLog {
    param(
        $Value
    )

    if ($null -eq $Value) {
        return $null
    }

    if ($Value -is [byte[]]) {
        return [Convert]::ToBase64String($Value)
    }

    if ($Value -is [array]) {
        return ($Value | ForEach-Object { "$_" }) -join ","
    }

    return "$Value"
}

function Add-ChangeLogEntry {
    param(
        [Parameter(Mandatory = $true)]
        [AllowEmptyCollection()]
        [System.Collections.Generic.List[object]]$Log,
        [Parameter(Mandatory = $true)]
        [string]$Type,
        [Parameter(Mandatory = $true)]
        [string]$Path,
        [Parameter(Mandatory = $true)]
        [string]$Name,
        $Before,
        $After
    )

    $Log.Add([pscustomobject]@{
        Type   = $Type
        Path   = $Path
        Name   = $Name
        Before = Convert-RegistryValueForLog $Before
        After  = Convert-RegistryValueForLog $After
    }) | Out-Null
}

function Get-RegistrySnapshot {
    param(
        [Parameter(Mandatory = $true)]
        [string]$Path,
        [Parameter(Mandatory = $true)]
        [string]$Name
    )

    if (-not (Test-Path -LiteralPath $Path)) {
        return @{
            Exists = $false
            Value  = $null
        }
    }

    $item = Get-ItemProperty -LiteralPath $Path -ErrorAction Stop
    $property = $item.PSObject.Properties[$Name]

    if ($null -eq $property) {
        return @{
            Exists = $false
            Value  = $null
        }
    }

    return @{
        Exists = $true
        Value  = $property.Value
    }
}

function Set-RegistryDword {
    param(
        [Parameter(Mandatory = $true)]
        [string]$Path,
        [Parameter(Mandatory = $true)]
        [string]$Name,
        [Parameter(Mandatory = $true)]
        [int]$Value,
        [Parameter(Mandatory = $true)]
        [AllowEmptyCollection()]
        [System.Collections.Generic.List[object]]$Log
    )

    Ensure-RegistryPath -Path $Path
    $before = Get-RegistrySnapshot -Path $Path -Name $Name

    if ($before.Exists -and [int]$before.Value -eq $Value) {
        Write-Step "No change: $Path -> $Name = $Value"
        return $false
    }

    if (-not $PSCmdlet.ShouldProcess("$Path\$Name", "Set DWORD to $Value")) {
        Write-Step "Would set: $Path -> $Name = $Value"
        return $false
    }

    New-ItemProperty -LiteralPath $Path -Name $Name -PropertyType DWord -Value $Value -Force | Out-Null
    Add-ChangeLogEntry -Log $Log -Type "DWord" -Path $Path -Name $Name -Before $before.Value -After $Value
    Write-Step "Set: $Path -> $Name = $Value"
    return $true
}

function Set-RegistryString {
    param(
        [Parameter(Mandatory = $true)]
        [string]$Path,
        [Parameter(Mandatory = $true)]
        [string]$Name,
        [Parameter(Mandatory = $true)]
        [AllowEmptyString()]
        [string]$Value,
        [Parameter(Mandatory = $true)]
        [AllowEmptyCollection()]
        [System.Collections.Generic.List[object]]$Log
    )

    Ensure-RegistryPath -Path $Path
    $before = Get-RegistrySnapshot -Path $Path -Name $Name

    if ($before.Exists -and [string]$before.Value -eq $Value) {
        Write-Step "No change: $Path -> $Name = $Value"
        return $false
    }

    if (-not $PSCmdlet.ShouldProcess("$Path\$Name", "Set string value")) {
        Write-Step "Would set: $Path -> $Name = $Value"
        return $false
    }

    New-ItemProperty -LiteralPath $Path -Name $Name -PropertyType String -Value $Value -Force | Out-Null
    Add-ChangeLogEntry -Log $Log -Type "String" -Path $Path -Name $Name -Before $before.Value -After $Value
    Write-Step "Set: $Path -> $Name = $Value"
    return $true
}

function Set-RegistryBinary {
    param(
        [Parameter(Mandatory = $true)]
        [string]$Path,
        [Parameter(Mandatory = $true)]
        [string]$Name,
        [Parameter(Mandatory = $true)]
        [byte[]]$Value,
        [Parameter(Mandatory = $true)]
        [AllowEmptyCollection()]
        [System.Collections.Generic.List[object]]$Log
    )

    Ensure-RegistryPath -Path $Path
    $before = Get-RegistrySnapshot -Path $Path -Name $Name

    if ($before.Exists -and $before.Value -is [byte[]] -and
        [Convert]::ToBase64String($before.Value) -eq [Convert]::ToBase64String($Value)) {
        Write-Step "No change: $Path -> $Name (binary)"
        return $false
    }

    if (-not $PSCmdlet.ShouldProcess("$Path\$Name", "Set binary value")) {
        Write-Step "Would set: $Path -> $Name (binary)"
        return $false
    }

    New-ItemProperty -LiteralPath $Path -Name $Name -PropertyType Binary -Value $Value -Force | Out-Null
    Add-ChangeLogEntry -Log $Log -Type "Binary" -Path $Path -Name $Name -Before $before.Value -After $Value
    Write-Step "Set: $Path -> $Name (binary)"
    return $true
}

function Get-OsInfo {
    $current = Get-ItemProperty "HKLM:\SOFTWARE\Microsoft\Windows NT\CurrentVersion"
    $build = [int]$current.CurrentBuildNumber

    return [pscustomobject]@{
        ProductName = $current.ProductName
        Build       = $build
        IsWindows11 = $build -ge 22000
    }
}

function New-DevMode {
    $mode = New-Object StudentSafeNativeMethods+DEVMODE
    $mode.dmSize = [System.UInt16][Runtime.InteropServices.Marshal]::SizeOf([type]"StudentSafeNativeMethods+DEVMODE")
    return $mode
}

function Format-DisplayMode {
    param(
        [Parameter(Mandatory = $true)]
        $Mode
    )

    return ("{0}x{1} {2}bpp @{3}Hz" -f $Mode.Width, $Mode.Height, $Mode.BitsPerPel, $Mode.DisplayFrequency)
}

function Get-CurrentDisplayMode {
    $controller = Get-CimInstance Win32_VideoController |
        Where-Object { $_.CurrentHorizontalResolution -and $_.CurrentVerticalResolution } |
        Sort-Object `
            @{ Expression = { [int64]$_.CurrentHorizontalResolution * [int64]$_.CurrentVerticalResolution }; Descending = $true }, `
            @{ Expression = { [int]$_.CurrentRefreshRate }; Descending = $true } |
        Select-Object -First 1

    if ($null -eq $controller) {
        throw "Unable to query the current display mode."
    }

    $bitsPerPel = if ($controller.CurrentBitsPerPixel) { [int]$controller.CurrentBitsPerPixel } else { 32 }
    $refreshRate = if ($controller.CurrentRefreshRate) { [int]$controller.CurrentRefreshRate } else { 60 }

    return [pscustomobject]@{
        Width            = [int]$controller.CurrentHorizontalResolution
        Height           = [int]$controller.CurrentVerticalResolution
        BitsPerPel       = $bitsPerPel
        DisplayFrequency = $refreshRate
    }
}

function Get-PreferredDisplayMode {
    $supported = Get-CimInstance -Namespace root\wmi -ClassName WmiMonitorListedSupportedSourceModes -ErrorAction SilentlyContinue |
        Where-Object { $_.Active } |
        Select-Object -First 1

    if ($null -eq $supported) {
        throw "Unable to query supported monitor source modes."
    }

    $modes = @(
        $supported.MonitorSourceModes | ForEach-Object {
            $refreshRate = if ($_.VerticalRefreshRateDenominator) {
                [int][Math]::Round($_.VerticalRefreshRateNumerator / [double]$_.VerticalRefreshRateDenominator, 0)
            }
            else {
                60
            }

            [pscustomobject]@{
                Width            = [int]$_.HorizontalActivePixels
                Height           = [int]$_.VerticalActivePixels
                BitsPerPel       = 32
                DisplayFrequency = $refreshRate
            }
        }
    )

    if ($modes.Count -eq 0) {
        throw "Supported monitor source modes were returned empty."
    }

    $preferredIndex = [int]$supported.PreferredMonitorSourceModeIndex
    if ($preferredIndex -ge 0 -and $preferredIndex -lt $modes.Count) {
        return $modes[$preferredIndex]
    }

    return $modes |
        Sort-Object `
            @{ Expression = { [int64]$_.Width * [int64]$_.Height }; Descending = $true }, `
            @{ Expression = { [int]$_.DisplayFrequency }; Descending = $true } |
        Select-Object -First 1
}

function Set-TaskbarPolicies {
    param(
        [Parameter(Mandatory = $true)]
        [AllowEmptyCollection()]
        [System.Collections.Generic.List[object]]$Log
    )

    $policyPath = "HKCU:\Software\Microsoft\Windows\CurrentVersion\Policies\Explorer"
    [void](Set-RegistryDword -Path $policyPath -Name "LockTaskbar" -Value 1 -Log $Log)
    [void](Set-RegistryDword -Path $policyPath -Name "NoSetTaskbar" -Value 1 -Log $Log)
    [void](Set-RegistryDword -Path $policyPath -Name "TaskbarLockAll" -Value 1 -Log $Log)
}

function Set-Win10TaskbarBottom {
    param(
        [Parameter(Mandatory = $true)]
        [AllowEmptyCollection()]
        [System.Collections.Generic.List[object]]$Log
    )

    $changed = $false
    $primaryPath = "HKCU:\Software\Microsoft\Windows\CurrentVersion\Explorer\StuckRects3"
    $primaryValue = Get-RegistrySnapshot -Path $primaryPath -Name "Settings"

    if ($primaryValue.Exists -and $primaryValue.Value -is [byte[]] -and $primaryValue.Value.Length -gt 12) {
        $bytes = [byte[]]$primaryValue.Value.Clone()
        if ($bytes[12] -ne 3) {
            $bytes[12] = 3
            $changed = (Set-RegistryBinary -Path $primaryPath -Name "Settings" -Value $bytes -Log $Log) -or $changed
        }
    }

    $multiPath = "HKCU:\Software\Microsoft\Windows\CurrentVersion\Explorer\MMStuckRects3"
    if (Test-Path -LiteralPath $multiPath) {
        $multiItem = Get-ItemProperty -LiteralPath $multiPath
        foreach ($property in $multiItem.PSObject.Properties) {
            if ($property.Name -like "PS*") {
                continue
            }

            if ($property.Value -is [byte[]] -and $property.Value.Length -gt 12) {
                $bytes = [byte[]]$property.Value.Clone()
                if ($bytes[12] -ne 3) {
                    $bytes[12] = 3
                    $changed = (Set-RegistryBinary -Path $multiPath -Name $property.Name -Value $bytes -Log $Log) -or $changed
                }
            }
        }
    }

    return $changed
}

function Set-TouchpadPolicy {
    param(
        [Parameter(Mandatory = $true)]
        [AllowEmptyCollection()]
        [System.Collections.Generic.List[object]]$Log
    )

    $path = "HKCU:\Software\Microsoft\Windows\CurrentVersion\PrecisionTouchPad"
    [void](Set-RegistryDword -Path $path -Name "LeaveOnWithMouse" -Value 0 -Log $Log)
}

function Set-Win10TabletModePreference {
    param(
        [Parameter(Mandatory = $true)]
        [AllowEmptyCollection()]
        [System.Collections.Generic.List[object]]$Log
    )

    $path = "HKCU:\Software\Microsoft\Windows\CurrentVersion\ImmersiveShell"
    [void](Set-RegistryDword -Path $path -Name "SignInMode" -Value 1 -Log $Log)
    [void](Set-RegistryDword -Path $path -Name "ConvertibleSlateModePromptPreference" -Value 0 -Log $Log)
}

function Set-MouseSpeedValue {
    param(
        [Parameter(Mandatory = $true)]
        [ValidateRange(1, 20)]
        [int]$Value,
        [Parameter(Mandatory = $true)]
        [AllowEmptyCollection()]
        [System.Collections.Generic.List[object]]$Log
    )

    $path = "HKCU:\Control Panel\Mouse"
    $before = Get-RegistrySnapshot -Path $path -Name "MouseSensitivity"

    if ($before.Exists -and [int]$before.Value -eq $Value) {
        Write-Step "No change: current user mouse speed = $Value"
        return $false
    }

    if (-not $PSCmdlet.ShouldProcess("Current user mouse speed", "Set to $Value")) {
        Write-Step "Would set: current user mouse speed = $Value"
        return $false
    }

    $ok = [StudentSafeNativeMethods]::SystemParametersInfoW(
        [StudentSafeNativeMethods]::SPI_SETMOUSESPEED,
        0,
        [IntPtr]$Value,
        [StudentSafeNativeMethods]::SPIF_UPDATEINIFILE -bor [StudentSafeNativeMethods]::SPIF_SENDCHANGE
    )

    if (-not $ok) {
        throw "Failed to update the current user mouse speed."
    }

    Add-ChangeLogEntry -Log $Log -Type "MouseSpeed" -Path $path -Name "MouseSensitivity" -Before $before.Value -After $Value
    Write-Step "Set: current user mouse speed = $Value"
    return $true
}

function Get-CursorSchemeNames {
    return @(
        "Arrow",
        "Help",
        "AppStarting",
        "Wait",
        "Crosshair",
        "IBeam",
        "NWPen",
        "No",
        "SizeNS",
        "SizeWE",
        "SizeNWSE",
        "SizeNESW",
        "SizeAll",
        "UpArrow",
        "Hand",
        "Pin",
        "Person"
    )
}

function Get-SystemCursorSchemeDefinition {
    param(
        [Parameter(Mandatory = $true)]
        [string]$SchemeName
    )

    $schemes = Get-ItemProperty "HKLM:\SOFTWARE\Microsoft\Windows\CurrentVersion\Control Panel\Cursors\Schemes"
    $schemeValue = $schemes.PSObject.Properties[$SchemeName]

    if ($null -eq $schemeValue -or [string]::IsNullOrWhiteSpace([string]$schemeValue.Value)) {
        throw "Cursor scheme '$SchemeName' was not found in the system cursor schemes."
    }

    $parts = [string]$schemeValue.Value -split ","
    $names = Get-CursorSchemeNames

    if ($parts.Length -lt $names.Length) {
        throw "Cursor scheme '$SchemeName' is incomplete."
    }

    $definition = @{}
    for ($i = 0; $i -lt $names.Length; $i++) {
        $definition[$names[$i]] = $parts[$i]
    }

    return $definition
}

function Set-CursorScheme {
    param(
        [Parameter(Mandatory = $true)]
        [string]$SchemeName,
        [Parameter(Mandatory = $true)]
        [string]$TargetPath,
        [Parameter(Mandatory = $true)]
        [AllowEmptyCollection()]
        [System.Collections.Generic.List[object]]$Log
    )

    $definition = Get-SystemCursorSchemeDefinition -SchemeName $SchemeName
    $changed = $false

    foreach ($name in Get-CursorSchemeNames) {
        $changed = (Set-RegistryString -Path $TargetPath -Name $name -Value $definition[$name] -Log $Log) -or $changed
    }

    return $changed
}

function Reload-Cursors {
    if (-not $PSCmdlet.ShouldProcess("Current user cursors", "Reload cursor resources")) {
        Write-Step "Would reload cursor resources."
        return $false
    }

    $ok = [StudentSafeNativeMethods]::SystemParametersInfoW(
        [StudentSafeNativeMethods]::SPI_SETCURSORS,
        0,
        [IntPtr]::Zero,
        [StudentSafeNativeMethods]::SPIF_SENDCHANGE
    )

    if (-not $ok) {
        throw "Failed to reload cursor resources."
    }

    Write-Step "Reloaded cursor resources."
    return $true
}

function Set-DisplayResolutionToHighestSupported {
    param(
        [Parameter(Mandatory = $true)]
        [AllowEmptyCollection()]
        [System.Collections.Generic.List[object]]$Log
    )

    $current = Get-CurrentDisplayMode
    $target = Get-PreferredDisplayMode
    $beforeText = Format-DisplayMode -Mode $current
    $afterText = Format-DisplayMode -Mode $target

    if ($current.Width -eq $target.Width -and
        $current.Height -eq $target.Height -and
        $current.BitsPerPel -eq $target.BitsPerPel -and
        $current.DisplayFrequency -eq $target.DisplayFrequency) {
        Write-Step "No change: primary display already uses the preferred supported mode ($beforeText)."
        return $false
    }

    if (-not $PSCmdlet.ShouldProcess("Primary display", "Change resolution from $beforeText to preferred mode $afterText")) {
        Write-Step "Would set: primary display = $afterText"
        return $false
    }

    $mode = New-DevMode
    $mode.dmPelsWidth = [uint32]$target.Width
    $mode.dmPelsHeight = [uint32]$target.Height
    $mode.dmBitsPerPel = [uint32]$target.BitsPerPel
    $mode.dmDisplayFrequency = [uint32]$target.DisplayFrequency
    $mode.dmFields = [StudentSafeNativeMethods]::DM_PELSWIDTH -bor
        [StudentSafeNativeMethods]::DM_PELSHEIGHT -bor
        [StudentSafeNativeMethods]::DM_BITSPERPEL -bor
        [StudentSafeNativeMethods]::DM_DISPLAYFREQUENCY

    $result = [StudentSafeNativeMethods]::ChangeDisplaySettingsW([ref]$mode, [StudentSafeNativeMethods]::CDS_UPDATEREGISTRY)
    if ($result -ne [StudentSafeNativeMethods]::DISP_CHANGE_SUCCESSFUL) {
        throw "Failed to change display resolution. Native API returned code $result."
    }

    Add-ChangeLogEntry -Log $Log -Type "DisplayMode" -Path "PrimaryDisplay" -Name "Resolution" -Before $beforeText -After $afterText
    Write-Step "Set: primary display = $afterText"
    return $true
}

function Invoke-InDefaultUserHive {
    param(
        [Parameter(Mandatory = $true)]
        [scriptblock]$ScriptBlock
    )

    $defaultHive = "$env:SystemDrive\Users\Default\NTUSER.DAT"
    $mountName = "HKU\CodexDefaultUser"

    & reg.exe load $mountName $defaultHive | Out-Null
    try {
        & $ScriptBlock
    }
    finally {
        & reg.exe unload $mountName | Out-Null
    }
}

function Set-DefaultUserProfileValues {
    param(
        [Parameter(Mandatory = $true)]
        [pscustomobject]$OsInfo,
        [Parameter(Mandatory = $true)]
        [ValidateRange(1, 20)]
        [int]$MouseSpeedValue,
        [Parameter(Mandatory = $true)]
        [string]$CursorSchemeName,
        [Parameter(Mandatory = $true)]
        [AllowEmptyCollection()]
        [System.Collections.Generic.List[object]]$Log
    )

    if (-not (Test-IsAdministrator)) {
        throw "Run PowerShell as Administrator when using -ApplyToDefaultUser."
    }

    Write-Step "Applying the same per-user settings to the default user profile."
    Invoke-InDefaultUserHive -ScriptBlock {
        $defaultPolicyPath = "Registry::HKEY_USERS\CodexDefaultUser\Software\Microsoft\Windows\CurrentVersion\Policies\Explorer"
        $defaultTouchpadPath = "Registry::HKEY_USERS\CodexDefaultUser\Software\Microsoft\Windows\CurrentVersion\PrecisionTouchPad"
        $defaultTabletPath = "Registry::HKEY_USERS\CodexDefaultUser\Software\Microsoft\Windows\CurrentVersion\ImmersiveShell"
        $defaultMousePath = "Registry::HKEY_USERS\CodexDefaultUser\Control Panel\Mouse"
        $defaultCursorPath = "Registry::HKEY_USERS\CodexDefaultUser\Control Panel\Cursors"

        [void](Set-RegistryDword -Path $defaultPolicyPath -Name "LockTaskbar" -Value 1 -Log $Log)
        [void](Set-RegistryDword -Path $defaultPolicyPath -Name "NoSetTaskbar" -Value 1 -Log $Log)
        [void](Set-RegistryDword -Path $defaultPolicyPath -Name "TaskbarLockAll" -Value 1 -Log $Log)
        [void](Set-RegistryDword -Path $defaultTouchpadPath -Name "LeaveOnWithMouse" -Value 0 -Log $Log)
        [void](Set-RegistryString -Path $defaultMousePath -Name "MouseSensitivity" -Value "$MouseSpeedValue" -Log $Log)
        [void](Set-CursorScheme -SchemeName $CursorSchemeName -TargetPath $defaultCursorPath -Log $Log)

        if (-not $OsInfo.IsWindows11) {
            [void](Set-RegistryDword -Path $defaultTabletPath -Name "SignInMode" -Value 1 -Log $Log)
            [void](Set-RegistryDword -Path $defaultTabletPath -Name "ConvertibleSlateModePromptPreference" -Value 0 -Log $Log)
        }
    }
}

$osInfo = Get-OsInfo
$changeLog = New-Object "System.Collections.Generic.List[object]"
$backupDir = Join-Path -Path $PSScriptRoot -ChildPath "backups"
Ensure-Directory -Path $backupDir

Write-Step "Detected OS: $($osInfo.ProductName) (Build $($osInfo.Build))"
Write-Step "Applying the student-safe baseline."

Set-TaskbarPolicies -Log $changeLog

$needExplorerRestart = $false
if ($osInfo.IsWindows11) {
    Write-Step "Windows 11 only supports bottom taskbar docking, so this script locks the taskbar without forcing its position."
    Write-Step "Windows 11 removed the manual tablet mode toggle, so this script avoids unsupported overrides."
}
else {
    $needExplorerRestart = Set-Win10TaskbarBottom -Log $changeLog
    Set-Win10TabletModePreference -Log $changeLog
}

Set-TouchpadPolicy -Log $changeLog
[void](Set-MouseSpeedValue -Value $MouseSpeed -Log $changeLog)
$cursorChanged = Set-CursorScheme -SchemeName $CursorScheme -TargetPath "HKCU:\Control Panel\Cursors" -Log $changeLog
if ($cursorChanged) {
    [void](Reload-Cursors)
}

if (-not $SkipDisplayResolution) {
    [void](Set-DisplayResolutionToHighestSupported -Log $changeLog)
}
else {
    Write-Step "Skipped display resolution changes by request."
}

if ($ApplyToDefaultUser) {
    Set-DefaultUserProfileValues -OsInfo $osInfo -MouseSpeedValue $MouseSpeed -CursorSchemeName $CursorScheme -Log $changeLog
}

if ($changeLog.Count -gt 0) {
    $backupFile = Join-Path -Path $backupDir -ChildPath ("changes-{0}.json" -f (Get-Date -Format "yyyyMMdd-HHmmss"))
    if ($PSCmdlet.ShouldProcess($backupFile, "Write change log")) {
        $changeLog | ConvertTo-Json -Depth 5 | Set-Content -LiteralPath $backupFile -Encoding UTF8
        Write-Step "Change log written to: $backupFile"
    }
    else {
        Write-Step "Would write change log to: $backupFile"
    }
}
else {
    Write-Step "No persisted changes were recorded."
}

if ($RestartExplorer -or $needExplorerRestart) {
    Write-Step "Restarting Explorer to apply taskbar changes."
    Get-Process explorer -ErrorAction SilentlyContinue | Stop-Process -Force
    Start-Process explorer.exe
}

Write-Step "Done."
Write-Host ""
Write-Host "Next steps:"
Write-Host "1. Run the script once for existing student accounts."
Write-Host "2. Use -ApplyToDefaultUser in an elevated session when future student accounts should inherit the same per-user defaults."
Write-Host "3. Use -SkipDisplayResolution if a specific classroom machine should keep a manually chosen display mode."
