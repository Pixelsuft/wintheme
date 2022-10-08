import sys


REG_PATH = 'Software\\Microsoft\\Windows\\CurrentVersion\\Themes\\Personalize'

THEME_UNKNOWN = 1 << 1
THEME_LIGHT = 1 << 2
THEME_DARK = 1 << 3

ERROR_SUCCESS = 1 << 1
ERROR_NOT_WINDOWS = 1 << 2
ERROR_FUNCTION_NOT_FOUND = 1 << 3
ERROR_UNKNOWN_THEME = 1 << 4
ERROR_NULL_HWND = 1 << 5

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
