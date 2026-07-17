---
title: "Candidate artifact precedence"
permalink: /decisions/0007-candidate-artifact-precedence/
parent: "Architectural Decisions"
artifact_type: "Architectural decision record"
normative_status: "Decision record"
---
{% include gaam-meta.html %}

**Status:** Accepted for v0.9.0  
**Date:** 2026-07-16

## Decision

The normative specification governs meaning; schemas govern structure; vocabularies govern enumerations; profile manifests govern composition; tests provide evidence and do not redefine requirements.

## Assurance consequence

The validator MUST produce evidence that the implemented repository state conforms to this decision.
