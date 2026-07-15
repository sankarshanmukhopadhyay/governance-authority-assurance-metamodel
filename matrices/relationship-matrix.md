# Relationship Matrix

| Relationship | Permitted source | Permitted target | Required semantics | Common misuse to prevent |
|---|---|---|---|---|
| holds | Actor | Role | Eligibility, activation, status, time | Treating role as permanent identity |
| governs | Authority / framework | Entity, process, artifact or framework | Mandate, scope, jurisdiction, powers | Assuming unlimited control |
| delegates | Delegator | Delegate | Authority source, scope, purpose, period, redelegation, propagation | Treating access or credentials as delegation |
| recognises | Relying authority / framework | External authority, framework, registry or determination | Accepted classes, purpose, limits, withdrawal | Confusing recognition with delegation |
| accredits | Accrediting authority | Assessor or provider | Competence scope, criteria, validity, status | Treating accreditation as outcome guarantee |
| asserts | Actor / artifact | Claim | Identity, authority to assert, time, context | Treating signed claim as established fact |
| supports | Evidence | Claim, control, assessment or decision | Relevance, provenance, freshness | Reusing evidence outside permitted context |
| verifies | Verifier | Condition or claim | Method, criteria, result, time | Confusing verification with full assurance |
| assesses | Assessor | Entity, control, profile or system | Criteria, evidence, scope, limitations | Generalising beyond assessed scope |
| permits | Authority / policy | Effect | Scope, conditions, validity | Assuming permission from capability |
| prohibits | Authority / policy | Effect | Scope, priority, exception rules | Ignoring prohibition due to lower-level permission |
| constrains | Authority / policy | Action, delegation or effect | Bound, threshold, condition | Silent broadening through implementation |
| depends-on | Entity, service or decision | Component, source or authority | Dependency class, criticality, fallback | Hiding concentration and cascading risk |
| accounts-for | Accountable party | Decision, action or effect | Duty to explain, remedy and bear consequence | Ending accountability at an agent |
| revokes | Authorised actor | Authority, delegation, status or relationship | Effective time, reason, scope, propagation | Ambiguous or delayed revocation |
| suspends | Authorised actor | Authority, delegation, status or relationship | Temporary effect, review, restoration | Treating suspension as deletion |
| supersedes | Artifact / state | Earlier artifact / state | Version order, transition, compatibility | Rollback or stale-state reliance |
| appeals | Affected / authorised party | Decision or effect | Grounds, evidence, route, time | Review without power to alter outcome |
| remedies | Authorised actor / process | Harm, error or non-conformance | Remedy type, authority, completion evidence | Symbolic remediation without restoration |
