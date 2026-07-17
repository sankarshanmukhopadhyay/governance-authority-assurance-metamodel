#!/usr/bin/env python3
"""Validate the rendered Just the Docs site in _site/.

Theme-specific structural checks (status banner / breadcrumb / artifact-meta
region ordering) that this script used to perform were tied to GAAM's old
hand-built jekyll-theme-minimal page template and no longer apply now that
the site uses Just the Docs, which owns its own page structure. What remains
theme-independent -- and still worth checking on every build -- is: the
required section pages actually render, every page has exactly one H1 (GAAM's
own page-title contract, unchanged), the site loads a stylesheet and ships a
search index, and every schema's canonical $id resolves to a real published
artifact.
"""
from html.parser import HTMLParser
from pathlib import Path
import json
import sys

ROOT = Path(__file__).resolve().parents[1]
SITE = ROOT / "_site"

REQUIRED = [
    "index.html", "specification/index.html", "profiles/index.html", "schemas/index.html",
    "vocabularies/index.html", "matrices/index.html", "docs/index.html", "conformance/index.html",
    "releases/index.html", "threat-model/index.html", "validation-report/index.html",
]


class PageStructureParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.h1_count = 0
        self.stylesheet = False

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if tag == "h1":
            self.h1_count += 1
        if tag == "link" and attrs.get("rel") == "stylesheet":
            self.stylesheet = True


errors = []
for rel in REQUIRED:
    if not (SITE / rel).is_file():
        errors.append(f"missing rendered page: {rel}")

html_pages = list(SITE.rglob("*.html"))
for page in html_pages:
    rel = str(page.relative_to(SITE))
    parser = PageStructureParser()
    parser.feed(page.read_text(errors="ignore"))
    if parser.h1_count != 1:
        errors.append(f"{rel} has {parser.h1_count} H1 elements; expected exactly one")
    if not parser.stylesheet:
        errors.append(f"{rel} does not load a stylesheet")

if not html_pages:
    errors.append("no rendered HTML pages found under _site/")

search_index = list((SITE / "assets" / "js").glob("*search-data*.json")) if (SITE / "assets" / "js").is_dir() else []
if not search_index:
    errors.append("no Just the Docs search index found under _site/assets/js/*search-data*.json")

for srcdir in ("schemas", "vocabularies"):
    for src in (ROOT / srcdir).glob("*.json"):
        out = SITE / srcdir / src.name
        if not out.is_file():
            errors.append(f"missing published artifact: {srcdir}/{src.name}")
        else:
            try:
                json.loads(out.read_text())
            except Exception as exc:
                errors.append(f"invalid published JSON {out}: {exc}")

for schema in (ROOT / "schemas").glob("*.json"):
    data = json.loads(schema.read_text())
    sid = data.get("$id", "")
    marker = "/governance-authority-assurance-metamodel/"
    if marker in sid:
        rel = sid.split(marker, 1)[1]
        if not (SITE / rel).is_file():
            errors.append(f"$id has no rendered artifact: {sid}")

if errors:
    print("Pages validation: FAIL")
    for error in errors:
        print("-", error)
    sys.exit(1)

print(f"Pages validation: PASS ({len(REQUIRED)} required pages; {len(html_pages)} pages checked for one-H1 and stylesheet; search index present)")
