# Tensile Test

A uniaxial quasi-static tensile experiment. Measures force, displacement, engineering stress,
engineering strain, and derived quantities (Young's modulus, tensile strength, elongation at break).

<table>
<tr><td><strong>Version</strong></td><td><code>0.1.1</code></td></tr>
<tr><td><strong>Inherits from</strong></td><td><a href="../characterization-process/">characterization-process</a> → <a href="../process/">process</a></td></tr>
<tr><td><strong>Ontology</strong></td><td>
<code>SteelPO:TensileTest</code>, <code>tto:TensileTest</code>, <code>obi:Assay</code> (inherited), <code>pmdco:Process</code> (inherited)
</td></tr>
<tr><td><strong>Semantic schemas</strong></td><td>
<code>characterization/tensile-test/PMDCo</code> v0.3.0<br>
<code>characterization/tensile-test/TTO</code> v0.2.0
</td></tr>
<tr><td><strong>Links to</strong></td><td>
expert (operator), measurement-device (instrument), specimen (specimen), dataset (result), all inherited from <a href="../characterization-process/">characterization-process</a>
</td></tr>
</table>

## What it inherits

From **process**: identifier, description, start/end time, KV properties.
From **characterization-process**: provenance schemas, three required relations (operator,
instrument, specimen), result dataset relation.

## What it adds

Two measurement-result semantic schemas:

| Schema | Ontology | When to use |
|---|---|---|
| `characterization/tensile-test/TTO` | TTO | Typed result nodes using Tensile Test Ontology classes |
| `characterization/tensile-test/PMDCo` | PMDCo | PMDCo-aligned result nodes |

Both schemas are listed; the consuming workflow decides which to apply based on the target
knowledge graph.

## Effective schema stack

```text
characterization/generic/PMDCo  v0.2.0   ← measurement step (inherited via characterization-process)
characterization/tensile-test/TTO v0.2.0    ← TTO typed result nodes
characterization/tensile-test/PMDCo v0.3.0  ← PMDCo result nodes
```
