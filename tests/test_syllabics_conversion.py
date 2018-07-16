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

from crk_orthography import sro2syllabics, syllabics2sro

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
    # Converting SRO to syllabics should work.
    assert sro2syllabics(sro) == syllabics
    # Converting syllabics to SRO should work.
    assert syllabics2sro(syllabics) == sro
    # With "perfect" orthography, each roundtrip should leave the input
    # unchanged.
    assert sro2syllabics(syllabics2sro(syllabics)) == syllabics
    assert syllabics2sro(sro2syllabics(sro)) == sro


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


@pytest.mark.parametrize("sro,syllabics", [
    ('\t namoya  tataspêyihtam. ', '\t ᓇᒧᔭ  ᑕᑕᐢᐯᔨᐦᑕᒼ. '),
    ('obviously english text', 'obviously english text'),
    ('write nêhiyawêwin', 'write ᓀᐦᐃᔭᐍᐏᐣ'),
])
def test_multiple_words(sro, syllabics):
    """
    Test transcoding multiple words. The test inputs here can be trivially
    converted back-and-forth.
    """
    assert sro2syllabics(sro) == syllabics
    assert syllabics2sro(syllabics) == sro


def test_alternate_y_final():
    """
    From Wikipedia:

    Some Plains Cree communities use a final for y which is different from the
    usual western final. This is a superposed dot ᐝ, instead of the usual ᐩ,
    as in ᓰᐱᐩ (ᓰᐱᐝ) sīpiy “river". When the dot y-final is placed after a
    syllabic which has a w-dot, the two dots combine to form a colon-like
    symbol, as in ᓅᐦᑖᐏᐩ (ᓅᐦᑖᐃ᛬) nōhtāwiy “my father".
    """
    syllabics = 'ᓰᐱᐝ'
    sro = 'sîpiy'
    assert syllabics2sro(syllabics) == sro


@pytest.mark.parametrize("sro,syllabics", [
    ('yōtinipēstāw', 'ᔫᑎᓂᐯᐢᑖᐤ'),
    ('īkatē', 'ᐄᑲᑌ'),
])
def test_macrons(sro, syllabics):
    """
    Test that macrons can be converted
    """
    assert sro2syllabics(sro) == syllabics


# TODO: test replace - with soft hyphen
# TODO: ...(sandhi)...
# TODO: test look-alikes.
