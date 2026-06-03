# Material

The abstract identity of an alloy or substance: its composition, designation, and
material-class properties. Use this k-type to represent a material as a concept
(e.g. DP800 steel, AA6016 aluminium alloy), not a specific physical piece.
For a traceable physical piece use [semi-finished-product](../semi-finished-product/)
or one of its subtypes.

<table>
<tr><td><strong>Version</strong></td><td><code>0.1.1</code></td></tr>
<tr><td><strong>Inherits from</strong></td><td>—</td></tr>
<tr><td><strong>Ontology</strong></td><td><code>pmdco:Material</code>, <code>emmo:Material</code></td></tr>
<tr><td><strong>Semantic schemas</strong></td><td>—</td></tr>
<tr><td><strong>Links to</strong></td><td>—</td></tr>
</table>

## When to use

Use `material` for generic material records. For more specific cases:

| If the material is… | Use instead |
|---|---|
| A specific physical piece (sheet, coil, bar) | [semi-finished-product](../semi-finished-product/) or a subtype |
| A physical test piece | [specimen](../specimen/) |
| Characterised by its elemental composition | [chemical-composition](../chemical-composition/) |

## What it defines

Custom properties: name, identifier, description.
Dynamic key-value properties enabled (with semantic mapping) for material-specific parameters.
