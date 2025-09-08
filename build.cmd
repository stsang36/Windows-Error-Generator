
@echo off

REM Compile the app using PyInstaller
pyinstaller --paths src src/app.py --onefile --windowed

echo Build complete. Find your executable in the dist\ directory.
pause