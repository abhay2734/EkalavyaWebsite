@echo off
echo Clearing SSL state and restarting Django server...
echo.

REM Close Chrome/Edge processes to clear SSL cache
taskkill /F /IM chrome.exe 2>nul
taskkill /F /IM msedge.exe 2>nul

REM Clear Windows SSL state
echo Clearing Windows SSL certificate store...
certutil -urlcache * delete

echo.
echo Starting Django server on port 8080...
cd /d "C:\Workspace\Ravindra Workspace\EkalavyaWebsite\ekalavya"
python manage.py runserver 8080

pause
