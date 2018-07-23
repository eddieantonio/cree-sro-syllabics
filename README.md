Plains Cree Orthography
=======================

[![Build Status](https://travis-ci.org/eddieantonio/crk_orthography.svg?branch=master)](https://travis-ci.org/eddieantonio/crk_orthography)
[![Documentation Status](https://readthedocs.org/projects/crk-orthography/badge/?version=stable)](https://crk-orthography.readthedocs.io/en/stable/?badge=stable)
[![PyPI package](https://img.shields.io/pypi/v/crk_orthography.svg)](https://pypi.org/project/crk_orthography/)
[![Calver MAJOR.YYYY0M0D.PATCH](https://img.shields.io/badge/calver-MAJOR.YYYY0M0D.PATCH-22bfda.svg)](http://calver.org/)

Convert between nêhiyawêwin/ᓀᐦᐃᔭᐍᐏᐣ (Plains Cree Y-dialect) Standard
Roman Orthography (SRO) and Canadian Aboriginal syllabics!

Install
-------

    pip install crk_orthography

Usage
-----

[Visit the full documentation here][documentation]! Confused about
words like "syllabics", "transliterator", or even "orthography"? Visit
[the glossary][glossary]!

[documentation]: https://crk-orthography.readthedocs.io/en/stable/
[glossary]: https://crk-orthography.readthedocs.io/en/stable/glossary.html


### As a Python module

Convert SRO to syllabics:

    >>> from crk_orthography import sro2syllabics
    >>> sro2syllabics('nêhiyawêwin')
    'ᓀᐦᔭᐍᐏᐣ'
    >>> sro2syllabics('write nêhiyawêwin')
    'write ᓀᐦᐃᔭᐍᐏᐣ'

Convert syllabics to SRO:

    >>> from crk_orthography import syllabics2sro
    >>> syllabics2sro('ᐊᒋᒧᓯᐢ')
    'acimosis'
    >>> syllabics2sro(' → ᒪᐢᑫᑯᓯᕽ  ᑎᕒᐁᕀᓬ ')
    ' → maskêkosihk  tireyl '


### On the command line

Once installed as a Python module, you can invoke its command line mode
by writing `python3 -m crk_orthography`. When invoked this way, it
converts each line of input from SRO to syllabics.

    $ echo "minôs" | python3 -m crk_orthography
    ᒥᓅᐢ


See also
--------

[nêhiyawêwin syllabics](https://github.com/UAlbertaALTLab/nehiyawewin-syllabics)


License
-------

Copyright (C) 2018 Eddie Antonio Santos

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU Affero General Public License as
published by the Free Software Foundation, either version 3 of the
License, or (at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU Affero General Public License for more details.

You should have received a copy of the GNU Affero General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/>.
