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

"""
Defines command line applications.
"""

import sys

from crk_orthography import sro2syllabics, syllabics2sro


def convert_with(converter: str) -> None:
    """
    Runs the converter on each line and prints the result.
    """
    for line in sys.stdin:
        print(converter(line), end='')


def syllabics2sro_cli() -> None:
    convert_with(syllabics2sro)


def sro2syllabics_cli() -> None:
    convert_with(sro2syllabics)
