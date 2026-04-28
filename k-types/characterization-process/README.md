# Characterization Process

**Inherits from:** [process](../process/)
**Ontology:** `obi:Assay`, `pmdco:CharacterisationProcess`, `pmdco:Process` (inherited)
**Semantic schemas:** `characterization/process/PMDCo` v1.0.0, `characterization/step/base/PMDCo` v2.0.0
**Links to:** expert (operator, required), measurement-device (instrument, required), specimen / material (specimen, required), dataset (result)

A process that measures or characterises material properties. The central provenance
k-type for experimental data: it records who ran the experiment, with which device, and
on which specimen.

## What it inherits from process

Custom properties: identifier, description, start time, end time. KV properties.

## What it adds

- Semantic schemas: `characterization/process/PMDCo` (provenance) and
  `characterization/step/base/PMDCo` (measurement step).
- Relations: operator (expert, **required**), instrument (measurement-device, **required**),
  specimen (**required**), result dataset.

## Two schema layers

| Schema | Role | What it records |
|---|---|---|
| `characterization/process/PMDCo` | Provenance | Operator IRI, device IRI, specimen IRI (who, with what, on what) |
| `characterization/step/base/PMDCo` | Measurement step | Generic assay structure; extended by specific variants |

The recommended pattern is to create one k-item for provenance (this k-type) and one
for measurement results (a subtype), linked via `has_dataset`.

## Subclasses in this library

| K-type | What was measured |
|---|---|
| [tensile-test](../tensile-test/) | Tensile properties (force, displacement, stress, strain) |
