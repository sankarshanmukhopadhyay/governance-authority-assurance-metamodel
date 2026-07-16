---
layout: page
title: Threat Model and Misuse Catalogue
permalink: /threat-model/
---
# Threat Model and Misuse Catalogue

| Threat | Required control/evidence |
|---|---|
| Forged or laundered authority | authority-source validation, integrity and provenance |
| Scope amplification | parent-child intersection and attenuation tests |
| Delegation replay | status, nonce/event and effective-time validation |
| Stale revocation | propagation and freshness controls |
| Agent/operator substitution | governance identity continuity checks |
| Policy downgrade or package rollback | version binding and checksums |
| Evidence/assurance laundering | provenance, criteria and context validation |
| Registry poisoning or graph manipulation | source authority, contradiction and recognition boundaries |
| Accountability fragmentation | non-terminal accountable-party mapping |
| Receipt over-disclosure | minimisation and redaction controls |
| Denial of remedy | review authority and remedy completion evidence |
| Emergency-authority abuse | time bounds and conflict-controlled review |
| Hidden systemic harm | effect aggregation and intervention thresholds |

Residual risk remains subject to implementation context and independent validation.
