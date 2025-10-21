@echo off
cd /d "%~dp0wave-server\wave-0.26.3-windows-amd64"
echo Starting Wave server...
echo Once started, you can access the app at: http://localhost:10101/info-sheet
echo Press Ctrl+C to stop the server
echo.
waved.exe
