# Connecting K-items

K-items in the DSMS are connected through three complementary mechanisms:

- **Semantic schema links**: `x-ktype` fields in a semantic schema define precise, typed
  connections between k-items — which specimens a test consumed, which datasets it
  produced, which expert ran it. This is the primary mechanism for expressing semantic
  relationships between k-items.
- **Context grouping**: a process k-item scopes a set of related k-items together as
  coarse membership, without ordering or roles.
- **Workflow ordering**: the `preceded_by` field in a semantic schema orders process steps
  into a directed sequence.

K-type specs declare *what a k-item is* (ontology class, custom form fields, inheritance).
They do not declare how k-items connect to each other; that belongs in the semantic schema.

---

## Semantic schema links

Connections between k-items are expressed using `x-ktype` fields in semantic schemas, not
in the k-type spec. This separates two concerns:

- The k-type spec declares *what a k-item is* (ontology class, custom form fields,
  inheritance).
- The semantic schema declares *how a k-item connects to other k-items* and *how those
  connections are serialised to RDF*.

A single k-type can reference multiple semantic schemas representing different ontological
frameworks. The underlying k-item links (stored in `KItemLink` with an ontology property
IRI) are the same regardless of which schema is active.

### Coverage by process k-type

| K-type | Schema | Connections expressed |
|---|---|---|
| `manufacturing-process` | `manufacturing/generic/PMDCo` | inputs (material/specimen), outputs (material/specimen/dataset), preceded by (process) |
| `characterization-process` | `characterization/generic/PMDCo` | inputs (specimen/material), outputs (dataset), preceded by (process), operator (expert), instrument (measurement-device) |
| `data-analysis` | `data-analysis/generic/PMDCo` | inputs (dataset), outputs (dataset), analyst (expert), preceded by (process) |
| `dataset` | `dataset/generic/DCAT` | has_part (dataset or document, for nested measurement series) |

---

## Context grouping

A **context** in the DSMS is a named scope that groups related k-items. When a k-item is
added to a context, the platform stores a `(context_id, kitem_id)` pair in the
`KItemContext` table: a flat many-to-many relationship with no ordering, no role, and no
hierarchy within a context.

Process k-types declare `context: true`, making any process k-item a context anchor.
Examples:

- A `manufacturing-process` k-item "Sheet Forming Campaign 2024" groups all specimens
  produced in that campaign.
- A `characterization-process` k-item "Tensile Test Batch A" groups the specimens tested,
  the raw data files, and the parsed result datasets.
- A `data-analysis` k-item "Material Card Generation DP800" groups the input datasets,
  intermediate results, and the final material card.

Context-scoped queries answer questions like "find all datasets within this characterisation
campaign" without traversing individual step connections.

Context is complementary to semantic schema links: links express precise semantic
relationships; context expresses coarse membership. Both are useful.

---

## Workflow ordering

A workflow is a directed sequence of process steps. The DSMS represents ordering using the
`preceded_by` field in semantic schemas, which maps to `BFO_0000062` (preceded by). Each
process step declares which steps directly precede it; the full sequence can be
reconstructed by following the `preceded_by` chain.

This approach avoids numbering (which requires renumbering when steps are inserted) and
allows non-linear graphs (a step can have multiple predecessors, supporting fan-in and
fan-out).

For the MaterialdatenDataFlow example:

```text
Sheet Forming
  └─preceded by──▶ Specimen Preparation
                     └─preceded by──▶ Tensile Test
                                        └─preceded by──▶ Evaluation
                                                           └─preceded by──▶ Material Card Generation
```

The `preceded_by` field is defined in each process schema with `x-ktype: ["process"]`.

---

## Process k-type hierarchy

```text
process  (abstract, context anchor)
  ├── manufacturing-process
  ├── characterization-process
  │     └── tensile-test
  └── data-analysis
```

`process` is abstract: users cannot create a k-item of type `process` directly. Use the
most specific subtype available. Extend a subtype when a specific technique requires its
own semantic schema (as `tensile-test` does for TTO and PMDCo variants).

---

## When to use context vs. links

| Use case | Mechanism |
|---|---|
| Scoping a query to "everything in this experiment" | Context membership (`KItemContext`) |
| Expressing "this test used this specimen" | `x-ktype` link in semantic schema (`KItemLink`) |
| Expressing "this step follows that step" | `preceded_by` link in semantic schema |
| Navigating to all steps in a workflow | Follow `preceded_by` chain on linked process k-items |
| Listing everything grouped under a campaign | Query by context anchor k-item |
