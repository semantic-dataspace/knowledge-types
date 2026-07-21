# Bulge Test

A hydraulic bulge test that characterises the biaxial flow behaviour of sheet metal by
pressurising a clamped blank until it bulges and fractures. Produces a biaxial
stress-strain curve used to calibrate material models for sheet forming simulations.

<table>
<tr><td><strong>Version</strong></td><td><code>0.1.1</code></td></tr>
<tr><td><strong>Inherits from</strong></td><td><a href="../characterization-process/">characterization-process</a> → <a href="../process/">process</a></td></tr>
<tr><td><strong>Ontology</strong></td><td><code>obi:Assay</code></td></tr>
<tr><td><strong>Semantic schemas</strong></td><td>
<code>characterization/generic/PMDCo</code> v0.2.0
</td></tr>
<tr><td><strong>Links to</strong></td><td>
expert (operator), measurement-device (instrument), specimen (specimen), dataset (result),
all inherited from <a href="../characterization-process/">characterization-process</a>
</td></tr>
</table>

## What it inherits

From **process**: identifier, description, start/end time, KV properties.
From **characterization-process**: provenance schema, three required relations (operator,
instrument, specimen), result dataset relation.

## What it adds

Synonyms: hydraulic bulge test, biaxial tensile test, Tiefungsversuch.

## Subclasses in this library

None.
