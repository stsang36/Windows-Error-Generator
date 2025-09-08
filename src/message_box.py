import settings as s
import win32api

settings = s.Settings()


def on_generate_button_click(title: str, body: str, type_msg: str, icon: str) -> None:
    # convert the type and icon from string to int
    type_int = getattr(s.MBType[type_msg], "value", s.Settings().type)
    icon_int = getattr(s.MBIcon[icon], "value", s.Settings().icon)

    
    win32api.MessageBox(
        0, body, title,
        icon_int | type_int | settings.default_button
    )

    settings.set_icon(icon_int)
    settings.set_type(type_int)
    # default button is not changed for now