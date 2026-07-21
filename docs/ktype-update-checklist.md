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
| New optional field, new `semantic_schemas` entry | **minor** (0.x.0) | Added optional `custom_properties` section, new semantic schema added |
| Field renamed or removed, `extends` changed, `ontology_classes` changed | **major** (x.0.0) | Renamed field, switched parent k-type |

The bump determines the new version string used in all subsequent steps.

---

## 1. `specs/k-type.spec.yaml`

- [ ] Bump `version` to the new version string.
- [ ] Update `$id`: replace the old per-k-type git tag in the URL with the new one
  (e.g. `specimen-v0.1.0` → `specimen-v0.1.1`).
  The tag does not need to exist yet; it is created in step 8.
- [ ] If a `semantic_schemas` entry changed in the
  [semantic-schemas](https://github.com/semantic-dataspace/semantic-schemas) repo:
  update the `version` and `url` fields for that entry to point to the new
  per-schema git tag.
- [ ] If a `semantic_schemas` entry was added, removed, or its version bumped:
  check whether any `x-kitem` fields in that schema were added or removed.
  If inter-k-item connections changed, update [CATALOG.md](../CATALOG.md) accordingly.
- [ ] If `extends` changed, verify that all inherited fields still apply and
  that no circular dependency was introduced.
- [ ] If `ontology_classes` changed: confirm each IRI exists in the ontology's
  published class index before committing. For PMDCo, use the
  [core ontology index](https://materialdigital.github.io/core-ontology/index-en.html)
  and record the numeric `PMD_XXXXXXX` form — not the human-readable name.

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
- [ ] Update the **Semantic schemas** table if any `semantic_schemas` entries changed.
- [ ] Update the **Extends** line if the parent k-type changed.
- [ ] Scan the prose body (What it adds, Schema composition, etc.) for any schema IDs or
  ontology class names that no longer match the spec and correct them.

---

## 4. Cross-k-type impact check

Run this before updating `CATALOG.md`, because impact hits may require additional
version bumps that then need to be reflected in the catalog.

Changes to one k-type can affect others. Run these searches from the repository root:

```bash
# Find k-types that extend this one
grep -rn "extends.*<id>" k-types/ --include="*.yaml"

# Find semantic schemas that use x-kitem pointing to this k-type
grep -rn "ktypeIds.*<id>" ../semantic-schemas/schemas/ --include="*.yaml"
```

For each hit, assess whether the change is a breaking one for that k-type or schema and
whether its spec or schema needs updating. If a k-type spec needs updating, run through
steps 1-3 for that k-type before continuing.

---

## 5. `CATALOG.md`

- [ ] Update the row for this k-type (and any k-types updated in step 4):
  - Version number
  - "Semantic schemas" column if `semantic_schemas` changed
  - "Extends" column if `extends` changed
- [ ] If `extends` changed, check whether the Mermaid inheritance diagram at
  the top needs updating.

---

## 6. End-to-end verification

> Run after all spec, CHANGELOG, README, and CATALOG changes are complete.

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

## 7. Commit

- [ ] Stage files by name; do not use `git add .` or `git add -A`:

  ```bash
  git add k-types/<id>/specs/k-type.spec.yaml \
          k-types/<id>/CHANGELOG.md \
          k-types/<id>/README.md \
          CATALOG.md
  ```

- [ ] Write a commit message that names the k-type and version:
  `ktype(<id>): bump to vX.Y.Z: <one-line reason>`
- [ ] Do **not** add a `Co-Authored-By:` trailer unless explicitly requested.

---

## 8. Push and tag

> Do not stop after committing. All three sub-steps below are required.

- [ ] Push the branch to the remote:

  ```bash
  git push
  ```

- [ ] Create the per-k-type tag on the k-type commit (note the commit SHA
  so the tag lands on the right commit if you made a follow-up fix):

  ```bash
  git tag <id>-vX.Y.Z <commit-sha>
  ```

  The tag slug must exactly match the tag embedded in `$id`.

- [ ] Push the tag:

  ```bash
  git push origin <id>-vX.Y.Z
  ```

- [ ] Verify the tag is visible on the remote:

  ```bash
  git ls-remote --tags origin | grep <id>
  ```

---

## Quick reference: which files change for common update types

| Update | k-type.spec.yaml | CHANGELOG | README | CATALOG.md |
|---|:---:|:---:|:---:|:---:|
| Description / typo fix | patch | patch | maybe | no |
| Bump `semantic_schemas` URL to newer schema version | patch | patch | yes | no |
| Add `semantic_schemas` entry | minor | minor | yes | yes |
| Add optional `custom_properties` field | minor | minor | yes | no |
| Change `extends` | **major** | major | yes | yes |
| Change `ontology_classes` | **major** | major | yes | maybe |

`—` = no change needed; `maybe` = check manually using the decision rules above.
