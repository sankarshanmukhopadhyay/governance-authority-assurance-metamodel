---
layout: page
title: GitHub Pages Publication Model
permalink: /docs/github-pages-publication/
artifact_type: Publication architecture
normative_status: Informative
---

# GitHub Pages Publication Model

The GitHub Pages site is a versioned publication surface for both human-readable and machine-readable GAAM artifacts.

## Presentation model

The site uses the `jekyll-theme-minimal` theme with a compact repository landing page and explicit, content-led navigation. The publication structure prioritizes the specification, architecture and implementation guidance, profiles, schemas, vocabularies, conformance evidence and release history without relying on theme-specific header navigation.

The repository root is the Pages source. GitHub Actions builds the complete site into `_site` with GitHub's supported Jekyll build action and deploys the resulting Pages artifact.

## Publication guarantees

- The normative specification and supporting guidance render as HTML with stable permalinks.
- Every schema and controlled vocabulary remains available as its original JSON media type.
- Canonical schema identifiers are tested against the generated `_site`.
- Traceability CSV files remain downloadable and receive human-readable table views.
- CI performs a production-equivalent strict Jekyll build before publication.
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
