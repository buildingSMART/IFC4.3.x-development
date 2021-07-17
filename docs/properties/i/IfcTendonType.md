IfcTendonType
=============

The reinforcing element type **IfcTendonType** defines commonly shared information for occurrences of tendons. The set of shared information may include:

* common properties with shared property sets
* common representations
* common materials
* common composition of elements

It is used to define a tendon type specification indicating the specific product information that is common to all occurrences of that product type. The **IfcTendonType** may be declared within _IfcProject_ or _IfcProjectLibrary_ using _IfcRelDeclares_ and may be exchanged with or without occurrences of the type. Occurrences of **IfcTendonType** are represented by instances of _IfcTendon_.

> HISTORY&nbsp; New entity in IFC4.

{ .use-head}
Material Use Definition

An associated material denotes the steel grade, preferrably via material classification. A material constituent set or material profile set may be associated if the cable, bonding mortar or corrosion protection, and tendon sheeth are to be described together by the material association.

{ .use-head}
Geometry Use Definition

The _IfcTendonType_ may define the shared geometric representation for many tendon occurrences. The _RepresentationMaps_ attribute refers to a list of _IfcRepresentationMap_'s, that allow for multiple geometric representations.
