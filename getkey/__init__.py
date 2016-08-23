from __future__ import absolute_import
from .platforms import platform

__platform = platform()
getkey = __platform.getkey
keys = __platform.keys
key = keys  # alias
bang = __platform.bang

# __all__ = [getkey, key, bang, platform]

__version__ = '0.6'
