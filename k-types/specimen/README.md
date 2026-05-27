# Specimen

A physical test piece prepared from a material for characterisation or mechanical testing.

<table>
<tr><td><strong>Version</strong></td><td><code>0.1.0</code></td></tr>
<tr><td><strong>Inherits from</strong></td><td><a href="../material/">material</a></td></tr>
<tr><td><strong>Ontology</strong></td><td>
<code>pmdco:Specimen</code>, <code>obi:Specimen</code>, <code>pmdco:Material</code> (inherited), <code>emmo:Material</code> (inherited)
</td></tr>
<tr><td><strong>Semantic schemas</strong></td><td>
<code>specimen/PMDCo</code> v0.1.0
</td></tr>
<tr><td><strong>Links to</strong></td><td>material (manufactured from)</td></tr>
</table>

## What it inherits from material

Custom properties: name, identifier, description.
KV properties with semantic mapping.

## What it adds

- Semantic schema: `specimen/PMDCo` for structured RDF representation.
- Custom properties: type, geometry, width, length, thickness, diameter, description.
- Relation: manufactured from (source material).
