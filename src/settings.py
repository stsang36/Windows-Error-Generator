
import win32con
from enum import Enum

class MBIcon(Enum):
    ERROR = win32con.MB_ICONERROR
    QUESTION = win32con.MB_ICONQUESTION
    WARNING = win32con.MB_ICONWARNING
    INFORMATION = win32con.MB_ICONINFORMATION

class MBType(Enum):
    OK = win32con.MB_OK
    OKCANCEL = win32con.MB_OKCANCEL
    ABORTRETRYIGNORE = win32con.MB_ABORTRETRYIGNORE
    YESNOCANCEL = win32con.MB_YESNOCANCEL
    YESNO = win32con.MB_YESNO
    RETRYCANCEL = win32con.MB_RETRYCANCEL


class Settings:
    def __init__(self) -> None:

        self.icon = win32con.MB_ICONERROR
        self.type = win32con.MB_OK
        self.default_button = win32con.MB_DEFBUTTON1

    def __str__(self) -> str:
        return f"Icon: {self.icon}, Type: {self.type}, Default Button: {self.default_button}"



def get_list_icons_names() -> dict[str, int]:
    icons = dict[str, int]()

    for attr in dir(win32con):
        if attr.startswith("MB_ICON"):
            icons[attr] = getattr(win32con, attr)
    
    return icons

def get_list_types_names() -> dict[str, int]:
    types = dict[str, int]()

    for attr in dir(win32con):
        if attr.startswith("MB_") and not attr.startswith("MB_ICON") and not attr.startswith("MB_DEFBUTTON"):
            types[attr] = getattr(win32con, attr)
    
    return types


        
