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


@pytest.mark.parametrize("sro,syllabics", [
    ('acimosis', 'ᐊᒋᒧᓯᐢ'),
    ('atahk', 'ᐊᑕᕽ'),
    ('mêriy', 'ᒣᕒᐃᕀ'),
    ('wîstihkêw', 'ᐑᐢᑎᐦᑫᐤ'),
])
def test_single_words(sro, syllabics):
    assert sro2syllabics(sro) == syllabics


# blah blah trail (road to enoch cree nation)
# ...(hk-medial)...
# ...(sandhi)...
# test NFD accents
