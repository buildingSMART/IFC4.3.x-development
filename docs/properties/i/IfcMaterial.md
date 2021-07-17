IfcMaterial
===========

_IfcMaterial_ is a homogeneous or inhomogeneous substance that can be used to form elements (physical products or their components).

_IfcMaterial_ is the basic entity for material designation and definition; this includes identification by name and classification (via reference to an external classification), as well as association of material properties (isotropic or anisotropic) defined by (subtypes of) _IfcMaterialProperties_. An instance of _IfcMaterial_ may be associated to an element or element type using the _IfcRelAssociatesMaterial_ relationship. The assignment might either be direct as a single material information, or via

* a material layer set
* a material profile set
* a material constituent set

An _IfcMaterial_ may also have presentation information associated. Such presentation information is provided by _IfcMaterialDefinitionRepresentation_, associating curve styles, hatching definitions or surface colouring/rendering information to a material.

> HISTORY New entity in IFC4

{ .change-ifc2x4}
> IFC4 CHANGE  The attributes _Description_ and _Category_ have been added.
