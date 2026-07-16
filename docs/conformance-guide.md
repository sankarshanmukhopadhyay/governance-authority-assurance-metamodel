---
layout: page
title: Conformance and Assurance Guide
permalink: /docs/conformance/
---
# Conformance and Assurance Guide

GAAM conformance applies to declared targets and profiles. It does not certify universal trustworthiness.

| Level | Evidence meaning |
|---|---|
| L0 — Documented | Required governance statements and artifacts exist |
| L1 — Structurally Valid | Machine-readable artifacts validate against GAAM schemas |
| L2 — Behaviourally Tested | Required lifecycle and governance invariants pass |
| L3 — Evidence Supported | Claims have traceable execution or assessment evidence |
| L4 — Independently Assessed | An independent party assessed the declared scope |

## Claim requirements

A claim identifies GAAM version, profiles, target, evidence level, evidence references, issuer, issue time and limitations. Profile dependency closure is mandatory. Partial implementations must not claim full profile conformance.

## Validation layers

1. Repository and publication integrity.
2. Normative requirement traceability.
3. Schema and fixture validation.
4. Governance invariants and lifecycle behaviour.
5. Profile composition and evidence completeness.
