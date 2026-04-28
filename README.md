# Knowledge Types

A curated library of k-type specifications for the Dataspace Management System (DSMS).

A **k-type** is a template that defines the structure, semantics, and relationships of Knowledge
Items (k-items). Each specification is a single self-contained YAML file, portable across any DSMS
instance.

> **New to k-types, the DSMS, or ontologies?**
> Start with [docs/1_concepts.md](docs/1_concepts.md) for a plain-language introduction.

---

## Background

Materials research data scattered across institutions and formats cannot be easily combined or
queried. The DSMS addresses this by organising data as a structured network of typed records. K-types
are the templates that give each record its type, its fields, its connections to other records, and
its meaning in a shared vocabulary of materials science ontologies.

For a full description of the DSMS and the dataspace concept:

> Nahshon, Y.; Morand, L.; Büschelberger, M.; Helm, D.; Kumaraswamy, K.; Zierep, P.; Weber, M.;
> de Andrés, P. (2025). *Semantic Orchestration and Exploitation of Material Data: A Dataspace
> Solution Demonstrated on Steel and Copper Applications.* Advanced Engineering Materials, 27(8),
> 2401448. <https://doi.org/10.1002/adem.202401448>

---

## Repository structure

```text
k-types/
  <k-type-id>/
    README.md        ← what this k-type is and how to use it
    CHANGELOG.md     ← version history
    specs/
      ktype.yaml     ← self-contained specification
    docs/            ← optional usage examples
templates/
  ktype.yaml         ← blank template for new k-type authors
docs/
  1_concepts.md      ← plain-language introduction to k-types, ontologies, and the DSMS
  2_format.md        ← field-by-field reference for ktype.yaml
  3_inheritance.md   ← how inheritance and multiple inheritance work
CATALOG.md           ← full registry with inheritance and relation graph
```

---

## Quick start

### I want to find a k-type to use

Browse [CATALOG.md](CATALOG.md). The graph at the top shows inheritance and links between k-types
at a glance; the table below lets you filter by ontology, semantic schema, or tag.

### I want to create a new k-type

1. Check [CATALOG.md](CATALOG.md): does an existing k-type already cover your concept? If so,
   consider extending it with `extends` rather than creating a new one.
2. Copy [templates/ktype.yaml](templates/ktype.yaml) into a new folder under `k-types/`.
3. Read [docs/2_format.md](docs/2_format.md) for a field-by-field reference.
4. Open a **New K-Type** issue to discuss before submitting a pull request.

---

## Documentation

| Document | Content |
|---|---|
| [docs/1_concepts.md](docs/1_concepts.md) | Plain-language introduction: what k-types are, what ontologies and knowledge graphs are, why this matters |
| [docs/2_format.md](docs/2_format.md) | Field-by-field reference for `ktype.yaml` |
| [docs/3_inheritance.md](docs/3_inheritance.md) | Inheritance mechanics, multiple inheritance, merge rules |

---

## Related projects

| Project | Role |
|---|---|
| [semantic-schemas](https://github.com/semantic-dataspace/semantic-schemas) | Structured data recording templates referenced by k-types |
| [DSMS](https://github.com/semantic-dataspace/dsms) | The knowledge management system that consumes k-types |
| [PMDCo](https://github.com/materialdigital/core-ontology) | Platform MaterialDigital Core Ontology |

---

## License

K-type specifications are published under [CC BY 4.0](LICENSE). You may use, adapt, and
redistribute them freely, including for commercial purposes, as long as you give appropriate credit.
