Cree SRO/Syllabics
==================

[![Build Status](https://travis-ci.org/eddieantonio/cree-sro-syllabics.svg?branch=master)](https://travis-ci.org/eddieantonio/cree-sro-syllabics)
[![codecov](https://codecov.io/gh/eddieantonio/cree-sro-syllabics/branch/master/graph/badge.svg)](https://codecov.io/gh/eddieantonio/cree-sro-syllabics)
[![Documentation Status](https://readthedocs.org/projects/crk-orthography/badge/?version=stable)](https://crk-orthography.readthedocs.io/en/stable/?badge=stable)
[![PyPI package](https://img.shields.io/pypi/v/cree-sro-syllabics.svg)](https://pypi.org/project/cree-sro-syllabics/)
[![Calver YYYY.MM.DD](https://img.shields.io/badge/calver-YYYY.MM.DD-22bfda.svg)](http://calver.org/)

Python 3 library to convert between Western Cree **standard Roman
Orthography** (SRO) to **syllabics** and back again!

Can be used for:

 - nêhiyawêwin/ᓀᐦᐃᔭᐍᐏᐣ/Cree Y-dialect
 - nīhithawīwin/ᓃᐦᐃᖬᐑᐏᐣ/Cree Th-dialect
 - nēhinawēwin/ᓀᐦᐃᓇᐍᐏᐣ/Cree N-dialect

Install
-------

Using `pip`:

    pip install cree-sro-syllabics

Or, you can copy-paste or download [`cree_sro_syllabics.py`][download] into
your own Python 3 project!

[download]: https://github.com/eddieantonio/cree-sro-syllabics/raw/master/cree_sro_syllabics.py


Usage
-----

[Visit the full documentation here][documentation]! Wondering about
words like "syllabics", "transliterator", or "orthography"? Visit
[the glossary][glossary]!

[documentation]: https://crk-orthography.readthedocs.io/en/stable/
[glossary]: https://crk-orthography.readthedocs.io/en/stable/glossary.html


Convert SRO to syllabics:

```python
>>> from cree_sro_syllabics import sro2syllabics
>>> sro2syllabics('nêhiyawêwin')
'ᓀᐦᔭᐍᐏᐣ'
>>> sro2syllabics('write nêhiyawêwin')
'write ᓀᐦᐃᔭᐍᐏᐣ'
```

Convert syllabics to SRO:

```python
>>> from cree_sro_syllabics import syllabics2sro
>>> syllabics2sro('ᐊᒋᒧᓯᐢ')
'acimosis'
>>> syllabics2sro(' → ᒪᐢᑫᑯᓯᕽ  ᑎᕒᐁᐩᓬ ')
' → maskêkosihk  tireyl '
```

See also
--------

[nêhiyawêwin syllabics](https://github.com/UAlbertaALTLab/nehiyawewin-syllabics)


License
-------

Copyright © 2018–2021 National Research Council Canada.

Licensed under the MIT license.
