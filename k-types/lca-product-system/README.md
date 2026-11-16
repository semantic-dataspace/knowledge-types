# LCA Product System

A process chain modelled for life cycle assessment: member unit process
inventories, the one delivering the functional unit, system boundary and
background database. Context anchor for inventories, processes, materials and
assessment results.

<table>
<tr><td><strong>Version</strong></td><td><code>0.1.0</code></td></tr>
<tr><td><strong>Inherits from</strong></td><td>—</td></tr>
<tr><td><strong>Ontology</strong></td><td><code>uplci:ProductSystem</code>, <code>iao:InformationContentEntity</code></td></tr>
<tr><td><strong>Semantic schemas</strong></td><td><code>life-cycle-assessment/product-system/PMDCo</code> v0.1.0</td></tr>
<tr><td><strong>Links to</strong></td><td>unit-process-inventory, material, expert, person, organization</td></tr>
</table>

Process links are not duplicated here: the chain is derived from the `provider`
links between member inventories.
