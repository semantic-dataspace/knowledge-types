# Specimen Batch

A collection of specimens produced or prepared together as a single lot, for example
test pieces cut from the same sheet or heat-treated in the same furnace run. Acts as a
context anchor: specimens are registered as members to scope characterization queries
and graph views to this batch.

<table>
<tr><td><strong>Version</strong></td><td><code>0.1.0</code></td></tr>
<tr><td><strong>Inherits from</strong></td><td><a href="../batch/">batch</a></td></tr>
<tr><td><strong>Ontology</strong></td><td><code>pmdco:PMD_0000891</code> (Disconnected Material Entity Aggregate), <code>prov:Collection</code> (inherited)</td></tr>
<tr><td><strong>Semantic schemas</strong></td><td>—</td></tr>
<tr><td><strong>Links to</strong></td><td>semi-finished-product (source)</td></tr>
</table>

## What it inherits from batch

Custom properties: batch ID, production / receipt date, quantity.
Context anchor (`context: true`), `context_member_types: [specimen]`.

## What it adds

- Relation: `source` (`prov:wasDerivedFrom`) — the semi-finished product the specimens were prepared from.
