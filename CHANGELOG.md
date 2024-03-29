# Changelog
All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](http://keepachangelog.com/en/1.0.0/)
and this project adheres to [Semantic Versioning](http://semver.org/spec/v2.0.0.html),
with [Calendar Versioning](https://calver.org/).

## [2021.7.26]

### BREAKING CHANGE

 - <U+167E CANADIAN SYLLABICS WOODS-CREE FINAL TH> is the correct
   Woods Cree th- final. I have no idea where the East Cree final <ᖮ>
   came from.

## [2020.6.23]

### BREAKING CHANGE

 - <U+1429 CANADIAN SYLLABICS FINAL PLUS> is now considered the
   “correct” Y final, instead of <U+1540 CANADIAN SYLLABICS WEST-CREE Y>
   See <https://github.com/UAlbertaALTLab/nehiyawewin-syllabics/issues/2>

## [2020.5.11]

### Added

 - Support for the th-dialect final -kw cluster

### Changed

 - Build system now uses Poetry instead of Pipenv


## [2018.12.07]

### Changed

 - Consider <’> U+2018 RIGHT SINGLE QUOTATION MARK to mark an elided short-i.

## [2018.11.08]

 - First stable release! 🎉

### Changed

 * Changed name from **crk-orthography** to **cree-sro-syllabics**.
 - Changed CalVer scheme from `0.YYYY0M0D.PATCH` to `YYYY.0M.0D`.

## [0.20181108.0]

### Changed

 - ‼︎ Convert from a package (a folder) to a module (a single `.py` file)!
 - Write deliberate test cases for nwV syllables.
 - Change word matching specification to disallow adjacent vowels.
 - Make "word boundary" more explicit, instead of using `\b`.

### Fixed

 - Typo in support for 'thî'/ᖩ syllabic.
 - Fix edge-case involving th-syllable in non-Sandhi conversion.

### Removed

 - **Removed** command line tools: `sro2syllabics(1)` and `syllabics2sro(1)`

## [0.20181005.0]

#w## Added

 - Support th-dialect syllabics; i.e., "ᖧᖨᖩᖪᖫᖬᖭᖮ"

### Changed

 - Fixed minor documentation typos and formatting issues.

### Removed

 - Inaccessible AT&T FST parser.Change word matching specification (

## [0.20180906.0]

### Changed

 - **Breaking change**: `syllabics2sro()` now converts look-alike characters
   in addition to the "canonical" syllabics characters.
 - Moderate refactoring to `syllabics2sro()`.

## [0.20180820.1]

### Changed

 - **Breaking change**: Added conversion of NNBSP in syllabics to
   hyphens in SRO in `syllabics2sro()`. This ensures round-trip
   conversion!

## [0.20180820.0]

### Added

 - **Breaking change**: Added bidirectional conversion of full-stop
   character (᙮).
 - Added `sro2syllabics()` `hyphens=` keyword argument.
 - Added `sro2syllabics -H/--hyphens` option.

### Changed

 - Minor updates to documentation.
 - **Breaking change**: hyphens are converted to \<U+02025 NARROW
   NO-BREAK SPACE> by default.
 - `syllabics2sro()` now converts sequences of a "w-less" syllabic + \<U+1427
   CANADIAN SYLLABICS FINAL MIDDLE DOT> as if they were the pre-composed
   "with w-dot" variant.

## [0.20180728.0]

### Added
 - New command line utilities: `sro2syllabics` and `syllabics2sro`!
 - Added `sro2syllabics` `--sandhi`/`--no-sandhi` options.
 - Added `syllabics2sro` `--macrons`/`--circumflexes` options.

### Fixed
 - Fix a bug in `sro2syllabics()` that crashes when transcribing a word
   with one or more hyphens.

### Changed

 - **Breaking change**: hyphens are no longer produced when calling
   `sro2syllabics(..., sandhi=False)`.

## [0.20180724.0]

### Changed

 - **Breaking change**: `sro2syllabics()` gains the `sandhi=True`
   keyword argument that applies the [sandhi][] orthographic convention
   by default on transcriptions from SRO to syllabics.
 - Enhanced comments.
 - Proofread and enhanced glossary.

[sandhi]: https://crk-orthography.readthedocs.io/en/stable/glossary.html#term-sandhi


[2018.11.08]: https://github.com/eddieantonio/cree-sro-syllabics/compare/v0.20181108.0...v2018.11.08
[0.20181108.0]: https://github.com/eddieantonio/cree-sro-syllabics/compare/v0.20181005.0...v0.20181108.0
[0.20181005.0]: https://github.com/eddieantonio/cree-sro-syllabics/compare/v0.20180906.0...v0.20181005.0
[0.20180906.0]: https://github.com/eddieantonio/cree-sro-syllabics/compare/v0.20180820.1...v0.20180906.0
[0.20180820.1]: https://github.com/eddieantonio/cree-sro-syllabics/compare/v0.20180820.0...v0.20180820.1
[0.20180820.0]: https://github.com/eddieantonio/cree-sro-syllabics/compare/v0.20180728.0...v0.20180820.0
[0.20180728.0]: https://github.com/eddieantonio/cree-sro-syllabics/compare/v0.20180724.0...v0.20180728.0
[0.20180724.0]: https://github.com/eddieantonio/cree-sro-syllabics/compare/v0.20180723.0...v0.20180724.0
