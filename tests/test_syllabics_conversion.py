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

import pytest

from crk_orthography import sro2syllabics

COMBINING_CIRCUMFLEX = '\u0302'


@pytest.mark.parametrize("sro,syllabics", [
    ('acimosis', 'ᐊᒋᒧᓯᐢ'),
    ('atahk', 'ᐊᑕᕽ'),
    ('mêriy', 'ᒣᕒᐃᕀ'),
    ('wîstihkêw', 'ᐑᐢᑎᐦᑫᐤ'),
    ('nêhiyawêwin', 'ᓀᐦᐃᔭᐍᐏᐣ'),
    ('tirêyl', 'ᑎᕒᐁᕀᓬ'),
])
def test_single_words(sro, syllabics):
    """
    Test single words with perfect SRO orthography.
    """
    assert sro2syllabics(sro) == syllabics


@pytest.mark.parametrize("sro,syllabics", [
    ("Tân'si", 'ᑖᓂᓯ'),
    ('Maskekosihk', 'ᒪᐢᑫᑯᓯᕽ'),
])
def test_normalize_single_words(sro, syllabics):
    """
    Test single word inputs with non-standard orthography.
    """
    assert sro2syllabics(sro) == syllabics


def test_unicode_normalization():
    """
    Test when the input string is not in NFC-normalized.
    """
    water = 'nipiy'
    leaf = 'ni' + COMBINING_CIRCUMFLEX + 'piy'
    assert water != leaf
    assert sro2syllabics(water) != sro2syllabics(leaf)
    assert sro2syllabics(water) == 'ᓂᐱᕀ'
    assert sro2syllabics(leaf) == 'ᓃᐱᕀ'


# ...(sandhi)...
# test NFD accents
