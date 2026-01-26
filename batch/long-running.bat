@echo off
REM Long running batch file

echo Starting long running batch script...
for /l %%i in (1,1,10) do (
    echo Progress: %%i/10
    timeout /t 1 /nobreak >nul
)
echo Long running script completed!
