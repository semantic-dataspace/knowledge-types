#!/usr/bin/env python3
"""Check README.md metadata tables stay in sync with k-type.spec.yaml.

For every k-types/*/specs/k-type.spec.yaml this script checks:
  1. Version row  — README <code>X.Y.Z</code> matches spec `version`
  2. Semantic schemas row — README entries match spec `semantic_schemas` list
     (same ids, same versions, sorted alphabetically by id)

Exits 1 if any mismatch is found.
"""

import pathlib
import re
import sys

import yaml

SPEC_GLOB = "k-types/*/specs/k-type.spec.yaml"

errors = []
checked = 0

root = pathlib.Path(__file__).parent.parent


def _schema_entries_from_readme(cell_text: str) -> list[tuple[str, str]]:
    """Extract (id, version) pairs from the Semantic schemas cell HTML."""
    return re.findall(r"<code>([^<]+)</code>\s*v([\d.]+)", cell_text)


for spec_path in sorted(root.glob(SPEC_GLOB)):
    k_type_dir  = spec_path.parent.parent
    readme_path = k_type_dir / "README.md"

    try:
        spec = yaml.safe_load(spec_path.read_text())
    except Exception as exc:  # noqa: BLE001
        errors.append(f"{spec_path.relative_to(root)}: could not parse YAML — {exc}")
        continue

    version = spec.get("version", "").strip('"')
    if not version:
        continue

    if not readme_path.exists():
        errors.append(
            f"{readme_path.relative_to(root)}: file missing "
            f"(spec version is {version!r})"
        )
        continue

    readme_text = readme_path.read_text()
    rel         = readme_path.relative_to(root)

    # ── 1. Version row ───────────────────────────────────────────────────────
    version_match = re.search(
        r"<strong>Version</strong>.*?<code>([^<]+)</code>", readme_text
    )
    if not version_match:
        errors.append(
            f"{rel}: no Version table row found — "
            f"add <td><code>{version}</code></td> to the metadata table"
        )
        continue

    if version_match.group(1) != version:
        errors.append(
            f"{rel}: Version row shows {version_match.group(1)!r} "
            f"but spec version is {version!r}"
        )

    # ── 2. Semantic schemas row ──────────────────────────────────────────────
    spec_schemas = sorted(
        [
            (s["id"], str(s["version"]))
            for s in spec.get("semantic_schemas", [])
            if isinstance(s, dict) and s.get("id") and s.get("version")
        ],
        key=lambda x: x[0],
    )

    if spec_schemas:
        cell_match = re.search(
            r"<strong>Semantic schemas</strong></td><td>(.*?)</td></tr>",
            readme_text, re.DOTALL
        )
        if not cell_match:
            errors.append(
                f"{rel}: Semantic schemas table row missing "
                f"(spec lists {len(spec_schemas)} schema(s))"
            )
        else:
            readme_schemas = _schema_entries_from_readme(cell_match.group(1))
            if readme_schemas != spec_schemas:
                expected = ", ".join(f"{i} v{v}" for i, v in spec_schemas)
                got      = ", ".join(f"{i} v{v}" for i, v in readme_schemas)
                errors.append(
                    f"{rel}: Semantic schemas mismatch\n"
                    f"    expected (sorted): {expected}\n"
                    f"    readme:            {got}"
                )

    checked += 1

if errors:
    print("README metadata check FAILED:")
    for msg in errors:
        print(f"  ✗ {msg}")
    sys.exit(1)

print(f"README metadata check passed ({checked} k-types).")
