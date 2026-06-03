# Creep Specimen

A specimen designed for creep and stress relaxation testing under sustained load at
elevated temperature, following standards such as ISO 204 and ASTM E139. May have a
cylindrical or flat gauge section with threaded or shouldered grip ends.

<table>
<tr><td><strong>Version</strong></td><td><code>0.1.0</code></td></tr>
<tr><td><strong>Inherits from</strong></td><td><a href="../specimen/">specimen</a></td></tr>
<tr><td><strong>Ontology</strong></td><td><code>pmdco:Specimen</code> (inherited), <code>obi:Specimen</code> (inherited)</td></tr>
<tr><td><strong>Semantic schemas</strong></td><td><code>specimen/PMDCo</code> v0.3.0 (inherited)</td></tr>
<tr><td><strong>Links to</strong></td><td>semi-finished-product (source, inherited)</td></tr>
</table>

## What it inherits from specimen

Custom properties: type, geometry, width, length, thickness, diameter, description.
Relations: `source` (physical piece), `schema:material` (alloy identity).

## What it adds

Custom properties: gauge length, gauge diameter, grip type, thread specification.
