# Project

A research or engineering project, such as a funded research initiative, collaborative programme, or industrial R&D project.

<table>
<tr><td><strong>Version</strong></td><td><code>0.3.0</code></td></tr>
<tr><td><strong>Inherits from</strong></td><td>—</td></tr>
<tr><td><strong>Ontology</strong></td><td><code>vivo:Project</code>, <code>schema:ResearchProject</code></td></tr>
<tr><td><strong>Semantic schemas</strong></td><td>—</td></tr>
<tr><td><strong>Links to</strong></td><td><a href="../expert/">expert</a> (members), <a href="../organization/">organization</a>, <a href="../dataset/">dataset</a></td></tr>
</table>

## What it defines

### Custom properties — Fundamental information

| Field | Widget | Required | Predicate |
|---|---|---|---|
| Project short name | Text | no | `steel:hasProjectName_Object` |
| Project name | Text | no | `steel:hasProjectName` |
| Organisation | Knowledge item (`organization`) | no | `org:organization` |
| Project number | Text | no | `steel:hasProjectNumber` |
| Project members | Knowledge item (`expert`) | no | `agrelon:isMemberOf` |
| Webpage of the project | Text | no | `emmo:EMMO_ac852bf0…` |

### Custom properties — Project related data

| Field | Widget | Required | Predicate |
|---|---|---|---|
| Dataset | Knowledge item (`dataset`) | no | `steel:related` |
| Dataset catalog | Knowledge item | no | `steel:related` |

## Context anchor

`context: true`: project instances act as context anchors; k-items can be registered
as members to scope graph views and queries to a specific project.
