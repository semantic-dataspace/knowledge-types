# DSC Heat Flow Dataset

Digital twin of a single DSC heat-flow measurement file (MTYPE=DSC). Stores scalar characterization results (onset/peak temperature, enthalpy, etc.) as MeasurementDatum nodes via the OO-LD semantic schema, and carries the raw heat-flow time-series (Temperature vs DSC/(µV/mg)) as an attached CSV file.

For specific heat capacity measurements (MTYPE=CP) use `cp-dataset` instead.

<table>
<tr><td><strong>Version</strong></td><td><code>0.1.1</code></td></tr>
<tr><td><strong>Inherits from</strong></td><td><a href="../dataset/">dataset</a></td></tr>
<tr><td><strong>Ontology</strong></td><td><code>DSMS:DSCHeatFlowMeasurement</code>, <code>dcat:Dataset</code></td></tr>
<tr><td><strong>Semantic schemas</strong></td><td><code>dataset/dsc/PMDCo</code> v0.1.0</td></tr>
<tr><td><strong>Links to</strong></td><td>parent dsc-heat-flow-measurement process KItem, specimen</td></tr>
</table>

## When to use

Use `dsc-heat-flow-dataset` for each DSC heat-flow file (MTYPE=DSC). For specific heat capacity files (MTYPE=CP), use `cp-dataset`.

## What it defines

Custom properties: onset temperature, peak temperature, enthalpy, and other scalar DSC results.
Raw heat-flow time-series attached as CSV file with data2rdf annotation.
