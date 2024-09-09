@echo off
setlocal enabledelayedexpansion

REM Find Python installation
set "pythonPath=C:\Users\%USERNAME%\AppData\Local\Programs\Python\Python311\python.exe"
if not exist "!pythonPath!" (
    echo Python 3.11 not found, checking for Python 3.10...
    set "pythonPath=C:\Users\%USERNAME%\AppData\Local\Programs\Python\Python310\python.exe"
    if not exist "!pythonPath!" (
        echo Python 3.10 not found. Please install Python 3.11 or 3.10.
        pause
        exit /b
    )
)

echo Using Python: !pythonPath!

REM Check if .env file exists, if not, copy .env.example to .env
if not exist ".env" (
    echo Copying .env.example to .env...
    copy ".env.example" ".env"
) else (
    echo .env file already exists. Skipping copy.
)



REM Create virtual environment if it doesn't exist
if not exist .venv (
    echo Creating virtual environment...
    "!pythonPath!" -m venv .venv
    if errorlevel 1 (
        echo Failed to create virtual environment.
        pause
        exit /b
    )
)

REM Activate the virtual environment
echo Activating virtual environment...
call .venv\Scripts\activate.bat

REM Install the requirements from requirements.txt
echo Installing requirements...
pip install -r requirements.txt

REM Deactivate the virtual environment
echo Deactivating virtual environment...
deactivate

echo Done.
