# Catalog

## Inheritance and relations graph

Solid arrows = inherits from (`extends`). Dashed arrows = links to (`relations`).

```mermaid
graph TD
  %% ── Inheritance ──────────────────────────────────────────────
  person --> expert
  process --> manufacturing-process
  process --> characterization-process
  characterization-process --> tensile-test
  material --> specimen

  %% ── Relations (dashed) ───────────────────────────────────────
  expert        -.->|employer / department| organization
  expert        -.->|knows| expert
  expert        -.->|expertise in| material
  expert        -.->|expertise in| measurement-device
  organization  -.->|sub-org of| organization
  specimen      -.->|manufactured from| material
  chemical-composition -.->|composition of| material
  chemical-composition -.->|composition of| specimen
  measurement-device   -.->|responsible org| organization
  manufacturing-process -.->|operator| expert
  manufacturing-process -.->|input / output| material
  manufacturing-process -.->|process data| dataset
  characterization-process -.->|operator ✱| expert
  characterization-process -.->|instrument ✱| measurement-device
  characterization-process -.->|specimen ✱| specimen
  characterization-process -.->|result data| dataset
  material-card -.->|describes ✱| material
  material-card -.->|includes| characterization-process
  material-card -.->|includes| tensile-test
  material-card -.->|includes| chemical-composition
  project -.->|coordinator / participants| expert
  project -.->|partner orgs / funder| organization
  project -.->|publications| document

  %% ── Styling ──────────────────────────────────────────────────
  classDef agent      fill:#dbeafe,stroke:#3b82f6
  classDef material   fill:#dcfce7,stroke:#22c55e
  classDef process    fill:#fef9c3,stroke:#eab308
  classDef equipment  fill:#fce7f3,stroke:#ec4899
  classDef data       fill:#f3f4f6,stroke:#6b7280
  classDef research   fill:#ede9fe,stroke:#8b5cf6

  class person,expert,organization agent
  class material,specimen,chemical-composition material
  class process,manufacturing-process,characterization-process,tensile-test process
  class measurement-device equipment
  class dataset,document,app,material-card data
  class project research
```

✱ = required relation

---

## Registry

| ID | Name | Extends | Ontologies | Semantic schemas | Links to | Tags |
|---|---|---|---|---|---|---|
| [app](k-types/app/) | App | | schema.org | | | software |
| [characterization-process](k-types/characterization-process/) | Characterization Process | process | OBI, PMDCo | characterization/generic/PMDCo v0.1.0 | expert ✱, measurement-device ✱, specimen ✱, dataset | process, characterization |
| [chemical-composition](k-types/chemical-composition/) | Chemical Composition | | PMDCo | chemical-composition/PMDCo v0.1.0, chemical-composition/BWMD v0.1.0 | material, specimen | material, composition |
| [dataset](k-types/dataset/) | Dataset | | DCAT | | | data |
| [document](k-types/document/) | Document | | DCTERMS, schema.org | | | data |
| [expert](k-types/expert/) | Expert | person | EMMO | expertise/VIVO v0.2.0 | organization, expert, material, measurement-device | agent, person |
| [manufacturing-process](k-types/manufacturing-process/) | Manufacturing Process | process | PMDCo | manufacturing/generic/PMDCo v0.1.0 | expert, material, dataset | process, manufacturing |
| [material](k-types/material/) | Material | | PMDCo, EMMO | | | material |
| [material-card](k-types/material-card/) | Material Card | | PMDCo | material-card/mechanical/PMDCo v0.1.0, workflow/OBI v0.1.0, specimen/PMDCo v0.1.0, chemical-composition/PMDCo v0.1.0 | material ✱, characterization-process, tensile-test, chemical-composition | material, data |
| [measurement-device](k-types/measurement-device/) | Measurement Device | | OBI, PMDCo | measurement-device/PMDCo v0.1.0 | organization | equipment |
| [organization](k-types/organization/) | Organization | | W3C-ORG, FOAF, schema.org | | organization | agent |
| [person](k-types/person/) | Person | | FOAF, schema.org | | | agent, person |
| [process](k-types/process/) | Process | | PMDCo | | | process |
| [project](k-types/project/) | Project | | VIVO, schema.org | | expert, organization, document | project, research |
| [specimen](k-types/specimen/) | Specimen | material | PMDCo, OBI | specimen/PMDCo v0.1.0 | material | material, specimen |
| [tensile-test](k-types/tensile-test/) | Tensile Test | characterization-process | SteelPO, TTO | characterization/tensile-test/TTO v0.1.0, characterization/tensile-test/PMDCo v0.1.0 | *(all inherited)* | process, characterization, mechanical-testing |

✱ = required relation
