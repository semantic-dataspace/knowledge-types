# Changelog — Chemical Composition

## [0.1.1] — 2026-07-21

### Changed

- Bumped `chemical-composition/PMDCo` schema reference to v0.2.0
  (`type` field aligned with JSON-LD array convention).
- Bumped `chemical-composition/BWMD` schema reference to v0.2.0
  (`type` field aligned with JSON-LD array convention).

---

## [0.1.0] — 2026-04-28

- Initial specification.
- Ontology class: `pmdco:ChemicalComposition`.
- Semantic schemas: `chemical-composition/PMDCo` v1.0.0, `chemical-composition/BWMD` v1.0.0.
- Relation: composition_of → material or specimen.

### Fixed

- Updated PMDCo IRI from human-readable `https://w3id.org/pmd/co/ChemicalComposition` to
  verified numeric form `https://w3id.org/pmd/co/PMD_0000551`.
