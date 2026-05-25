import json
import os
from pathlib import Path

import pytest
import yaml

REPO_ROOT = Path(__file__).parent.parent
SEMANTIC_SCHEMAS_ROOT = Path(
    os.environ.get("SEMANTIC_SCHEMAS_PATH", REPO_ROOT.parent / "semantic-schemas")
)
MANIFEST_PATH = SEMANTIC_SCHEMAS_ROOT / "schemas" / "manifest.json"


def load_manifest():
    if not MANIFEST_PATH.exists():
        pytest.exit(
            f"semantic-schemas manifest not found at {MANIFEST_PATH}. "
            "Set SEMANTIC_SCHEMAS_PATH to the semantic-schemas repo root.",
            returncode=1,
        )
    with open(MANIFEST_PATH) as f:
        data = json.load(f)
    result = {}
    for entry in data["tree"]:
        parts = Path(entry["path"]).parts
        specs_idx = parts.index("specs")
        schema_id = "/".join(parts[1:specs_idx])
        result[schema_id] = entry
    return result


def collect_refs():
    refs = []
    for spec_file in sorted(REPO_ROOT.glob("k-types/*/specs/k-type.spec.yaml")):
        ktype_id = spec_file.parts[-3]
        with open(spec_file) as f:
            data = yaml.safe_load(f)
        for ref in data.get("semantic_schemas") or []:
            refs.append((ktype_id, ref))
    return refs


MANIFEST = load_manifest()
REFS = collect_refs()
REF_IDS = [f"{ktype}/{ref['id']}" for ktype, ref in REFS]


@pytest.mark.parametrize("ktype_id,ref", REFS, ids=REF_IDS)
def test_schema_id_exists(ktype_id, ref):
    assert ref["id"] in MANIFEST, (
        f"{ktype_id}: schema '{ref['id']}' not found in the semantic-schemas manifest"
    )


@pytest.mark.parametrize("ktype_id,ref", REFS, ids=REF_IDS)
def test_schema_version_matches(ktype_id, ref):
    if ref["id"] not in MANIFEST:
        pytest.skip("schema not in manifest — caught by test_schema_id_exists")
    expected = MANIFEST[ref["id"]]["version"]
    assert ref["version"] == expected, (
        f"{ktype_id}: '{ref['id']}' version is '{ref['version']}', "
        f"manifest has '{expected}'"
    )


@pytest.mark.parametrize("ktype_id,ref", REFS, ids=REF_IDS)
def test_url_is_pinned(ktype_id, ref):
    url = ref.get("url", "")
    assert "/main/" not in url, (
        f"{ktype_id}: '{ref['id']}' URL points to 'main' — replace with a pinned tag"
    )
