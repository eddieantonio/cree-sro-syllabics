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

import re

from .sro import sro2syllabics_lookup


# Derive the Syllabics -> SRO lookup table from the SRO -> Syllabics table.
syllabics2sro_lookup = {syl: sro for sro, syl in sro2syllabics_lookup.items()}
# Initially, no syllabics should map to an SRO string more than once
# (hence, the two tables should have an equal amount of entries).
assert len(syllabics2sro_lookup) == len(sro2syllabics_lookup)
# Add alternate and "look-alike" forms:
syllabics2sro_lookup.update({
    # Some communities use the ᐝ symbol instead of ᕀ for the y-final.
    # See:
    # https://en.wikipedia.org/w/index.php?title=Plains_Cree&oldid=848160114#Canadian_aboriginal_syllabics
    # for an explanation of this special y-final.
    '\N{CANADIAN SYLLABICS Y-CREE W}': 'y'
})

# Translation table to convert syllabics to SRO.
SYLLABICS_TO_SRO = str.maketrans(syllabics2sro_lookup)

# Match a stretch of characters entirely within the CANADIAN SYLLABICS block.
syllabics_pattern = re.compile(r'[\u1400-\u167f]+')

circumflex_to_macrons = str.maketrans('âêîô',
                                      'āēīō')


def syllabics2sro(syllabics: str, produce_macrons=False) -> str:
    """
    Convert Cree words written in syllabics to SRO.

    Finds all instances of syllabics in the given string, and converts it to
    SRO. Anything that is not written in
    syllabics is simply ignored:

    >>> syllabics2sro('Eddie ᓂᑎᓯᔨᑲᓱᐣ')
    'Eddie nitisiyikason'

    By default, the SRO will be produced with circumflexes (âêîô):

    >>> syllabics2sro('ᐁᐍᐹᐲᐦᑫᐍᐱᓇᒪᕽ')
    'êwêpâpîhkêwêpinamahk'

    This can be changed to macrons (āēīō) by setting ``produce_macrons`` to
    ``True``:

    >>> syllabics2sro('ᐁᐍᐹᐲᐦᑫᐍᐱᓇᒪᕽ', produce_macrons=True)
    'ēwēpāpīhkēwēpinamahk'

    In both cases, the character produced will be a pre-composed character,
    rather than an ASCII character followed by a combining diacritical mark.

    :param str syllabics: the text with Cree words written in syllabics.
    :param produce_macrons: if ``True``, produces macrons (āēīō) instead of
                            circumflexes (âêîô).
    :return: the text with Cree words written in SRO.
    :rtype: str
    """
    def replace_syllabics(match):
        return transcribe_syllabics_word_to_sro(match.group(0))

    sro_string = syllabics_pattern.sub(replace_syllabics, syllabics)

    if produce_macrons:
        return sro_string.translate(circumflex_to_macrons)
    return sro_string


def transcribe_syllabics_word_to_sro(word):
    return word.translate(SYLLABICS_TO_SRO)
