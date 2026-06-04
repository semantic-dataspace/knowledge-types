import re
from pathlib import Path

import pytest
import yaml

REPO_ROOT = Path(__file__).parent.parent

# GitHub browsing URLs are not valid ontology term IRIs.
# Ontology terms must use a persistent identifier namespace (w3id.org, purl.*, etc.).
_GITHUB_BROWSE_RE = re.compile(r"^https://github\.com/")

_PMDCO_NUMERIC_RE = re.compile(r"^https://w3id\.org/pmd/co/PMD_\d+$")
_PMDCO_BASE = "https://w3id.org/pmd/co/"


def collect_ontology_classes():
    items = []
    for spec_file in sorted(REPO_ROOT.glob("k-types/*/specs/k-type.spec.yaml")):
        ktype_id = spec_file.parts[-3]
        with open(spec_file) as f:
            data = yaml.safe_load(f)
        for cls in data.get("ontology_classes") or []:
            items.append((ktype_id, cls))
    return items


CLASSES = collect_ontology_classes()
CLASS_IDS = [
    f"{ktype}/{cls.get('ontology', '?')}/{cls.get('label', '?')}"
    for ktype, cls in CLASSES
]


@pytest.mark.parametrize("ktype_id,cls", CLASSES, ids=CLASS_IDS)
def test_iri_is_absolute_uri(ktype_id, cls):
    iri = cls.get("iri", "")
    assert iri.startswith(("http://", "https://")), (
        f"{ktype_id}: IRI '{iri}' is not an absolute HTTP(S) URI"
    )


@pytest.mark.parametrize("ktype_id,cls", CLASSES, ids=CLASS_IDS)
def test_iri_not_github_browsing_url(ktype_id, cls):
    iri = cls.get("iri", "")
    assert not _GITHUB_BROWSE_RE.match(iri), (
        f"{ktype_id}: '{iri}' is a GitHub browsing URL, not an ontology term IRI — "
        "use the persistent identifier namespace (e.g. https://w3id.org/pmd/tto/) instead"
    )


@pytest.mark.parametrize("ktype_id,cls", CLASSES, ids=CLASS_IDS)
def test_pmdco_iri_is_numeric(ktype_id, cls):
    iri = cls.get("iri", "")
    if not iri.startswith(_PMDCO_BASE):
        return
    assert _PMDCO_NUMERIC_RE.match(iri), (
        f"{ktype_id}: PMDCo IRI '{iri}' uses a human-readable name — "
        "PMDCo redirects unknown term IRIs to its homepage, making human-readable "
        "names unverifiable. Use the numeric form (https://w3id.org/pmd/co/PMD_XXXXXXX) instead."
    )
