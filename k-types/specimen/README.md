# Specimen

A physical test piece prepared from a material for characterisation or mechanical testing.

<table>
<tr><td><strong>Version</strong></td><td><code>0.2.1</code></td></tr>
<tr><td><strong>Inherits from</strong></td><td>—</td></tr>
<tr><td><strong>Ontology</strong></td><td>
<code>pmdco:Specimen</code>, <code>obi:Specimen</code>
</td></tr>
<tr><td><strong>Semantic schemas</strong></td><td>
<code>specimen/PMDCo</code> v0.4.0
</td></tr>
<tr><td><strong>Links to</strong></td><td>semi-finished-product (source)</td></tr>
</table>

## What it defines

Custom properties: type, geometry, width, length, thickness, diameter, description.

Relations:

| Relation | Target | Cardinality | Predicate |
|---|---|---|---|
| Source | [semi-finished-product](../semi-finished-product/) | 0..1 | `prov:wasDerivedFrom` |

The abstract alloy identity is linked via `schema:material` in the `specimen/PMDCo`
semantic schema (PMDCo duality object/material pattern) rather than as a ktype relation.
When `source` is set, the UI should offer to auto-populate `schema:material` from
the source's `made_of` link.

## Subclasses in this library

| K-type | Description |
|---|---|
| [flat-specimen](../flat-specimen/) | Flat dog-bone or rectangular test piece |
| [creep-specimen](../creep-specimen/) | Test piece for creep and stress relaxation testing |
