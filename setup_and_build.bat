@echo off
setlocal enabledelayedexpansion
REM ONE-CLICK: installs everything it can, downloads the gesture model, builds PAC.
REM Uses Python 3.15 (the newest Python found). Very new Pythons may lack some packages (e.g. mediapipe),
REM in which case those features are listed at the end and PAC still builds with the rest.
REM Usage: double-click, or   setup_and_build.bat 1.0.0 YOUR-GITHUB-NAME
cd /d "%~dp0"
set VER=%1
if "%VER%"=="" set VER=1.0.0
set GH=%2
if "%GH%"=="" set GH=YOUR-GITHUB-NAME

set PYCMD=
py -3.12 --version >nul 2>nul && set PYCMD=py -3.12
if "%PYCMD%"=="" py -3.15 --version >nul 2>nul && set PYCMD=py -3.15
if "%PYCMD%"=="" py -3 --version >nul 2>nul && set PYCMD=py -3
if "%PYCMD%"=="" python --version >nul 2>nul && set PYCMD=python
if "%PYCMD%"=="" (echo No Python found. Install Python from python.org, tick "Add to PATH", and run this again. & pause & exit /b 1)
echo Using: & %PYCMD% --version

echo [1/5] Creating environment...
REM Reuse an existing environment (deleting it fails while any program still has its files open).
if exist venv\Scripts\python.exe (
  echo    Reusing the existing environment.
) else (
  %PYCMD% -m venv venv || goto :fail
)
call venv\Scripts\activate
python -m pip install --upgrade pip

echo [2/5] Installing packages one by one (several minutes)...
set MISSING=
for %%P in (numpy opencv-python SpeechRecognition sounddevice pyttsx3 edge-tts pyautogui pillow psutil sympy segno keyring mediapipe zstandard nuitka) do (
  echo    installing %%P ...
  python -m pip install %%P >nul 2>&1 || (echo    !! %%P could not be installed & set MISSING=!MISSING! %%P)
)
if defined MISSING echo.& echo NOT INSTALLED:%MISSING%& echo ^(mediapipe = hand gestures; opencv-python = AR/face/gestures; others as named. Python 3.12 supports them all.^)
echo %MISSING% | findstr /i "nuitka" >nul && (echo Nuitka is required to build. Install Python 3.12 and run again. & pause & exit /b 1)

echo [3/5] Getting the gesture model...
if not exist hand_landmarker.task (
  powershell -NoProfile -Command "try { Invoke-WebRequest -UseBasicParsing -Uri 'https://storage.googleapis.com/mediapipe-models/hand_landmarker/hand_landmarker/float16/latest/hand_landmarker.task' -OutFile hand_landmarker.task } catch { Write-Host 'Could not download the model - gestures will fetch it on first use.' }"
)
if not exist "%USERPROFILE%\.pac" mkdir "%USERPROFILE%\.pac"
if exist hand_landmarker.task copy /y hand_landmarker.task "%USERPROFILE%\.pac\hand_landmarker.task" >nul

echo [4/5] Checking what loads...
python -c "import importlib;m=['cv2','numpy','mediapipe','speech_recognition','sounddevice','pyttsx3','edge_tts','pyautogui','PIL','psutil','sympy','segno','keyring'];bad=[x for x in m if importlib.util.find_spec(x) is None];print('Missing features:',bad or 'none')"

echo [5/5] Building PAC (10-30 minutes; close other programs)...
python build_release.py %VER% %GH% || goto :fail

echo.
echo DONE.  App: dist\pac.dist\PAC.exe    Zip: dist\PAC-%VER%.zip
if defined MISSING echo Some features were left out: %MISSING%
pause
exit /b 0
:fail
echo.
echo Something failed - copy the last 20 lines above and send them to Claude.
pause
exit /b 1
