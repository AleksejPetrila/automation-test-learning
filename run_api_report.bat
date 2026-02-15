@echo off
REM Create reports folder if it doesn't exist
if not exist reports mkdir reports

pytest -m api -v --html=reports\report_latest.html --self-contained-html

echo.
echo Report generated: reports\report_latest.html
pause