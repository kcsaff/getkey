# Script used to generate getkey/unikeys.py

from __future__ import absolute_import, print_function
import sys
sys.path.insert(0, '..')
try:
    from urllib2 import urlopen
except ImportError:
    from urllib.request import urlopen
import argparse
import string
import itertools


UNIDATA = 'ftp://ftp.unicode.org/Public/UNIDATA/NamesList.txt'


MAX_CODE = 0x7f


PRINTABLE_SET = set(string.printable)


def format_name(name):
    if ',' in name:
        return itertools.chain(*(format_name(subname) for subname in name.split(',')))
    name = name.upper().strip()
    if '(' in name:
        name = name[:name.find('(')].strip()
    name = name.replace(' ', '_').replace('-', '_')
    if set(name).issubset(PRINTABLE_SET):
        return [name]
    else:
        return []


def print_name(name, char):
    for name in format_name(name):
        print('{} = {!r}'.format(name, char))


def parse_unicode_names(text, max_code=MAX_CODE, min_code=0):
    code = -1
    for line in text.splitlines():
        if line[0].startswith('0'):
            code, name = line.split(None, 1)
            code = int(code, 16)
            if code > max_code:
                break
            char = chr(code)
            if code >= min_code and name == name.upper():
                for name in format_name(name):
                    yield (name, char)
        elif code >= min_code and line.startswith('\t= '):
            name = line[3:].strip()
            for name in format_name(name):
                yield (name, char)


def main():
    response = urlopen(UNIDATA)
    text = response.read()
    print('class UnicodeAsciiKeys(object):')
    for name, char in parse_unicode_names(text):
        print('    {} = {!r}'.format(name, char))


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description=
        '''Parse unicode names & write as `UnicodeAsciiKeys` class.'''
    )
    parser.parse_args()
    main()
