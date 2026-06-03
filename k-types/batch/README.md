# Batch

Abstract base k-type for collections of items produced, processed, or received together
as a single lot. Acts as a context anchor: its members define the scope of the group.
Do not use directly; extend it for specific batch types.

<table>
<tr><td><strong>Version</strong></td><td><code>0.1.0</code></td></tr>
<tr><td><strong>Inherits from</strong></td><td>—</td></tr>
<tr><td><strong>Ontology</strong></td><td><code>prov:Collection</code></td></tr>
<tr><td><strong>Semantic schemas</strong></td><td>—</td></tr>
<tr><td><strong>Links to</strong></td><td>—</td></tr>
</table>

## Subclasses in this library

| K-type | Description |
|---|---|
| [specimen-batch](../specimen-batch/) | A batch of specimens prepared together |
| [metal-sheet-batch](../metal-sheet-batch/) | A delivery lot of metal sheets |

## What it defines

Custom properties: batch ID, production / receipt date, quantity.
Context anchor: `context: true` (inherited by all subclasses).
