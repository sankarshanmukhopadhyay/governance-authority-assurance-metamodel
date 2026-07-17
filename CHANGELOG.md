---
layout: page
title: "Changelog"
permalink: /releases/changelog/
artifact_type: "Changelog"
normative_status: "Release record"
---
## [0.9.0] - 2026-07-16

### Added
- Candidate stability and artifact-precedence governance.
- Canonical schema catalogue, behavioural vectors, threat register and traceability matrices.
- Modular validation evidence, CI workflow and reproducible v0.9.0 governance package.

### Changed
- Corrected the normative specification identity from v0.1.0 to v0.9.0.
- Updated active profiles, manifests, schemas, vocabularies, examples and claims to v0.9.0.
- Corrected TSMM references to the canonical repository.
- Operationalised L0–L4 conformance evidence and independence boundaries.


## Unreleased

### Fixed

- Remove duplicate body-level H1 headings from page-layout documents and establish front matter as the authoritative title source.
- Refactor the GAAM page header and artifact metadata to prevent overlapping or floating titles across responsive layouts.
- Declare `kramdown-parser-gfm` explicitly so strict Jekyll builds do not depend on transitive gem resolution.

### Changed

- Upgrade supported first-party GitHub Actions to Node 24-compatible major releases.
- Add source and rendered-publication checks for the one-H1 rule, publication-region ordering and stylesheet availability.


### Documentation

- Align the GitHub Pages publication surface with the compact `jekyll-theme-minimal` scheme, explicit landing-page navigation and the supported Pages build action.
- Replace theme-dependent header navigation with content-led entry points for the specification, implementation guidance, profiles, schemas, vocabularies, conformance and releases.

- Replace oblique references to an external governance metamodel with explicit attribution to the ToIP Governance Metamodel Specification v1.0 and Companion Guide v1.0.
- Reframe the TSMM crosswalk as a GAAM source-adoption and architectural-differentiation record.
- Remove residual language implying that GAAM is a successor “v2” of the ToIP specification.
- Add repository-level source attribution and a GitHub Pages landing page for mappings.


## [0.9.0] - 2026-07-16

### Added
- Feature-complete normative requirements for canonical artifacts, lifecycle, assurance, profiles, decisions, safety, remedy, systemic harm and market integrity.
- Eight exhaustive profile manifests, canonical JSON Schemas and controlled vocabularies.
- Three end-to-end implementation patterns with positive and negative fixtures.
- Executable validation, generated evidence, threat model, ADRs and GitHub workflows.
- Full GitHub Pages navigation and `AI_USAGE.md` disclosure.

### Changed
- Replaced open markers with v0.9.0 decision dispositions.
- Reframed unexplained predecessor-version language as independent architectural provenance.
- Expanded conformance, implementation and lifecycle guidance.

All notable changes will be documented here. The project uses Semantic Versioning adapted for an evolving specification.

## [0.1.0] - 2026-07-15

### Added

- Initial public draft of the Governance, Authority and Assurance Metamodel.
- Core concepts for authority, delegation, evidence, assurance, trust decisions, effects and accountability.
- Normative governance for agentic systems, runtime evaluation, registries and decentralised trust graphs.
- Composable conformance profiles.
- Requirements, relationship and conformance matrices.
- Implementation, conformance and reviewer guidance.
- Initial examples and architecture diagrams.
- Repository governance, contribution, security and release hygiene.


## v0.9.0 publication hardening

- publish canonical schemas and controlled vocabularies through GitHub Pages
- add stable permalinks, shared layouts, status metadata and full documentation navigation
- add human-readable schema, vocabulary and traceability catalogues
- add production-equivalent strict Jekyll build and rendered-site validation
- add least-privilege GitHub Pages deployment workflow
