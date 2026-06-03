# Metal Sheet Batch

A delivery or production lot of metal sheets sharing the same alloy identity and
supplier. Acts as a context anchor: individual metal-sheet k-items are registered as
members to group them by origin and enable batch-level queries.

<table>
<tr><td><strong>Version</strong></td><td><code>0.1.0</code></td></tr>
<tr><td><strong>Inherits from</strong></td><td><a href="../batch/">batch</a></td></tr>
<tr><td><strong>Ontology</strong></td><td><code>pmdco:PMD_0020138</code> (Lot), <code>prov:Collection</code> (inherited)</td></tr>
<tr><td><strong>Semantic schemas</strong></td><td>—</td></tr>
<tr><td><strong>Links to</strong></td><td>material (made of), organization (supplier)</td></tr>
</table>

## What it inherits from batch

Custom properties: batch ID, production / receipt date, quantity.
Context anchor (`context: true`), `context_member_types: [metal-sheet]`.

## What it adds

- Relation: `made_of` (`schema:material`) — alloy identity shared by all sheets in this batch.
- Relation: `supplier` (`schema:supplier`) — organisation that supplied this batch.
