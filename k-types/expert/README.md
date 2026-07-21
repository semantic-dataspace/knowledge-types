# Expert

A researcher, engineer, or technician with domain expertise. The central actor k-type in
the DSMS: experts are linked to processes as operators, to organisations as members, and to
materials and devices as subject-matter experts.

<table>
<tr><td><strong>Version</strong></td><td><code>0.1.1</code></td></tr>
<tr><td><strong>Inherits from</strong></td><td><a href="../person/">person</a></td></tr>
<tr><td><strong>Ontology</strong></td><td><code>emmo:Expert</code>, <code>foaf:Person</code> (inherited), <code>schema:Person</code> (inherited)</td></tr>
<tr><td><strong>Semantic schemas</strong></td><td>
<code>expertise/VIVO</code> v0.3.0
</td></tr>
<tr><td><strong>Links to</strong></td><td>
organization (employer, department), expert (knows), material (expertise in), measurement-device (expertise in)
</td></tr>
</table>

## What it inherits from person

Custom properties: first name, last name, email, ORCID.

## What it adds

- Semantic schema: `expertise/VIVO` for a machine-readable expertise profile.
- Custom properties: education / field of study.
- Relations: employer, department, knows, expertise in material, expertise in measurement device.
