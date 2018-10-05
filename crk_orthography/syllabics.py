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
    '\N{CANADIAN SYLLABICS Y-CREE W}': 'y',

    # Convert ᙮ into a Latin full-stop.
    '\N{CANADIAN SYLLABICS FULL STOP}': '.',

    # Look-alikes characters:
    '\N{CANADIAN SYLLABICS T}': 'm',  # ᑦ looks like ᒼ or "m"
    '\N{CANADIAN SYLLABICS SAYISI YI}': 'hk',  # ᕁ looks like ᕽ or "hk"
    '\N{CANADIAN SYLLABICS FINAL PLUS}': 'y',  # ᐩ looks like ᕀ or "y"

    # Convert NNBSP within syllabics to hyphens to support round-trip
    # conversion between syllabics and SRO.
    '\N{NARROW NO-BREAK SPACE}': '-',
})

# Translation table to convert syllabics to SRO.
SYLLABICS_TO_SRO = str.maketrans(syllabics2sro_lookup)

# For use when converting SYLLABIC + FINAL MIDDLE DOT into the syllabic with a 'w'
SYLLABIC_WITH_DOT = {
    'ᐁ': 'ᐍ', 'ᐃ': 'ᐏ', 'ᐄ': 'ᐑ', 'ᐅ': 'ᐓ', 'ᐆ': 'ᐕ', 'ᐊ': 'ᐘ', 'ᐋ': 'ᐚ',
    'ᐯ': 'ᐻ', 'ᐱ': 'ᐽ', 'ᐲ': 'ᐿ', 'ᐳ': 'ᑁ', 'ᐴ': 'ᑃ', 'ᐸ': 'ᑅ', 'ᐹ': 'ᑇ',
    'ᑌ': 'ᑘ', 'ᑎ': 'ᑚ', 'ᑏ': 'ᑜ', 'ᑐ': 'ᑞ', 'ᑑ': 'ᑠ', 'ᑕ': 'ᑢ', 'ᑖ': 'ᑤ',
    'ᑫ': 'ᑵ', 'ᑭ': 'ᑷ', 'ᑮ': 'ᑹ', 'ᑯ': 'ᑻ', 'ᑰ': 'ᑽ', 'ᑲ': 'ᑿ', 'ᑳ': 'ᒁ',
    'ᒉ': 'ᒓ', 'ᒋ': 'ᒕ', 'ᒌ': 'ᒗ', 'ᒍ': 'ᒙ', 'ᒎ': 'ᒛ', 'ᒐ': 'ᒝ', 'ᒑ': 'ᒟ',
    'ᒣ': 'ᒭ', 'ᒥ': 'ᒯ', 'ᒦ': 'ᒱ', 'ᒧ': 'ᒳ', 'ᒨ': 'ᒵ', 'ᒪ': 'ᒷ', 'ᒫ': 'ᒹ',
    'ᓀ': 'ᓊ',                                         'ᓇ': 'ᓌ', 'ᓈ': 'ᓎ',
    'ᓭ': 'ᓷ', 'ᓯ': 'ᓹ', 'ᓰ': 'ᓻ', 'ᓱ': 'ᓽ', 'ᓲ': 'ᓿ', 'ᓴ': 'ᔁ', 'ᓵ': 'ᔃ',
    'ᔦ': 'ᔰ', 'ᔨ': 'ᔲ', 'ᔩ': 'ᔴ', 'ᔪ': 'ᔶ', 'ᔫ': 'ᔸ', 'ᔭ': 'ᔺ', 'ᔮ': 'ᔼ',
}
final_dot_pattern = re.compile(r'([{without_dot}])ᐧ'.format(
    without_dot=''.join(SYLLABIC_WITH_DOT.keys())
))

circumflex_to_macrons = str.maketrans('êîôâ',
                                      'ēīōā')


def syllabics2sro(syllabics: str, produce_macrons=False) -> str:
    """
    Convert Cree words written in syllabics to SRO.

    Finds all instances of syllabics in the given string, and converts it to
    SRO. Anything that is not written in
    syllabics is simply ignored:

    >>> syllabics2sro('Eddie ᓂᑎᓯᔨᐦᑳᓱᐣ᙮')
    'Eddie nitisiyihkâson.'

    You should be able to convert words written in Y-dialect (a.k.a., Plains Cree):

    >>> syllabics2sro('ᓂᔭ')
    'niya'

    ... and Th-dialect (a.k.a., Woods Cree):

    >>> syllabics2sro('ᓂᖬ')
    'nitha'

    By default, the SRO will be produced with circumflexes (âêîô):

    >>> syllabics2sro('ᐁᐍᐹᐲᐦᑫᐍᐱᓇᒪᕽ')
    'êwêpâpîhkêwêpinamahk'

    This can be changed to macrons (āēīō) by setting ``produce_macrons`` to
    ``True``:

    >>> syllabics2sro('ᐁᐍᐹᐲᐦᑫᐍᐱᓇᒪᕽ', produce_macrons=True)
    'ēwēpāpīhkēwēpinamahk'

    In both cases, the character produced will be a pre-composed character,
    rather than an ASCII character followed by a combining diacritical mark.
    That is, vowels are returned in *NFC normalization form*.

    For compatibility with :py:meth:`crk_orthography.sro2syllabics`,
    ``syllabics2sro`` will convert any instances of \<U+202F NARROW NO BREAK
    SPACE\> to a hyphen in the SRO transliteration.

    >>> syllabics2sro('ᑳ ᒪᐦᐃᐦᑲᓂ ᐱᒧᐦᑌᐟ')
    'kâ-mahihkani-pimohtêt'

    In some syllabics text, syllabics with a 'w' dot are rendered as two
    characters: the syllabic without the 'w' dot followed by \<U+1427 CANADIAN
    SYLLABICS FINAL MIDDLE DOT\>; this differs from the more appropriate
    pre-composed syllabic character with the 'w' dot. For example,

        | ᐃᑘᐏᓇ  --- pre-composed syllabic
        | ᐃᑌᐧᐃᐧᓇ --- syllabic + ``CANADIAN SYLLABICS FINAL MIDDLE DOT``

    ``syllabics2sro()`` can convert both cases appropriately:

    >>> syllabics2sro('ᐃᑘᐏᓇ')
    'itwêwina'
    >>> syllabics2sro('ᐃᑌᐧᐃᐧᓇ')
    'itwêwina'

    Some syllabics converters produce erroneous yet very similar looking
    characters. ``syllabics2sro()`` knows the following look-alike characters:

     ================================= ==================================
      Look-alike                        Correct character
     ================================= ==================================
      ᐩ CANADIAN SYLLABICS FINAL PLUS   ᕀ CANADIAN SYLLABICS WEST-CREE Y
      ᑦ CANADIAN SYLLABICS T            ᒼ CANADIAN SYLLABICS WEST-CREE M
      ᕁ CANADIAN SYLLABICS SAYISI YI    ᕽ CANADIAN SYLLABICS HK
     ================================= ==================================

    ``syllabics2sro()`` automatically interprets erroneous look-alikes as their
    visually equivalent characters.

    >>> syllabics2sro('ᒌᐯᐦᑕᑳᐧᐱᑲᐧᓂᐩ')
    'cîpêhtakwâpikwaniy'
    >>> syllabics2sro('ᐊᓴᒧᐱᑕᑦ')
    'asamopitam'
    >>> syllabics2sro('ᒫᒥᕁ')
    'mâmihk'

    :param str syllabics: the text with Cree words written in syllabics.
    :param produce_macrons: if ``True``, produces macrons (āēīō) instead of
                            circumflexes (âêîô).
    :return: the text with Cree words written in SRO.
    :rtype: str
    """

    def fix_final_dot(match):
        "Translate syllabic + FINAL MIDDLE DOT to syllabic with 'w'"
        return SYLLABIC_WITH_DOT[match.group(1)]

    # Normalize all SYLLABIC + FINAL MIDDLE DOT to the composed variant of the
    # syllabic.
    normalized = final_dot_pattern.sub(fix_final_dot, syllabics)
    # **AFTER** normalization, translate syllabics characters to SRO
    sro_string = normalized.translate(SYLLABICS_TO_SRO)

    if produce_macrons:
        return sro_string.translate(circumflex_to_macrons)
    return sro_string
