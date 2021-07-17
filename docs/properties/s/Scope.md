Scope
=====

The Industry Foundation Classes, IFC, are an open international standard for Building Information Model (BIM) data that are exchanged and shared among software applications used by the various participants in the construction or facility management industry sector. The standard includes definitions that cover data required for buildings and bridges over their life cycle. This release, and upcoming releases, extend the scope to include data definitions for infrastructure assets over their life cycle as well.

The Industry Foundation Classes specify a data schema and an exchange file format structure. The data schema is defined in

* EXPRESS data specification language, defined in [ISO 10303-11](../schema/chapter-2.htm#iso-10303-11),
* XML Schema definition language (XSD), defined in [XML Schema W3C Recommendation](../schema/chapter-2.htm#w3c-xml-schema-part-1),

whereas the EXPRESS schema definition is the source and the XML schema definition is generated from the EXPRESS schema according to the mapping rules defined in [ISO 10303-28](../schema/chapter-2.htm#iso-10303-28). The exchange file formats for exchanging and sharing data according to the conceptual schema are

* Clear text encoding of the exchange structure, defined in [ISO 10303-21](../schema/chapter-2.htm#iso-10303-21),
* Extensible Markup Language (XML), defined in [XML W3C Recommendation](../schema/chapter-2.htm#w3c-xml).

Alternative exchange file formats may be used if they conform to the data schemas.

This release of IFC consists of the data schemas, represented as an EXPRESS schema and an XML schema, and reference data, represented as definitions of property and quantity names, and formal and informative descriptions.

A subset of the data schema and referenced data is referred to as a Model View Definition (MVD). A particular MVD is defined to support one or many recognized workflows in the construction and facility management industry sector. Each workflow identifies data exchange requirements for software applications. Conforming software applications need to identity the model view definition they conform to.
