# Characterization Process

A process that measures or characterises material properties. The central provenance
k-type for experimental data: it records who ran the experiment, with which device, and
on which specimen.

<table>
<tr><td><strong>Version</strong></td><td><code>0.1.1</code></td></tr>
<tr><td><strong>Inherits from</strong></td><td><a href="../process/">process</a></td></tr>
<tr><td><strong>Ontology</strong></td><td><code>obi:Assay</code>, <code>chameo:CharacterisationExperiment</code>, <code>pmdco:Process</code> (inherited)</td></tr>
<tr><td><strong>Semantic schemas</strong></td><td>
<code>characterization/generic/PMDCo</code> v0.2.0
</td></tr>
<tr><td><strong>Links to</strong></td><td>
expert (operator, required), measurement-device (instrument, required), specimen / material (specimen, required), dataset (result)
</td></tr>
</table>

## What it inherits from process

Custom properties: identifier, description, start time, end time. KV properties.

## What it adds

- Semantic schema: `characterization/generic/PMDCo` (measurement step with provenance fields).
- Relations: operator (expert, **required**), instrument (measurement-device, **required**),
  specimen (**required**), result dataset.

## Subclasses in this library

| K-type | What was measured |
|---|---|
| [tensile-test](../tensile-test/) | Tensile properties (force, displacement, stress, strain) |
