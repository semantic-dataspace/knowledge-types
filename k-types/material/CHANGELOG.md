# Changelog — Material

## [0.1.1] — 2026-06-03

### Fixed

- Removed `emmo:Material` (`https://w3id.org/emmo#EMMO_4207e895_8b83_4318_996a_72cfb32acd94`) —
  IRI does not resolve to a specific class.
- Updated PMDCo IRI from human-readable `https://w3id.org/pmd/co/Material` to verified numeric
  form `https://w3id.org/pmd/co/PMD_0000000`.

### Changed

- Description updated to clarify that `material` represents the abstract alloy or
  substance identity (composition, designation) and is not a specific physical piece.
  For physical pieces, use `semi-finished-product` or one of its subtypes.

---

## [0.1.0] — 2026-04-28

- Initial specification.
- Ontology classes: `pmdco:Material`, `emmo:Material`.
- Custom properties: name, identifier, description.
- KV properties enabled with semantic mapping.
