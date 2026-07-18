---
title: "Governance-package integrity"
permalink: /decisions/0010-package-integrity-model/
parent: "Architectural Decisions"
artifact_type: "Architectural decision record"
normative_status: "Decision record"
---
# Governance-package integrity

{% include gaam-meta.html %}

**Status:** Accepted for v0.9.0  
**Date:** 2026-07-16

## Decision

Release packages use deterministic assembly and a non-circular SHA-256 manifest over declared artifacts.

## Assurance consequence

The validator MUST produce evidence that the implemented repository state conforms to this decision.
