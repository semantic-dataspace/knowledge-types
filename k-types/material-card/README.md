# Material Card

A structured summary of a material's properties combining identity, chemical composition,
mechanical characterisation results, and provenance in one record.

<table>
<tr><td><strong>Version</strong></td><td><code>0.1.0</code></td></tr>
<tr><td><strong>Inherits from</strong></td><td>—</td></tr>
<tr><td><strong>Ontology</strong></td><td><code>pmdco:Material</code></td></tr>
<tr><td><strong>Semantic schemas</strong></td><td>
<code>chemical-composition/PMDCo</code> v0.1.0<br>
<code>material-card/mechanical/PMDCo</code> v0.1.0<br>
<code>specimen/PMDCo</code> v0.1.0<br>
<code>workflow/OBI</code> v0.1.0
</td></tr>
<tr><td><strong>Links to</strong></td><td>material (required), characterization-process / tensile-test, chemical-composition</td></tr>
</table>

## Role in the dataspace

A material card is a *cross-schema template*: it does not introduce new RDF classes but
orchestrates multiple semantic schemas to produce a coherent multi-graph record describing
a material in full.

The workflow schema (`workflow/PMDCo`) links the sub-graphs together; the other three
schemas populate the individual sections.

## Schema composition

```text
material-card/mechanical/PMDCo     ← top-level template (routes input to sub-schemas)
  ├─ specimen/PMDCo                ← specimen envelope
  ├─ chemical-composition/PMDCo   ← element fractions
  └─ workflow/PMDCo               ← overall workflow record
```

## Relations

| Relation | Target k-type | Required | Description |
|---|---|---|---|
| `describes_material` | material | yes | The material this card summarises |
| `includes_characterization` | characterization-process, tensile-test | no | Experiments that contributed data |
| `includes_composition` | chemical-composition | no | Linked composition record |
