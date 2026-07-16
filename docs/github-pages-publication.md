---
layout: page
title: GitHub Pages Publication Model
permalink: /docs/github-pages-publication/
artifact_type: Publication architecture
normative_status: Informative
---

# GitHub Pages Publication Model

The GitHub Pages site is a versioned publication surface for both human-readable and machine-readable GAAM artifacts.

## Publication guarantees

- The normative specification and supporting guidance render as HTML with stable permalinks.
- Every schema and controlled vocabulary remains available as its original JSON media type.
- Canonical schema identifiers are tested against the generated `_site`.
- Traceability CSV files remain downloadable and receive human-readable table views.
- CI performs a production-equivalent strict Jekyll build before publication.
- Deployment uses GitHub's official Pages artifact and deployment actions with least-privilege permissions.

## Authority boundary

Rendering does not alter normative meaning. Where presentation and source differ, the repository source and the artifact-precedence rules govern.
