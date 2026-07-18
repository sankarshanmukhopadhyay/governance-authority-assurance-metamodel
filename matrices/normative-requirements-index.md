---
title: "Normative Requirements Index"
permalink: /matrices/normative-requirements-index/
parent: "Matrices"
artifact_type: Traceability matrix
normative_status: Assurance supporting
---
# Normative Requirements Index

{% include gaam-meta.html %}


[Download CSV](normative-requirements-index.csv)

<div class="table-wrap">

| requirement_id | section | requirement |
| --- | --- | --- |
| GAAM-CORE-001 | 2.1 Governed entity | A governance framework MUST identify the classes of governed entities within its scope. |
| GAAM-CORE-002 | 2.1 Governed entity | Where a governed entity is a machine, software component or agent, the framework MUST identify one or more accountable persons or organisations and the basis of their accountability. |
| GAAM-CORE-003 | 2.2 Actor | A framework MUST define each governed actor role, including its responsibilities, eligibility, authority limits, obligations and lifecycle. |
| GAAM-CORE-004 | 2.4 Agent | A framework permitting agent participation MUST state which agent classes are permitted and which effects each class may request, recommend, approve or perform. |
| GAAM-CORE-005 | 2.5 Role | A role definition MUST specify the conditions under which the role is assigned, activated, suspended, transferred and terminated. |
| GAAM-AUTH-001 | 2.6 Authority | Every authority recognised by a framework MUST identify its source. |
| GAAM-AUTH-002 | 2.6 Authority | Authority MUST be bounded by sufficient scope information to determine whether a proposed effect falls within it. |
| GAAM-AUTH-003 | 2.6 Authority | Identification, authentication, possession of a credential, registry inclusion or technical capability MUST NOT be treated as sufficient proof of authority unless the framework explicitly defines and validates the authority semantics represented by that artifact or state. |
| GAAM-AUTH-004 | 2.7 Capability | A framework MUST distinguish capability from authority. |
| GAAM-AUTH-005 | 2.7 Capability | Systems enforcing a framework MUST NOT admit a consequential effect solely because an actor possesses the technical means to cause it. |
| GAAM-DEL-001 | 2.8 Delegation | A delegation MUST identify the delegator, delegate, delegated authority, effective period and termination conditions. |
| GAAM-DEL-002 | 2.8 Delegation | Redelegation MUST be expressly authorised. |
| GAAM-DEL-003 | 2.8 Delegation | Each delegation hop MUST NOT enlarge the authority available at the parent hop unless an independently valid authority source authorises the enlargement. |
| GAAM-DEL-004 | 2.8 Delegation | Delegated authority MUST remain traceable to its authority source and, where applicable, to the originating principal. |
| GAAM-DEL-005 | 2.8 Delegation | Suspension, revocation or expiry of parent authority MUST affect descendant authority according to explicit propagation rules. |
| GAAM-DEL-006 | 2.8 Delegation | Delegation MUST NOT extinguish the accountability of a delegator, principal, operator, provider or other party whose accountability is established by law, agreement or framework policy. |
| GAAM-POL-001 | 2.9 Permission, prohibition, obligation and constraint | A framework MUST define how conflicts among permissions, prohibitions, obligations and constraints are resolved. |
| GAAM-POL-002 | 2.9 Permission, prohibition, obligation and constraint | A framework MUST identify the authority under which a permission, prohibition, obligation or constraint is established. |
| GAAM-POL-003 | 2.10 Policy, rule and control | Machine-actionable rules MUST be traceable to their normative policy source and the authority that approved that source. |
| GAAM-POL-004 | 2.10 Policy, rule and control | A governance framework MUST define precedence when human-readable normative text and machine-actionable representations conflict. |
| GAAM-POL-005 | 2.10 Policy, rule and control | Unless the framework explicitly designates a machine-actionable representation as co-normative and defines equivalence tests, the human-readable normative text MUST prevail. |
| GAAM-EVID-001 | 2.11 Claim and assertion | A framework MUST define the classes of claims that may be relied upon and the evidence, provenance, status and assurance needed for each class. |
| GAAM-EVID-002 | 2.12 Evidence | Evidence relied upon for a consequential decision MUST have sufficient provenance to identify its origin and relevant transformations. |
| GAAM-EVID-003 | 2.12 Evidence | A framework MUST define freshness requirements for evidence whose relevance may change over time. |
| GAAM-EVID-004 | 2.12 Evidence | An inability to validate required evidence MUST result in denial, restriction, suspension or human review according to framework policy; it MUST NOT silently result in acceptance. |
| GAAM-ASSUR-001 | 2.13 Verification and assessment | A framework MUST distinguish verification results from broader assurance conclusions. |
| GAAM-ASSUR-002 | 2.13 Verification and assessment | Verification and assessment results MUST identify the criteria, evaluator, time, scope, limitations and evidence used. |
| GAAM-ASSUR-003 | 2.14 Assurance | Assurance MUST NOT be represented as permanent where the underlying conditions, evidence or system state may change. |
| GAAM-ASSUR-004 | 2.14 Assurance | A framework MUST define the validity, renewal, suspension, withdrawal and review conditions of each assurance conclusion it recognises. |
| GAAM-DEC-001 | 2.15 Trust decision | A trust decision MUST be attributable to a decision-maker or accountable decision service. |
| GAAM-DEC-002 | 2.15 Trust decision | A trust path, credential, registry entry, reputation value or assurance mark MUST NOT by itself constitute a trust decision. |
| GAAM-DEC-003 | 2.15 Trust decision | A decision MUST be evaluated in the context of the relying party’s applicable policy, purpose and risk tolerance. |
| GAAM-EFF-001 | 2.16 Effect | A framework MUST identify the consequential effect classes within its scope. |
| GAAM-EFF-002 | 2.16 Effect | A consequential effect MUST NOT be admitted unless the applicable authority, policy, evidence and runtime conditions have been evaluated to the level required by the framework. |
| GAAM-CTX-001 | 2.17 Governance context | A framework MUST identify the governance contexts in which its requirements apply. |
| GAAM-CTX-002 | 2.17 Governance context | Cross-context reliance MUST be governed by explicit recognition, mapping or conflict-resolution rules. |
| GAAM-EVT-001 | 2.18 Governance event | A framework MUST define the governance events that materially affect authority, assurance, status, eligibility, policy or accountability. |
| GAAM-EVT-002 | 2.18 Governance event | Material governance events MUST be attributable, time-stamped and reconstructable. |
| GAAM-ACC-001 | 2.19 Accountability | Every consequential effect MUST have at least one identifiable accountable party. |
| GAAM-ACC-002 | 2.19 Accountability | Machine actors and agents MUST NOT be treated as the terminal point of accountability. |
| GAAM-ACC-003 | 2.19 Accountability | A framework MUST define how accountability is allocated when multiple actors, agents, services, registries or authorities contribute to an effect. |
| GAAM-HARM-001 | 2.20 Harm and remedy | A framework MUST identify material harms that may arise from governed effects, including cumulative and systemic harms where applicable. |
| GAAM-HARM-002 | 2.20 Harm and remedy | A framework governing consequential effects MUST define accessible challenge, review and remedy mechanisms. |
| GAAM-REL-001 | 3.1 Required relationship properties | A relationship used in an automated trust decision MUST have an unambiguous type and declared semantics. |
| GAAM-REL-002 | 3.1 Required relationship properties | A relationship MUST NOT imply broader authority or recognition than its declared scope. |
| GAAM-REL-003 | 3.3 Relationship invariants | Recognition MUST NOT be treated as delegation unless the relationship explicitly grants authority. |
| GAAM-REL-004 | 3.3 Relationship invariants | Accreditation MUST NOT be treated as a guarantee of every output produced by the accredited actor. |
| GAAM-REL-005 | 3.3 Relationship invariants | Registry inclusion MUST NOT be treated as universal trustworthiness. |
| GAAM-REL-006 | 3.3 Relationship invariants | Revocation and suspension semantics MUST identify the affected relationship, effective time, authority and propagation consequences. |
| GAAM-GF-001 | 4.1 Governance framework | A conforming governance framework MUST include a Primary Document and an authoritative Schedule of Controlled Documents. |
| GAAM-GF-002 | 4.1 Governance framework | The Primary Document MUST identify the exact framework version using a persistent identifier. |
| GAAM-GF-003 | 4.1 Governance framework | The framework MUST publish a conformance statement identifying the profiles and conformance targets claimed. |
| GAAM-GF-004 | 4.2.3 Localisation | The framework MUST identify its official language or languages and SHOULD use BCP 47 language tags. |
| GAAM-GF-005 | 4.2.3 Localisation | Where multiple official versions exist, the framework MUST define how inconsistencies are resolved. |
| GAAM-GF-006 | 4.2.5 Governance topology | The framework MUST identify where decision rights, enforcement powers, revision powers and emergency powers reside. |
| GAAM-GF-007 | 4.2.6 Governing authority | Where no single governing authority exists, the framework MUST identify the authority topology and the process by which valid governance decisions are formed. |
| GAAM-GF-008 | 4.2.10 Agentic applicability declaration | Every framework MUST declare whether agents may participate and, if so, whether they may recommend, decide, transact, delegate, use tools, create sub-agents or produce binding effects. |
| GAAM-GF-009 | 4.2.12 Governance-state publication | Governance state required for a runtime decision MUST be discoverable, authenticated and sufficiently current for the decision context. |
| GAAM-GF-010 | 4.2.15 Revisions | The framework MUST define how revisions are proposed, reviewed, approved, versioned, published, deprecated and withdrawn. |
| GAAM-GF-011 | 4.2.15 Revisions | A publicly available framework SHOULD include a public review period for substantive revisions. |
| GAAM-GF-012 | 4.2.15 Revisions | Material policy changes affecting active authority or runtime decisions MUST define transition and notification rules. |
| GAAM-AUTH-006 | 5.1 Authority topology patterns | A framework MUST identify conflicts that may arise among authorities and the procedure for resolving or containing them. |
| GAAM-AUTH-007 | 5.1 Authority topology patterns | Where authorities overlap, the framework MUST define precedence, coordination, refusal or escalation semantics. |
| GAAM-DEL-007 | 5.2 Delegation lifecycle | A delegation MUST NOT become active before required acceptance, registration, verification or other activation conditions are met. |
| GAAM-DEL-008 | 5.2 Delegation lifecycle | The framework MUST define whether delegation is transferable and whether an agent or actor may substitute another delegate. |
| GAAM-DEL-009 | 5.2 Delegation lifecycle | Material substitution of an agent, model, operator, toolchain or execution environment MUST trigger reassessment where it may affect authority, assurance or risk. |
| GAAM-DEL-010 | 5.3 Multi-hop delegation | A multi-hop delegation decision MUST validate each active hop, parent-child scope compatibility, originating-principal continuity, redelegation permission and revocation state. |
| GAAM-DEL-011 | 5.3 Multi-hop delegation | A framework MUST define maximum delegation depth or the policy by which depth is determined. |
| GAAM-DEL-012 | 5.4 Fan-out and convergence | Where authority is divided among multiple delegates, the framework MUST define whether branches are independent, cumulative, mutually exclusive or jointly controlled. |
| GAAM-DEL-013 | 5.4 Fan-out and convergence | Where delegated branches converge on one effect, the aggregate effect MUST be evaluated against the originating authority and applicable aggregate limits. |
| GAAM-AUTH-008 | 5.5 Emergency authority | Emergency authority MUST be narrowly scoped, time-limited, attributable, reviewable and subject to post-event accountability. |
| GAAM-RUN-001 | 6.1 Runtime governance envelope | A framework governing consequential effects MUST define the minimum runtime governance envelope required for each effect class. |
| GAAM-RUN-002 | 6.1 Runtime governance envelope | A runtime decision MUST fail safely when required authority, policy, evidence, status or context cannot be validated. |
| GAAM-RUN-003 | 6.1 Runtime governance envelope | Runtime governance MUST evaluate current revocation and suspension state to the freshness required by the effect’s risk. |
| GAAM-RUN-004 | 6.2 Decision outcomes | Outcome semantics MUST be unambiguous to the enforcement point. |
| GAAM-RUN-005 | 6.3 Decision receipt | Each consequential effect MUST produce or reference a decision receipt proportionate to the effect’s risk and accountability requirements. |
| GAAM-RUN-006 | 6.3 Decision receipt | A receipt MUST NOT expose confidential evidence beyond what is necessary for authorised audit, review or challenge. |
| GAAM-RUN-007 | 6.3 Decision receipt | The framework MUST define retention, access, disclosure, correction and deletion rules for receipts. |
| GAAM-RUN-008 | 6.4 Ongoing evaluation | Where authority, risk or evidence may materially change during execution, the framework MUST define conditions for re-evaluation, interruption or containment. |
| GAAM-RUN-009 | 6.4 Ongoing evaluation | Runtime revocation MUST be capable of stopping or constraining ongoing activity where technically and legally feasible. |
| GAAM-AGT-001 | 7.1 Agent identity and continuity | A framework MUST define the attributes needed to identify an agent for governance purposes. |
| GAAM-AGT-002 | 7.1 Agent identity and continuity | A framework MUST define when changes to model, instructions, memory, tools, operator, provider, execution environment or policy configuration constitute a material change of agent state or identity. |
| GAAM-AGT-003 | 7.1 Agent identity and continuity | Material changes MUST trigger re-registration, renewed assurance, restricted operation or another declared lifecycle response where necessary. |
| GAAM-AGT-004 | 7.2 Agent principals and accountable parties | An agent performing an effect on behalf of a principal MUST carry or reference verifiable authority for that effect. |
| GAAM-AGT-005 | 7.2 Agent principals and accountable parties | The framework MUST identify the principal, operator, provider, deployer and supervisor roles applicable to each agent class and allocate accountability among them. |
| GAAM-AGT-006 | 7.3 Task-bound authority | Agent authority SHOULD be bound to a task, purpose or effect class wherever practical. |
| GAAM-AGT-007 | 7.3 Task-bound authority | Tool access SHOULD be limited to what is necessary for the authorised task. |
| GAAM-AGT-008 | 7.3 Task-bound authority | An agent MUST NOT infer authority from mere access to accounts, credentials, data, APIs or tools. |
| GAAM-AGT-009 | 7.4 Planning and policy evaluation | An agent or supervising service MUST evaluate applicable governance constraints before executing a consequential plan step. |
| GAAM-AGT-010 | 7.4 Planning and policy evaluation | Where an agent cannot determine whether a planned effect is authorised, it MUST deny, restrict or escalate rather than assume permission. |
| GAAM-AGT-011 | 7.5 Redelegation and sub-agents | An agent MUST NOT create a sub-agent, substitute another agent or redelegate authority unless explicitly permitted. |
| GAAM-AGT-012 | 7.5 Redelegation and sub-agents | A sub-agent MUST receive no more authority than the delegating agent is authorised to redelegate. |
| GAAM-AGT-013 | 7.5 Redelegation and sub-agents | The originating principal and accountable-party chain MUST remain discoverable across sub-agent relationships. |
| GAAM-AGT-014 | 7.6 Multi-agent coordination | A framework permitting multi-agent coordination MUST define how authority, task state, evidence, obligations and accountability are partitioned and reconciled. |
| GAAM-AGT-015 | 7.6 Multi-agent coordination | Coordination protocols MUST NOT be assumed to provide governance semantics unless those semantics are explicitly defined and validated. |
| GAAM-AGT-016 | 7.6 Multi-agent coordination | Where multiple agents contribute to one effect, the decision receipt MUST identify the material contributions and accountable parties. |
| GAAM-AGT-017 | 7.7 Tool governance | Tools capable of producing consequential effects MUST enforce or receive sufficient authority and policy context to prevent unauthorised invocation. |
| GAAM-AGT-018 | 7.7 Tool governance | Tool outputs used as evidence MUST carry provenance and integrity appropriate to the decision. |
| GAAM-AGT-019 | 7.8 Human oversight and guardianship | A framework requiring human oversight MUST specify who performs it, when it occurs, what information is available, and what intervention powers exist. |
| GAAM-AGT-020 | 7.8 Human oversight and guardianship | A guardian or supervisory agent MUST itself be governed by explicit authority, constraints and accountability. |
| GAAM-AGT-021 | 7.9 Agent suspension and termination | A framework MUST define mechanisms to suspend, isolate, contain or terminate an agent when authority, assurance or safety conditions fail. |
| GAAM-AGT-022 | 7.9 Agent suspension and termination | Termination MUST address outstanding tasks, delegated authority, retained data, tools, obligations and evidence preservation. |
| GAAM-GRAPH-001 | 8.1 Trust graph | Graph relationships used for automated decisions MUST be typed, scoped, attributable, time-bounded where applicable and linked to status or revocation semantics. |
| GAAM-GRAPH-002 | 8.1 Trust graph | A graph path MUST be treated as evidence for a decision, not as the decision itself. |
| GAAM-GRAPH-003 | 8.4 Graph provenance and integrity | Each material graph assertion MUST identify the asserting party and authority basis. |
| GAAM-GRAPH-004 | 8.4 Graph provenance and integrity | A graph implementation MUST provide integrity and provenance sufficient to detect unauthorised alteration of relied-upon assertions. |
| GAAM-GRAPH-005 | 8.4 Graph provenance and integrity | Derived edges or computed trust values MUST identify their derivation method, input sources and applicable policy. |
| GAAM-GRAPH-006 | 8.5 Graph traversal | A framework MUST define permitted traversal depth, relationship types, path constraints and evidence thresholds for each automated decision class. |
| GAAM-GRAPH-007 | 8.5 Graph traversal | A relying party MUST apply its own policy to determine whether a discovered path is sufficient. |
| GAAM-GRAPH-008 | 8.6 Conflicting claims | A framework MUST define how conflicting, stale, superseded or contested graph assertions are represented and evaluated. |
| GAAM-GRAPH-009 | 8.6 Conflicting claims | Absence of a negative assertion MUST NOT automatically be interpreted as positive trust unless the framework explicitly justifies that inference. |
| GAAM-REG-001 | 8.7 Registry governance | Registry inclusion MUST have explicit semantics and MUST NOT be represented as general trustworthiness. |
| GAAM-REG-002 | 8.7 Registry governance | A registry framework MUST define who may create, update, suspend, revoke, correct and archive each record class. |
| GAAM-REG-003 | 8.7 Registry governance | Registry records used for decisions MUST expose sufficient status, provenance, authority and version information. |
| GAAM-REG-004 | 8.7 Registry governance | A registry MUST provide a correction and dispute path for materially incorrect or unauthorised records. |
| GAAM-REG-005 | 8.8 Registry federation and recognition | Federation MUST distinguish data replication, technical interoperability, recognition of authority and reliance upon determinations. |
| GAAM-REG-006 | 8.8 Registry federation and recognition | Recognition of another registry MUST state the accepted record classes, purposes, assurance thresholds, jurisdictional limits and withdrawal conditions. |
| GAAM-ASSUR-005 | 9.1 Assurance forms | The framework MUST define what each assurance form establishes and what it does not establish. |
| GAAM-ASSUR-006 | 9.2 Assurance providers | Assurance providers MUST disclose material conflicts of interest and the basis of their competence and authority. |
| GAAM-ASSUR-007 | 9.2 Assurance providers | Assurance results MUST be challengeable and correctable when materially wrong. |
| GAAM-ASSUR-008 | 9.3 Continuous assurance | A Continuous Assurance Profile framework MUST define monitored controls, evidence sources, sampling or event frequency, thresholds, drift conditions, escalation and suspension actions. |
| GAAM-ASSUR-009 | 9.3 Continuous assurance | A continuous assurance service MUST identify data gaps, blind spots and periods during which assurance could not be maintained. |
| GAAM-OBS-001 | 9.4 Observability | Observability requirements MUST be proportionate and MUST account for privacy, confidentiality, minimisation and security. |
| GAAM-OBS-002 | 9.4 Observability | The absence of observable data MUST NOT be presented as evidence of compliant behaviour. |
| GAAM-ASSUR-010 | 9.5 Trust marks | A trust mark MUST identify or resolve to its issuer, scope, criteria, validity, status and limitations. |
| GAAM-ASSUR-011 | 9.5 Trust marks | A trust mark MUST NOT imply broader assurance than the underlying assessment supports. |
| GAAM-RISK-001 | 10.1 Risk model | Risk assessment MUST examine authority paths, evidence paths, dependencies, graph edges, delegated capabilities and affected parties, not only roles and processes. |
| GAAM-RISK-002 | 10.2 Impact thresholds | A framework MUST define effect classes or thresholds that require enhanced evidence, approval, assurance, monitoring or human review. |
| GAAM-HARM-003 | 10.3 Cumulative and systemic harm | A framework MUST consider harms arising cumulatively across repeated low-level decisions where such harms are reasonably foreseeable. |
| GAAM-HARM-004 | 10.3 Cumulative and systemic harm | A framework SHOULD identify concentration, lock-in, exclusion, manipulation and market-power risks created by trust infrastructure. |
| GAAM-RISK-003 | 10.4 Safety controls | Controls relied upon to prevent high-impact effects MUST be testable or auditable and linked to accountable owners. |
| GAAM-RED-001 | 11.1 Affected parties | A framework MUST identify affected-party classes, including persons who are not members of the trust community. |
| GAAM-RED-002 | 11.2 Notice and explanation | Affected parties SHOULD receive notice of consequential decisions where lawful and practicable. |
| GAAM-RED-003 | 11.2 Notice and explanation | A framework MUST define the explanation information available for consequential decisions, including reason codes, applicable policy and review route. |
| GAAM-RED-004 | 11.3 Challenge and review | A challenge mechanism MUST permit submission of corrections, contrary evidence and claims of unauthorised action. |
| GAAM-RED-005 | 11.3 Challenge and review | Review MUST be performed by an actor or process with authority to confirm, modify, reverse or remedy the decision. |
| GAAM-RED-006 | 11.3 Challenge and review | A framework MUST define response and resolution time expectations proportionate to the potential harm. |
| GAAM-RED-007 | 11.4 Remedy | A framework MUST identify which remedies are available, who may order them and how compliance is verified. |
| GAAM-RED-008 | 11.5 Cross-framework disputes | Where an effect depends on multiple governance frameworks, the frameworks SHOULD define coordination, evidence sharing, jurisdiction and fallback procedures for disputes. |
| GAAM-MAG-001 | 13. Machine-actionable governance package | A machine-actionable package MUST be traceable to the authoritative human-readable framework. |
| GAAM-MAG-002 | 13. Machine-actionable governance package | The package MUST identify its version, effective period, status and integrity mechanism. |
| GAAM-MAG-003 | 13. Machine-actionable governance package | A material package change MUST follow the framework’s revision and transition requirements. |
| GAAM-MAG-004 | 13. Machine-actionable governance package | A package MUST NOT silently broaden authority or reduce obligations relative to the authoritative framework. |
| GAAM-MAG-005 | 13. Machine-actionable governance package | Conformance tests SHOULD include valid, invalid and boundary-condition examples. |
| GAAM-PROF-001 | 14.7 High-Impact Systems Profile | A profile claim MUST identify the specification version, profile version, applicable conformance targets, exclusions and evidence location. |
| GAAM-PROF-002 | 14.7 High-Impact Systems Profile | A framework MUST NOT claim a profile when a mandatory category or requirement is omitted without an explicitly permitted exception. |
| GAAM-CONF-001 | 15.2 Conformance claim | Conformance claims MUST be scoped to an identified target and MUST NOT be generalised to related entities or transactions without evidence. |
| GAAM-CONF-002 | 15.2 Conformance claim | Framework conformance MUST NOT be presented as proof that every governed actor, agent, decision or transaction conforms. |
| GAAM-CONF-003 | 15.2 Conformance claim | An agent conformance claim MUST NOT be presented as proof that every future action of that agent is authorised or safe. |
| GAAM-CONF-004 | 15.3 Evidence of conformance | Evidence MUST be sufficient to reproduce or independently evaluate the conformance conclusion to the degree required by the claimed profile. |
| GAAM-CONF-005 | 15.4 Exceptions and compensating controls | Exceptions MUST identify the requirement, rationale, authority, duration, risk, compensating control and review date. |
| GAAM-CONF-006 | 15.5 Non-conformance | A framework MUST define classification, notification, remediation, suspension and appeal procedures for non-conformance. |
| GAAM-SEC-001 | 16. Security, privacy and resilience considerations | Governance-critical artifacts MUST be protected against unauthorised modification and rollback. |
| GAAM-SEC-002 | 16. Security, privacy and resilience considerations | Frameworks MUST define recovery and continuity procedures for unavailable or compromised governance services. |
| GAAM-PRIV-001 | 16. Security, privacy and resilience considerations | Evidence, receipts and observability data MUST be minimised to what is necessary for governance, assurance, accountability and lawful obligations. |
| GAAM-PRIV-002 | 16. Security, privacy and resilience considerations | Access to sensitive governance records MUST be controlled, auditable and purpose-bound. |
| GAAM-RES-001 | 16. Security, privacy and resilience considerations | A framework MUST identify critical dependencies and define safe behaviour when they are unavailable or untrustworthy. |
| GAAM-ART-001 | 18.1 Canonical authority records | A machine-actionable authority record MUST identify its authority source, issuer, subject, permitted effects, scope, effective period, status, revocation authority and accountable parties. |
| GAAM-ART-002 | 18.1 Canonical authority records | An authority record MUST distinguish permissions, prohibitions, obligations and constraints. |
| GAAM-ART-003 | 18.1 Canonical authority records | A system MUST NOT treat an authority record as operative when its status, effective period, governing context or integrity cannot be validated. |
| GAAM-ART-004 | 18.2 Canonical delegation records | A delegation record MUST identify its parent authority, delegator, delegate, delegated scope, effective period, redelegation rule, status and propagation behaviour. |
| GAAM-ART-005 | 18.2 Canonical delegation records | Effective child authority MUST be no broader than the intersection of valid parent authority, delegated scope, applicable policy, current context, active status, valid time and applicable constraints. |
| GAAM-ART-006 | 18.2 Canonical delegation records | A delegation transition MUST emit or preserve a governance event sufficient to reconstruct the transition authority, time, prior state, new state and supporting evidence. |
| GAAM-LIFE-001 | 18.3 Governance artifact lifecycles | A conformant implementation MUST apply declared lifecycle states and transitions to governance-critical artifacts. |
| GAAM-LIFE-002 | 18.3 Governance artifact lifecycles | Lifecycle transition rules MUST identify the authority permitted to cause each transition and the evidence required for that transition. |
| GAAM-LIFE-003 | 18.3 Governance artifact lifecycles | An invalid, unauthorised or out-of-sequence lifecycle transition MUST fail without activating the requested governance state. |
| GAAM-LIFE-004 | 18.3 Governance artifact lifecycles | Suspension, revocation, expiry, supersession and termination MUST have explicit effects on dependent artifacts and active decisions. |
| GAAM-LIFE-005 | 18.3 Governance artifact lifecycles | Archived governance artifacts MUST remain reconstructable but MUST NOT be treated as operative unless explicitly restored through an authorised transition. |
| GAAM-ASR-001 | 18.4 Assurance expressions | An assurance assertion MUST identify its subject, evaluated property, criteria, evaluator, method, evidence, scope, governance context, validity period, status, limitations and challenge route. |
| GAAM-ASR-002 | 18.4 Assurance expressions | Assurance labels from different domains or profiles MUST NOT be treated as equivalent without an explicit mapping of criteria, scope, evidence, evaluator competence, context and validity. |
| GAAM-ASR-003 | 18.4 Assurance expressions | Stale, suspended, withdrawn or contradicted assurance MUST trigger profile-defined safe behaviour. |
| GAAM-PCOMP-001 | 18.5 Profile composition | Every profile other than the Foundation Profile MUST declare the Foundation Profile as a dependency. |
| GAAM-PCOMP-002 | 18.5 Profile composition | A profile MUST declare its conformance targets, normative requirement mappings, required artifacts, required evidence, required tests, permitted exclusions and dependencies. |
| GAAM-PROF-003 | 18.5 Profile composition | A composite profile claim MUST satisfy dependency closure and MUST NOT suppress conflicting or additional requirements without an explicit resolution rule. |
| GAAM-PROF-004 | 18.5 Profile composition | A partial implementation MUST NOT claim full profile conformance. |
| GAAM-OUT-001 | 18.6 Decision outcomes and receipts | A trust decision MUST use a declared outcome vocabulary and identify any conditions attached to the outcome. |
| GAAM-OUT-002 | 18.6 Decision outcomes and receipts | The base outcome vocabulary MUST support permit, deny, permit-with-conditions, restrict, suspend, require-additional-evidence, require-additional-approval, route-for-review and terminate. |
| GAAM-OUT-003 | 18.6 Decision outcomes and receipts | A decision receipt for a consequential effect MUST identify the decision, applicable authority, policy, evidence references, assurance references, outcome, conditions, decision time, enforcement point and accountable party. |
| GAAM-DEC-004 | 18.6 Decision outcomes and receipts | A receipt MUST minimise disclosed information while preserving sufficient provenance for review and reconstruction. |
| GAAM-SAFE-001 | 18.7 Privacy, safety and affected-party protections | Governance evidence and receipts MUST be limited to information necessary for the declared purpose and review obligations. |
| GAAM-SAFE-002 | 18.7 Privacy, safety and affected-party protections | A high-impact system MUST define interruption authority, degraded operation, safe failure, recovery and post-event review. |
| GAAM-SAFE-003 | 18.7 Privacy, safety and affected-party protections | Emergency authority MUST be time-bounded, purpose-bounded, attributable and subject to independent or otherwise conflict-controlled review. |
| GAAM-APR-001 | 18.7 Privacy, safety and affected-party protections | A consequential effect MUST identify affected-party notice, explanation, challenge, review and remedy arrangements proportionate to the effect. |
| GAAM-APR-002 | 18.7 Privacy, safety and affected-party protections | A review mechanism MUST have practical authority to suspend, reverse, correct or remediate an outcome. |
| GAAM-APR-003 | 18.7 Privacy, safety and affected-party protections | Remedy completion MUST produce evidence linked to the original decision and effect. |
| GAAM-SYS-001 | 18.7 Privacy, safety and affected-party protections | A high-impact framework MUST define how individual effect records are aggregated to detect recurring, cohort-level or systemic harm. |
| GAAM-SYS-002 | 18.7 Privacy, safety and affected-party protections | Detection of a declared systemic-harm threshold MUST trigger a governed intervention and preserve evidence of the response. |
| GAAM-MKT-001 | 18.8 Market integrity and recognition | Registry inclusion, accreditation or recognition MUST NOT be represented as universal trustworthiness. |
| GAAM-MKT-002 | 18.8 Market integrity and recognition | A framework MUST disclose material conflicts of interest affecting registry, accreditation or assurance decisions. |
| GAAM-MKT-003 | 18.8 Market integrity and recognition | A high-impact recognition arrangement MUST address opaque exclusion, portability barriers, self-preferencing and unsupported equivalence claims. |

</div>
