---
title: GAAM v0.9.0 Validation Report
permalink: /validation-report/
nav_exclude: true
artifact_type: Validation evidence
normative_status: Repository generated
---
# GAAM v0.9.0 Validation Report

{% include gaam-meta.html %}

**Status:** PASS  
**Checks:** 64  
**Passed:** 64  
**Failed:** 0  

This report evidences repository publication, structural and included behavioural checks. It is not an independent L4 assessment.

| ID | Kind | Status | Evidence |
|---|---|---|---|
| `PUB-001-version-source` | publication | PASS | authoritative version=0.9.0 |
| `PUB-002-active-version-coherence` | publication | PASS | no stale active v0.5.0 references |
| `PUB-003-specification-identity` | publication | PASS | normative specification identifies candidate release |
| `REQ-001-unique` | normative | PASS | 190 identifiers |
| `REQ-002-index-exact` | normative | PASS | 190 indexed requirements |
| `REQ-003-normative-language` | normative | PASS | 190 indexed statements classified |
| `SCH-agent-governance-identity` | schema | PASS | valid Draft 2020-12 schema |
| `SCH-appeal` | schema | PASS | valid Draft 2020-12 schema |
| `SCH-assurance` | schema | PASS | valid Draft 2020-12 schema |
| `SCH-authority` | schema | PASS | valid Draft 2020-12 schema |
| `SCH-conformance-claim` | schema | PASS | valid Draft 2020-12 schema |
| `SCH-decision-receipt` | schema | PASS | valid Draft 2020-12 schema |
| `SCH-delegation` | schema | PASS | valid Draft 2020-12 schema |
| `SCH-evidence` | schema | PASS | valid Draft 2020-12 schema |
| `SCH-gaam-package` | schema | PASS | valid Draft 2020-12 schema |
| `SCH-governance-event` | schema | PASS | valid Draft 2020-12 schema |
| `SCH-profile-manifest` | schema | PASS | valid Draft 2020-12 schema |
| `SCH-remedy` | schema | PASS | valid Draft 2020-12 schema |
| `SCH-runtime-envelope` | schema | PASS | valid Draft 2020-12 schema |
| `SCH-IDS` | schema | PASS | 13 unique canonical identifiers |
| `SCH-CATALOG` | schema | PASS | catalog covers all schemas |
| `VOC-assurance-statuses` | vocabulary | PASS | 7 governed values |
| `VOC-decision-outcomes` | vocabulary | PASS | 9 governed values |
| `VOC-governance-event-types` | vocabulary | PASS | 11 governed values |
| `VOC-lifecycle-states` | vocabulary | PASS | 14 governed values |
| `VOC-relationship-types` | vocabulary | PASS | 19 governed values |
| `PRO-agentic-systems` | profile | PASS | 51 requirements; dependencies=True; document=True |
| `PRO-continuous-assurance` | profile | PASS | 19 requirements; dependencies=True; document=True |
| `PRO-delegated-authority` | profile | PASS | 32 requirements; dependencies=True; document=True |
| `PRO-foundation` | profile | PASS | 36 requirements; dependencies=True; document=True |
| `PRO-high-impact-systems` | profile | PASS | 22 requirements; dependencies=True; document=True |
| `PRO-machine-actionable-governance` | profile | PASS | 26 requirements; dependencies=True; document=True |
| `PRO-runtime-governance` | profile | PASS | 21 requirements; dependencies=True; document=True |
| `PRO-trust-graph` | profile | PASS | 9 requirements; dependencies=True; document=True |
| `PRO-DEPENDENCIES` | profile | PASS | all profile dependencies resolve |
| `FIX-cross-registry-recognition-authority.valid` | fixture | PASS | accepted as expected |
| `FIX-cross-registry-recognition-decision-receipt.valid` | fixture | PASS | accepted as expected |
| `FIX-cross-registry-recognition-authority.invalid` | fixture | PASS | rejected as expected |
| `CLM-cross-registry-recognition` | conformance | PASS | schema, evidence and independence rules satisfied |
| `FIX-delegated-agent-purchase-authority.valid` | fixture | PASS | accepted as expected |
| `FIX-delegated-agent-purchase-decision-receipt.valid` | fixture | PASS | accepted as expected |
| `FIX-delegated-agent-purchase-authority.invalid` | fixture | PASS | rejected as expected |
| `CLM-delegated-agent-purchase` | conformance | PASS | schema, evidence and independence rules satisfied |
| `FIX-high-impact-multi-agent-service-authority.valid` | fixture | PASS | accepted as expected |
| `FIX-high-impact-multi-agent-service-decision-receipt.valid` | fixture | PASS | accepted as expected |
| `FIX-high-impact-multi-agent-service-authority.invalid` | fixture | PASS | rejected as expected |
| `CLM-high-impact-multi-agent-service` | conformance | PASS | schema, evidence and independence rules satisfied |
| `BEH-authority-active-valid` | behavioural | PASS | expected=True; actual=True |
| `BEH-authority-revoked-rejected` | behavioural | PASS | expected=False; actual=False |
| `BEH-decision-missing-evidence-rejected` | behavioural | PASS | expected=False; actual=False |
| `BEH-decision-traceable-valid` | behavioural | PASS | expected=True; actual=True |
| `BEH-delegation-amplification-rejected` | behavioural | PASS | expected=False; actual=False |
| `BEH-delegation-attenuated-valid` | behavioural | PASS | expected=True; actual=True |
| `BEH-delegation-depth-rejected` | behavioural | PASS | expected=False; actual=False |
| `BEH-high-impact-no-remedy-rejected` | behavioural | PASS | expected=False; actual=False |
| `BEH-high-impact-remedy-valid` | behavioural | PASS | expected=True; actual=True |
| `THR-TRACE` | threat | PASS | 7 threats mapped to requirements and tests |
| `DOC-PAGE-TITLE-CONTRACT` | documentation | PASS | all rendered Markdown pages declare exactly one H1 matching front matter |
| `DOC-CTWG-GLOSSARY-ALIGNMENT` | documentation | PASS | 26 glossary terms covered by CTWG alignment register |
| `DOC-LOCAL-LINKS` | documentation | PASS | all local links resolve |
| `DOC-TSMM-CANONICAL` | provenance | PASS | canonical TSMM repository link present |
| `CI-WORKFLOW` | automation | PASS | validation workflow present |
| `PKG-MANIFEST` | package | PASS | package manifest conforms |
| `PKG-INTEGRITY` | package | PASS | 43 checksums verified |
