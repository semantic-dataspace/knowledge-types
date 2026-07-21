# Use Case

Top-level context k-type for an end-to-end materials data workflow: from raw material
through characterisation, data analysis, and modelling to a final deliverable such as a
material card or simulation parameter set.

<table>
<tr><td><strong>Version</strong></td><td><code>0.1.0</code></td></tr>
<tr><td><strong>Inherits from</strong></td><td><a href="../process/">process</a></td></tr>
<tr><td><strong>Ontology</strong></td><td><code>obi:Assay</code> (OBI_0000070)</td></tr>
<tr><td><strong>Semantic schemas</strong></td><td>—</td></tr>
<tr><td><strong>Links to</strong></td><td>—</td></tr>
</table>

## What it defines

Context anchor (`context: true`): all KItems belonging to one workflow instance are
registered as members of the use-case KItem to scope graph views and queries.

Inherits the Basic Information custom properties from `process` (Identifier, Description,
Start time, End time) and adds two sections:

**Scope** — describes what the workflow covers:

| Field | Widget | Notes |
|---|---|---|
| Material system | Text | e.g. AWX5 stainless steel, AA6016-T4 aluminium |
| Objective | Textarea | e.g. Generate FEM material card for deep-drawing simulation |
| Test types | Text | e.g. Tensile, Bulge, Nakajima |
| Standard / norm | Text | e.g. ISO 6892-1, DIN EN 10002 |

**Deliverable** — describes the expected output:

| Field | Widget | Notes |
|---|---|---|
| Deliverable type | Text | e.g. Material card, Flow curve, FEM input deck |
| Deliverable format | Text | e.g. Abaqus .mat, LS-DYNA *MAT, JSON |
