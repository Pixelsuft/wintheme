import ctypes
from . import flags


def get_theme(value_name: str) -> int:
    return flags.THEME_UNKNOWN


def get_system_theme() -> int:
    return get_theme('SystemUsesLightTheme')


def get_apps_theme() -> int:
    return get_theme('AppsUseLightTheme')


def create_bool_buffer(boolean: bool) -> ctypes.c_buffer:
    return ctypes.c_buffer(
        bytes([int(boolean), 0x00, 0x00, 0x00])
    )


def set_window_theme(hwnd: int, theme: int) -> int:
    return flags.ERROR_NOT_WINDOWS
