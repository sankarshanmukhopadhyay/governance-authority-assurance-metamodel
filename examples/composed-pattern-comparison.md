---
title: "Composed Pattern Comparison"
permalink: /examples/composed-pattern-comparison/
parent: "Implementation Patterns"
artifact_type: Informative implementation pattern
normative_status: Informative
---
# Composed Pattern Comparison
The three composed patterns apply a common GAAM control structure to materially different governance problems.

| Pattern | Primary authority source | Delegation model | Lifecycle focus | Enforcement | Evidence | Review authority | Privacy focus | Security focus | Affected-party route | Interoperability |
|---|---|---|---|---|---|---|---|---|---|---|
| [Delegated Agent Purchasing](delegated-agent-purchase/) | principal purchasing mandate | delegated and attenuated | issued, active, suspended, revoked | merchant transaction gateway | delegation registry | principal review authority | minimisation and purpose limitation | stale or forged authority/state | scoped remedy and downstream correction | not independently tested |
| [Cross-Registry Recognition](cross-registry-recognition/) | source registry mandate | recognition does not imply delegation | proposed, active, restricted, suspended | relying registry query gateway | source registry | recognition review authority | minimisation and purpose limitation | stale or forged authority/state | scoped remedy and downstream correction | not independently tested |
| [High-Impact Multi-Agent Service](high-impact-multi-agent-service/) | service operating mandate | delegated and attenuated | proposed, active, restricted, suspended | orchestration runtime | component agents | independent human review function | minimisation and purpose limitation | stale or forged authority/state | scoped remedy and downstream correction | not independently tested |

## Interpretation

The comparison prevents superficial reuse. A registry-recognition decision is not a purchasing delegation, and a multi-agent orchestration graph cannot dilute composite accountability. Each pattern therefore shares validation mechanics while retaining differentiated authority, lifecycle, evidence and remedy logic.
