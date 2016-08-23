# Simple script to verify keys read correctly & their codes

from __future__ import absolute_import, print_function
import argparse
import sys
sys.path.insert(0, '..')
from getkey import bang


def main():
    bang()


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description=
        'Type to discover key names & codes on this system. Ctrl-C to exit.'
    )
    parser.parse_args()
    main()
