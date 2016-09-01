from __future__ import absolute_import, print_function
import sys
from .platforms import platform, PlatformError, PlatformInvalid

try:
    __platform = platform()
except PlatformError as err:
    print('Error initializing standard platform: {}'.format(err.args[0]),
          file=sys.stderr)
    __platform = PlatformInvalid()

getkey = __platform.getkey
keys = __platform.keys
key = keys  # alias
bang = __platform.bang

__version__ = '0.6.5'
