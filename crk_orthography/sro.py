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
from unicodedata import normalize
from collections import ChainMap

CONSONANT = '[ptkcshmnyw]'
STRICT_VOWEL = '[aioâêîô]'
VOWEL = "{STRICT_VOWEL}|[e'āēīō]".format_map(globals())

# Match an SRO syllable.
sro_pattern = re.compile(r'''
    # A syllable that should be joined under the sandhi rule:
    # We're setting this up so that the onset (consonant and optional w) can
    # be glued together with the vowel. The parts are joined to
    # form one syllable, even though the intervening hyphen indicates that
    # they are in separate morphemes. That's sandhi!  See the front-matter in
    # Arok Wolvengrey's dictionary for more information and examples.
    #   Wolvengrey, Arok, ed. "ᓀᐦᐃᔭᐍᐏᐣ: ᐃᑗᐏᓇ / nēhiýawēwin: itwēwina/Cree:
    #   Words". Canadian Plains Research Center, October 2001. pp. xvi–xviii.

    ({CONSONANT}w?)-({STRICT_VOWEL}) |

    # Listing all of the syllables.
    # NOTE: List the longer syllable first, since
    # the regular expression will match the first alternative that will
    # work—which must be the longest match!
    wê|wi|wî|wo|wô|wa|wâ|w|
    pê|pi|pî|po|pô|pa|pâ|pwê|pwi|pwî|pwo|pwô|pwa|pwâ|p|
    tê|ti|tî|to|tô|ta|tâ|twê|twi|twî|two|twô|twa|twâ|t|
    kê|ki|kî|ko|kô|ka|kâ|kwê|kwi|kwî|kwo|kwô|kwa|kwâ|k|
    cê|ci|cî|co|cô|ca|câ|cwê|cwi|cwî|cwo|cwô|cwa|cwâ|c|
    mê|mi|mî|mo|mô|ma|mâ|mwê|mwi|mwî|mwo|mwô|mwa|mwâ|m|
    nê|ni|nî|no|nô|na|nâ|nwê|nwa|nwâ|n|
    sê|si|sî|so|sô|sa|sâ|swê|swi|swî|swo|swô|swa|swâ|s|
    yê|yi|yî|yo|yô|ya|yâ|ywê|ywi|ywî|ywo|ywô|ywa|ywâ|y|
    h|l|r|
    ê|i|î|o|ô|a|â|
    -
'''.format_map(globals()), re.VERBOSE)


# A complete SRO to syllabics look-up table.
sro2syllabics_lookup = {
    "ê": "ᐁ", "i": "ᐃ", "î": "ᐄ", "o": "ᐅ", "ô": "ᐆ", "a": "ᐊ", "â": "ᐋ",
    "wê": "ᐍ", "wi": "ᐏ", "wî": "ᐑ", "wo": "ᐓ", "wô": "ᐕ", "wa": "ᐘ", "wâ": "ᐚ", "w": "ᐤ",
    "p": "ᑊ", "pê": "ᐯ", "pi": "ᐱ", "pî": "ᐲ", "po": "ᐳ", "pô": "ᐴ", "pa": "ᐸ", "pâ": "ᐹ",
    "pwê": "ᐻ", "pwi": "ᐽ", "pwî": "ᐿ", "pwo": "ᑁ", "pwô": "ᑃ", "pwa": "ᑅ", "pwâ": "ᑇ",
    "t": "ᐟ", "tê": "ᑌ", "ti": "ᑎ", "tî": "ᑏ", "to": "ᑐ", "tô": "ᑑ", "ta": "ᑕ", "tâ": "ᑖ",
    "twê": "ᑘ", "twi": "ᑚ", "twî": "ᑜ", "two": "ᑞ", "twô": "ᑠ", "twa": "ᑢ", "twâ": "ᑤ",
    "k": "ᐠ", "kê": "ᑫ", "ki": "ᑭ", "kî": "ᑮ", "ko": "ᑯ", "kô": "ᑰ", "ka": "ᑲ", "kâ": "ᑳ",
    "kwê": "ᑵ", "kwi": "ᑷ", "kwî": "ᑹ", "kwo": "ᑻ", "kwô": "ᑽ", "kwa": "ᑿ", "kwâ": "ᒁ",
    "c": "ᐨ", "cê": "ᒉ", "ci": "ᒋ", "cî": "ᒌ", "co": "ᒍ", "cô": "ᒎ", "ca": "ᒐ", "câ": "ᒑ",
    "cwê": "ᒓ", "cwi": "ᒕ", "cwî": "ᒗ", "cwo": "ᒙ", "cwô": "ᒛ", "cwa": "ᒝ", "cwâ": "ᒟ",
    "m": "ᒼ", "mê": "ᒣ", "mi": "ᒥ", "mî": "ᒦ", "mo": "ᒧ", "mô": "ᒨ", "ma": "ᒪ", "mâ": "ᒫ",
    "mwê": "ᒭ", "mwi": "ᒯ", "mwî": "ᒱ", "mwo": "ᒳ", "mwô": "ᒵ", "mwa": "ᒷ", "mwâ": "ᒹ",
    "n": "ᐣ", "nê": "ᓀ", "ni": "ᓂ", "nî": "ᓃ", "no": "ᓄ", "nô": "ᓅ", "na": "ᓇ", "nâ": "ᓈ",
    "nwê": "ᓊ", "nwa": "ᓌ", "nwâ": "ᓎ",
    "s": "ᐢ", "sê": "ᓭ", "si": "ᓯ", "sî": "ᓰ", "so": "ᓱ", "sô": "ᓲ", "sa": "ᓴ", "sâ": "ᓵ",
    "swê": "ᓷ", "swi": "ᓹ", "swî": "ᓻ", "swo": "ᓽ", "swô": "ᓿ", "swa": "ᔁ", "swâ": "ᔃ",
    "y": "ᕀ", "yê": "ᔦ", "yi": "ᔨ", "yî": "ᔩ", "yo": "ᔪ", "yô": "ᔫ", "ya": "ᔭ", "yâ": "ᔮ",
    "ywê": "ᔰ", "ywi": "ᔲ", "ywî": "ᔴ", "ywo": "ᔶ", "ywô": "ᔸ", "ywa": "ᔺ", "ywâ": "ᔼ",
    "l": "ᓬ", "r": "ᕒ", "h": "ᐦ", "hk": "ᕽ",
}


# TODO: Document these regular expressions:
ONSET = '[ptkcshmny]w?|w'
CODA = '[hs]?[ptkcmn]|h|s|y|w'
SYLLABLE = '(?:{ONSET})?(?:{VOWEL})(?:{CODA})?|r|l'.format_map(globals())
SYLLABLES = r'(?:{SYLLABLE})+'.format_map(globals())
WORD = r'\b{SYLLABLES}(?:(?:{CODA})?-{SYLLABLES})*\b'.format_map(globals())
word_pattern = re.compile(WORD, re.IGNORECASE)

# Converts macron and alternate forms of vowels into "canonical" forms.
TRANSLATE_ALT_FORMS = str.maketrans("ā'īōeē",
                                    'âiîôêê')


def sro2syllabics(sro: str, sandhi: bool = True) -> str:
    """
    Convert Cree words written in SRO text to syllabics.

    Finds instances of SRO words in strings, and converts them all to
    syllabics.

    >>> sro2syllabics('Eddie nitisiyikason')
    'Eddie ᓂᑎᓯᔨᑲᓱᐣ'

    Any word that does not have the "structure" of a Plains Cree word is not
    converted:

    >>> sro2syllabics('Maskêkosihk trail')
    'ᒪᐢᑫᑯᓯᕽ trail'
    >>> sro2syllabics('Maskêkosihk tireyl')
    'ᒪᐢᑫᑯᓯᕽ ᑎᕒᐁᕀᓬ'

    ``sro2syllabics()`` can handle variations in orthography. For example,
    it can convert circumflexes (âêîô):

    >>> sro2syllabics('êwêpâpîhkêwêpinamahk')
    'ᐁᐍᐹᐲᐦᑫᐍᐱᓇᒪᕽ'

    It can convert macrons (āēīō):

    >>> sro2syllabics('ēwēpâpīhkēwēpinamahk')
    'ᐁᐍᐹᐲᐦᑫᐍᐱᓇᒪᕽ'

    And it can convert an unaccented "e" just as if it had the appropriate
    accent:

    >>> sro2syllabics('ewepapihkewepinamahk')
    'ᐁᐍᐸᐱᐦᑫᐍᐱᓇᒪᕽ'

    Additionally, apostrophes are interpreted as short-i's. For example,
    converting "tânsi" will not work as expected:

    >>> sro2syllabics("tânsi")
    'ᑖᐣᓯ'

    However, add an apostrophe after the 'n' and it will work correctly:

    >>> sro2syllabics("tân'si")
    'ᑖᓂᓯ'

    Sandhi orthographic rule
    ------------------------

    In SRO, the most orthographically correct way to write certain compounds
    is to separate two *morphemes* with a hyphen. For example:

        | pîhc-âyihk — inside
        | nîhc-âyihk — outside

    However, both words are pronounced as if discarding the hyphen:

        | pîhcâyihk — inside
        | nîhcâyihk — outside

    This is called :term:`sandhi`.  When transliterated into syllabics,
    the transcription should follow the latter, blended interpretation, rather
    than the former, separated interpretation. By default, ``sro2syllabics()``
    applies the sandhi rule and joins the syllable as if there were no hyphen:

    >>> sro2syllabics('pîhc-âyihk')
    'ᐲᐦᒑᔨᕽ'

    However, if this is not desired, you can set ``sandhi=False`` as a keyword
    argument:

    >>> sro2syllabics('pîhc-âyihk', sandhi=False)
    'ᐲᐦᐨᐋᔨᕽ'

    :param str sro: the text with Cree words written in SRO.
    :param bool sandhi: whether to apply sandhi orthography rule (default:
                        ``True``).
    :return: the text with Cree words written in syllabics.
    :rtype: str
    """
    def transcode_match(match) -> str:
        return transcode_sro_word_to_syllabics(match.group(0), sandhi)
    return word_pattern.sub(transcode_match, nfc(sro))


def transcode_sro_word_to_syllabics(sro_word: str, sandhi: bool) -> str:
    """
    Transcribes one word at a time.
    """

    to_transcribe = sro_word.lower().\
        translate(TRANSLATE_ALT_FORMS)

    # Augment the lookup table with an entry for «-» so that we can simply
    # delete all instances of '-' easily.
    lookup = ChainMap({'-': ''}, sro2syllabics_lookup)

    parts = []

    match = sro_pattern.match(to_transcribe)
    while match:
        onset, vowel = match.groups()
        if sandhi and onset is not None:
            # Apply sandhi rule
            assert vowel is not None
            syllable = onset + vowel
            next_syllable_pos = match.end()
        elif onset is not None:
            # This is a consonant
            syllable = onset[:1]
            # Skip the first consonant.
            next_syllable_pos = 1
            assert syllable in CONSONANT
        else:
            syllable = match.group(0)
            next_syllable_pos = match.end()

        # Get the syllabic
        syllabic = lookup[syllable]
        parts.append(syllabic)

        # Chop off transcribed part
        to_transcribe = to_transcribe[next_syllable_pos:]
        match = sro_pattern.match(to_transcribe)

    # Special-case word-final 'hk': we did not convert it in the above loop,
    # because it can only happen at the end of words, and if we did convert it
    # in the prior loop, it would convert '-ihkwê-' -> 'ᐃᕽᐍ' instead of 'ᐃᐦᑵ'
    # as intended. We know the end of the word is 'hk' because it got
    # converted to «ᐦ» followed by «ᐠ».
    if parts[-2:] == ['ᐦ', 'ᐠ']:
        parts[-2:] = [sro2syllabics_lookup['hk']]

    assert to_transcribe == '', 'could not transcribe %r' % (to_transcribe)
    return ''.join(parts)


def nfc(text):
    """
    Return NFC-normalized text.
    """
    return normalize('NFC', text)


def test_word_pattern():
    """
    Test that the WORD regex can match entire nêhiyawêwin words and loanwords,
    NFC-normalized.
    """
    entire_word = re.compile('^' + WORD + '$')
    assert entire_word.match("n'")
    assert entire_word.match('amisk')
    assert entire_word.match('meriy')
    assert entire_word.match('waskahikanahk')
