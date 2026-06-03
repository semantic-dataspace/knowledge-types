# Process

Abstract base k-type for all process-like concepts. Do not use directly; extend it.

<table>
<tr><td><strong>Version</strong></td><td><code>0.2.0</code></td></tr>
<tr><td><strong>Inherits from</strong></td><td>—</td></tr>
<tr><td><strong>Ontology</strong></td><td><code>pmdco:Process</code></td></tr>
<tr><td><strong>Semantic schemas</strong></td><td>—</td></tr>
<tr><td><strong>Links to</strong></td><td>—</td></tr>
</table>

## Subclasses in this library

| K-type | Description |
|---|---|
| [manufacturing-process](../manufacturing-process/) | A process that transforms material |
| [characterization-process](../characterization-process/) | A process that measures material properties |

## What it defines

Custom properties: identifier, description, start time, end time.
KV properties enabled with semantic mapping for process-specific parameters.
Context anchor (`context: true`): all process subtypes act as context anchors; k-items
can be registered as members to scope graph views and queries to a specific process.
