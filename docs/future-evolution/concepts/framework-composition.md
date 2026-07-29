---
title: Governance-Framework Composition
permalink: /docs/future-evolution/concepts/framework-composition/
nav_exclude: true
artifact_type: Candidate future concept
normative_status: Informative
---
# Governance-Framework Composition

{% include gaam-meta.html %}

> This is an informative candidate concept for evaluation. It does not modify GAAM v0.9.0 requirements, schemas, profiles, vocabularies, or conformance semantics.

A composed governance system may include a primary framework, jurisdictional overlays, credential frameworks, service rules, assurance programmes, contractual instruments, and continuity plans. Candidate relationships include `extends`, `specialises`, `depends-on`, `imports-requirements-from`, `overrides`, `recognises`, `inherits-authority-from`, `shares-assurance-with`, and `terminates-with-parent`.

A composition model must declare inherited and local requirements, conflict precedence, permitted overrides, authority sources, version compatibility, lifecycle dependencies, and conformance dependency closure.

## Evaluation questions

- Can the current GAAM model represent the concept without ambiguous interpretation?
- Do multiple implementation patterns require the same semantics?
- Is a draft profile, experimental schema, vocabulary, or behavioural vector necessary?
- What privacy, security, affected-party, market, and continuity consequences arise?
- What evidence would justify normative promotion?
