# Manufacturing Process

A process that transforms, shapes, or produces a material or component. Extend this k-type
for specific manufacturing operations such as cold rolling, heat treatment, or casting.

<table>
<tr><td><strong>Version</strong></td><td><code>0.1.1</code></td></tr>
<tr><td><strong>Inherits from</strong></td><td><a href="../process/">process</a></td></tr>
<tr><td><strong>Ontology</strong></td><td><code>pmdco:ManufacturingProcess</code>, <code>pmdco:Process</code> (inherited)</td></tr>
<tr><td><strong>Semantic schemas</strong></td><td>
<code>manufacturing/generic/PMDCo</code> v0.2.0
</td></tr>
<tr><td><strong>Links to</strong></td><td>expert (operator), material / specimen (input, output), dataset (process data)</td></tr>
</table>

## What it inherits from process

Custom properties: identifier, description, start time, end time. KV properties.

## What it adds

- Semantic schema: `manufacturing/generic/PMDCo`.
- Custom properties: duration, temperature.
- Relations: operator (expert), input material, output material, process data (dataset).
