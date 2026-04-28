# Manufacturing Process

**Inherits from:** [process](../process/)
**Ontology:** `pmdco:ManufacturingProcess`, `pmdco:Process` (inherited)
**Semantic schemas:** `manufacturing/step/base/PMDCo` v2.0.0
**Links to:** expert (operator), material / specimen (input, output), dataset (process data)

A process that transforms, shapes, or produces a material or component. Extend this k-type
for specific manufacturing operations such as cold rolling, heat treatment, or casting.

## What it inherits from process

Custom properties: identifier, description, start time, end time. KV properties.

## What it adds

- Semantic schema: `manufacturing/step/base/PMDCo`.
- Custom properties: duration, temperature.
- Relations: operator (expert), input material, output material, process data (dataset).
