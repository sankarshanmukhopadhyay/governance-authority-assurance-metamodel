---
title: "Evidence Catalogue"
permalink: /implementation-reports/evidence-catalogue/
parent: "Implementation Reports"
nav_order: 6
artifact_type: "Evidence catalogue"
normative_status: "Informative"
---
# Evidence Catalogue

{% include gaam-meta.html %}

This catalogue identifies practical evidence classes that may support GAAM implementation and conformance review. It is not an exhaustive normative mapping and does not add requirements. Implementers must determine applicability from the normative specification and selected profile manifests.

| ID | Evidence class | Typical producer | Supports review of | Verification focus | Freshness or lifecycle trigger | Independence consideration |
|---|---|---|---|---|---|---|
| EVD-GOV-001 | Governance package and controlled-document schedule | Governance authority | Applicable rules, precedence, ownership and version | Authority, identifier, version, integrity and approval history | Policy approval, supersession or withdrawal | Operator may produce; accountable approval must be attributable |
| EVD-AUT-001 | Authority source and status record | Competent authority or authoritative registry | Source, scope, validity and status of authority | Issuer competence, scope, effective time and revocation state | Authority transition or source update | Verify source is not merely asserted by the relying implementation |
| EVD-DEL-001 | Delegation record and chain | Principal, delegator or delegation service | Purpose, effects, duration, jurisdiction and redelegation | Parent authority, attenuation, chain integrity and current status | Any parent or child lifecycle transition | Chain evaluator should disclose operational relationship to parties |
| EVD-STR-001 | Schema validation result | Build system, validator or assessor | Structural validity of machine-readable artifacts | Schema identifier, validator version, input digest and errors | Artifact or schema change | Self-produced evidence is suitable for L1 with disclosure |
| EVD-STR-002 | Profile dependency closure result | Conformance harness or assessor | Complete applicability of claimed profiles | Manifest versions, dependency resolution and missing profiles | Profile or GAAM version change | Reviewer should reproduce from canonical manifests |
| EVD-INT-001 | Package manifest and integrity record | Build or release process | Artifact identity and modification detection | Declared scope, hashes, signatures and source revision | Every package build or publication | Separate signing or reproducible build increases assurance |
| EVD-BEH-001 | Positive and negative behavioural test result | Test harness | Enforcement of applicable governance invariants | Test input, expected result, actual result and target version | Code, configuration, policy or dependency change | Test author and operator relationship should be disclosed |
| EVD-BEH-002 | Boundary and failure-mode test result | Test harness or resilience exercise | Expiry, revocation, stale state, partition and fail behaviour | Timing, injected condition, enforcement response and recovery | Material architecture or policy change | Independent witnessing may be needed for higher-risk claims |
| EVD-DEC-001 | Decision receipt | Runtime decision point | Authority, policy, evidence, outcome and accountability for a decision | Binding to target, time, policy, evidence and accountable party | Per decision or declared sampling period | Receipt source may be the target; integrity and completeness need separate verification |
| EVD-LIF-001 | Governance lifecycle event history | Authoritative event source | Issuance, activation, suspension, revocation, expiry and remedy transitions | Ordering, transition authority, effective time and affected descendants | Every material transition | Protect against source equivocation and selective history |
| EVD-OPS-001 | Operational monitoring and control observation | Operator or monitoring service | Continued operation of runtime and assurance controls | Coverage, collection method, gaps, alerts and retained history | Continuous or defined observation window | External monitoring may strengthen but does not automatically establish independence |
| EVD-INC-001 | Incident and corrective-action record | Incident authority or operator | Control failure, impact, correction and claim consequences | Detection, affected scope, root cause, action and verification | Incident detection through closure and follow-up | Material incidents should be available to the claim assessor |
| EVD-REM-001 | Notice, appeal and remedy execution record | Decision operator, review authority or remedy authority | Affected-party notice, review access and implemented correction | Standing, deadlines, independence, outcome and downstream propagation | Per challenge, review or remedy | Review authority should be distinguishable from original decision authority where required |
| EVD-PRI-001 | Privacy and disclosure assessment | Privacy reviewer or accountable authority | Data minimisation, correlation, access, retention and disclosure controls | Data flows, purposes, audiences, risks and mitigations | Material data, purpose or architecture change | Affected-party input and independent review may be necessary for high-impact contexts |
| EVD-SEC-001 | Security assessment and vulnerability disposition | Security team or assessor | Integrity, availability, confidentiality and attack resistance | Scope, method, findings, severity, remediation and retest | Material release, incident or threat change | Independence and assessor competence should be explicit |
| EVD-INTOP-001 | Cross-implementation interoperability result | Two or more implementers or test coordinator | Shared interpretation of receipts, events and artifacts | Producer-consumer matrix, versions, semantic outcomes and failures | Implementation or specification change | No single implementation should control all sides of the test |
| EVD-ASS-001 | Assessment report and assessor declaration | Assessor | Method, sampling, findings, exceptions and assurance conclusion | Scope, competence, independence, evidence reviewed and validity | Review date, expiry, incident or material target change | Required independence must match the claimed conformance level |
| EVD-CLA-001 | Conformance claim status history | Claim issuer or registry | Issuance, limitation, expiry, suspension, withdrawal and supersession | Claim identity, evidence references, authority and status transitions | Every claim lifecycle change | Claim issuer relationship to target must be disclosed |

The machine-readable companion is [`evidence-catalogue.json`](evidence-catalogue.json). Evidence quality should be assessed using the [Evidence Quality Model](evidence-quality-model.md), not inferred from catalogue membership alone.
