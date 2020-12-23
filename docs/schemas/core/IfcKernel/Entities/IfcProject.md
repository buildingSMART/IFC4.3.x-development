# IfcProject

_IfcProject_ indicates the undertaking of some design, engineering, construction, or maintenance activities leading towards a product. The project establishes the context for information to be exchanged or shared, and it may represent a construction project but does not have to. The _IfcProject_'s main purpose in an exchange structure is to provide the root instance and the context for all other information items included.

The context provided by the _IfcProject_ includes:

* the default units
* the geometric representation context for exchange structures including shape representations 
    * the project coordinate system
    * the coordinate space dimension
    * the precision used within the geometric representations
    * optionally the indication of the true north
    * optionally the map conversion between the project coordinate system and the geospatial coordinate reference system. 

> HISTORY&nbsp; New entity in IFC1.0

{ .change-ifc2x4}
> IFC4 CHANGE&nbsp; The attributes _RepresentationContexts_ and _UnitsInContext_ are made optional and are promoted to supertype _IfcContext_.

{ .spec-head}
Informal Propositions:

1. There shall only be one project within the exchange context. This is enforced by the global rule _IfcSingleProjectInstance_.

## Formal Propositions

### HasName
The _Name_ attribute has to be provided for _IfcProject_. It is the short name for the project.

### CorrectContext
If a _RepresentationContexts_ relation is provided then there shall be no instance of _IfcGeometricRepresentationSubContext_ directly included in the set of _RepresentationContexts_.

### NoDecomposition
The _IfcProject_ represents the root of the any decomposition tree. It shall therefore not be used to decompose any other object definition.
