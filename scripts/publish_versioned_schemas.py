#!/usr/bin/env python3
"""Mirror schemas/*.json into the versioned path their $id declares.

Every schema in schemas/*.json carries a canonical $id such as
  https://sankarshanmukhopadhyay.github.io/governance-authority-assurance-metamodel/v0.9.0/schemas/authority.schema.json

Jekyll publishes schemas/ verbatim to _site/schemas/, but nothing publishes
a copy at _site/v0.9.0/schemas/, so every $id is a dead link on the built
site. This script derives the version segment from release.json (the same
source of truth scripts/validate.py uses) and copies each schema into
_site/<version>/schemas/ after the Jekyll build, so the canonical URLs the
schemas themselves declare actually resolve.

Run after `jekyll build` and before validating or uploading _site/.
"""
from pathlib import Path
import json
import shutil
import sys

ROOT = Path(__file__).resolve().parents[1]
SITE = ROOT / "_site"


def main() -> int:
    release = json.loads((ROOT / "release.json").read_text())
    version = release["version"]
    schema_base = release["schemaBase"]

    if not SITE.is_dir():
        print(f"error: {SITE} does not exist; run jekyll build first", file=sys.stderr)
        return 1

    dest = SITE / version / "schemas"
    dest.mkdir(parents=True, exist_ok=True)

    # Matches scripts/validate.py's schema selection: *.schema.json only.
    # schemas/catalog.json is a catalog document (key "id", not "$id") and
    # is intentionally excluded here, same as in validate.py.
    schemas = sorted((ROOT / "schemas").glob("*.schema.json"))
    if not schemas:
        print("error: no schema files found under schemas/", file=sys.stderr)
        return 1

    for src in schemas:
        shutil.copy2(src, dest / src.name)

    # Fail loudly if the mirror doesn't actually match what the $id values expect,
    # rather than publishing a versioned path nobody's $id points at.
    mismatched = []
    for src in schemas:
        data = json.loads(src.read_text())
        sid = data.get("$id", "")
        if not sid.startswith(schema_base):
            mismatched.append((src.name, sid))
    if mismatched:
        for name, sid in mismatched:
            print(f"error: {name} $id does not start with schemaBase: {sid}", file=sys.stderr)
        return 1

    print(f"Mirrored {len(schemas)} schema(s) to {dest.relative_to(ROOT)} (version {version})")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
