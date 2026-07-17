---
title: "GAAM Source Adoption and Architectural Differentiation Crosswalk"
permalink: /mappings/tsmm-v0.22.0/
parent: "Mappings and Source Crosswalks"
artifact_type: "Source adoption crosswalk"
normative_status: "Informative"
---
{% include gaam-meta.html %}

## ToIP Governance Metamodel v1.0, Companion Guide v1.0, and TSMM v0.22.0

**Status:** Informative provenance and architectural differentiation record  
**Canonical repository:** [Trust Systems Meta-Model](https://github.com/sankarshanmukhopadhyay/trust-systems-meta-model)  
**Reviewed baseline:** v0.22.0 archive  
**Reference status:** Informative; no normative dependency  
**Immutable revision:** To be recorded from the source tag or reviewed archive digest before v1.0.0  
**Governance sources:** ToIP Governance Metamodel Specification v1.0 and ToIP Governance Metamodel Specification Companion Guide v1.0, 21 December 2021  
**Purpose:** Document how the ToIP governance-framework architecture and TSMM operational semantics informed GAAM, while preserving GAAM as an independent specification.

---

## Source status, attribution and independence

This crosswalk records source materials and design inputs considered during the development of GAAM. GAAM is an independent specification. It is not a revision, extension, profile or implementation of the ToIP Governance Metamodel Specification, and it does not claim Trust Over IP Foundation endorsement or ToIP conformance. References to ToIP and TSMM materials are informative unless an individual GAAM provision expressly states otherwise. GAAM requirements, profiles, schemas, conformance claims and versioning are governed solely by the GAAM repository.

The following source identifiers are used throughout this document:

| Source identifier | Source | Function in this crosswalk |
|---|---|---|
| `TOIP-GMS-1.0` | Trust Over IP Foundation, *ToIP Governance Metamodel Specification*, Version 1.0, 21 December 2021 | Institutional and documentary governance-framework source model |
| `TOIP-GMCG-1.0` | Trust Over IP Foundation, *ToIP Governance Metamodel Specification Companion Guide*, Version 1.0, 21 December 2021 | Explanatory guidance for modular documents, terminology, drafting and publication |
| `TSMM-0.22.0` | *Trust Systems Meta-Model*, Version 0.22.0 | Operational semantics for authority, delegation, evidence, assurance, effects and runtime governance |
| `GAAM` | Governance, Authority and Assurance Metamodel | Independent synthesis, extension and normative treatment |

The two ToIP documents are published under the Creative Commons Attribution 4.0 International licence. GAAM adaptations, classifications and conclusions are the responsibility of the GAAM maintainers. See [`ATTRIBUTIONS.md`](../ATTRIBUTIONS.md).

---

## 1. Executive determination

The TSMM v0.22.0 archive should be treated as a major source model for the GAAM, but it should not be imported wholesale and should not replace the governance metamodel.

The two models address different architectural layers:

| Model | Primary concern | Role in GAAM development |
|---|---|---|
| ToIP Governance Metamodel Specification v1.0 | How a governance framework is constituted, documented, administered and revised | Institutional and documentary foundation |
| TSMM v0.22.0 | How authority, policy, evidence, verification and context combine to govern operational effects | Operational semantic foundation |
| GAAM | How institutions and technical systems govern authority, delegation, decisions, effects, assurance and accountability across human, agentic and decentralised environments | Integrated governance, authority and assurance metamodel |

The core drafting rule should be:

> **TSMM describes the trust-system objects and relationships through which operational trust decisions are formed. GAAM defines how those objects, relationships, decisions and effects must be constituted, governed, evidenced, challenged and made accountable.**

The crosswalk reaches five principal conclusions:

1. **Adopt the effect-centred operating thesis.** Governance should ultimately control whether a defined effect may occur, not merely whether an actor or document is compliant.
2. **Adopt authority, delegation, evidence, trust decision, effect and lifecycle event as first-class concepts.** These extend areas that are not developed in the ToIP v1.0 source model.
3. **Adopt runtime governance envelopes and decision receipts with modification.** They provide the bridge from framework policy to transaction-level execution and accountability.
4. **Adopt typed graph relationships, delegation lineage and lifecycle semantics.** These are essential for decentralised trust graphs and multi-agent systems.
5. **Retain institutional legitimacy, legal authority, affected-party protection, redress and framework constitution in GAAM.** TSMM does not sufficiently cover these matters.


---

## 2. Method and source quality

### 2.1 Materials assessed

The review covered the TSMM v0.22.0 repository structure, including:

- core model and relationship documentation;
- the canonical entity and graph models;
- authority and delegation models;
- lifecycle and effect-evaluation models;
- runtime governance envelope and decision receipt;
- agentic AI, assurance and verifiable trust community extensions;
- agent discovery, capability negotiation, interaction and task-evidence models;
- conformance profiles and testability documentation;
- registry and interoperability models;
- threat model;
- JSON Schemas, YAML models, examples and test vectors;
- protocol and ecosystem bindings.

The ToIP Governance Metamodel Specification v1.0 was used as an informative institutional and documentary source model. The Companion Guide was used to interpret its modular document architecture, terminology discipline, drafting conventions and publication model. Their relevant strengths include the primary-document model, governing and administering authority sections, controlled-document architecture, separation of human-auditable policies from machine-testable rules, risk and assurance categories, legal agreements and revision governance.

### 2.2 Validation results

The archive is materially executable rather than merely conceptual.

The following validation surfaces passed:

- all published examples against their schemas;
- canonical YAML models;
- valid and invalid conformance test vectors;
- schema property coverage;
- documentation metadata and internal-link checks.

One catalog-level validation issue was found:

- `bindings/dcas/tsmm-dcas-binding.json` fails the binding schema because the required `maturity` property is absent.

Two release-freshness inconsistencies were also found:

- the root `VERSION` file and v0.22.0 release notes identify the release as v0.22.0;
- portions of the README still display v0.21.0 badges, version text and release posture.

These issues do not invalidate TSMM as the conceptual baseline, but they demonstrate why GAAM should distinguish **semantic adoption** from **normative external dependency**. GAAM should adopt stable semantics from the v0.22.0 snapshot rather than normatively importing the repository as an undifferentiated whole.

### 2.3 Adoption classifications

| Classification | Meaning in this crosswalk |
|---|---|
| **Adopt directly** | Carry the essential TSMM concept and semantics into the GAAM core with only standards-language normalization |
| **Adopt with modification** | Preserve the concept but broaden, constrain or reposition it for governance use |
| **Normative compatibility reference** | Keep detailed expression outside GAAM but require compatible semantics or artifacts |
| **Informative reference** | Cite or explain as implementation guidance without creating conformance dependency |
| **Retain in TSMM** | Useful operational or protocol-level detail that should not become part of the governance metamodel |
| **Reject or replace** | Do not carry the concept as currently framed |
| **Open design issue** | Requires a deliberate drafting choice or community decision |

---

## 3. Boundary between TSMM and GAAM

### 3.1 What GAAM should own

The GAAM specification should be authoritative for:

- constitution and legitimacy of governing arrangements;
- authority topology and institutional mandates;
- governed roles and accountability assignments;
- governance-framework document architecture;
- normative policy and controlled-document requirements;
- requirements for delegation, agent operation, evidence and assurance;
- trust-graph governance requirements;
- affected-party rights, challenge and redress;
- cross-framework recognition and policy conflict;
- conformance targets and claims;
- governance-state publication;
- change control, revisions, extensions and deprecation.

### 3.2 What TSMM should continue to own

TSMM should remain the portable semantic and implementation-facing reference model for:

- reusable trust-system primitives;
- graph instance structures;
- reusable authority and delegation patterns;
- protocol and ecosystem bindings;
- executable schemas and examples;
- implementation walkthroughs;
- interoperability comparison artifacts;
- detailed runtime payloads where GAAM only specifies required semantics.

### 3.3 What should be jointly aligned

The models should share compatible definitions for:

- actor and role;
- authority;
- delegation;
- policy and requirement;
- evidence;
- verification and assessment;
- trust decision;
- effect;
- lifecycle event;
- governance context;
- profile;
- trust boundary;
- runtime governance record;
- decision receipt.

The definitions need not be textually identical. They must, however, avoid semantic contradiction.

---

## 4. Core concept adoption matrix

### 4.1 Foundational entities

| TSMM concept | TSMM meaning | ToIP v1.0 treatment | Adoption decision | GAAM treatment |
|---|---|---|---|---|
| Entity | Any actor, component or participant in a trust system | Implicit through actor and governed party | **Adopt with modification** | Define **governed entity** as the broad superclass; avoid allowing the abstraction to obscure legal or accountable persons |
| Actor | Person, organization, software agent or system component capable of participating | Actor may be human or machine, but is minimally developed | **Adopt directly** | Make actor a first-class participant capable of requesting, performing, approving, denying or being affected by an action |
| Role | Context-specific capacity in which an actor operates | Primary governed roles are mentioned in scope | **Adopt directly** | Require roles to have responsibilities, authority limits, obligations, eligibility and lifecycle |
| Agent | Software system capable of action under delegated or native authority | Not developed | **Adopt with modification** | Define agent classes and distinguish principal, operator, deployer, provider, supervisor and affected party |
| Resource | Object or service against which an action is attempted | Not explicit | **Adopt with modification** | Include as an optional core concept where access, modification, transfer or control is governed |
| Artifact | Structured object carrying trust-relevant information | Controlled documents and governed artifacts exist, but the term is not generalized | **Adopt directly** | Use for credentials, registry records, policies, receipts, evidence bundles, status records and other governed objects |

**Recommendation:** GAAM should retain the broad actor model but require accountable-party mappings whenever the actor is a machine, component or agent. “The agent acted” must never be allowed to terminate the accountability chain.

### 4.2 Authority and delegation

| TSMM concept | Adoption decision | Required GAAM refinement |
|---|---|---|
| Authority | **Adopt directly** | Define as a bounded and recognised ability to permit, perform, approve, prohibit, delegate or constrain an effect |
| Authority source | **Adopt directly** | Require the legal, contractual, technical, communal or policy basis from which authority originates |
| Scope | **Adopt directly** | Make scope multidimensional: action, resource, purpose, jurisdiction, time, value, risk, subject and delegation depth |
| Delegation | **Adopt with modification** | Add delegator, delegate, originating principal, acceptance, obligations, redelegation, termination and accountability consequences |
| Direct authority | **Adopt directly** | Use as a recognised authority topology pattern |
| Delegated authority | **Adopt directly** | Require parent-chain verification, attenuation and revocation propagation |
| Federated authority | **Adopt with modification** | Separate mutual recognition from transfer of authority; local relying policy remains decisive |
| Conditional authority | **Adopt directly** | Conditions must be re-evaluated at the point of effect where material |
| Chained delegation | **Adopt directly** | Make originating-principal continuity and monotonic attenuation normative for agentic profiles |
| Fan-out delegation | **Adopt directly** | Require aggregate-authority checks when branches converge |
| Authority graph | **Adopt with modification** | Expand the graph to include recognition, accreditation, dependency, accountability, prohibition and revocation relationships |
| Capability | **Adopt with modification** | State the invariant: capability does not establish authority |

#### Normative invariants recommended for GAAM

1. An actor **MUST NOT** be treated as authorised merely because it has the technical capability or credentials needed to perform an effect.
2. Delegated authority **MUST** remain traceable to an authority source and, where applicable, an originating principal.
3. Each delegation hop **MUST NOT** enlarge the authority granted by its parent unless an independently valid authority source authorises the enlargement.
4. Redelegation **MUST** be explicitly authorised.
5. Revocation, suspension or expiry of a parent authority **MUST** affect descendant authority according to declared propagation rules.
6. Where fan-out delegations converge, the aggregate effect **MUST** remain within the parent authority.
7. Delegation **MUST NOT** extinguish the accountability of the delegating principal or other accountable parties.

### 4.3 Claims, policy and controls

| TSMM concept | Adoption decision | GAAM treatment |
|---|---|---|
| Claim | **Adopt directly** | A proposition subject to evaluation, not a fact merely because it is signed or registered |
| Requirement | **Adopt with modification** | Align with the ToIP v1.0 RFC 2119-based requirement model; distinguish normative requirement from expectation |
| Policy | **Adopt with modification** | Preserve the ToIP v1.0 human-auditable policy concept while also defining policy artifacts that guide or govern automated evaluation |
| Rule | **Retain and strengthen from ToIP v1.0** | A machine-testable expression of a requirement; connect it explicitly to policy source and authority |
| Control | **Adopt directly** | Safeguard that reduces risk, constrains unsafe operation or provides evidence of governance implementation |
| Threat | **Adopt with modification** | Broaden beyond technical threats to harms, abuse cases, institutional failure and market manipulation |
| Profile | **Adopt directly** | A composable package of requirements, controls, evidence expectations, tests and permitted effects |
| Governance Context | **Adopt directly** | Context in which policy, authority, evidence and trust decisions are interpreted |

#### Terminology reconciliation

TSMM currently describes a requirement as a condition a system or participant “should” satisfy. The ToIP Governance Metamodel Specification v1.0 defines requirements more rigorously through RFC 2119 keywords. GAAM should preserve the ToIP v1.0 discipline. TSMM-compatible artifacts may describe expectations, but only provisions expressed according to the specification’s normative-language rules should be considered GAAM requirements.

The GAAM specification should distinguish:

- **principle:** non-testable statement of intent or value;
- **policy:** human-auditable normative requirement or coherent policy set;
- **rule:** machine-testable normative expression;
- **control:** mechanism intended to satisfy or enforce requirements;
- **procedure:** prescribed operational sequence;
- **decision criterion:** condition used to produce an outcome;
- **obligation:** action that becomes due following a trigger.

### 4.4 Evidence, assessment and verification

| TSMM concept | Adoption decision | Required GAAM refinement |
|---|---|---|
| Evidence | **Adopt directly** | Require provenance, subject, producer, integrity, status, freshness, permitted use and confidentiality metadata where applicable |
| Evidence Artifact | **Adopt directly** | Define a governed artifact capable of supporting a claim, requirement, control, decision or outcome |
| Evidence Bundle | **Adopt directly** | Use for replayable assessment and transaction accountability |
| Verification | **Adopt directly** | A bounded check of whether a specified condition holds |
| Assessment | **Adopt directly** | Broader evaluation that may consume evidence and verification results |
| Assurance Activity | **Adopt with modification** | Place within the assurance controlled-document category and continuous-assurance model |
| Assurance Decision | **Adopt with modification** | Clarify that it is contextual, time-bounded and distinct from a runtime trust decision |
| Validation Record | **Adopt directly** | Use as evidence of a specific validation or test operation |
| Assurance Level | **Adopt with modification** | Require declared semantics; do not permit level labels to imply universal trustworthiness |

#### Normative invariants recommended for GAAM

1. Evidence **MUST** be distinguishable from the claim or conclusion it supports.
2. Verification **MUST** identify the condition checked, method, inputs, time and result.
3. Assessment **MUST** identify the applicable requirements or profile and the evidence used.
4. Assurance conclusions **MUST** be bounded by scope, context, time and method.
5. Absence of negative evidence **MUST NOT** automatically be interpreted as positive assurance.
6. Evidence used for consequential effects **SHOULD** be reproducible or independently reviewable to the extent permitted by privacy, confidentiality and security constraints.

### 4.5 Decision and effect

| TSMM concept | Adoption decision | Required GAAM refinement |
|---|---|---|
| Trust Decision | **Adopt with modification** | Define as a contextual relying decision, not an assertion that an entity is intrinsically trustworthy |
| Action | **Adopt directly from agentic extension** | Distinguish attempted or performed operation from its wider operational or legal effect |
| Effect | **Adopt directly** | Make the operational consequence the terminal object of governance evaluation |
| Decision outcome | **Adopt with modification** | Support permit, deny, restrict, warn, suspend, route, degrade and require-review outcomes |
| Effect evaluation | **Adopt directly** | Require pre-effect evaluation for governed consequential actions |
| Decision-to-effect linkage | **Adopt directly** | Every consequential effect should be linked to the decision that admitted or denied it |

#### Critical GAAM principle

> A governance framework does not govern “trust” in the abstract. It governs the conditions under which actors, evidence and authority may produce defined effects.

This principle should shape the entire GAAM structure.

### 4.6 Lifecycle and state

| TSMM concept | Adoption decision | GAAM treatment |
|---|---|---|
| Lifecycle Event | **Adopt directly** | A material event that changes governance or trust-relevant state |
| Issuance/onboarding | **Adopt directly** | Establish entry into valid circulation or governed participation |
| Delegation | **Adopt directly** | Treat as both relationship creation and lifecycle event |
| Activation | **Adopt directly** | Separate approval from operational availability |
| Suspension | **Adopt directly** | Temporary restriction with review and restoration rules |
| Revocation | **Adopt directly** | Permanent or defined withdrawal with propagation obligations |
| Expiry | **Adopt directly** | Time-based end of validity |
| Remediation | **Adopt with modification** | Include correction, reassessment, restoration and affected-party remedy |
| Archival | **Adopt directly** | Retain for evidence, audit and historical reconstruction without implying active validity |

GAAM should add further governance events:

- challenge;
- appeal;
- override;
- delegation acceptance or rejection;
- policy supersession;
- framework recognition and derecognition;
- incident declaration;
- compensation or restitution;
- restoration;
- agent substitution;
- model or toolchain change;
- evidence invalidation.

---

## 5. Relationship and invariant crosswalk

### 5.1 TSMM relationships recommended for direct adoption

| Source | Relationship | Target | GAAM decision |
|---|---|---|---|
| Actor | holds | Role | Adopt |
| Role | carries | Authority | Adopt, but allow authority to be attached directly to an actor only when explicitly justified |
| Authority | bounded by | Policy | Adopt as a core invariant |
| Authority | permits or constrains | Effect | Adopt |
| Actor | creates, controls or relies on | Artifact | Adopt |
| Artifact | contains | Claim | Adopt |
| Governance Context | shapes | Policy | Adopt |
| Governance Context | shapes | Profile | Adopt |
| Profile | bundles | Requirement | Adopt |
| Profile | expects | Control | Adopt |
| Control | mitigates | Threat | Adopt with harm-oriented expansion |
| Evidence | supports | Claim, control, requirement, assessment or verification | Adopt |
| Assessment | evaluates | Requirement or profile | Adopt |
| Verification | checks | Artifact, claim, control or state | Adopt |
| Policy | evaluates | Claim, assessment, verification and contextual state | Adopt with care: policy may govern the evaluation rather than perform it itself |
| Policy evaluation | produces | Trust decision | Adopt using a separate evaluation-function concept where needed |
| Trust decision | permits, denies, degrades or routes | Effect | Adopt |
| Lifecycle event | changes state of | Governed object or relationship | Adopt and broaden |

### 5.2 Relationships GAAM must add

| Source | Relationship | Target | Purpose |
|---|---|---|---|
| Principal | delegates | Authority to agent or delegate | Express agency and origin |
| Delegate | accepts | Delegation | Prevent one-sided assumption of duties where acceptance is material |
| Actor | requests | Action or effect | Identify request origin |
| Actor | performs | Action | Identify executor |
| Action | produces or contributes to | Effect | Separate conduct from consequence |
| Accountable party | answers for | Action, decision or effect | Preserve responsibility |
| Affected party | is affected by | Effect | Support impact and redress |
| Governing authority | recognises | External authority or framework | Model cross-framework reliance |
| Accreditor | accredits | Assessor, auditor or service | Model assurance chains |
| Registry operator | publishes | Assertion or status | Distinguish publication from truth or authority |
| Relying party | relies on | Evidence or recognition path | Make reliance contextual |
| Actor | challenges | Decision, claim or status | Support contestability |
| Authority | revokes or suspends | Delegation, status or role | Make state change explicit |
| Policy | conflicts with or supersedes | Policy | Support precedence and change |
| Agent | invokes | Tool or service | Expose operational dependencies |
| System | depends on | Component, registry, model or evidence source | Support systemic risk analysis |
| Framework | extends, profiles or recognises | Framework | Replace a purely hierarchical extension model |

### 5.3 Trust-graph edge requirements

A GAAM-compatible trust-graph relationship should carry, as applicable:

- edge identifier and type;
- source and target;
- asserting or creating authority;
- scope and purpose;
- governance context;
- jurisdiction;
- validity interval;
- current status;
- provenance;
- evidence references;
- assurance level and method;
- permitted reliance;
- revocation or termination mechanism;
- challenge and correction route;
- propagation semantics;
- confidentiality or disclosure constraints.

The specification should explicitly state:

> A graph path is evidence available to a relying party. It is not, by itself, an instruction to trust or a substitute for a local trust decision.

---

## 6. Agentic systems crosswalk

### 6.1 Agentic AI extension

| TSMM abstraction | Adoption decision | GAAM recommendation |
|---|---|---|
| Agent | Adopt with modification | Include identity, operator, principal, agent class, lifecycle and change state |
| Action | Adopt directly | Model requested, planned, attempted, performed, refused, reversed and contested states |
| Delegation | Adopt and strengthen | Require source, scope, task, purpose, time, redelegation and revocation |
| Capability | Adopt | Explicitly separate capability from permission and authority |
| Resource | Adopt where applicable | Use for access-control and effect-scoping purposes |
| Execution Context | Adopt directly | Include transaction, environment, tools, current policy and evidence state |
| Oversight Mode | Adopt with modification | Define actual intervention authority and service level, not merely “human in the loop” |
| Trace Record | Adopt with modification | Position as one component of a broader decision and evidence package |
| Risk Tier | Adopt with modification | Require declared basis, effect class and review triggers |
| Agent Class | Adopt informatively in core, normatively in profile | Avoid hard-coding a taxonomy that may age quickly |
| Control Mode | Adopt with modification | Connect advisory, supervised, constrained and autonomous modes to permitted effects |
| Attention Policy | Adopt as optional profile concept | Useful for resource and review prioritisation, but not universal core material |

### 6.2 Discovery governance

TSMM treats discovery as a governed process rather than neutral lookup. GAAM should adopt the following principles:

- discoverability does not imply authorisation;
- registry inclusion does not imply suitability for a specific task;
- discovery metadata must have provenance, integrity and lifecycle status;
- the party publishing a descriptor must have authority to make the relevant assertions;
- relying parties must apply local policy before invoking a discovered agent or service;
- stale, disputed or revoked discovery records must not continue to drive consequential effects.

Detailed discovery payloads and bindings should remain in TSMM or companion specifications.

### 6.3 Capability negotiation

Capability negotiation should be adopted as a governed pre-task mechanism for agentic profiles. GAAM should require that:

- claimed capability be distinguishable from verified capability;
- negotiated capability remain within delegated authority;
- required extensions, assurance levels or controls be disclosed before execution;
- negotiation cannot enlarge the authority of either party;
- accepted capability and constraints be recorded where the task is consequential.

### 6.4 Interaction context and task evidence lifecycle

TSMM’s interaction and task models should inform, but not overload, the GAAM core. The specification should require agentic governance frameworks to define:

- task identifier and purpose;
- originating principal;
- requesting and executing actors;
- relevant delegation lineage;
- effect class and risk tier;
- negotiated capabilities;
- policy and evidence references;
- tool invocations that materially contribute to the effect;
- lifecycle states;
- decision receipt or equivalent record;
- interruption, cancellation and remediation mechanisms.

### 6.5 Multi-agent coordination

TSMM’s chained and fan-out delegation work is particularly important. GAAM should make the following mandatory for multi-agent profiles:

- preservation of originating-principal identity;
- monotonic scope attenuation;
- branch-specific authority and evidence;
- explicit trust-domain transitions;
- convergence checks before aggregate effects;
- handling of partial revocation and orphaned branches;
- attribution of contributions and failures;
- a clear accountable party for the final effect.

### 6.6 Agent opacity and observability

TSMM’s opacity-boundary and observability-mode concepts should be adopted with modification. GAAM should not require disclosure of proprietary internal reasoning or unrestricted telemetry. Instead, it should require **governance-sufficient observability**, including the evidence needed to determine:

- what authority was asserted;
- what policy was applied;
- what evidence and tools were used;
- what action occurred;
- what effect resulted;
- whether constraints were satisfied;
- how the decision can be challenged.

This supports accountability without making private chain-of-thought disclosure a governance requirement.

---

## 7. Decentralised trust graph crosswalk

### 7.1 Graph model

TSMM’s graph layer should be adopted as a semantic foundation, not as the complete normative graph format. GAAM should define minimum graph semantics and permit compatible serialisations.

The graph should support at least these node classes:

- actor or principal;
- role;
- authority source;
- delegation;
- governance framework or context;
- policy and profile;
- registry and registry entry;
- claim and evidence artifact;
- assessor, verifier and assurance service;
- trust decision;
- action and effect;
- lifecycle event;
- affected party and remedy path.

### 7.2 Typed trust relationships

TSMM’s generic relationship grammar is useful, but GAAM should explicitly distinguish:

- identity assertion;
- authority grant;
- delegation;
- recognition;
- accreditation;
- assurance;
- reliance;
- dependency;
- accountability;
- prohibition;
- sanction;
- revocation;
- challenge;
- remediation.

This prevents a graph visualisation from collapsing legally and operationally different relationships into an ambiguous “trusts” edge.

### 7.3 Peer trust relation

The peer-trust concept should be adopted with modification. Peer relationships should not imply symmetry. GAAM should require each direction of recognition or reliance to be modelled independently, because:

- A may recognise B for one purpose while B does not recognise A;
- assurance levels may differ by direction;
- permitted reliance may be limited by jurisdiction or effect;
- revocation and status propagation may not be reciprocal.

### 7.4 Trust boundaries

Trust boundaries should be adopted directly. A boundary may be:

- organizational;
- jurisdictional;
- technical;
- contractual;
- policy-based;
- data-governance based;
- assurance based;
- agent-to-tool or agent-to-agent.

Frameworks should identify boundary-crossing effects and the additional policy, evidence, authorisation or assurance required at each boundary.

### 7.5 Verifiable trust communities

The TSMM extension contributes useful concepts:

| Concept | Decision | GAAM use |
|---|---|---|
| Community | Adopt with modification | A governed domain or association, not necessarily the full trust ecosystem |
| Membership | Adopt | A status subject to lifecycle and policy |
| Standing | Adopt | Current eligibility or good-standing state |
| Charter | Adopt | One possible institutional authority source |
| Recognition | Adopt and broaden | Contextual acknowledgement of another authority, framework, status or assurance scheme |
| Boundary Rule | Adopt | Rule controlling entry, exit or cross-domain reliance |
| Sanction | Adopt | Operational consequence of non-conformance |
| Remediation Path | Adopt and strengthen | Include restoration, appeal, correction and affected-party remedy |

The TSMM extension correctly separates community assertion from local trust decision. This should become a GAAM invariant.

### 7.6 Registry governance

TSMM registry concepts should be combined with stronger GAAM requirements. Registry inclusion or lookup must not be represented as proof of universal trustworthiness. A GAAM registry controlled document should specify:

- authority to create, modify, suspend and remove records;
- semantics and provenance of each published field;
- status and freshness;
- correction and dispute handling;
- historical retention;
- federation and recognition rules;
- privacy and disclosure controls;
- operator accountability;
- protection against poisoning, stale data and unauthorised assertion;
- reliance limitations.

---

## 8. Runtime governance and assurance crosswalk

### 8.1 Runtime Governance Envelope

**Decision: Adopt with modification as a normative artifact class.**

The TSMM envelope answers the correct execution-time questions: requester, requested effect, trust boundary, authority basis, policy, evidence, revocation freshness and decision outcome.

GAAM should define a **Runtime Governance Evaluation Record** as a semantic artifact class. A conforming profile may serialise it using TSMM or another compatible schema.

Minimum fields should include:

- evaluation identifier;
- request and transaction context;
- requesting actor and originating principal;
- proposed action and effect;
- affected resource or party where known;
- trust boundary;
- authority and delegation lineage;
- applicable policy and profile;
- evidence and verification results;
- status and revocation freshness;
- risk or impact tier;
- decision outcome and rationale code;
- required obligations or restrictions;
- decision time and validity;
- receipt requirement;
- review or escalation path.

The GAAM specification should preserve the TSMM principle that this is a **pre-effect admission surface**, not only an after-the-fact log.

### 8.2 Decision Receipt

**Decision: Adopt with modification as a normative evidence class.**

The TSMM decision receipt is one of the strongest assets in the repository. It creates a reconstructable link between authority, policy, evidence, revocation state, boundary and admitted effect.

GAAM should require a decision receipt or equivalent evidence package for:

- high-impact effects;
- denied or suspended delegated actions;
- agent actions that create legal, financial or material commitments;
- cross-domain effects where accountability could otherwise fragment;
- decisions subject to appeal or mandatory review;
- incidents and emergency overrides.

The receipt should be described as **commitment-grade evidence**, not merely a logging record.

GAAM should add:

- originating-principal reference;
- accountable-party reference;
- affected-party and notice information where appropriate;
- delegation-chain digest or reference;
- model, tool or service dependencies material to the effect;
- obligation and remedy status;
- integrity and retention metadata;
- privacy-preserving disclosure rules.

### 8.3 Assurance extension

TSMM’s assurance extension should substantially inform GAAM assurance model.

Recommended adoption:

| TSMM assurance concept | Decision |
|---|---|
| Assurance Activity | Adopt |
| Trust Task | Adopt with modification as an auditable assurance unit |
| Control Family | Adopt |
| Control Objective | Adopt |
| Evidence Artifact | Adopt |
| Evidence Bundle | Adopt |
| Validation Record | Adopt |
| Assurance Decision | Adopt with contextual and temporal limits |
| Assurance Method | Adopt |

GAAM must preserve a strong separation among:

- raw evidence;
- verification result;
- assessment result;
- assurance conclusion;
- operational trust decision.

These objects answer different questions and must not be conflated.

### 8.4 Continuous assurance

TSMM provides the ingredients, but GAAM should more explicitly require continuous and event-driven assurance for appropriate profiles.

A continuous-assurance controlled document should specify:

- monitored state and controls;
- telemetry or evidence sources;
- freshness windows;
- drift thresholds;
- incident triggers;
- reassessment conditions;
- automated and human response authority;
- suspension and restoration procedures;
- evidence retention and privacy;
- publication of material status changes.

The guiding invariant should be:

> Assurance is a time-bounded conclusion produced from defined evidence and method. It is not a permanent property of an entity, agent or registry record.

---

## 9. Threat, harm and failure crosswalk

### 9.1 TSMM threat classes to adopt

| TSMM threat class | Adoption decision | GAAM expansion |
|---|---|---|
| Authority misuse | Adopt | Include authority laundering, over-delegation and principal substitution |
| Policy bypass | Adopt | Include hidden alternate paths and emergency-mode abuse |
| Artifact forgery | Adopt | Include synthetic evidence and compromised provenance |
| Evidence suppression | Adopt | Include selective logging and inaccessible review records |
| Registry poisoning | Adopt | Include governance capture and malicious recognition edges |
| Misleading signal presentation | Adopt | Include assurance-label inflation and trust-mark theatre |
| Lifecycle drift | Adopt | Include stale delegation, agent substitution and unpropagated revocation |
| Assessment theatre | Adopt | Include certification disconnected from runtime effects |

### 9.2 Additional agentic failure modes from v0.22.0

The delegation catalog identifies six highly relevant failure modes that should become explicit GAAM risk considerations:

- broken lineage;
- scope expansion;
- principal substitution;
- domain-translation amplification;
- aggregation amplification;
- partial revocation.

GAAM should also cover:

- confused-deputy execution;
- tool misuse;
- memory or instruction contamination;
- cross-agent collusion;
- unauthorised sub-agent creation;
- hidden agent or model substitution;
- stale capability claims;
- convergence without aggregate-authority evaluation;
- inability to interrupt or reverse an autonomous effect.

### 9.3 Areas beyond TSMM

GAAM must go beyond the TSMM threat model by making harm and affected-party impact first-class. It should cover:

- discrimination and exclusion;
- loss of autonomy;
- surveillance and function creep;
- economic or legal injury;
- systemic and cumulative harm;
- vulnerable or marginalised groups;
- market concentration and dependency;
- inability to obtain explanation, correction or remedy;
- public-interest and democratic-governance impacts.

Threat analysis asks what can fail. Harm analysis asks who bears the consequences, how severe they are, whether they are reversible and what remedy exists.

---

## 10. Conformance model crosswalk

### 10.1 TSMM profiles

TSMM’s profile progression is useful:

- Minimal;
- Operational;
- Assured;
- Agentic.

These should not be copied as the sole GAAM profile structure, because they mix maturity, operational posture and domain applicability. They should instead inform two orthogonal dimensions:

#### Governance maturity levels

1. **Documented**: roles, authority, policies and artifacts are defined.
2. **Operational**: lifecycle, publication, verification and enforcement are implemented.
3. **Assured**: evidence, assessment, controls and review are demonstrable.
4. **Continuously Assured**: material state is monitored and assurance is refreshed at runtime or on events.

#### Applicability profiles

- Foundation Governance Profile;
- Machine-Actionable Governance Profile;
- Agentic Systems Profile;
- Delegated Authority Profile;
- Decentralised Trust Graph Profile;
- Registry and Discovery Profile;
- Continuous Assurance Profile;
- High-Impact Systems Profile.

A framework could therefore claim, for example:

> Agentic Systems Profile, Delegated Authority Profile and High-Impact Systems Profile at the Assured maturity level.

### 10.2 Conformance targets

GAAM should define distinct targets rather than one blanket “GAAM-conformant governance framework” claim.

| Conformance target | Required question |
|---|---|
| Governance framework | Does the framework contain and govern the required structures? |
| Controlled document | Does the document satisfy its category and profile requirements? |
| Governing or administering authority | Does the authority meet mandate, accountability and publication requirements? |
| Governed party | Does the party satisfy applicable policies and controls? |
| Agent | Is the agent identified, authorised, constrained, observable and accountable? |
| Delegation | Is the delegation valid, scoped, traceable and current? |
| Authority graph | Are origins, edges, bounds, status and propagation semantics complete? |
| Registry | Does the registry publish governed, current and contestable assertions? |
| Assurance service | Are methods, evidence, competence and conclusions governed? |
| Trust decision | Was the decision formed under applicable authority, policy and evidence? |
| Transaction or effect | Was the effect admitted and executed within authority and constraints? |
| Decision receipt | Is there sufficient evidence to reconstruct and challenge the decision? |
| Machine-actionable package | Does the package satisfy syntax, semantic and integrity requirements? |

### 10.3 Testability

The TSMM repository demonstrates a valuable implementation discipline: documentation, schema, examples, invalid vectors and validation scripts evolve together.

GAAM should require or strongly recommend that machine-actionable controlled documents include:

- normative schema or rule artifact;
- at least one valid example;
- at least one invalid test vector for every mandatory invariant;
- version and compatibility metadata;
- deterministic validation instructions;
- mapping from machine artifact to human-readable normative requirement;
- conformance-report format.

However, repository-specific script layout and programming language should remain non-normative.

---

## 11. Controlled-document adoption recommendation

The following structure is recommended for GAAM.

| Proposed controlled-document category | Existing ToIP v1.0 basis | TSMM contribution | Recommendation |
|---|---|---|---|
| Glossary and Semantic Model | Glossary | Entity and relationship catalog | Expand and make core semantic model mandatory |
| Governance Constitution and Authority | Governance Requirements; Governing Authority | Governance Context; Authority Source | Retain institutional focus and add authority topology |
| Risk, Threat, Harm and Impact | Risk Assessment | Threat model and control mapping | Expand beyond ISO-style technical risk |
| Authority, Delegation and Agency | New | Authority graph; delegation patterns; agentic extension | Mandatory when delegation or agents are permitted |
| Agent Lifecycle and Operational Control | New | Agent classification, task lifecycle, observability | Mandatory for Agentic Systems Profile |
| Business and Market Integrity | Business Requirements | Effect-centred flows | Add incentive, capture, liability and concentration analysis |
| Technical Interoperability | Technical Requirements | Bindings and interoperability matrix | Retain; keep protocol mappings outside core where possible |
| Information Trust and Data Governance | Information Trust Requirements | Evidence and artifact semantics | Expand to provenance, permitted use and evidence handling |
| Evidence, Provenance and Traceability | New | Evidence artifacts, bundles, validation records | Mandatory for Assured and High-Impact profiles |
| Trust Graph, Registry and Discovery | New | Graph, registry, discovery and VTC extension | Mandatory for Decentralised Trust Graph or Registry profiles |
| Trust Assurance and Certification | Trust Assurance and Certification | Assurance extension | Retain and modernise |
| Continuous Assurance and Observability | New | Runtime governance, lifecycle and assurance | Mandatory at Continuous Assurance maturity |
| Inclusion, Equitability and Accessibility | Existing category | Limited TSMM contribution | Retain and strengthen affected-person analysis |
| Human Oversight and Guardianship | New | Oversight mode and control mode | Mandatory where human or guardian intervention is relied on |
| Incident Response, Dispute and Redress | Partial governance/legal coverage | Review path, sanction, remediation path | Create dedicated operational category |
| Legal Agreements and Liability | Legal Agreements | Authority and effect mapping | Retain, with agentic commitments and delegation liability |
| Cross-Framework Recognition and Conflict | Extensions | Federated authority, recognition, peer relations | Replace purely hierarchical extension assumptions |
| Machine-Actionable Governance Package | New | Schemas, artifacts and validation discipline | Define package semantics and conformance |

---

## 12. Concepts to reference rather than absorb

### 12.1 Normative compatibility references

The following are good candidates for a companion TSMM profile or future normative compatibility reference after stabilization:

- TSMM authority graph schema;
- TSMM delegation-pattern schema;
- TSMM runtime-governance schema;
- TSMM decision-receipt schema;
- TSMM evidence-artifact and assurance-extension schemas;
- TSMM task-evidence lifecycle schema;
- TSMM graph and registry schemas.

The GAAM draft should define required semantics without making conformance dependent on a pre-standard repository version.

### 12.2 Informative references

The following should remain informative implementation guidance:

- A2A and other protocol bindings;
- ecosystem-specific crosswalks;
- walkthroughs;
- current interoperability matrix;
- implementation-path guides;
- repository scripts and CI design;
- OASF publication guidance;
- specific example ecosystems.

### 12.3 Retain only in TSMM

- binding catalog mechanics;
- schema file organisation;
- repository-specific documentation tiers;
- detailed protocol property mappings;
- implementation-specific validation commands;
- ecosystem names and experimental mappings not necessary to define the governance metamodel.

---

## 13. Concepts to reject, replace or constrain

No major TSMM core concept needs outright rejection. Several formulations require constraints.

### 13.1 Reject undifferentiated “trust” edges

A generic `trusts` relationship should not be normative. It should be replaced by typed recognition, reliance, assurance, authority, delegation or accreditation relationships.

### 13.2 Reject identity or registry inclusion as authority

An identifier, credential or registry record may support an authority determination. It must not be treated as authority by default.

### 13.3 Reject capability as permission

Capability negotiation cannot grant authority beyond an independently valid source.

### 13.4 Reject assurance labels without declared semantics

Labels such as “high assurance,” “trusted,” or “certified” should not be conforming unless their scope, method, evidence, validity and issuer authority are discoverable.

### 13.5 Replace a single linear lifecycle assumption

Governed artifacts and relationships may branch, suspend, partially revoke, remediate and be recognised differently across domains. GAAM should allow state machines and linked events rather than a simplistic universal sequence.

### 13.6 Constrain effect-centred governance

Effect-centred modeling should not exclude cumulative, diffuse or systemic harm. GAAM must support both discrete effects and system-level outcomes.

---

## 14. Design issues considered during GAAM development

These issues were treated as explicit design questions. Their recommended dispositions informed the GAAM architecture and remain useful for future review.

### OI-1: Normative dependency on TSMM

**Recommended first-draft position:** adopt aligned concepts and include an informative TSMM mapping annex. Do not require a specific TSMM version for GAAM conformance.

### OI-2: Human-readable versus machine-readable precedence

**Recommended position:** the human-readable normative specification is authoritative unless a framework explicitly designates a machine-readable artifact as co-normative and supplies deterministic equivalence tests.

### OI-3: DID requirement for every governance framework

The ToIP v1.0 specification mandates a DID and DID URLs for versions. GAAM should reconsider whether a DID is the only acceptable persistent identifier.

**Recommended position:** require a globally unique, persistent, resolvable and version-specific identifier; permit DIDs as one conforming method rather than the exclusive method.

### OI-4: Meaning of “trust decision”

**Recommended position:** define it as a contextual relying decision about whether a proposed effect satisfies applicable policy and risk constraints. Avoid implying objective truth or universal trustworthiness.

### OI-5: Agent identity continuity

**Recommended position:** require frameworks to define material-change thresholds for model, prompt, memory, tools, operator, deployment environment and authority source. A material change may require a new agent version, renewed assurance or new identifier.

### OI-6: Decision-receipt confidentiality

**Recommended position:** require reconstructability and selective disclosure, not universal public disclosure. Receipts may contain sensitive policy, identity or operational data.

### OI-7: Cross-domain revocation propagation

**Recommended position:** require declared propagation semantics, freshness windows and fail-safe behavior, while recognizing that instantaneous global convergence may be impossible.

### OI-8: Legal personality of agents

**Recommended position:** remain neutral on legal personality. Require identification of the human or legal persons bearing authority, responsibility and liability under applicable law.

### OI-9: Autonomous authority

**Recommended position:** an agent may hold directly assigned operational authority, but the framework must still identify the authority source and accountable party. “Self-authorised” consequential agents should not be a conforming pattern.

### OI-10: Trust-score and reputation systems

**Recommended position:** permit as evidence inputs only where methodology, provenance, bias, update and contestability requirements are satisfied. A score must not substitute for explicit authority or policy evaluation.

---

## 15. Recommended GAAM primary-document structure

The ToIP v1.0 primary-document structure should be retained and expanded. The following sections are recommended:

1. Introduction
2. Terminology, notation and semantic model
3. Localization
4. Governance framework identification and versioning
5. Governance topology
6. Governing authorities and authority sources
7. Administering and operating authorities
8. Purpose
9. Scope and applicability
10. Objectives
11. Principles
12. Governed actors, roles and affected parties
13. Authority and delegation model
14. Agentic-system applicability declaration
15. Trust-decision and effect model
16. Trust-boundary and cross-domain model
17. Accountability, challenge and redress model
18. Governance-state publication
19. General requirements
20. Revisions, deprecation and emergency change
21. Extensions, profiles and cross-framework recognition
22. Schedule of controlled documents and machine-actionable artifacts
23. Conformance claims and evidence

The **Agentic-System Applicability Declaration** should state whether agents may:

- participate as governed actors;
- represent principals;
- make recommendations;
- make binding decisions;
- invoke tools or services;
- incur legal or financial obligations;
- create sub-agents;
- redelegate authority;
- cross trust or jurisdictional boundaries;
- operate without synchronous human approval.

The declaration should determine which controlled documents and profiles become mandatory.

---

## 16. GAAM normative principles derived from the crosswalk

The first draft should incorporate at least the following principles and convert them into detailed requirements where testable.

1. **Effect orientation:** governance requirements should identify the effects they permit, constrain, deny or make reviewable.
2. **Bounded authority:** authority is always scoped and derived from a recognised source.
3. **Capability-authority separation:** technical ability does not establish permission or legitimacy.
4. **Delegation continuity:** delegated authority remains traceable to its source and originating principal.
5. **Monotonic attenuation:** downstream delegation cannot silently expand authority.
6. **Contextual reliance:** trust decisions are local, purpose-specific and policy-dependent.
7. **Evidence separation:** evidence is distinct from claims, verification, assessment, assurance and decision.
8. **Temporal assurance:** validity, authority and assurance are time-sensitive.
9. **Pre-effect governance:** consequential effects should be evaluated before execution where technically and operationally possible.
10. **Decision reconstructability:** high-impact decisions should produce sufficient evidence to reconstruct authority, policy, evidence and outcome.
11. **Accountability preservation:** automation and delegation do not erase responsible persons or institutions.
12. **Typed relationships:** graph edges must state their legal and operational meaning.
13. **Contestability:** consequential decisions, statuses and assertions must have review and correction paths.
14. **Revocation propagation:** downstream systems must define how withdrawal or suspension affects reliance and active tasks.
15. **Aggregate-authority control:** coordinated agents cannot produce an effect exceeding their combined lawful mandate.
16. **Governance-sufficient observability:** systems must expose enough evidence for assurance and challenge without requiring disclosure of private internal reasoning.
17. **Affected-party protection:** governance must consider persons and communities affected by effects, not only framework members.
18. **Machine-human coherence:** machine-actionable artifacts must remain traceable to authoritative human-readable governance requirements.
19. **No universal trust inference:** membership, certification, discovery or graph proximity does not create universal trustworthiness.
20. **Remedy as infrastructure:** incident response, correction, appeal and remediation are operational governance capabilities, not optional prose.

---

## 17. Drafting adoption register

### 17.1 Adopt directly into the GAAM core

- actor;
- role;
- authority;
- claim;
- artifact;
- evidence;
- verification;
- assessment;
- trust decision;
- effect;
- lifecycle event;
- governance context;
- profile;
- trust boundary;
- direct, delegated, conditional and chained authority patterns;
- explicit decision-to-effect relationship;
- contextual and time-bounded assurance;
- typed relationship model.

### 17.2 Adopt with modification

- entity;
- policy;
- requirement;
- threat;
- agent;
- capability;
- delegation;
- federated authority;
- fan-out delegation;
- authority graph;
- runtime governance envelope;
- decision receipt;
- assurance level;
- oversight mode;
- trace record;
- verifiable trust community;
- registry entry;
- peer trust relation;
- observability and opacity boundary;
- sanction and remediation path.

### 17.3 Normative compatibility candidates

- runtime governance artifact schema;
- decision receipt schema;
- authority graph schema;
- delegation pattern schema;
- evidence artifact and bundle schemas;
- lifecycle schema;
- registry and graph schemas;
- conformance evidence format.

### 17.4 Informative references

- protocol bindings;
- ecosystem crosswalks;
- implementation walkthroughs;
- current graph examples;
- interoperability matrix;
- implementation scripts.

### 17.5 Retain outside the GAAM specification

- TSMM repository governance mechanics;
- binding catalog structure;
- low-level protocol payloads;
- ecosystem-specific implementation mappings;
- schema and file naming conventions;
- current release badges and repository-specific maturity labels.

### 17.6 Replace or prohibit as ambiguous

- untyped “trust” relationships;
- capability interpreted as authority;
- registry inclusion interpreted as general endorsement;
- assurance labels without scope and method;
- delegation without authority source or revocation path;
- agent autonomy without accountable-party mapping;
- graph traversal as an automatic trust decision.

---

## 18. Final adoption recommendation

The crosswalk recommends proceeding to a complete first draft of GAAM with TSMM v0.22.0 used in three ways:

### 18.1 As the semantic foundation

Use TSMM’s effect-centred chain:

```text
Actor / Principal
  → Role
  → Authority and Delegation
  → Policy and Profile
  → Claims and Evidence
  → Verification and Assessment
  → Trust Decision
  → Action
  → Effect
  → Receipt, Accountability and Remedy
```

GAAM should extend this chain upward into institutional legitimacy and downward into execution, impact and redress.

### 18.2 As the operational-artifact reference

Use the runtime governance envelope, decision receipt, authority graph, delegation lineage, evidence bundle and lifecycle model as design references for GAAM artifact classes. Specify the required semantics in GAAM while leaving detailed serialisation to TSMM, TIS or other compatible implementation specifications.

### 18.3 As the validation-quality benchmark

Adopt TSMM’s documentation-plus-schema-plus-example-plus-negative-test discipline as the expected quality model for machine-actionable governance artifacts. Do not bind the specification to the repository’s current scripts or unresolved catalog inconsistency.

### 18.4 What GAAM adds beyond TSMM

The new specification must independently and comprehensively define:

- institutional legitimacy and authority constitution;
- legal identity and jurisdiction;
- accountability and liability allocation;
- public-interest and affected-party protections;
- harm assessment;
- appeal, correction, restitution and redress;
- governance change and emergency powers;
- cross-framework policy conflict;
- market power, incentives and capture;
- normative controlled-document and conformance requirements.

### 18.5 Go/no-go decision

**GO.** The TSMM prerequisite is complete. No further conceptual repository review is required before beginning the GAAM draft.

The drafting process should use this crosswalk as a control document. Every adopted concept should be traceable to:

- its GAAM definition;
- its normative relationships and invariants;
- the primary-document or controlled-document section in which it is governed;
- its conformance target;
- any machine-actionable artifact or evidence requirement.

A final drafting validation should compare the completed GAAM draft against this register to confirm that no adopted concept has been omitted, duplicated or semantically weakened.

---

## Annex A: Recommended first-draft structure

### Part I: Foundations

1. Document status and conformance language
2. Purpose and scope
3. Design goals and non-goals
4. Core principles
5. Semantic conventions

### Part II: Core Governance and Trust-System Metamodel

6. Actors, principals and affected parties
7. Roles and responsibilities
8. Authority sources and topology
9. Delegation and agency
10. Policy, requirements, rules and controls
11. Claims, evidence, verification and assessment
12. Trust decisions, actions and effects
13. Trust boundaries and governance contexts
14. Lifecycle events and governance state
15. Accountability, harm and remedy
16. Trust graphs and typed relationships

### Part III: Governance Framework Structure

17. Primary document
18. Governance framework identification and versioning
19. Governing, administering and operating authorities
20. Purpose, scope, objectives and principles
21. Agentic-system applicability declaration
22. Authority and delegation declaration
23. Trust-decision and effect declaration
24. Accountability and redress declaration
25. Governance-state publication
26. Revision, extension, recognition and deprecation
27. Schedule of controlled documents and executable artifacts

### Part IV: Controlled Documents

28. Glossary and semantic model
29. Governance constitution and authority
30. Risk, threat, harm and impact
31. Authority, delegation and agency
32. Agent lifecycle and operational control
33. Business and market integrity
34. Technical interoperability
35. Information trust and data governance
36. Evidence, provenance and traceability
37. Trust graphs, registries and discovery
38. Assurance and certification
39. Continuous assurance and observability
40. Inclusion, accessibility and affected-party protection
41. Human oversight and guardianship
42. Incident response, dispute and redress
43. Legal agreements and liability
44. Cross-framework recognition and policy conflict
45. Machine-actionable governance package

### Part V: Profiles and Conformance

46. Conformance model
47. Conformance targets
48. Applicability profiles
49. Governance maturity levels
50. Conformance statements and evidence
51. Testability and validation
52. Security, privacy and safety considerations

### Annexes

A. Core glossary  
B. Relationship and cardinality model  
C. Runtime governance evaluation record  
D. Decision receipt  
E. Authority and delegation graph  
F. Conformance matrix  
G. ToIP v1.0-to-GAAM source mapping  
H. TSMM alignment mapping  
I. Open issues and reviewer questions

---

## Annex B: Source-quality findings for the TSMM baseline

| Finding | Severity | Effect on crosswalk | Recommended handling |
|---|---:|---|---|
| Root `VERSION` and release note identify v0.22.0 | Positive | Establishes authoritative snapshot | Use as baseline |
| README retains v0.21.0 badge and release prose | Low | Documentation freshness inconsistency | Do not rely on README version text |
| Example, YAML, test-vector, schema-coverage and docs checks pass | Positive | Demonstrates mature executable model | Use as quality benchmark |
| DCAS binding lacks required `maturity` field | Moderate, localized | Full binding catalog validation fails | Treat binding catalog as informative, not normative dependency |
| Core and v0.22.0 delegation documentation declare applicable version v0.22.0 | Positive | Confirms intended concept set | Use semantics from snapshot |
| Repository is a draft reference model | Material | Concepts may evolve | Adopt semantics into GAAM rather than normatively importing all files |

---

## Annex C: Minimum traceability table for drafting

GAAM drafting workspace should maintain the following fields for each adopted concept:

| Field | Purpose |
|---|---|
| Concept identifier | Stable drafting reference |
| TSMM source | Source document, schema or model |
| Adoption class | Direct, modified, reference or retained |
| GAAM definition | Proposed normative definition |
| Relationships | Permitted source/target relationships |
| Invariants | Mandatory semantic rules |
| Controlled document | Location of governance requirements |
| Profile applicability | Profiles in which it is required |
| Conformance target | Framework, agent, transaction, artifact, etc. |
| Evidence requirement | Evidence needed to demonstrate conformance |
| Machine artifact | Applicable schema or representation |
| Open issue | Any unresolved design question |
