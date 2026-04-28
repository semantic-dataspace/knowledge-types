# Material Card

**Ontology:** `pmdco:Material`
**Semantic schemas:** `material-card/mechanical/PMDCo` v1.0.0, `workflow/PMDCo` v1.1.0, `specimen/PMDCo` v1.0.0, `chemical-composition/PMDCo` v1.0.0
**Links to:** material (required), characterization-process / tensile-test, chemical-composition

A structured summary of a material's properties combining identity, chemical composition,
mechanical characterisation results, and provenance in one record.

## Role in the dataspace

A material card is a *cross-schema template*: it does not introduce new RDF classes but
orchestrates multiple semantic schemas to produce a coherent multi-graph record describing
a material in full.

The workflow schema (`workflow/PMDCo`) links the sub-graphs together; the other three
schemas populate the individual sections.

## Schema composition

```
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
