# Changelog — Metal Sheet

## [0.1.0] — 2026-06-03

- Initial specification.
- Extends `semi-finished-product`; inherits relations and base custom properties.
- Custom properties: thickness, width, length, surface condition.

### Fixed

- Replaced `bfo:Object` (BFO_0000030) with `pmdco:PMD_0020172` (Sheet) — PMDCo defines a
  dedicated Sheet class that is more specific than the BFO top-level Object class.
