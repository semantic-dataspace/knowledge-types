# Project

**Ontology:** `vivo:Project`, `schema:ResearchProject`
**Links to:** expert (coordinator, participants), organization (partner organisations, funder), document (publications)

A research or engineering project, such as a funded research initiative, collaborative programme, or industrial R&D project.

## What it defines

### Custom properties

| Field | Widget | Required | Predicate |
|---|---|---|---|
| Project homepage | Text | no | `schema:url` |
| Start date | Date | no | `schema:startDate` |
| End date | Date | no | `schema:endDate` |
| Grant / project ID | Text | no | `schema:identifier` |
| Funding programme | Text | no | `dcterms:isPartOf` |
| Call / programme URL | Text | no | `dcat:accessURL` |

### Relations

| Relation | Target | Cardinality | Predicate |
|---|---|---|---|
| Coordinator / PI | [expert](../expert/) | 0..1 | `vivo:pi` |
| Participants | [expert](../expert/) | 0..n | `schema:participant` |
| Partner organisations | [organization](../organization/) | 0..n | `org:hasMember` |
| Funder | [organization](../organization/) | 0..n | `schema:funder` |
| Publications | [document](../document/) | 0..n | `schema:hasPart` |

## Notes

- `Grant / project ID` holds the funder-assigned number (e.g. `101058682` for EC, `03XP0337A` for BMBF).
- `Funding programme` is free text naming the programme (e.g. `Horizon Europe`, `BMBF`, `DFG`).
- `Call / programme URL` links to the project's entry on the funder's portal (e.g. CORDIS).
- Publications are linked as [document](../document/) k-items rather than embedded records.
