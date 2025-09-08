from settings import Settings, MBType, MBIcon
from win32api import MessageBox

settings = Settings()


def on_generate_button_click(title: str, body: str, type_msg: str, icon: str) -> None:
    # convert the type and icon from string to int
    type_int = getattr(MBType[type_msg], "value", Settings().type)
    icon_int = getattr(MBIcon[icon], "value", Settings().icon)

    
    MessageBox(
        0, body, title,
        icon_int | type_int | settings.default_button
    )

    settings.set_icon(icon_int)
    settings.set_type(type_int)
    # default button is not changed for now