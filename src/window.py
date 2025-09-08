import customtkinter as ctk
from ctypes import windll
from typing import Callable
from message_box import on_generate_button_click
from threading import Thread

WINDOW_WIDTH = 870
WINDOW_HEIGHT = 540
BODY_TEXTBOX_WIDTH = 400
BODY_TEXTBOX_HEIGHT = 300
TITLE_X = 20
TITLE_Y = 20
PADDING_BETWEEN = 40

TITLE_INPUT_X = 20
TITLE_INPUT_Y = 160

BODY_INPUT_X = 20
BODY_INPUT_Y = TITLE_INPUT_Y + PADDING_BETWEEN

SEL_ICON_FRAME_X = BODY_INPUT_X + BODY_TEXTBOX_WIDTH + 40
SEL_ICON_FRAME_Y = BODY_INPUT_Y
SEL_ICON_FRAME_WIDTH = 200
SEL_ICON_FRAME_HEIGHT = 300

BUTTON_X = SEL_ICON_FRAME_X + SEL_ICON_FRAME_WIDTH - 30
BUTTON_Y = SEL_ICON_FRAME_Y + SEL_ICON_FRAME_HEIGHT - 30


# Window procedure
try:
    windll.shcore.SetProcessDpiAwareness(1)  # System DPI aware
except Exception:
    windll.user32.SetProcessDPIAware()  # Fallback for older Windows

class Window(ctk.CTk):

    def __init__(self) -> None:
        super().__init__()
        self.title("Windows Error Generator")
        self.geometry(f"{WINDOW_WIDTH}x{WINDOW_HEIGHT}")
        self.resizable(False, False)
        
        self.headers: dict[str, ctk.CTkLabel] = dict[str, ctk.CTkLabel]()
        headers(self)
        self.body_input = input_body_field(self)
        self.title_input = input_title_field(self)
        self.icon_frame = selector_frame_error_icon(self)
        self.button_frame = selector_frame_types(self)

        self.icon: ctk.StringVar 
        self.type: ctk.StringVar 
        self.gen_button = generate_button(
            self,
            error_message_run=lambda: on_generate_button_click(
                self.get_title_text(),
                self.get_body_text(),
                self.get_type(),
                self.get_icon()
            )
        )

    def __str__(self) -> str:
        return f"Window(title={self.get_title_text()}, body={self.get_body_text()}, icon={self.get_icon()}, type={self.get_type()})"

    def get_body_text(self) -> str:
        return self.body_input.get("1.0", "end").strip()
    
    def get_title_text(self) -> str:
        return self.title_input.get()
    
    def get_icon(self) -> str:
        return self.icon.get()
    
    def get_type(self) -> str:
        return self.type.get()
    
    def add_headers(self, name:str, label: ctk.CTkLabel) -> None:
        # get current header dict and append new headers
        self.headers[name] = label
    
    
        


def input_body_field(w: Window) -> ctk.CTkTextbox:

        # Text box for message body
    text_box = ctk.CTkTextbox(w, width=BODY_TEXTBOX_WIDTH, height=BODY_TEXTBOX_HEIGHT)
    text_box.place(x=BODY_INPUT_X, y=BODY_INPUT_Y)

    label = ctk.CTkLabel(w, text="Message Body:", font=ctk.CTkFont(size=16))
    label.place(x=BODY_INPUT_X, y=BODY_INPUT_Y - PADDING_BETWEEN)

    w.add_headers("body_label", label)
    return text_box

def input_title_field(w: Window) -> ctk.CTkEntry:
    # Entry for title
    title_entry = ctk.CTkEntry(w, width=300)
    title_entry.place(x=TITLE_INPUT_X, y=TITLE_INPUT_Y - PADDING_BETWEEN)

    label = ctk.CTkLabel(w, text="Title:", font=ctk.CTkFont(size=16))
    label.place(x=TITLE_INPUT_X, y=TITLE_INPUT_Y - PADDING_BETWEEN - 30)

    w.add_headers("title_label", label)
    return title_entry
        

def headers(w: Window) -> None:
    title = ctk.CTkLabel(w, text="Windows Error Generator", font=ctk.CTkFont(size=24, weight="bold"))
    title.place(x=TITLE_X, y=TITLE_Y)
    subtitle = ctk.CTkLabel(w, text="Generate custom Windows error messages", font=ctk.CTkFont(size=16))
    subtitle.place(x=TITLE_X, y= TITLE_Y + PADDING_BETWEEN)

    
    w.add_headers("title", title)
    w.add_headers("subtitle", subtitle)

    return

def selector_frame_error_icon(w: Window) -> ctk.CTkFrame:
    # radio buttons for error icon selection
    frame = ctk.CTkFrame(w, width=SEL_ICON_FRAME_WIDTH, height=SEL_ICON_FRAME_HEIGHT)
    frame.place(x=SEL_ICON_FRAME_X, y=SEL_ICON_FRAME_Y)
    label = ctk.CTkLabel(frame, text="Select Icon:", font=ctk.CTkFont(size=16))
    label.pack(pady=10)
    w.add_headers("select_icon_label", label)

    icon_var = ctk.StringVar(value="ERROR")
    icons = ['ERROR', 'QUESTION', 'WARNING', 'INFORMATION']
    for icon_name in icons:
        radio = ctk.CTkRadioButton(
            frame,
            text=icon_name.capitalize(),
            variable=icon_var,
            value=icon_name
        )
        radio.pack(anchor="w", padx=20, pady=10)
    w.icon = icon_var


    return frame

def selector_frame_types(w: Window) -> ctk.CTkFrame:
    # radio buttons for error type selection
    frame = ctk.CTkFrame(w, width=SEL_ICON_FRAME_WIDTH, height=SEL_ICON_FRAME_HEIGHT)
    frame.place(x=SEL_ICON_FRAME_X + SEL_ICON_FRAME_WIDTH - 30, y=SEL_ICON_FRAME_Y)
    label = ctk.CTkLabel(frame, text="Select Type:", font=ctk.CTkFont(size=16))
    label.pack(pady=10)
    w.add_headers("select_type_label", label)

    type_var = ctk.StringVar(value="OK")
    
    #types = ['OK', 'OKCANCEL', 'ABORTRETRYIGNORE', 'YESNOCANCEL', 'YESNO', 'RETRYCANCEL']
    types = dict(
        OK='OK',
        OKCANCEL='OK / CANCEL',
        ABORTRETRYIGNORE='ABORT / RETRY / IGNORE',
        YESNOCANCEL='YES / NO / CANCEL',
        YESNO='YES / NO',
        RETRYCANCEL='RETRY / CANCEL'
    )
    
    for type_name, type_label in types.items():
        radio = ctk.CTkRadioButton(
            frame,
            text=type_label,
            variable=type_var,
            value=type_name
        )
        radio.pack(anchor="w", padx=20, pady=5)
    
    w.type = type_var


    return frame

def generate_button(w: Window, error_message_run: Callable) -> ctk.CTkButton:
    btn = ctk.CTkButton(w, text="Generate Error", command=lambda: Thread(target=error_message_run).start())
    btn.place(x=BUTTON_X, y=BUTTON_Y)
    return btn