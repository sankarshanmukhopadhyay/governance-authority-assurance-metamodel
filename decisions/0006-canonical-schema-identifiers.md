---
layout: page
title: "Canonical schema identifiers"
permalink: /decisions/0006-canonical-schema-identifiers/
artifact_type: "Architectural decision record"
normative_status: "Decision record"
---
# Canonical schema identifiers

**Status:** Accepted for v0.9.0  
**Date:** 2026-07-16

## Decision

Use the versioned GitHub Pages namespace for v0.9.0 schemas. This makes identifiers repository-controlled, publishable and immutable by release.

## Assurance consequence

The validator MUST produce evidence that the implemented repository state conforms to this decision.
