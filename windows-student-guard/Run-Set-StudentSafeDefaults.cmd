@echo off
setlocal
cd /d "%~dp0"
powershell -NoProfile -ExecutionPolicy Bypass -Command "Start-Process PowerShell -Verb RunAs -ArgumentList '-NoProfile -ExecutionPolicy Bypass -File ""%~dp0Set-StudentSafeDefaults.ps1"" -ApplyToDefaultUser -RestartExplorer'"
endlocal
