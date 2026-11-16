# Unit Process Inventory (LCI)

Life cycle inventory dataset of one unit process: inputs and outputs per
reference flow, technology parameters and data provenance.

<table>
<tr><td><strong>Version</strong></td><td><code>0.1.0</code></td></tr>
<tr><td><strong>Inherits from</strong></td><td>—</td></tr>
<tr><td><strong>Ontology</strong></td><td><code>uplci:UnitProcessInventory</code>, <code>dcat:Dataset</code>, <code>iao:InformationContentEntity</code></td></tr>
<tr><td><strong>Semantic schemas</strong></td><td><code>life-cycle-assessment/unit-process-inventory/PMDCo</code> v0.1.0</td></tr>
<tr><td><strong>Links to</strong></td><td>manufacturing-process, material, unit-process-inventory (provider), expert, person, organization</td></tr>
</table>

## Why a separate k-type (not a manufacturing-process subtype)

An inventory is information *about* a process: normalised, partly estimated
numbers with their own provider, validity and confidentiality. The physical
process stays a `manufacturing-process` KItem that can be described by several
inventories and reused outside LCA.

## Links (declared in the semantic schema)

| Field | Target k-type | Meaning |
|---|---|---|
| `describes_process` | manufacturing-process | process the inventory is about |
| exchange `material` | material | material a flow consists of |
| exchange `provider` | unit-process-inventory | upstream inventory supplying an input (builds the chain) |
| `creator`, `reviewer` | expert, person | data generators / reviewers |
| `publisher` | organization | data owner |
