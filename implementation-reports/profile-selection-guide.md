---
title: "Profile Selection Guide"
permalink: /implementation-reports/profile-selection/
parent: "Implementation Reports"
nav_order: 1
artifact_type: "Implementation guidance"
normative_status: "Informative"
---
# Profile Selection Guide

{% include gaam-meta.html %}

Use this guide to define a reviewable target of evaluation before collecting evidence. Profile selection should follow the implementation's actual governed effects, authority relationships and assurance claims rather than the labels preferred by the operator.

## 1. Define the target of evaluation

Record a target that another reviewer can locate and distinguish from adjacent systems.

| Attribute | Minimum description |
|---|---|
| Target identifier | Stable identifier for the service, component, deployment or governance package |
| Version or build | Exact software, configuration or package version evaluated |
| Environment | Development, test, staging, production or another declared environment |
| Organisational boundary | Operator, accountable authority and material service providers |
| Technical boundary | Included components, interfaces, stores and enforcement points |
| Governed effects | Decisions or actions the target may permit, deny, restrict, suspend or route for review |
| Evaluation period | Observation start and end, or point-in-time assessment date |
| Exclusions | Explicitly excluded components, profiles, jurisdictions or effects |

A report should not use labels such as “the platform” or “the service” without a stable scope definition.

## 2. Establish profile dependency closure

The Foundation Profile is the common dependency for the specialised profiles. Select every profile whose governed semantics the implementation claims to provide, then include all dependencies declared in the profile manifests.

| Profile family | Select when the target materially implements |
|---|---|
| Foundation | Core authority, governance, evidence, assurance, decision and accountability semantics |
| Delegated Authority | Authority is granted, constrained, exercised or revoked through delegation |
| Runtime Governance | Proposed effects are evaluated against authority, policy, evidence and context during execution |
| Agentic Systems | Software agents act for principals or exercise bounded delegated authority |
| Continuous Assurance | Assurance state is renewed, degraded, suspended or withdrawn using ongoing evidence |
| High-Impact Systems | Decisions or effects create heightened safety, rights, welfare or systemic consequences |
| Machine-Actionable Governance | Governance controls and records are represented for automated evaluation or enforcement |
| Trust Graph | Typed relationships and graph traversal contribute to trust or governance decisions |

The profile manifests are authoritative for profile identifiers, dependencies and requirement membership. This guide does not replace them.

## 3. Apply the least-claim principle

Select the narrowest profile set and conformance level supported by the evidence. Do not claim a specialised profile merely because the implementation exchanges similarly named data.

A profile claim is unsuitable when:

- required profile dependencies are absent;
- the target only documents a control that is not implemented;
- applicable runtime behaviour has not been tested;
- evidence refers to a different version or environment;
- exclusions remove a material part of the claimed profile;
- the evidence level exceeds the weakest material control or evidence source.

## 4. Record the selection decision

Include this table in the implementation report.

| Profile | Included | Rationale | Dependencies satisfied | Evidence locations | Material exclusions |
|---|---:|---|---:|---|---|
| Foundation |  |  |  |  |  |
| Delegated Authority |  |  |  |  |  |
| Runtime Governance |  |  |  |  |  |
| Agentic Systems |  |  |  |  |  |
| Continuous Assurance |  |  |  |  |  |
| High-Impact Systems |  |  |  |  |  |
| Machine-Actionable Governance |  |  |  |  |  |
| Trust Graph |  |  |  |  |  |

## 5. Re-evaluate profile selection after change

Repeat selection when the target's authority source, delegation model, governed effects, enforcement architecture, evidence sources, assurance process or affected-party consequences materially change. A previously valid claim should not be carried forward solely because the product name or deployment identifier remains unchanged.
