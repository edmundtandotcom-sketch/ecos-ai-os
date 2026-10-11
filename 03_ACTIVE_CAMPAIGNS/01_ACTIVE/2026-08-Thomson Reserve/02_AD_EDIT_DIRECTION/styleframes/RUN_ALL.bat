@echo off
cd /d "%~dp0"
powershell -NoProfile -ExecutionPolicy Bypass -File "%~dp0run_all.ps1"
echo.
echo Finished. The ads are in the RENDERS folder inside the Daughter Spin Off folder. If there was an error above, take a screenshot and send it to Claude.
pause
