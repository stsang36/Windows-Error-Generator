import pytest
import sys
from os import path, environ
import win32con

sys.path.insert(0, path.abspath(path.join(path.dirname(__file__), '../src')))

import settings
import message_box


def test_default_settings():
    s = settings.Settings()
    print(s)
    assert s.icon == win32con.MB_ICONERROR  # 16
    assert s.type == win32con.MB_OK  # 0
    assert s.default_button == win32con.MB_DEFBUTTON1  
    assert str(s) == f"Icon: {win32con.MB_ICONERROR}, Type: {win32con.MB_OK}, Default Button: {win32con.MB_DEFBUTTON1}"
    assert settings.get_list_icons_names()["MB_ICONERROR"] == win32con.MB_ICONERROR
    assert settings.get_list_types_names()["MB_OK"] == win32con.MB_OK
    assert "MB_ICONWARNING" in settings.get_list_icons_names()
    assert "MB_YESNOCANCEL" in settings.get_list_types_names()

def test_set_icon():
    s = settings.Settings()
    s.set_icon(win32con.MB_ICONWARNING)
    assert s.icon == win32con.MB_ICONWARNING

def test_set_type():
    s = settings.Settings()
    s.set_type(win32con.MB_YESNOCANCEL)
    assert s.type == win32con.MB_YESNOCANCEL

def test_set_default_button():
    s = settings.Settings()
    s.set_default_button(win32con.MB_DEFBUTTON2)
    assert s.default_button == win32con.MB_DEFBUTTON2
    
@pytest.mark.skipif(environ.get("CI") == "true", reason="Skip GUI tests in CI")
def test_message_box():
    # Test that message box can be created without error
    message_box.on_generate_button_click("Test Title", "Test Body", "OK", "ERROR")
    message_box.on_generate_button_click("Test Title", "Test Body", "YESNOCANCEL", "INFORMATION")
    message_box.on_generate_button_click("Test Title", "Test Body", "RETRYCANCEL", "WARNING")
    message_box.on_generate_button_click("Test Title", "Test Body", "ABORTRETRYIGNORE", "QUESTION")

    assert True

