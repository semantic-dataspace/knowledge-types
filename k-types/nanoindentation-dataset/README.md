# Nanoindentation Dataset

The digital twin of a single nanoindentation indent file (one load-displacement curve). Stores per-indent metadata (index, stage position, timestamp, analysis warnings) and all scalar results from the Oliver-Pharr analysis (HIT, EIT, E*, Er, HVIT, hmax, hc, hr, hp, S, Ap, Welast, Wplast, Wtotal, nIT, RIT, m, Epsilon, R², F/S²). The raw time-series (load-displacement CSV) is attached as a file and annotated via data2rdf.

<table>
<tr><td><strong>Version</strong></td><td><code>0.1.1</code></td></tr>
<tr><td><strong>Inherits from</strong></td><td><a href="../dataset/">dataset</a></td></tr>
<tr><td><strong>Ontology</strong></td><td><code>dcat:Dataset</code></td></tr>
<tr><td><strong>Semantic schemas</strong></td><td><code>dataset/nanoindentation/PMDCo</code> v0.1.0</td></tr>
<tr><td><strong>Links to</strong></td><td><a href="../nanoindentation-characterization-process/">nanoindentation-characterization-process</a></td></tr>
</table>

## When to use

Use `nanoindentation-dataset` for each individual indent file produced by a nanoindentation session. For the session-level record (instrument configuration, test protocol, summary statistics), use [nanoindentation-characterization-process](../nanoindentation-characterization-process/).

## What it defines

Custom properties: per-indent metadata and Oliver-Pharr scalar results (hardness HIT, elastic modulus EIT, contact depth hc, etc.).
Raw time-series attached as CSV file with data2rdf annotation.
