#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

# Copyright (C) 2018 Eddie Antonio Santos <easantos@ualberta.ca>
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as
# published by the Free Software Foundation, either version 3 of the
# License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

import sys
import argparse

from crk_orthography import sro2syllabics, syllabics2sro
from crk_orthography import __version__ as version

"""
Defines command line applications.
"""


EPILOG = 'Report bugs at https://github.com/eddieantonio/crk_orthography/issues'


def sro2syllabics_cli() -> None:
    parser = argparse.ArgumentParser(
        description='convert Cree text in SRO to syllabics',
        epilog=EPILOG
    )
    add_common_arguments(parser)
    sandhi = parser.add_mutually_exclusive_group()
    sandhi.add_argument(
            '-s', '--sandhi',
            action='store_true', dest='sandhi',
            help='apply sandhi orthographic rule'
    )
    sandhi.add_argument(
            '-S', '--no-sandhi',
            action='store_false', dest='sandhi',
            help='do not apply sandhi orthographic rule'
    )
    parser.set_defaults(sandhi=True)
    args = parser.parse_args()
    convert_with(args.filename, sro2syllabics,
                 sandhi=args.sandhi)


def syllabics2sro_cli() -> None:
    parser = argparse.ArgumentParser(
        description='convert Cree text in syllabics to SRO',
        epilog=EPILOG
    )
    add_common_arguments(parser)
    macrons = parser.add_mutually_exclusive_group()
    macrons.add_argument(
            '-^', '--circumflexes',
            action='store_false', dest='produce_macrons', default=False,
            help='write long vowels with circumflexes (âêîô) [default]'
    )
    macrons.add_argument(
            '-_', '--macrons',
            action='store_true', dest='produce_macrons',
            help='write long vowels with macrons (āēīō)'
    )
    parser.set_defaults(produce_macrons=False)
    args = parser.parse_args()
    convert_with(args.filename, syllabics2sro,
                 produce_macrons=args.produce_macrons)


def convert_with(stream: str, converter, *args, **kwargs) -> None:
    """
    Runs the suplied converter on each line and prints the result.
    """

    with stream:
        for line in stream:
            print(converter(line, *args, **kwargs), end='')


def add_common_arguments(parser) -> None:
    parser.add_argument('-v', '--version', action='version',
                        version='%(prog)s ' + version)
    parser.add_argument('filename', nargs='?',
                        help=('The filename to be converted. '
                              'If provided as a single hyphen (-) '
                              'stdin is opened instead.'),
                        type=stream_from_name,
                        default=stream_from_name())


def stream_from_name(filename=None):
    """
    Opens the filename. If the filename is '-', opens stdin (as per UNIX
    convention).
    """
    if filename is None or filename == '-':
        return sys.stdin
    return open(filename, 'r')


# if invoked as python3 -m crk_orthography, run as sro2syllabics(1)
if __name__ == '__main__':
    sro2syllabics_cli()
