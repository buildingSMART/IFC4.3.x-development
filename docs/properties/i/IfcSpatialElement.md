IfcSpatialElement
=================

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
