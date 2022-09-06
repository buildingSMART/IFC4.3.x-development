The Industry Foundation Classes, IFC, are an open international standard for Building Information Model (BIM) data that are exchanged and shared among software applications used by the various participants in the construction or facility management industry sector. The standard includes definitions that cover data required for buildings and infrastructure works over their life cycle.
The coverage of infrastructure facilities now incorporated into IFC includes bridges, roads, railways, waterways and port facilities.

The Industry Foundation Classes specify a data schema and an exchange file format structure.
The schema, property sets and usage constraints are internally authored as a UML Class diagram, [available as XMI file](https://github.com/buildingSMART/IFC4.3.x-development/tree/master/schemas)
and published as [computer interpretable schemas](https://github.com/buildingSMART/IFC4.3.x-output), including:

* [EXPRESS data specification language](https://github.com/buildingSMART/IFC4.3.x-output/blob/master/IFC.exp), defined in ISO 10303-11,
* XML Schema definition language (XSD) (under development),
* RDF/OWL Schema  (under development),
* JavaScript Object Notation Schema (under development),
* JSON structured [taxonomy](https://github.com/buildingSMART/IFC4.3.x-output/blob/master/IFC.json) of entities, predefined types and properties.

The exchange file formats for exchanging and sharing data according to the conceptual schema are

* Clear text encoding of the exchange structure, defined in ISO 10303-21,
* Extensible Markup Language (XML), defined in XML Schema W3C Recommendation with IFC specific translations,
* RDF/OWL, defined by W3C and the buildingSMART projects,
* JSON JavaScript Object Notation, defined by the buildingSMART projects.

An overview of the file formats can be seen on [the technical website](https://technical.buildingsmart.org/standards/ifc/ifc-formats/),
Alternative exchange file formats may be used if they conform to the data schemas.

This release of IFC consists of the data schemas (represented in different formats), and reference data, represented as definitions of property and quantity names, and formal and informative descriptions (available in Markdown and HTML).

The full IFC standard is used to define one or many recognized workflows in the construction and facility management industry sector. Such an exchange scenario definition of the IFC data schema and referenced data is referred to as a Model View Definition (MVD). Each MVD identifies data exchange requirements for software applications. Conforming software applications need to identity the model view definition they conform to to apply for Software Certification.

## General use

The following are within the entire scope of this release of IFC:

 1. BIM exchange format definitions that are required during the life cycle phases of buildings and infrastructure:

    * demonstrating the need;
    * conception of need;
    * outline feasibility;
    * substantive feasibility study and outline financial authority;
    * outline conceptual design;
    * full conceptual design;
    * coordinated design;
    * procurement and full financial authority;
    * production information;
    * construction;
    * operation and maintenance.

 2. BIM exchange format definitions that are required by the various disciplines involved within the life cycle phases:

    * architecture and civil engineering design;
    * service and utilities engineering;
    * structural engineering;
    * procurement;
    * construction planning;
    * facility and utility management;
    * project management;
    * client requirement management;
    * industry authorities for permits and approval.

 3. BIM exchange format definitions including:

    * project structure;
    * physical components;
    * spatial components;
    * analysis items;
    * processes;
    * resources;
    * controls;
    * actors;
    * context definition.

The following are outside the scope of this release of IFC:

 1. Exchange format definitions outside of the domains of design, construction and facility maintenance;
 2. Behavioral aspects of components and other information items.
