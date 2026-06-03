# Changelog — Specimen

## [0.2.0] — 2026-06-03

### Changed

- **Breaking:** removed `extends: material`. Specimen is now a standalone k-type and no
  longer inherits material identity fields; those are linked via `schema:material` in the
  semantic schema.
- **Breaking:** renamed relation `manufactured_from` to `source`; changed IRI from
  `pmd:manufacturingOutput` to `prov:wasDerivedFrom`; changed target k-type from
  `material` to `semi-finished-product`. The relation now captures the specific physical
  piece the specimen was cut from.
- Bumped `specimen/PMDCo` schema reference to v0.3.0 (added `prov:wasDerivedFrom` field).

---

## [0.1.1] - 2026-05-27

### Changed

- Bumped `specimen/PMDCo` schema reference to v0.2.0.

---

## [0.1.0] — 2026-04-28

- Initial specification.
- Extends `material`.
- Ontology classes: `pmdco:Specimen`, `obi:Specimen`.
- Semantic schema: `specimen/PMDCo` v1.0.0.
- Custom properties: type, geometry, width, length, thickness, diameter, description.
- Relation: manufactured_from → material.
