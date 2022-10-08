import ctypes
from .flags import *


if hasattr(ctypes, 'windll'):
    from .wintheme import *
else:
    from .blank import *


__version__ = '1.0.1'
