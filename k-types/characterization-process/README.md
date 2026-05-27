# Characterization Process

A process that measures or characterises material properties. The central provenance
k-type for experimental data: it records who ran the experiment, with which device, and
on which specimen.

<table>
<tr><td><strong>Version</strong></td><td><code>0.1.0</code></td></tr>
<tr><td><strong>Inherits from</strong></td><td><a href="../process/">process</a></td></tr>
<tr><td><strong>Ontology</strong></td><td><code>obi:Assay</code>, <code>pmdco:CharacterisationProcess</code>, <code>pmdco:Process</code> (inherited)</td></tr>
<tr><td><strong>Semantic schemas</strong></td><td>
<code>characterization/generic/PMDCo</code> v0.1.0
</td></tr>
<tr><td><strong>Links to</strong></td><td>
expert (operator, required), measurement-device (instrument, required), specimen / material (specimen, required), dataset (result)
</td></tr>
</table>

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
