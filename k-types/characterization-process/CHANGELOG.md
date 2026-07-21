# Changelog — Characterization Process

## [0.1.1] — 2026-07-21

### Changed

- Bumped `characterization/generic/PMDCo` schema reference to v0.2.0
  (`type` field aligned with JSON-LD array convention).

---

## [0.1.0] — 2026-04-28

- Initial specification.
- Extends `process`.
- Ontology classes: `obi:Assay`, `pmdco:CharacterisationProcess`.
- Semantic schemas: `characterization/process/PMDCo` v1.0.0, `characterization/step/base/PMDCo` v2.0.0.
- Relations: has_operator (required), uses_instrument (required), has_specimen (required), has_dataset.

### Fixed

- Removed `pmdco:CharacterisationProcess` (`https://w3id.org/pmd/co/CharacterisationProcess`) —
  class does not exist in PMDCo.
- Added `chameo:CharacterisationExperiment`
  (`https://w3id.org/emmo/domain/characterisation-methodology/chameo#CharacterisationExperiment`)
  alongside `obi:Assay`.
