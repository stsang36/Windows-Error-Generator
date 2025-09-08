# Windows Error Message Generator
Generate Windows errors of your choosing and input. Uses the Win32API to generate these messages. 

![Main App](images/Demo1.png?raw=true)

## Pre-requisites:
- Windows
- Python

## Installation:
1. Use the Python package manager to install the required libraries ```pip install -r requirements.txt```
2. Launch ```app.py``` in src folder.
3. A window should pop up, and you should be able to input text and generate messages of your choosing.

Note: You can compile this into a single excutable by running the ```build.cmd``` file located in the root directory. You will need to have PyInstaller installed ```pip install pyinstaller```.

## Required Libraries:
- customtkinter
- pywin32

## Optional Libraries (for development):
- pytest (for testing)
- pyinstaller (for compiling into an executable)
