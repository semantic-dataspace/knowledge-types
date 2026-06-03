# Semi-Finished Product

Abstract base k-type for traceable physical pieces of material that have been produced
or delivered but not yet brought to final form. Examples include metal sheets, coils,
billets, and bars. Not to be confused with the material k-type, which represents the
abstract alloy or substance identity. Do not use directly; extend it for specific forms.

<table>
<tr><td><strong>Version</strong></td><td><code>0.1.0</code></td></tr>
<tr><td><strong>Inherits from</strong></td><td>—</td></tr>
<tr><td><strong>Ontology</strong></td><td><code>bfo:Object</code></td></tr>
<tr><td><strong>Semantic schemas</strong></td><td>—</td></tr>
<tr><td><strong>Links to</strong></td><td>material (made of), organization (supplier)</td></tr>
</table>

## Subclasses in this library

| K-type | Description |
|---|---|
| [metal-sheet](../metal-sheet/) | A flat-rolled metal product |

## What it defines

Custom properties: lot / heat number, receipt date, quantity.
Relations: `made_of` (`schema:material`) to abstract material identity; `supplier` to organization.
