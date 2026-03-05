@echo off
REM Master Script - Run all compiler design experiments
REM Usage: run_all.bat

echo.
echo ================================================================================
echo   COMPILER DESIGN - ALL EXPERIMENTS RUNNER
echo ================================================================================
echo.

cd /d "%~dp0"

echo Starting automated execution...
python run_all_automated.py

echo.
echo All experiments completed. Check output above for details.
pause
