# Changelog — Process

## [0.2.0] — 2026-06-03

### Fixed

- Replaced `pmdco:Process` (`https://w3id.org/pmd/co/Process`) with `bfo:Process`
  (`http://purl.obolibrary.org/obo/BFO_0000015`) — process is a BFO class; the PMDCo IRI
  was unverifiable as PMDCo redirects all unknown term IRIs to its homepage.

### Added

- `abstract: true` — formalises the existing "do not use directly" documentation into an
  enforceable spec flag; the knowledge service now blocks direct instantiation.
- `context: true` — marks all process instances as context anchors; k-items can be
  registered as members to scope graph views and queries to a specific process.

---

## [0.1.0] — 2026-04-28

- Initial specification.
- Ontology class: `pmdco:Process`.
- Custom properties: identifier, description, start time, end time.
- KV properties enabled with semantic mapping.
