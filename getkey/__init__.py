from __future__ import absolute_import
from .platforms import platform

__platform = platform()
getkey = __platform.getkey
key = __platform.key
bang = __platform.bang

__all__ = [getkey, key, bang, platform]

__version__ = '1.1.1'
