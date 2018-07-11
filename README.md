Plains Cree Orthography
=======================

[![](https://img.shields.io/badge/calver-MAJOR.YYYY0M0D.PATCH-22bfda.svg)](http://calver.org/)

Convert between nêhiyawêwin/ᓀᐦᐃᔭᐍᐏᐣ (Plains Cree Y-dialect) Standard
Roman Orthography (SRO) and Canadian Aboriginal syllabics.

Usage
-----

Convert SRO to syllabics:

```python
>>> from crk_orthography import sro2syllabics
>>> sro2syllabics('nêhiyawêwin')
'ᓀᐦᔭᐍᐏᐣ'
```

Convert syllabics to SRO:

```python
>>> from crk_orthography import syllabics2sro
>>> syllabics2sro('ᐊᒋᒧᓯᐢ')
'acimosis'
```


See also
--------

[nêhiyawêwin syllabics](https://github.com/UAlbertaALTLab/nehiyawewin-syllabics)


License
-------

Copyright (C) 2018 Eddie Antonio Santo

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
