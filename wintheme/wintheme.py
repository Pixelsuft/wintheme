import ctypes
import ctypes.wintypes
import winreg
from . import flags


try:
    dwm = ctypes.windll.dwmapi
    try:
        DwmSetWindowAttribute = dwm.DwmSetWindowAttribute
        DwmSetWindowAttribute.argtypes = (
            ctypes.wintypes.HWND,
            ctypes.wintypes.DWORD,
            ctypes.wintypes.LPCVOID,
            ctypes.wintypes.DWORD
        )
        DwmSetWindowAttribute.restype = ctypes.wintypes.LONG
    except AttributeError:
        DwmSetWindowAttribute = None
except FileNotFoundError:
    dwm = None


def get_theme(value_name: str) -> int:
    try:
        key = winreg.OpenKeyEx(winreg.HKEY_CURRENT_USER, flags.REG_PATH)
    except FileNotFoundError:
        return flags.THEME_UNKNOWN
    try:
        value = winreg.QueryValueEx(key, value_name)[0]
        if value == 1:
            result = flags.THEME_LIGHT
        elif value == 0:
            result = flags.THEME_DARK
        else:
            result = flags.THEME_UNKNOWN
    except FileNotFoundError:
        result = flags.THEME_UNKNOWN
    winreg.CloseKey(key)
    return result


def get_system_theme() -> int:
    return get_theme('SystemUsesLightTheme')


def get_apps_theme() -> int:
    return get_theme('AppsUseLightTheme')


def create_bool_buffer(boolean: bool) -> ctypes.c_buffer:
    return ctypes.c_buffer(
        bytes([int(boolean), 0x00, 0x00, 0x00])
    )


def set_window_theme(hwnd: int, theme: int) -> int:
    if not hwnd:
        return flags.ERROR_NULL_HWND
    if not theme == flags.THEME_LIGHT and not theme == flags.THEME_DARK:
        return flags.ERROR_UNKNOWN_THEME
    if dwm is None or DwmSetWindowAttribute is None:
        return flags.ERROR_FUNCTION_NOT_FOUND
    buffer1 = create_bool_buffer(theme == flags.THEME_DARK)
    if not DwmSetWindowAttribute(hwnd, 20, buffer1, ctypes.sizeof(buffer1)):
        buffer2 = create_bool_buffer(theme == flags.THEME_DARK)
        DwmSetWindowAttribute(hwnd, 19, buffer2, ctypes.sizeof(buffer2))
    return flags.ERROR_SUCCESS
