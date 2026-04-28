# Concepts

## Background

Modern materials research produces data in many formats, at many institutions, using many different
naming conventions. A tensile test result from one lab cannot easily be combined with one from
another if "Force" means something different in each dataset, or if specimen dimensions are stored
in incompatible units and column names.

The **Dataspace Management System (DSMS)** is a research data platform designed to solve this
problem. It stores experimental and computational data as a structured network of connected records
called **knowledge items** (k-items). By giving each record a well-defined type and a set of typed
connections to other records, the DSMS makes data machine-readable: software can answer questions
like "find all tensile tests on DP800 steel performed at Fraunhofer IWM in 2025" without a human
having to manually search through files.

For a full description of the DSMS and the dataspace concept:

> Nahshon, Y.; Morand, L.; Büschelberger, M.; Helm, D.; Kumaraswamy, K.; Zierep, P.; Weber, M.;
> de Andrés, P. (2025). *Semantic Orchestration and Exploitation of Material Data: A Dataspace
> Solution Demonstrated on Steel and Copper Applications.* Advanced Engineering Materials, 27(8),
> 2401448. <https://doi.org/10.1002/adem.202401448>

---

## Knowledge items and k-types

A **knowledge item** is a record in the DSMS. Think of it like a row in a spreadsheet or an entry
in a database. Concrete examples:

- A specific tensile test run on 14 March 2026
- The Zwick Z100 testing machine in lab 3
- DP800 steel sheet as delivered by a supplier

A **knowledge type** (k-type) is the *template* for a class of knowledge items: what fields it has,
what connections it can make to other records, and what its meaning is in the wider data landscape.
Think of it as the column headers of the spreadsheet, or the table schema in a database.

Every knowledge item belongs to exactly one k-type. The k-type `tensile-test` defines that a
tensile-test record must link to an operator, a testing machine, and a specimen. The k-type
`measurement-device` defines that a device record has a name, manufacturer, and serial number.
This repository is the library of those templates.

---

## What is an ontology, and why do k-types use one?

An **ontology** is a shared vocabulary for a domain. Instead of everyone inventing their own name
for a concept, an ontology gives each concept a unique, permanent web address (called an **IRI**,
for example `https://w3id.org/steel/ProcessOntology/TensileTest`). Two datasets that both use this
IRI for "tensile test" are unambiguously talking about the same thing, regardless of the language
the researchers used or the software that produced the data.

K-types declare **ontology class mappings** that specify which ontological concept a k-type
corresponds to. When the DSMS builds a knowledge graph from k-items, each item is labelled with
these IRIs, making the data interpretable by any software or institution that understands the same
ontology.

You do not need to understand ontologies to use an existing k-type. The mappings are filled in by
the k-type author. They become relevant when you want to query or exchange data across institutions,
or when you are writing a new k-type.

---

## What is a knowledge graph?

A **knowledge graph** is a network of connected data. Each node is a record (a k-item); each edge
is a typed connection between two records.

For example, a tensile-test k-item connects to several other k-items:

```
[tensile-test: TT-DP800-001]
    --[operator]--> [expert: Jane Doe]
    --[instrument]--> [device: Zwick Z100]
    --[specimen]--> [specimen: DP800-S1Q]
    --[result data]--> [dataset: TT-DP800-001-raw.csv]
```

Because each connection is labelled with an ontology property (e.g. `prov:wasAssociatedWith` for
"operator"), the graph can be queried in standard ways by machines. K-types define which connections
are possible and which are required; the actual connections are made by users when they create or
edit a k-item.

---

## What are semantic schemas?

A **semantic schema** (from the
[semantic-schemas](https://github.com/semantic-dataspace/semantic-schemas) library) is a template
that converts a plain data record into **RDF**, the standard web format for linked data. You do not
need to know what RDF is to use k-types — it is the output format consumed by the knowledge graph
builder in the background.

The practical flow is:

1. A user fills in a simple form or JSON file with measurement values (force, displacement, etc.).
2. The semantic schema converts those values to RDF using the correct ontology terms.
3. The result is stored in the knowledge graph and can be queried alongside data from other sources.

K-types reference semantic schemas to specify which templates apply to k-items of that type, with
pinned version numbers so the correct schema is always used. You do not need to write or modify
semantic schemas to use a k-type.

---

## How a k-type ties it all together

A k-type specification is a single YAML file that captures four things:

| What | Purpose |
|---|---|
| **Ontology class mappings** | Labels k-items of this type in the knowledge graph with standard IRIs |
| **Semantic schemas** | Specifies how to convert k-item data to linked data (RDF) |
| **Relations** | Declares which other k-types a k-item can or must link to |
| **Custom properties** | Defines the form users fill in when creating a k-item |

This means a k-type spec is both a *human-readable description* of a concept (what a tensile test
is, what data it contains, how it relates to experts and devices) and a *machine-readable
specification* that software uses to store, display, and connect data correctly.

---

## Inheritance

K-types can build on each other. A `tensile-test` is a specialisation of a
`characterization-process`, which is itself a specialisation of `process`. A child k-type inherits
all definitions from its parents and only declares what is new or different.

This avoids duplication: the three required relations (operator, instrument, specimen) are declared
once on `characterization-process` and automatically apply to every measurement k-type that
extends it, including `tensile-test`.

K-types support multiple inheritance: a k-type can extend more than one parent when it belongs to
more than one category simultaneously. See [docs/3_inheritance.md](3_inheritance.md) for the full
mechanics.

---

## This repository

This repository curates a shared library of k-type specifications for materials science. The goal
is a common vocabulary: a `tensile-test` k-type defined here carries the same meaning in every DSMS
instance that imports it, enabling data exchange and comparison across institutions without
additional mapping work.

K-types are versioned using semantic versioning. Breaking changes (renamed fields, removed
relations, incompatible ontology classes) increment the major version; backwards-compatible
additions increment the minor version.
