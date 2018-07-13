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


# Match an SRO syllable.
sro_pattern = re.compile(r'''
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
    ê|i|î|o|ô|a|â
''', re.VERBOSE)


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


ONSET = '[ptkcshmny]w?|w'
VOWEL = "[aâi'îoôêe]"
CODA = '[hs]?[ptkcmn]|h|s|y|w'
SYLLABLE = '(?:{ONSET})?{VOWEL}(?:{CODA})?|r|l'.format(**globals())
WORD = r'\b(?:{SYLLABLE})+\b'.format(**globals())
word_pattern = re.compile(WORD, re.IGNORECASE)


def sro2syllabics(sro_text: str) -> str:
    """
    Converts SRO text to syllabics.
    """
    def transcode_match(match) -> str:
        return transcode_sro_word_to_syllabics(match.group(0))
    return word_pattern.sub(transcode_match, nfc(sro_text))


def transcode_sro_word_to_syllabics(sro_word) -> str:
    """
    Transcribes one word at a time.
    """

    to_transcribe = sro_word.lower().\
        replace('e', 'ê').replace("'", 'i')

    parts = []

    match = sro_pattern.match(to_transcribe)
    while match:
        # Get the syllabic
        syllabic = sro2syllabics_lookup[match.group(0)]
        parts.append(syllabic)
        # Chop off transcribed part
        to_transcribe = to_transcribe[match.end():]
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
