
@echo off

REM Compile the app using PyInstaller
pyinstaller --paths src src/app.py --onefile --windowed --name="WinErrorGenerator" --icon=src/assets/error_icon.ico --add-data "src/assets/error_icon.ico;assets"

echo Build complete. Find your executable in the dist\ directory.
pause