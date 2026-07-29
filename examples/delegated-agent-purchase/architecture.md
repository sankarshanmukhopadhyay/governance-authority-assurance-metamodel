---
title: "Architecture and Trust Boundaries"
permalink: /examples/delegated-agent-purchase/architecture/
parent: "Delegated Agent Purchasing"
nav_exclude: true
artifact_type: Informative implementation pattern
normative_status: Informative
---
# Architecture and Trust Boundaries
The pattern separates governance authority, policy decision, runtime enforcement, evidence production and review. Trust boundaries exist wherever an actor accepts authority, evidence, state or an effect from another component.

```mermaid
flowchart LR
  A[Authority source] --> P[Policy decision]
  E[Evidence producers] --> P
  P --> X[Enforcement point]
  X --> R[Decision receipt]
  R --> V[Review and remedy]
```

No component may infer missing authority from technical possession or connectivity.
