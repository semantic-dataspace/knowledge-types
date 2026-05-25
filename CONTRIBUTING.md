# Contributing

## Adding a new k-type

1. Check [CATALOG.md](CATALOG.md) first. If your concept is a specialisation of something already
   there, extend it with `extends` rather than creating a new k-type.
2. Copy [templates/k-type.spec.yaml](templates/k-type.spec.yaml) into a new folder under
   `k-types/<your-id>/`.
3. Add a `README.md` and `CHANGELOG.md` alongside the spec (follow the existing k-types as examples).
4. Open a **New K-Type** issue to discuss the design before submitting a pull request.

## Referencing semantic schemas

The `semantic_schemas` field in a spec must stay in sync with the
[semantic-schemas](https://github.com/semantic-dataspace/semantic-schemas) repository. Three rules
are enforced by the CI tests on every pull request:

- The schema `id` must exist in the semantic-schemas `manifest.json`.
- The `version` must match the version recorded in that manifest.
- The `url` must point to a pinned git tag, not to `main`.

When the semantic-schemas repo releases a new version, bump the affected `version` and `url` fields
in the relevant k-type specs and update [CATALOG.md](CATALOG.md) to match.

## The maturity field

Every spec carries a `maturity` field:

| Value | When to use |
|---|---|
| `draft` | Fields or semantics may still change |
| `stable` | Only backwards-compatible changes will be accepted |
| `deprecated` | Replaced by another k-type; kept for compatibility |

New k-types start as `draft`. Propose a change to `stable` via a pull request with a brief
rationale.

## Running the tests locally

The schema reference checks require a local clone of semantic-schemas as a sibling directory:

```
semantic-dataspace/
  knowledge-types/   ← this repo
  semantic-schemas/  ← sibling clone
```

```bash
pip install -r tests/requirements.txt
pytest tests/ -v
```

If semantic-schemas lives elsewhere, set `SEMANTIC_SCHEMAS_PATH`:

```bash
SEMANTIC_SCHEMAS_PATH=/path/to/semantic-schemas pytest tests/ -v
```

## Pull request checklist

- [ ] Spec file is at `k-types/<id>/specs/k-type.spec.yaml`
- [ ] `README.md` and `CHANGELOG.md` are present
- [ ] `maturity` is set
- [ ] All `semantic_schemas` entries have pinned URLs and versions matching the manifest
- [ ] [CATALOG.md](CATALOG.md) is updated
- [ ] CI passes
