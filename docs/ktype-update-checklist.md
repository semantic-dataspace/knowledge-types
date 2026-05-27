# K-Type Update Checklist

Use this file whenever you modify an existing k-type, whether you are a human
contributor or an LLM agent. Work through the sections in order. Each section
states which files to touch, what to verify, and what the correct output looks
like.

Commands in this file assume your working directory is the **repository root**
and your virtual environment is active.

---

## 0. Classify the change

Determine the semantic-versioning impact before touching any file:

| Change type | Version bump | Examples |
|---|---|---|
| Typo, description fix, update `semantic_schemas` URL to newer schema version | **patch** (0.0.x) | Description reword, schema reference bumped |
| New optional field, new relation, new `semantic_schemas` entry | **minor** (0.x.0) | Added optional `custom_properties` section, new relation added |
| Field renamed or removed, `extends` changed, `ontology_classes` changed | **major** (x.0.0) | Renamed relation, switched parent k-type |

The bump determines the new version string used in all subsequent steps.

---

## 1. `specs/k-type.spec.yaml`

- [ ] Bump `version` to the new version string.
- [ ] Update `$id`: replace the old per-k-type git tag in the URL with the new one
  (e.g. `specimen-v0.1.0` → `specimen-v0.1.1`).
  The tag does not need to exist yet; it is created after merging (step 7).
- [ ] If a `semantic_schemas` entry changed in the
  [semantic-schemas](https://github.com/semantic-dataspace/semantic-schemas) repo:
  update the `version` and `url` fields for that entry to point to the new
  per-schema git tag.
- [ ] If the update adds or removes a `semantic_schemas` entry, update the
  `relations` block if the removed schema contributed a relation, and
  update [CATALOG.md](../CATALOG.md) accordingly.
- [ ] If `extends` changed, verify that all inherited fields still apply and
  that no circular dependency was introduced.

**Verify:**

```bash
python -c "import yaml; yaml.safe_load(open('k-types/<id>/specs/k-type.spec.yaml'))"
```

Must produce no output (no exception).

**Verify that schema references are consistent with semantic-schemas manifest:**

```bash
pytest tests/ -v -k "test_schema_references"
```

All entries in `semantic_schemas` must match the version and URL recorded in
`../semantic-schemas/schemas/manifest.json`.

---

## 2. `CHANGELOG.md`

- [ ] Add a new version section **above** the previous entry:

  ```markdown
  ## [x.y.z] - YYYY-MM-DD

  ### Changed
  - Description of what changed and why.

  ---

  ## [previous version] - ...
  ```

- [ ] Use today's date in `YYYY-MM-DD` format.
- [ ] Classify changes under `Added`, `Changed`, `Removed`, or `Fixed` as appropriate.

---

## 3. `README.md`

- [ ] Update the version badge or version line if one exists.
- [ ] Update the **Relations** table if any relations were added, removed, or changed.
- [ ] Update the **Semantic schemas** table if any `semantic_schemas` entries changed.
- [ ] Update the **Extends** line if the parent k-type changed.

---

## 4. `CATALOG.md`

- [ ] Update the row for this k-type:
  - Version number
  - "Links to" column if `relations` changed
  - "Extends" column if `extends` changed
- [ ] If `extends` changed, check whether the Mermaid inheritance diagram at
  the top needs updating.

---

## 5. Cross-k-type impact check

Changes to one k-type can affect others. Run these searches from the
repository root:

```bash
# Find k-types that extend this one
grep -rn "extends.*<id>" k-types/ --include="*.yaml"

# Find k-types with relations that target this one
grep -rn "target_k_types.*<id>" k-types/ --include="*.yaml"
```

For each hit, assess whether the change is a breaking one for that k-type and
whether its spec needs updating.

---

## 6. End-to-end verification

```bash
# YAML syntax
python -c "import yaml; yaml.safe_load(open('k-types/<id>/specs/k-type.spec.yaml'))"

# Schema reference consistency (requires sibling semantic-schemas clone)
pytest tests/ -v

# Pre-commit hooks (catches README version mismatches and linting)
pre-commit run --all-files
```

All checks must pass before committing.

---

## 7. Commit and tag

- [ ] Stage files by name; do not use `git add .` or `git add -A`:

  ```bash
  git add k-types/<id>/specs/k-type.spec.yaml \
          k-types/<id>/CHANGELOG.md \
          k-types/<id>/README.md \
          CATALOG.md
  ```

- [ ] Write a commit message that names the k-type and version:
  `ktype(<id>): bump to vX.Y.Z: <one-line reason>`
- [ ] After merging, create the per-k-type git tag:

  ```bash
  git tag <id>-vX.Y.Z
  git push origin <id>-vX.Y.Z
  ```

  The tag slug must exactly match the tag embedded in `$id`.

---

## Quick reference: which files change for common update types

| Update | k-type.spec.yaml | CHANGELOG | README | CATALOG.md |
|---|:---:|:---:|:---:|:---:|
| Description / typo fix | patch | patch | maybe | no |
| Bump `semantic_schemas` URL to newer schema version | patch | patch | yes | no |
| Add `semantic_schemas` entry | minor | minor | yes | yes |
| Add optional `custom_properties` field | minor | minor | yes | no |
| Add relation | minor | minor | yes | yes |
| Rename or remove relation | **major** | major | yes | yes |
| Change `extends` | **major** | major | yes | yes |
| Change `ontology_classes` | **major** | major | yes | maybe |

`—` = no change needed; `maybe` = check manually using the decision rules above.
