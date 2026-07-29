---
title: "Pattern Maturity Model"
permalink: /examples/pattern-maturity-model/
parent: "Implementation Patterns"
artifact_type: Informative implementation pattern
normative_status: Informative
---
# Pattern Maturity Model
| Level | Meaning | Minimum evidence |
|---|---|---|
| Conceptual | Roles and governance flow | Narrative and diagram |
| Structural | Machine-readable artifacts | Valid fixtures and manifest |
| Behavioural | Positive and negative outcomes | Behavioural-vector references |
| Operational | Lifecycle, enforcement and evidence | Runtime sequence and state handling |
| Assurance-ready | Requirement and evidence mapping | Traceability and conformance limitations |
| Interoperability-tested | Multiple independent implementations | Cross-validator evidence |

A pattern may claim only the highest level for which all lower-level evidence is present. The three composed patterns in this commit claim `assurance-ready`; they do not claim interoperability testing.
