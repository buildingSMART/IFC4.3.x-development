# IfcMaterial

_IfcMaterial_ is a homogeneous or inhomogeneous substance that can be used to form elements (physical products or their components).

_IfcMaterial_ is the basic entity for material designation and definition; this includes identification by name and classification (via reference to an external classification), as well as association of material properties (isotropic or anisotropic) defined by (subtypes of) _IfcMaterialProperties_. An instance of _IfcMaterial_ may be associated to an element or element type using the _IfcRelAssociatesMaterial_ relationship. The assignment might either be direct as a single material information, or via

* a material layer set
* a material profile set
* a material constituent set

An _IfcMaterial_ may also have presentation information associated. Such presentation information is provided by _IfcMaterialDefinitionRepresentation_, associating curve styles, hatching definitions or surface colouring/rendering information to a material.

> HISTORY New entity in IFC4

{ .change-ifc2x4}
> IFC4 CHANGE  The attributes _Description_ and _Category_ have been added.

## Attributes

### Name
Name of the material. 
> EXAMPLE A view definition may require _Material.Name_ to uniquely specify e.g. concrete or steel grade, in which case the attribute Material.Category could take the value 'Concrete' or 'Steel'.

> NOTE&nbsp; Material grade may have different meaning in different view definitions, e.g. strength grade for structural design and analysis, or visible appearance grade in architectural application. Also, more elaborate material grade definition may be associated as classification via inverse attribute _HasExternalReferences_.

### Description
Definition of the material in more descriptive terms than given by attributes _Name_ or _Category_.
{ .change-ifc2x4}
> IFC4 CHANGE&nbsp; The attribute has been added at the end of attribute list.

### Category
Definition of the category (group or type) of material, in more general terms than given by attribute _Name_.  
> EXAMPLE A view definition may require each _Material.Name_ to be unique, e.g. for each concrete or steel grade used in a project, in which case _Material.Category_ could take the values 'Concrete' or 'Steel'.

{ .change-ifc2x4}
> IFC4 CHANGE&nbsp; The attribute has been added at the end of attribute list.

### HasRepresentation
Reference to the _IfcMaterialDefinitionRepresentation_ that provides presentation information to a representation common to this material in style definitions.
  
{ .change-ifc2x3}
> IFC2x3 CHANGE&nbsp; The inverse attribute _HasRepresentation_ has been added.

### IsRelatedWith
Reference to a material relationship indicating that this material is a part (or constituent) in a material composite.
{ .change-ifc2x4}
> IFC4 CHANGE&nbsp; The inverse attribute has been added.

### RelatesTo
Reference to a material relationship indicating that this material composite has parts (or constituents).
{ .change-ifc2x4}
> IFC4 CHANGE&nbsp; The inverse attribute has been added.
