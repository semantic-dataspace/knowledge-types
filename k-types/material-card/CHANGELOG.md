# Changelog — Material Card

## [0.1.3] — 2026-07-21

### Changed

- Bumped `material-card/mechanical/PMDCo` schema reference to v0.3.0
  (`type` field aligned with JSON-LD array convention).
- Bumped `workflow/OBI` schema reference to v0.2.0
  (`type` field aligned with JSON-LD array convention).
- Bumped `specimen/PMDCo` schema reference to v0.4.0
  (`type` field aligned with JSON-LD array convention).
- Bumped `chemical-composition/PMDCo` schema reference to v0.2.0
  (`type` field aligned with JSON-LD array convention).

---

## [0.1.2] — 2026-06-03

### Fixed

- Replaced `pmdco:Material` (PMD_0000000) with `orchester:MaterialCard`
  (`https://w3id.org/dsms/orchester/MaterialCard`) — a material card is a simulation input
  record, not a material entity.

### Changed

- Bumped `specimen/PMDCo` schema reference to v0.3.0.

---

## [0.1.1] - 2026-05-27

### Changed

- Bumped `material-card/mechanical/PMDCo` schema reference to v0.2.0.
- Bumped `specimen/PMDCo` schema reference to v0.2.0.

---

## [0.1.0] — 2026-04-28

- Initial specification.
- Ontology class: `pmdco:Material`.
- Semantic schemas: material-card/mechanical/PMDCo v1.0.0, workflow/PMDCo v1.1.0,
  specimen/PMDCo v1.0.0, chemical-composition/PMDCo v1.0.0.
- Relations: describes_material (required), includes_characterization, includes_composition.
- KV properties enabled with semantic mapping.
