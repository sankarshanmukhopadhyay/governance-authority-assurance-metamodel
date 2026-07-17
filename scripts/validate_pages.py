#!/usr/bin/env python3
from html.parser import HTMLParser
from pathlib import Path
import json
import sys

ROOT = Path(__file__).resolve().parents[1]
SITE = ROOT / "_site"
# Pages listed here are exempt from the shared page-template structural contract
# (status banner, breadcrumbs, artifact-meta, one-H1 rule) checked below. This set
# is intentionally empty: every published page is expected to use `layout: page`
# and carry the `gaam-page` marker. Add a page here only with an explicit,
# documented rationale in docs/github-pages-publication.md -- do not let this
# check silently skip pages that fall through to a bare theme layout.
STRUCTURAL_CONTRACT_EXEMPT = set()

REQUIRED = [
    "index.html", "specification/index.html", "profiles/index.html", "schemas/index.html",
    "vocabularies/index.html", "docs/index.html", "conformance/index.html", "releases/index.html",
    "threat-model/index.html", "validation-report/index.html",
]

class PageStructureParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.h1_count = 0
        self.stylesheet = False
        self.positions = {}
        self._sequence = 0

    def handle_starttag(self, tag, attrs):
        self._sequence += 1
        attrs = dict(attrs)
        classes = set(attrs.get("class", "").split())
        if tag == "h1":
            self.h1_count += 1
        for name, marker in (
            ("status", "status-banner"),
            ("breadcrumbs", "breadcrumbs"),
            ("header", "gaam-page-header"),
            ("title", "gaam-page-title"),
            ("metadata", "artifact-meta"),
            ("content", "gaam-page-content"),
        ):
            if marker in classes and name not in self.positions:
                self.positions[name] = self._sequence
        if tag == "link" and attrs.get("rel") == "stylesheet" and "assets/css/gaam.css" in attrs.get("href", ""):
            self.stylesheet = True

errors = []
for rel in REQUIRED:
    if not (SITE / rel).is_file():
        errors.append(f"missing rendered page: {rel}")

for page in SITE.rglob("*.html"):
    rel = str(page.relative_to(SITE))
    parser = PageStructureParser()
    text = page.read_text(errors="ignore")
    parser.feed(text)
    if "gaam-page" not in text:
        if rel not in STRUCTURAL_CONTRACT_EXEMPT:
            errors.append(
                f"{rel} does not use the shared page template (no gaam-page marker) "
                "and is not in STRUCTURAL_CONTRACT_EXEMPT"
            )
        continue
    if parser.h1_count != 1:
        errors.append(f"{page.relative_to(SITE)} has {parser.h1_count} H1 elements; expected exactly one")
    if not parser.stylesheet:
        errors.append(f"{page.relative_to(SITE)} does not load assets/css/gaam.css")
    ordered = [parser.positions.get(k) for k in ("status", "breadcrumbs", "header", "title", "content")]
    if any(v is None for v in ordered) or ordered != sorted(ordered):
        errors.append(f"{page.relative_to(SITE)} has invalid publication-region ordering")
    if "artifact-meta" in page.read_text(errors="ignore"):
        title = parser.positions.get("title", 0)
        metadata = parser.positions.get("metadata", 0)
        content = parser.positions.get("content", 0)
        if not (title < metadata < content):
            errors.append(f"{page.relative_to(SITE)} has invalid title/metadata/content ordering")

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

print(f"Pages validation: PASS ({len(REQUIRED)} required pages; one-H1 and publication-region contracts verified)")
