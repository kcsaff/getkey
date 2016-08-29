
See it at:

- `pypi`_
- `GitHub`_

==============  ===============  =========  ============
VERSION         DOWNLOADS        TESTS      COVERAGE
==============  ===============  =========  ============
|pip version|   |pip downloads|  |travis|   |coveralls|
==============  ===============  =========  ============

Library to easily read single chars and key strokes.


Quick Start
===========

.. code:: python

  from getkey import getkey, keys
  key = getkey()
  if key == keys.UP:
    ...  # Handle the UP key
  elif key == keys.DOWN:
    ...  # Handle the DOWN key
  elif key == 'a':
    ...  # Handle the `a` key
  elif key == 'Y':
    ...  # Handle `shift-y`
  else:
    # Handle other text characters
    buffer += key
    print(buffer)

History
=======


This library seems to have started as a gist by Danny Yoo & made the rounds in
various versions until Miguel Ángel García turned it into a portable package
for their `python-inquirer`_ project.  Then K.C.Saff forked it & smashed it
into this new form for their own command line input library.


Philosophy
==========


Keys will be returned as strings representing the received key codes, however
as some keys may have multiple possible codes on a platform, the key code will
be canonicalized so you can test :code:`key == keys.UP` instead of
:code:`key in keys.UP`. This means non-control keys will be returned just as
the text they represent, and you can just as easily test :code:`key == 'a'` to
see if the user pressed :code:`a`.

In addition, by default we will throw :code:`KeyboardInterrupt` for
:code:`Ctrl-C` which would otherwise be suppressed.  However, it is possible
to disable this if you wish:

.. code:: python

  from getkey import plaform
  my_platform = platform(interrupts={})
  my_getkey = my_platform.getkey


Now :code:`my_getkey` will be a function returning keys that won't throw on
:code:`Ctrl-C`. Warning!  This may make it difficult to exit a running script.


Plans
=====


This library will not hit 1.0 until we can verify it works correctly with
unicode & international keyboards.  This is not yet tested.



Documentation
=============

Installation
------------

::

   pip install getkey

The :code:`getkey` library is compatible with python 2.7, and 3.2+.

Usage
-----

Usage example:

.. code:: python

  from getkey import getkey, keys
  key = getkey()
  if key == keys.UP:
    ...  # Handle the UP key
  elif key == keys.DOWN:
    ...  # Handle the DOWN key
  ... # Handle all other desired control keys
  else:  # Handle text characters
    buffer += key
    print(buffer)


Please consult :code:`tools/keys.txt` for a full list of key names available on
different platforms, or :code:`tools/controls.txt` for the abridged version
just containing control (normally non-printing) characters.

API
----

There is one primary method:

:code:`getkey(blocking=True)`
/////////////////////////////

Reads the next key-stroke from :code:`stdin`, returning it as an string.

A key-stroke can have:

- 1 character for normal keys: 'a', 'z', '9'...
- 1 character for certain control combinations: '\x01' as Ctrl-A, for example
- more for other control keys (system dependent, but with portable names)
- check :code:`tools/keys.txt` for keys available on different systems.

Interpreting the keycode response is made easier with the :code:`keys` object:

:code:`keys`
////////////

Contains portable names for keys, so that :code:`keys.UP` will mean the up
key on both Linux or Windows, even though the actual key codes are
different.

Because the list of key names is generated dynamically, please consult
:code:`tools/keys.txt` for a full list of key names.  It is not necessary to
use key names for single characters: if the user pushes `a` the key returned
is very portably just that single character `a` itself.

:code:`keys.name(code)`
///////////////////////

Returns the canonical name of the key which yields this key code on this
platform.  One key code may have multiple aliases, but only the canonical
name will be returned.  The canonical names are marked with an
asterisk in :code:`tools/keys.txt`.


OS Support
----------

This library has been tested on both Mac & Windows, & the Mac keys should work
much the same on Linux.  If planning to use more esoteric control keys,
please verify compatibility by checking

How to contribute
=================

You can download the code, make some changes with their tests, and make a
pull-request.

In order to develop or running the tests, you can do:

1. Clone the repository.

.. code:: bash

   git clone https://github.com/kcsaff/getkey.git

2. Create a virtual environment:

.. code:: bash

   virtualenv venv

3. Enter in the virtual environment

.. code:: bash

   source venv/bin/activate

4. Install dependencies

.. code:: bash

    pip install -r requirements.txt -r requirements-dev.txt

5. Run tests

.. code:: bash

    make


Please, **Execute the tests before any pull-request**. This will avoid invalid builds.


License
=======

Copyright (c) 2014, 2015 Miguel Ángel García (`@magmax9`_).

Copyright (c) 2016 K.C.Saff (`@kcsaff`_)

Based on previous work on gist `getch()-like unbuffered character reading from stdin on both Windows and Unix (Python recipe)`_, started by `Danny Yoo`_.

Licensed under `the MIT license`_.


.. |travis| image:: https://travis-ci.org/kcsaff/getkey.png
  :target: `Travis`_
  :alt: Travis results

.. |coveralls| image:: https://coveralls.io/repos/kcsaff/getkey/badge.png
  :target: `Coveralls`_
  :alt: Coveralls results_

.. |pip version| image:: https://img.shields.io/pypi/dd/getkey.svg
    :target: https://pypi.python.org/pypi/getkey
    :alt: Latest PyPI version

.. |pip downloads| image:: https://img.shields.io/pypi/v/getkey.svg
    :target: https://pypi.python.org/pypi/getkey
    :alt: Number of PyPI downloads

.. _pypi: https://pypi.python.org/pypi/getkey
.. _GitHub: https://github.com/kcsaff/getkey
.. _Travis: https://travis-ci.org/kcsaff/getkey
.. _Coveralls: https://coveralls.io/r/magmax/python-readchar
.. _@magmax9: https://twitter.com/magmax9
.. _@kcsaff: https://twitter.com/kcsaff
.. _python-inquirer: https://github.com/magmax/python-inquirer

.. _the MIT license: http://opensource.org/licenses/MIT
.. _getch()-like unbuffered character reading from stdin on both Windows and Unix (Python recipe): http://code.activestate.com/recipes/134892/
.. _Danny Yoo: http://code.activestate.com/recipes/users/98032/
