---
title: "Threat Control Test Matrix"
permalink: /matrices/threat-control-test-matrix/
parent: "Matrices"
artifact_type: Traceability matrix
normative_status: Assurance supporting
---
{% include gaam-meta.html %}


[Download CSV](threat-control-test-matrix.csv)

<div class="table-wrap">

| threat_id | control_objective | test_ids |
| --- | --- | --- |
| GAAM-THR-001 | Prevent or detect authority laundering | authority-active-valid;authority-revoked-rejected |
| GAAM-THR-002 | Prevent or detect delegation amplification | delegation-attenuated-valid;delegation-amplification-rejected |
| GAAM-THR-003 | Prevent or detect stale revocation | authority-revoked-rejected |
| GAAM-THR-004 | Prevent or detect assurance inflation | claim-level-evidence |
| GAAM-THR-005 | Prevent or detect accountability fragmentation | decision-traceable-valid |
| GAAM-THR-006 | Prevent or detect remedy obstruction | high-impact-remedy-valid;high-impact-no-remedy-rejected |
| GAAM-THR-007 | Prevent or detect package substitution | package-integrity |

</div>
