#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

from crk_orthography import sro2syllabics


def test_simple():
    assert sro2syllabics('acimosis') == 'ᐊᒋᒧᓯᐢ'
    assert sro2syllabics('atahk') == 'ᐊᑕᕽ'


# meriy
# blah blah trail (road to enoch cree nation)
# ...(hk-medial)...
# ...(sandhi)...
# test NFD accents
