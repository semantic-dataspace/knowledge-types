# Changelog — Expert

## [0.1.0] — 2026-04-28

- Initial specification.
- Extends `person`.
- Ontology class: `emmo:Expert`.
- Semantic schema: `expertise/schema.org` v1.0.0.
- Relations: employer, department, knows, expertise_in_material, expertise_in_device.
- Custom properties: field of study (inherited: first name, last name, email, ORCID).

### Fixed

- Replaced `emmo:Expert` (`https://w3id.org/emmo#EMMO_27c5d8c6_8af7_4d63_beb1_ec37cd8b3fa3`) —
  IRI does not resolve to a specific class — with `orchester:Expert`
  (`https://w3id.org/dsms/orchester/Expert`).
