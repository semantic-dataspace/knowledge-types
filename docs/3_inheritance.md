# Inheritance

K-types support single and multiple inheritance through the `extends` field.
A child k-type IS-A instance of its parent and inherits its definitions.

---

## Basic usage

```yaml
# k-types/characterization-process/specs/ktype.yaml
id: characterization-process
extends: ../process/specs/ktype.yaml
```

```yaml
# k-types/tensile-test/specs/ktype.yaml
id: tensile-test
extends: ../characterization-process/specs/ktype.yaml
```

This creates a chain: `tensile-test` IS-A `characterization-process` IS-A `process`.

---

## What is inherited

| Field | Merge behaviour |
|---|---|
| `ontology_classes` | Appended; child is an instance of all parent classes |
| `semantic_schemas` | Merged by `id`; child adds entries or overrides a version |
| `relations` | Merged by `id`; child inherits all parent relations |
| `custom_properties` sections | Merged by section `id`; child adds sections or adds inputs to existing ones |
| `tags` | Appended |
| `kv_properties` | Inherited as-is; child overrides individual keys |

**Narrowing vs. widening**: a child can make a field more restrictive (e.g. make a
`required: false` relation `required: true`) but cannot relax a parent's constraint.

---

## Multiple inheritance

A k-type can extend more than one parent:

```yaml
extends:
  - ../manufacturing-process/specs/ktype.yaml
  - ../material-forming/specs/ktype.yaml
```

**Merge order**: parents are resolved left-to-right, with later entries taking precedence
over earlier ones. The child's own definitions override everything. This is analogous to
Python's MRO for linear chains.

If two parents declare a `relation` with the same `id`, the last parent's definition wins,
then the child's definition overrides that.

---

## `extends` resolution

During local development, use a relative path:
```yaml
extends: ../process/specs/ktype.yaml
```

At publish time, tooling replaces relative paths with the parent's `$id` (a pinned GitHub
URL), making the published spec fully self-contained:
```yaml
extends: "https://github.com/semantic-dataspace/knowledge-types/blob/v1.0.0/k-types/process/specs/ktype.yaml"
```

Both forms are valid in the repository at all times.

---

## Cycle detection

A k-type must not extend itself directly or indirectly. Tooling walks the `extends` chain
and raises an error if the same `$id` is encountered twice. Authoring tools should validate
this before accepting a pull request.

---

## Practical example: tensile-test

`tensile-test` declares no relations of its own, but inherits three from
`characterization-process`:

| Relation id | From | Target k-type | Ontology property |
|---|---|---|---|
| `has_operator` | characterization-process | expert | `prov:wasAssociatedWith` |
| `uses_instrument` | characterization-process | measurement-device | `schema:instrument` |
| `has_specimen` | characterization-process | specimen | PMDCo property |

And its effective `ontology_classes` are:

| Class | Source |
|---|---|
| `pmdco:Process` | process (grandparent) |
| `obi:Assay` | characterization-process (parent) |
| `tto:TensileTest` | tensile-test (self) |
| `SteelPO:TensileTest` | tensile-test (self) |

The child only needs to declare the delta; the rest propagates automatically.
