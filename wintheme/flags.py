import sys


REG_PATH = 'Software\\Microsoft\\Windows\\CurrentVersion\\Themes\\Personalize'

THEME_UNKNOWN = 1 << 2
THEME_LIGHT = 2 << 2
THEME_DARK = 3 << 2

ERROR_SUCCESS = 1 << 2
ERROR_NOT_WINDOWS = 2 << 2
ERROR_FUNCTION_NOT_FOUND = 3 << 2
ERROR_UNKNOWN_THEME = 4 << 2
ERROR_NULL_HWND = 5 << 2

theme_to_string = {
    THEME_UNKNOWN: 'Unknown',
    THEME_LIGHT: 'Light',
    THEME_DARK: 'Dark'
}

error_to_string = {
    ERROR_SUCCESS: 'Success',
    ERROR_NOT_WINDOWS: f'{sys.platform.title()} is not supported',
    ERROR_FUNCTION_NOT_FOUND: 'DwmSetWindowAttribute was not found in dwmapi.dll',
    ERROR_UNKNOWN_THEME: 'Unknown theme',
    ERROR_NULL_HWND: 'Window handle is null'
}
