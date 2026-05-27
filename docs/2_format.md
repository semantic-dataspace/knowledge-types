# Format reference: k-type.spec.yaml

This document describes every field in a k-type specification file.
For a blank template see [templates/k-type.spec.yaml](../templates/k-type.spec.yaml).

---

## Top-level fields

### `format_version`
**Required.** The version of the k-type.spec.yaml format itself. Current value: `"0.1"`.

### `$id`
**Required.** The canonical URL of this file. During development use the main-branch URL:
```
https://github.com/semantic-dataspace/knowledge-types/blob/main/k-types/<id>/specs/k-type.spec.yaml
```
At release time, replace `main` with the git tag (e.g. `v1.2.0`) so the URL is pinned and
reproducible.

### `id`
**Required.** Stable kebab-case identifier, unique across all k-types. Once published, never
change this: it is the key used in `extends` references and in the DSMS database.

### `version`
**Required.** Semantic version of this k-type specification (`MAJOR.MINOR.PATCH`).

- **MAJOR**: breaking changes (renamed or removed fields, changed ontology classes, removed relations).
- **MINOR**: backwards-compatible additions (new optional fields, new relations, new schemas).
- **PATCH**: corrections that do not affect structure or semantics (typos, description fixes).

### `maturity`
**Required.** Readiness level of this specification. One of:

| Value | Meaning |
|---|---|
| `draft` | Early design; fields and semantics may still change |
| `stable` | Finalized; only backwards-compatible changes are accepted |
| `deprecated` | Replaced by another k-type; retained for compatibility only |

### `abstract`
**Optional.** Set to `true` when this k-type is not intended to be instantiated directly.
Consumers should hide it from k-item creation UIs and present it only as a base for inheritance.
Omit the field (or set it to `false`) for normal k-types.

### `name`
**Required.** Human-readable name. Either a plain string or a multilingual map:
```yaml
name: "Tensile Test"
# or:
name:
  en: "Tensile Test"
  de: "Zugversuch"
```

### `description`
**Required.** One to three sentences describing what this k-type represents.
Same plain string / multilingual map as `name`.

### `synonyms`
**Optional.** Alternative names. Flat list or multilingual map:
```yaml
synonyms:
  - "uniaxial tensile test"
# or:
synonyms:
  en: ["uniaxial tensile test"]
  de: ["Einachsiger Zugversuch"]
```

---

## `extends`

**Optional.** Makes this k-type a subtype of one or more parent k-types.

Single parent (relative path during development, `$id` URL when published):
```yaml
extends: ../process/specs/k-type.spec.yaml
```

Multiple parents:
```yaml
extends:
  - ../manufacturing-process/specs/k-type.spec.yaml
  - ../material-forming/specs/k-type.spec.yaml
```

See [docs/3_inheritance.md](3_inheritance.md) for merge rules and cycle detection.

---

## `ontology_classes`

**Required** (can be empty list). Ontology classes that k-items of this type are instances of.
Used when constructing the knowledge graph.

```yaml
ontology_classes:
  - iri: "http://purl.obolibrary.org/obo/OBI_0000070"
    label: "Assay"
    ontology: OBI
```

| Sub-field | Description |
|---|---|
| `iri` | Full IRI of the ontology class |
| `label` | Human-readable class label |
| `ontology` | Short name of the ontology (e.g. PMDCo, OBI, schema.org) |

Child k-types inherit and extend the parent's list. Only declare classes that are new at this
level.

---

## `semantic_schemas`

**Optional.** References to [semantic-schemas](https://github.com/semantic-dataspace/semantic-schemas)
with pinned versions.

```yaml
semantic_schemas:
  - id: "characterization/process/PMDCo"
    version: "1.0.0"
    url: "https://github.com/semantic-dataspace/semantic-schemas/blob/characterization-process-PMDCo-v1.0.0/schemas/characterization/process/PMDCo/specs/schema.oold.yaml"
    role: provenance
```

| Sub-field | Description |
|---|---|
| `id` | Schema path within the semantic-schemas repo |
| `version` | Pinned semver of the schema |
| `url` | GitHub tree URL at the per-schema release tag |
| `role` | Optional: how this schema is used (e.g. `process_step`, `provenance`, `input_material`) |

---

## `relations`

**Optional.** Typed links from k-items of this type to k-items of other k-types.
These become edges in the knowledge graph and drive the k-item picker in the UI.

```yaml
relations:
  - id: has_operator
    label: "Operator"
    description: "Expert who performed this process."
    iri: "http://www.w3.org/ns/prov#wasAssociatedWith"
    target_k_types: [expert]
    cardinality: "0..n"
    required: false
```

| Sub-field | Description |
|---|---|
| `id` | Snake-case identifier, unique within this k-type's effective relations |
| `label` | Human-readable label shown in the UI |
| `description` | Optional clarification |
| `iri` | Ontology property IRI used for the RDF triple |
| `target_k_types` | List of k-type IDs that are valid targets for this relation |
| `cardinality` | `"0..1"` \| `"1..1"` \| `"0..n"` \| `"1..n"` |
| `required` | Whether the relation must be filled when creating a k-item |

Relations are inherited from parent k-types. A child can override a relation by declaring
one with the same `id`.

---

## `custom_properties`

**Optional.** Webform shown to users when creating or editing a k-item.
The structure is backwards-compatible with the webform builder format.

```yaml
custom_properties:
  semantics_enabled: true
  sections_enabled: true
  sections:
    - id: section-general
      name: "General Information"
      inputs:
        - id: input-first-name
          label: "First Name"
          widget: Text
          required: false
          relation_mapping:
            iri: "http://xmlns.com/foaf/0.1/firstName"
            type: data_property
```

**Widget types:** `Text` | `Number` | `Textarea` | `Date` | `Datetime` | `Checkbox` |
`Select` | `Multi-select` | `Slider` | `File` | `Knowledge item` | `Array group`

**`relation_mapping` fields:**

| Sub-field | Description |
|---|---|
| `iri` | Ontology property IRI |
| `type` | `data_property` or `object_property` |
| `class_iri` | Optional: the range class IRI (for object properties) |

Sections from parent k-types are merged by `id`. A child can add new sections or add
inputs to an existing section.

---

## `kv_properties`

**Optional.** Enables free-form key-value annotations on k-items.

```yaml
kv_properties:
  enabled: true
  semantic_mapping: true   # each entry may carry an arbitrary ontology IRI
```

---

## `tags`

**Optional.** Free-form labels for filtering in the catalog.

```yaml
tags: [process, characterization, mechanical-testing]
```

---

## `process_schemas`

**Optional, legacy.** Retained for backwards compatibility with the knowledge-type service.
Leave empty unless migrating an existing k-type.

```yaml
process_schemas:
  - name: "My Process Context"
    spec: []
```
