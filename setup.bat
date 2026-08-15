@echo off
echo ========================================================
echo   Launching Reframe Automated Setup...
echo ========================================================
python setup.py
if errorlevel 1 (
    echo.
    echo Python was not found in PATH. Running fallback installer...
    winget install MiKTeX.MiKTeX --silent --accept-source-agreements --accept-package-agreements
)
pause
