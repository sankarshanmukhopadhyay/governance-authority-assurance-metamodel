---
title: "Architecture Diagrams"
permalink: /diagrams/
parent: "Documentation"
artifact_type: "Architecture diagrams"
normative_status: "Informative"
---
# Architecture Diagrams

{% include gaam-meta.html %}

These diagrams are informative and use Mermaid syntax.

## 1. Core decision chain

```mermaid
flowchart LR
  P[Principal] -->|delegates bounded authority| A[Agent or Actor]
  S[Authority Source] --> AU[Authority]
  AU --> D[Delegation]
  D --> A
  POL[Policy and Rules] --> TD[Trust Decision]
  E[Evidence and Status] --> TD
  A -->|requests effect| TD
  TD -->|allow, deny, restrict, suspend, review| EF[Effect]
  TD --> DR[Decision Receipt]
  EF --> AC[Accountability and Remedy]
  DR --> AC
```

## 2. Governance framework architecture

```mermaid
flowchart TD
  PD[Primary Document] --> SC[Schedule of Controlled Documents]
  PD --> AT[Authority Topology]
  PD --> TM[Trust-Decision Model]
  PD --> AR[Accountability and Redress Model]
  SC --> GOV[Governance]
  SC --> RISK[Risk, Safety and Impact]
  SC --> DEL[Authority and Delegation]
  SC --> AGT[Agent Lifecycle]
  SC --> EVID[Evidence and Provenance]
  SC --> GRAPH[Trust Graph and Registry]
  SC --> ASSUR[Assurance and Observability]
  SC --> LEGAL[Legal and Cross-Framework]
```

## 3. Multi-hop delegation

```mermaid
flowchart LR
  O[Originating Principal] -->|scope S0| D1[Delegate 1]
  D1 -->|attenuated scope S1| D2[Delegate 2]
  D2 -->|attenuated scope S2| D3[Agent]
  R[Revocation or Expiry] -.propagates.-> D1
  R -.propagates.-> D2
  R -.propagates.-> D3
```

## 4. Runtime governance

```mermaid
sequenceDiagram
  participant Actor
  participant PDP as Governance Decision Service
  participant Registry
  participant Evidence
  participant Tool as Enforcement Point
  Actor->>PDP: Proposed effect + authority context
  PDP->>Registry: Resolve authority, delegation and status
  PDP->>Evidence: Verify evidence and assurance freshness
  PDP->>PDP: Apply policy, risk and impact rules
  alt Allowed
    PDP->>Tool: Permit with constraints and obligations
    Tool-->>PDP: Execution result
  else Review required
    PDP-->>Actor: Route for accountable review
  else Denied
    PDP-->>Actor: Deny with reason code
  end
  PDP->>PDP: Produce decision receipt
```

## 5. Trust graph evaluation

```mermaid
flowchart LR
  RP[Relying Party Policy] --> TD[Contextual Trust Decision]
  N1[Authority Node] -->|recognises| N2[Registry Node]
  N2 -->|asserts status| N3[Actor Node]
  N3 -->|delegates| N4[Agent Node]
  N1 --> EV[Graph Evidence Paths]
  N2 --> EV
  N3 --> EV
  N4 --> EV
  EV --> TD
  ST[Status, Revocation and Conflicts] --> TD
```

## 6. Governance-event lifecycle

```mermaid
stateDiagram-v0.1.0
  [*] --> Proposed
  Proposed --> Issued
  Issued --> Active: acceptance/activation
  Active --> Suspended: incident or policy trigger
  Suspended --> Active: restoration
  Active --> Revoked: withdrawal
  Active --> Expired: time bound reached
  Revoked --> Archived
  Expired --> Archived
  Suspended --> Revoked
```
