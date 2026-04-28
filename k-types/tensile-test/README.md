# Tensile Test

**Inherits from:** [characterization-process](../characterization-process/) → [process](../process/)
**Ontology:** `SteelPO:TensileTest`, `tto:TensileTest`, `obi:Assay` (inherited), `pmdco:Process` (inherited)
**Semantic schemas:** `characterization/step/tensile-test/TTO` v3.0.2, `characterization/step/tensile-test/PMDCo` v1.1.0 (plus inherited schemas)
**Links to:** expert (operator), measurement-device (instrument), specimen (specimen), dataset (result), all inherited from [characterization-process](../characterization-process/)

A uniaxial quasi-static tensile experiment. Measures force, displacement, engineering stress,
engineering strain, and derived quantities (Young's modulus, tensile strength, elongation at break).

## What it inherits

From **process**: identifier, description, start/end time, KV properties.
From **characterization-process**: provenance schemas, three required relations (operator,
instrument, specimen), result dataset relation.

## What it adds

Two measurement-result semantic schemas:

| Schema | Ontology | When to use |
|---|---|---|
| `characterization/step/tensile-test/TTO` | TTO | Typed result nodes using Tensile Test Ontology classes |
| `characterization/step/tensile-test/PMDCo` | PMDCo | PMDCo-aligned result nodes |

Both schemas are listed; the consuming workflow decides which to apply based on the target
knowledge graph.

## Effective schema stack

```
characterization/process/PMDCo  v1.0.0   ← provenance (who, device, specimen)
characterization/step/base/PMDCo v2.0.0  ← generic assay step structure
characterization/step/tensile-test/TTO v3.0.2   ← TTO typed result nodes
characterization/step/tensile-test/PMDCo v1.1.0 ← PMDCo result nodes
```
