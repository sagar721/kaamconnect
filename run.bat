@echo off
REM KaamConnect Startup Script for Windows

echo.
echo ===================================
echo   KaamConnect - Startup Script
echo ===================================
echo.

REM Check if Python is installed
python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo ERROR: Python is not installed or not in PATH
    echo Please install Python 3.8+ from https://www.python.org
    pause
    exit /b 1
)

REM Check if required files exist
if not exist "app.py" (
    echo ERROR: app.py not found!
    echo Please run this script from the kaamconnect directory
    pause
    exit /b 1
)

if not exist "requirements.txt" (
    echo ERROR: requirements.txt not found!
    echo Please ensure requirements.txt exists in the kaamconnect directory
    pause
    exit /b 1
)

REM Create data directory if it doesn't exist
if not exist "data" (
    echo Creating data directory...
    mkdir data
)

REM Install/upgrade dependencies
echo.
echo Installing dependencies...
python -m pip install --upgrade pip >nul 2>&1
python -m pip install -r requirements.txt

if %errorlevel% neq 0 (
    echo ERROR: Failed to install dependencies
    pause
    exit /b 1
)

REM Start the Flask application
echo.
echo ===================================
echo Starting KaamConnect...
echo ===================================
echo.
echo The application will be available at: http://localhost:5000
echo Press CTRL+C to stop the server
echo.
echo Default Admin Credentials:
echo   Username: admin
echo   Password: admin123
echo.
echo ===================================
echo.

python app.py

pause
