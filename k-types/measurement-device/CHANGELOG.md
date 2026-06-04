# Changelog — Measurement Device

## [0.1.0] — 2026-04-28

- Initial specification.
- Ontology classes: `obi:Device`, `pmdco:MeasuringDevice`.
- Semantic schema: `measurement-device/PMDCo` v1.0.0.
- Custom properties: name, manufacturer, type, serial number, inventory number, room, measurement range.
- Relation: responsible_organization → organization.

### Fixed

- Replaced `pmdco:MeasuringDevice` (`https://w3id.org/pmd/co/MeasuringDevice`) — class does not
  exist in PMDCo — with `pmdco:PMD_0000602` (Device) and
  `chameo:CharacterisationMeasurementInstrument`
  (`https://w3id.org/emmo/domain/characterisation-methodology/chameo#CharacterisationMeasurementInstrument`).
