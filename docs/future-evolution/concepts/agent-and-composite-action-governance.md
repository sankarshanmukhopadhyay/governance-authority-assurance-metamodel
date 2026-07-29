---
title: Agent and Composite-Action Governance
permalink: /docs/future-evolution/concepts/agent-and-composite-action-governance/
nav_exclude: true
artifact_type: Candidate future concept
normative_status: Informative
---
# Agent and Composite-Action Governance

{% include gaam-meta.html %}

> This is an informative candidate concept for evaluation. It does not modify GAAM v0.9.0 requirements, schemas, profiles, vocabularies, or conformance semantics.

Agent governance should track model version, policy version, instructions, memory, tools, credentials, runtime environment, operator, provider, deployment instance, and task context. Material state changes may require re-registration, reassurance, authority suspension, or new testing.

Control modes should distinguish advisory, drafting, approval-required, supervised execution, bounded autonomy, continuous autonomy, and emergency autonomy. Plans, steps, tool calls, partial effects, irreversible boundaries, rollback, orchestration, and composite accountability require separate traceability.

## Evaluation questions

- Can the current GAAM model represent the concept without ambiguous interpretation?
- Do multiple implementation patterns require the same semantics?
- Is a draft profile, experimental schema, vocabulary, or behavioural vector necessary?
- What privacy, security, affected-party, market, and continuity consequences arise?
- What evidence would justify normative promotion?
