# Nanoindentation Characterization Process

A depth-sensing indentation characterization process in which a hard indenter tip is pressed into a material surface to measure mechanical properties (hardness HIT, elastic modulus EIT) from the load-displacement curve. Covers instrument identity, test protocol, and session-level summary statistics. Individual per-indent datasets are linked as [nanoindentation-dataset](../nanoindentation-dataset/) KItems.

<table>
<tr><td><strong>Version</strong></td><td><code>0.1.0</code></td></tr>
<tr><td><strong>Inherits from</strong></td><td><a href="../characterization-process/">characterization-process</a></td></tr>
<tr><td><strong>Ontology</strong></td><td><code>chameo:Nanoindentation</code></td></tr>
<tr><td><strong>Semantic schemas</strong></td><td><code>characterization/nanoindentation/PMDCo</code> v0.1.0</td></tr>
<tr><td><strong>Links to</strong></td><td><a href="../nanoindentation-dataset/">nanoindentation-dataset</a></td></tr>
</table>

## When to use

Use `nanoindentation-characterization-process` for the session-level record of a nanoindentation experiment. For each individual indent file (one load-displacement curve), use [nanoindentation-dataset](../nanoindentation-dataset/).

Generic across instruments (Anton Paar, Bruker, Keysight, Hysitron, etc.) and control modes (depth-controlled, load-controlled, constant strain rate, CSM).

## What it defines

Custom properties: instrument identity, control mode, indenter geometry, test conditions, analysis method, session-level summary statistics (mean HIT, EIT).
