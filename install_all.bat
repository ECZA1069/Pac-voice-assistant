@echo off
REM Installs everything PAC needs into a fresh virtual environment (folder "venv") using Python 3.12.
cd /d "%~dp0"
where py >nul 2>nul || (echo Python launcher not found. Install Python 3.12 from python.org and tick "Add to PATH". & pause & exit /b 1)
py -3.12 --version >nul 2>nul || (echo Python 3.12 is not installed. Install it from https://www.python.org/downloads/release/python-3120/ & pause & exit /b 1)
if not exist venv\Scripts\python.exe py -3.12 -m venv venv || (echo Could not create the environment. Close other windows using it and try again. & pause & exit /b 1)
call venv\Scripts\activate
python -m pip install --upgrade pip
python -m pip install -r requirements.txt || (echo One package failed - read the message above. & pause & exit /b 1)
echo.
echo Done. Test with:   python pac.py
echo Build the app with:   python build_release.py 1.0.0 YOUR-GITHUB-NAME
pause
