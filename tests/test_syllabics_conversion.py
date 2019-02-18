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

import pytest  # type: ignore

from cree_sro_syllabics import sro2syllabics, syllabics2sro

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
    ('obviously english text', 'obviously english text'),
    ('write nêhiyawêwin', 'write ᓀᐦᐃᔭᐍᐏᐣ'),
    ('\t namoya  tataspêyihtam. ', '\t ᓇᒧᔭ  ᑕᑕᐢᐯᔨᐦᑕᒼ᙮ '),
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
    assert syllabics2sro(syllabics, produce_macrons=True) == sro


@pytest.mark.parametrize("sro,syllabics", [
    # NOTE: the embedded NARROW NO-BREAK SPACE (NNBSP) characters
    # in the syllabics transliteration may not render properly in
    # fixed-width fonts!
    ('paskwâwi-mostos', 'ᐸᐢᒁᐏ ᒧᐢᑐᐢ'),
    ('amiskwaciy-waskahikan', 'ᐊᒥᐢᑿᒋᕀ ᐘᐢᑲᐦᐃᑲᐣ'),
    ('kâ-mahihkani-pimohtêt isiyihkâsow', 'ᑳ ᒪᐦᐃᐦᑲᓂ ᐱᒧᐦᑌᐟ ᐃᓯᔨᐦᑳᓱᐤ'),
])
def test_hyphens(sro, syllabics):
    """
    Tests that intraword hyphens are converted to NARROW NO-BREAK SPACE
    characters in the transliteration.
    """
    assert sro2syllabics(sro) == syllabics ==\
        sro2syllabics(sro, hyphens="\N{NARROW NO-BREAK SPACE}")
    assert syllabics2sro(syllabics) == sro


@pytest.mark.parametrize("sro,syllabics,hyphens,alt_syllabics", [
    ('osk-âya', 'ᐅᐢᑳᔭ', '', 'ᐅᐢᐠᐋᔭ'),
    # NOTE: this /still/ might not be the right transliteration, but
    # the correct transliteration requires even more phonological knowledge,
    # so I'm not even going to go there...
    ('miyw-âyâw', 'ᒥᔼᔮᐤ', '', 'ᒥᕀᐤᐋᔮᐤ'),
    ('pîhc-âyihk', 'ᐲᐦᒑᔨᕽ', '', 'ᐲᐦᐨᐋᔨᕽ'),

    # NOTE: not orthographically correct, but demonstrates Sandhi in th-Cree
    ('wîhth-owin', 'ᐑᐦᖪᐏᐣ', '', 'ᐑᐦᖮᐅᐏᐣ'),
])
def test_sandhi(sro, syllabics, hyphens, alt_syllabics):
    """
    Test that sandhi orthographic rule is applied when converting to
    syllabics.

    See: Wolvengrey 2001, pp. xxvi–xviii
    """
    assert sro2syllabics(sro) == sro2syllabics(sro, sandhi=True) == syllabics
    assert sro2syllabics(sro, sandhi=False, hyphens=hyphens) == alt_syllabics


@pytest.mark.parametrize("sro,syllabics", [
    ('êtî nitisiyihkâson.', 'ᐁᑏ ᓂᑎᓯᔨᐦᑳᓱᐣ᙮'),
    ('She told Dr. Thunder: "ninôhtêhkatân."',
        'She told Dr. Thunder: "ᓂᓅᐦᑌᐦᑲᑖᐣ᙮"'),
    ('tânisi. êtî nitisiyihkâson. ', 'ᑖᓂᓯ᙮ ᐁᑏ ᓂᑎᓯᔨᐦᑳᓱᐣ᙮ '),
])
def test_full_stop(sro, syllabics):
    """
    Tests that full stops in SRO get converted into
    <U+166E CANADIAN SYLLABICS FULL STOP>, and vice-versa.
    """
    assert sro2syllabics(sro) == syllabics
    assert syllabics2sro(syllabics) == sro


@pytest.mark.parametrize("original_syllabics,sro,clean_syllabics", [
    ('ᐋᐧᐱ ᑭᐦᐃᐤ', 'wâpi kihiw', 'ᐚᐱ ᑭᐦᐃᐤ'),
    ('ᐋᐱᐦᑕᐃᐧᑯᓯᓵᐣᐃᐢᑫᐧᐤ', 'âpihtawikosisâniskwêw', 'ᐋᐱᐦᑕᐏᑯᓯᓵᓂᐢᑵᐤ'),
])
def test_final_middle_dot(original_syllabics, sro, clean_syllabics):
    """
    Test that final middle dots <U+1427> get converted into their "w" syllabic
    equivilent.
    """
    assert syllabics2sro(original_syllabics) == sro
    assert sro2syllabics(syllabics2sro(original_syllabics)) == clean_syllabics


@pytest.mark.parametrize("erroneous_syllabics,sro,correct_syllabics", [
    ('ᐚᐸ\u1466', 'wâpam', 'ᐚᐸᒼ'),  # ᑦ|ᒼ <U+1466 CANADIAN SYLLABICS T>
    ('ᓂᐲ\u1541', 'nipîhk', 'ᓂᐲᕽ'),  # ᕁ|ᕽ <U+1541 CANADIAN SYLLABICS SAYISI YI>
    ('ᓂᐱ\u1429', 'nipiy', 'ᓂᐱᕀ'),  # ᐩ|ᕀ <U+1429 CANADIAN SYLLABICS FINAL PLUS>
])
def test_syllabics_lookalikes(erroneous_syllabics, sro, correct_syllabics):
    assert erroneous_syllabics != correct_syllabics
    assert syllabics2sro(erroneous_syllabics) == sro
    assert sro2syllabics(syllabics2sro(erroneous_syllabics)) ==\
        correct_syllabics


@pytest.mark.parametrize("original_sro,syllabics,sro", [
    ("tân'si", 'ᑖᓂᓯ', 'tânisi'),
    ("tân\N{RIGHT SINGLE QUOTATION MARK}si", 'ᑖᓂᓯ', 'tânisi'),
])
def test_short_i_ellision(original_sro, syllabics, sro):
    """
    Test that an apostrophe can be substituted instead of a short-i.
    """
    assert sro2syllabics(original_sro) == syllabics
    assert syllabics2sro(sro2syllabics(original_sro)) == sro


@pytest.mark.parametrize('sro,syllabics', [
    # I've anecdotally noticed that Saskatchewan writers prefer macrons,
    # and th-dialect is primarily spoke in northern Saskatchewan,
    # hence, long vowels in this test are written with macrons.
    ('wīhthēw', 'ᐑᐦᖧᐤ'),
    ('nampithi-sīpīhk', 'ᓇᒼᐱᖨ ᓰᐲᕽ'),
    ('mithomon', 'ᒥᖪᒧᐣ'),
    ('namōtha', 'ᓇᒨᖬ'),
    ('thāhkan', 'ᖭᐦᑲᐣ'),
    ('namēpith', 'ᓇᒣᐱᖮ'),
    # Test each syllable.
    ('thē thi tho tha thī thō thā', 'ᖧ ᖨ ᖪ ᖬ ᖩ ᖫ ᖭ'),
])
def test_cree_th_dialect(sro, syllabics):
    assert sro2syllabics(sro) == syllabics
    assert syllabics2sro(syllabics, produce_macrons=True) == sro


def test_rare_nwV_forms():
    """
    Not all nwV forms are attested in Western Cree. Only
    nwe, nwa, and nwâ exist. However, the UCAS Extended block includes Ojibway
    syllabics that fill in the rest of the nwV syllabics.  For now, I am NOT
    including the Ojibway syllabics; only the syllabics explicitly intended
    for Plains Cree.
    """
    assert sro2syllabics('nwe nwa nwā') == 'ᓊ ᓌ ᓎ'


def test_word_cannot_match_adjacent_vowels():
    """
    The word matching should not be able to match adjacent, de-normalized vowels.
    """
    assert sro2syllabics("I'm") == "I'm"


@pytest.mark.parametrize('sro,syllabics', [
    ('âh-ayinânêw', 'ᐋᐦᐊᔨᓈᓀᐤ'),
    ('âh-ayîtaw', 'ᐋᐦᐊᔩᑕᐤ'),
    ('mistah-âya', 'ᒥᐢᑕᐦᐋᔭ'),
    # This is a fake word, but it tests an edge case:
    ('atihw-âya', 'ᐊᑎᐦᐚᔭ'),
])
def test_sandhi_with_h(sro, syllabics):
    """
    https://github.com/eddieantonio/cree-sro-syllabics/issues/17
    """
    assert sro2syllabics(sro, sandhi=True) == syllabics
