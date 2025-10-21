@echo off
REM start_wave.bat - Windows helper to start Wave server and run the app
REM Usage: double-click or run from cmd/powershell

set WAVE_DIR=wave-server
set WAVE_EXE=%WAVE_DIR%\waved.exe

if not exist "%WAVE_EXE%" (
  echo Wave server not found. Please download Wave for Windows from:
  echo https://github.com/h2oai/wave/releases
  pause
  exit /b 1
)

start "Wave Server" "%WAVE_EXE%"

REM Wait for server to warm up
ping -n 2 127.0.0.1 >nul

REM Try to use wave CLI if installed
where wave >nul 2>nul
if %errorlevel%==0 (
  wave run app.py
) else (
  REM Try python module
  python -m h2o_wave run app.py
)
