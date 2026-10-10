@echo off
cd /d "%~dp0"
powershell -NoProfile -ExecutionPolicy Bypass -File "%~dp0run_short.ps1"
echo.
echo Finished. If there was an error above, take a screenshot and send it to Claude.
pause
