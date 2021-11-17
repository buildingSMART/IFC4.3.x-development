# IfcSpatialElement

A spatial element is the generalization of all spatial elements that might be used to define a spatial structure or to define spatial zones.

* a hierarchical spatial structure element as _IfcSpatialStructureElement_ 
    * a spatial structure is a hiearchical decomposition of the project. That spatial structure is often used to provide a project structure to organize a building project.
    * A spatial project structure might define as many levels of decomposition as necessary for the building project. Elements within the spatial project structure are site, building, storey, and space or alternatively, site, bridge and bridge part 
* a spatial zone as _IfcSpatialZone_ 
    * a spatial zone is a non-hierarchical and potentially overlapping decomposition of the project under some functional consideration.
    * a spatial zone might be used to represent a thermal zone, a lighting zone, a usable area zone.
    * a spatial zone might be used to represent a horizontal spatial structure as used in civil works.
    * a spatial zone might have its independent placement and shape representation. 

> HISTORY&nbsp; New entity in IFC4.

## Attributes

### LongName
Long name for a spatial structure element, used for informal purposes. It should be used, if available, in conjunction with the inherited _Name_ attribute.
> NOTE&nbsp; In many scenarios the _Name_ attribute refers to the short name or number of a spacial element, and the _LongName_ refers to the full descriptive name.

### ContainsElements
Set of spatial containment relationships, that holds those elements, which are contained within this element of the project spatial structure.
> NOTE&nbsp; The spatial containment relationship, established by _IfcRelContainedInSpatialStructure_, is required to be an hierarchical relationship, where each element can only be assigned to 0 or 1 spatial structure element.

### ServicedBySystems
Set of relationships to systems, that provides a certain service to the spatial element for which it is defined. The relationship is handled by the objectified relationship _IfcRelServicesBuildings_.
{ .change-ifc2x4}
> IFC4 CHANGE&nbsp; The inverse attribute has been promoted to the new supertype _IfcSpatialElement_ with upward compatibility for file based exchange.

### ReferencesElements
Set of spatial reference relationships, that holds those elements, which are referenced, but not contained, within this element of the project spatial structure.
{ .change-ifc2x4}
> NOTE&nbsp; The spatial reference relationship, established by _IfcRelReferencedInSpatialStructure_, is not required to be an hierarchical relationship, i.e. each element can be assigned to 0, 1 or many spatial structure elements.

> EXAMPLE&nbsp; A curtain wall maybe contained in the ground floor, but maybe referenced in all floors, it reaches.

{ .change-ifc2x3}
> IFC2x3 CHANGE&nbsp; The inverse attribute has been added with upward compatibility for file based exchange.

{ .change-ifc2x4}
> Ø\X

## Concepts

### FootPrint GeomSet Geometry


### Property Sets for Objects


