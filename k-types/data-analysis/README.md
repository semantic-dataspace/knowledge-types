# Data Analysis

A process that transforms or derives new data from existing datasets.

<table>
<tr><td><strong>Version</strong></td><td><code>0.1.0</code></td></tr>
<tr><td><strong>Inherits from</strong></td><td><a href="../process/">process</a></td></tr>
<tr><td><strong>Ontology</strong></td><td><code>obi:DataTransformation</code></td></tr>
<tr><td><strong>Semantic schemas</strong></td><td>
<code>data-analysis/generic/PMDCo</code> v0.1.0
</td></tr>
<tr><td><strong>Links to</strong></td><td>dataset, expert</td></tr>
</table>

## What it defines

Extends `process` with two relations specific to data transformation: an input dataset
(required) and an output dataset. Inherits `is_input_to`, `has_output`, and `precedes`
from `process`.

## Relations

| ID | Label | Target | Cardinality | Required |
|---|---|---|---|---|
| `has_input_dataset` | Input dataset | dataset | 1..n | yes |
| `has_output_dataset` | Output dataset | dataset | 0..n | no |
| `has_operator` | Operator | expert | 0..n | no |
