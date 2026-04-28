# Expert

**Inherits from:** [person](../person/)
**Ontology:** `emmo:Expert`, `foaf:Person` (inherited), `schema:Person` (inherited)
**Semantic schemas:** `expertise/schema.org` v1.0.0
**Links to:** organization (employer, department), expert (knows), material (expertise in), measurement-device (expertise in)

A researcher, engineer, or technician with domain expertise. The central actor k-type in
the DSMS: experts are linked to processes as operators, to organisations as members, and to
materials and devices as subject-matter experts.

## What it inherits from person

Custom properties: first name, last name, email, ORCID.

## What it adds

- Semantic schema: `expertise/schema.org` for a machine-readable expertise profile.
- Custom properties: education / field of study.
- Relations: employer, department, knows, expertise in material, expertise in measurement device.
