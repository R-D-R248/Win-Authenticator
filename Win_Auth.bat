@echo off
:: Get the dynamic Desktop path using PowerShell
for /f "delims=" %%D in ('powershell -NoProfile -Command "[System.Environment]::GetFolderPath('Desktop')"') do set DesktopPath=%%D

:: Check if the Desktop path is correct
if not exist "%DesktopPath%" (
    echo Desktop folder not found!
    pause
    exit /b
)

:: Change to the Desktop directory
cd /d "%DesktopPath%"

:: Run the Python script
python "%DesktopPath%\Win_Auth.py"

