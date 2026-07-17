---
layout: page
title: "GitHub Pages Publication Model"
permalink: /docs/github-pages-publication/
artifact_type: Publication architecture
normative_status: Informative
---

The GitHub Pages site is a versioned publication surface for both human-readable and machine-readable GAAM artifacts.

## Presentation model

The site retains `jekyll-theme-minimal` as its base shell while GAAM owns the semantic page layout, title hierarchy, metadata presentation and responsive publication styling. This ownership extends to the theme's default layout itself: `_layouts/default.html` is a local override of the theme's bundled layout, replacing its own `<h1>` site-title banner with a non-heading `.site-title` element, so that the page-specific `<h1>` supplied by `_layouts/page.html` remains the page's sole level-one heading. Without this override, every page rendered through the theme carries two `h1` elements -- the theme's site-title banner and GAAM's own page title -- which is what the rendered-site validation below is designed to catch. The compact repository landing page uses explicit, content-led navigation. The publication structure prioritizes the specification, architecture and implementation guidance, profiles, schemas, vocabularies, conformance evidence and release history without relying on theme-specific header navigation.

The repository root is the Pages source. GitHub Actions builds the complete site into `_site` with GitHub's supported Jekyll build action, mirrors `schemas/*.json` into the versioned path declared by each schema's `$id` (`scripts/publish_versioned_schemas.py`; see Canonical identifier publication below), and deploys the resulting Pages artifact.

## Page-title contract

Pages using `layout: page` derive their sole level-one heading from the front-matter `title`. Markdown bodies begin below that title and MUST NOT declare another level-one heading. Source validation enforces this authoring rule, and rendered-site validation requires exactly one `h1` plus the ordered status, breadcrumb, page-header, metadata and content regions. This contract depends on the local `_layouts/default.html` override described above; every page in the site uses `layout: page` (there are no `STRUCTURAL_CONTRACT_EXEMPT` pages), so the one-`h1` requirement applies without exception.

## Canonical identifier publication

Every file in `schemas/*.json` declares a canonical `$id` under `release.json`'s `schemaBase`, which includes a version segment (for example `v0.9.0/schemas/authority.schema.json`). Jekyll publishes `schemas/` verbatim to `_site/schemas/` for human browsing and relative links from `schemas/index.md`, but that path has no version segment. `scripts/publish_versioned_schemas.py` runs after the Jekyll build and copies each schema into `_site/<version>/schemas/`, so the `$id` a schema declares is also the URL at which it is actually published. The script fails the build if any schema's `$id` does not start with `schemaBase`, keeping the two in lockstep.

## Publication guarantees

- The normative specification and supporting guidance render as HTML with stable permalinks.
- Every schema and controlled vocabulary remains available as its original JSON media type.
- Canonical schema identifiers are tested against the generated `_site`.
- Traceability CSV files remain downloadable and receive human-readable table views.
- CI performs a production-equivalent strict Jekyll build before publication.
- The GFM parser is an explicit dependency, preventing dependency-resolution drift.
- GitHub-hosted workflows use Node 24-compatible first-party action releases without insecure runtime overrides.
- Deployment uses GitHub's official Pages build, artifact and deployment actions with least-privilege permissions.
- Navigation is maintained in repository content rather than depending on theme-specific menus.
- Scripts, tests, generated packages, validation internals and local build files are excluded from the public site.

## Information architecture

The landing page provides direct routes to:

1. the Candidate Specification;
2. architecture and implementation guidance;
3. implementation and conformance profiles;
4. machine-readable schemas and vocabularies;
5. conformance, evidence and threat traceability;
6. examples, releases and migration guidance.

Section index pages remain the authoritative navigation surfaces for their respective artifact families.

## Authority boundary

Rendering does not alter normative meaning. Where presentation and source differ, the repository source and the artifact-precedence rules govern.
