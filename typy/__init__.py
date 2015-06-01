#!/usr/bin/env python

"""A static type checker for Python"""

from typy import checker
from typy.exceptions import CheckError, NotYetSupported
import argparse
import logging


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('-v', '--verbose', action='store_true')
    parser.add_argument('file', type=open)
    args = parser.parse_args()

    if args.verbose:
        logging.basicConfig(format='%(levelname)s: %(message)s',
                            level=logging.DEBUG)

    try:
        checker.check(args.file)
        print('All checks passed!')
    except CheckError as error:
        print('Error:', error.msg)
    except NotYetSupported as error:
        print(error.msg)


if __name__ == '__main__':
    import sys

    sys.exit(main())
