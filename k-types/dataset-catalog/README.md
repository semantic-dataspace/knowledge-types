# Dataset Catalog

A curated collection of datasets, typically grouping the outputs of a measurement campaign
or experimental series. Extends dataset with a `dcat:dataset` field that lists member
datasets.

<table>
<tr><td><strong>Version</strong></td><td><code>0.1.0</code></td></tr>
<tr><td><strong>Inherits from</strong></td><td><a href="../dataset/">dataset</a></td></tr>
<tr><td><strong>Ontology</strong></td><td><code>dcat:Catalog</code></td></tr>
<tr><td><strong>Semantic schemas</strong></td><td>
<code>dataset/catalog/DCAT</code> v0.1.0
</td></tr>
<tr><td><strong>Links to</strong></td><td>dataset (members)</td></tr>
</table>

## What it inherits

From **dataset**: description, license, format; dynamic KV properties.

## What it adds

Groups multiple dataset k-items into a named catalog. The `dataset/catalog/DCAT` semantic
schema produces a `dcat:Catalog` node whose `dcat:dataset` property links to each member
dataset by IRI.
