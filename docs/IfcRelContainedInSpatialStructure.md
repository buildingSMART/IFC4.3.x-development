IfcRelContainedInSpatialStructure
=================================
This objectified relationship, _IfcRelContainedInSpatialStructure_, is used to
assign elements to a certain level of the spatial project structure. Any
element can only be assigned once to a certain level of the spatial structure.
The question, which level is relevant for which type of element, can only be
answered within the context of a particular project and might vary within the
various regions.  
  
> EXAMPLE A multi-storey space is contained (or belongs to) the building
> storey at which its ground level is, but it is referenced by all the other
> building storeys, in which it spans. A lift shaft might be contained by the
> basement, but referenced by all storeys, through which it spans.  
  
The containment relationship of an element within a spatial structure has to
be a hierarchical relationship; an element can only be contained within a
single spatial structure element. The reference relationship between an
element and the spatial structure need not be hierarchical; that is, an
element can reference many spatial structure elements.  
  
> NOTE The reference relationship is expressed by
> _IfcRelReferencedInSpatialStructure_.  
  
Predefined spatial structure elements to which elements can be assigned are  

  

  * site as [_IfcSite_]($element://{2E1AEFD9-0C13-4c37-ADD3-F1FF076F7A3C})
  

  * facility as [_IfcFacility_]($element://{BF7D2E47-9C5D-4d0e-873E-34760E593EAC}) or its subtypes [_IfcBridge_]($element://{0E1DDD89-891A-4501-94C0-776937C5A9B6}), [_IfcBuilding_]($element://{6A41B6BC-5685-455c-84F7-0CBCEAF26389}), [_IfcMarineFacility_]($element://{A52886FF-ABF1-486e-80BC-B8FA83F34756}), [_IfcRailway_]($element://{CA669BBF-23DC-4d50-B4A3-F34551C17181}) or [_IfcRoad_]($element://{2CF12FC5-92DB-4151-AA2F-D3D8644AC83A})
  

  * part of facility as [_IfcFaciltityPart_]($element://{61C7E8E9-D8A6-4955-ACCB-2865F2D81503}), or more specifically as [_IfcBuildingStorey_]($element://{9AEF2BF9-C883-4d6d-9C97-3ECF9D333235}) or [_IfcSpace_]($element://{51F70274-0484-4e6b-899A-1D0445F25124})
  

  
Occurrences of the same element type can be assigned to different spatial
structure elements depending on the context of the occurrence.  
  
> EXAMPLE A wall might be normally assigned to a storey, however the curtain
> wall might be assigned to the building and the retaining wall in the terrain
> might be assigned to the site.  
  
Figure 1 shows the use of _IfcRelContainedInSpatialStructure_ to assign a
stair and two walls to two different levels within the spatial structure.  
  
!["fig1"](figures/ifcrelcontainedinspatialstructure-fig1.png "Figure 1 —
Relationship for spatial structure containment")  
  
> HISTORY New entity in IFC2x.  
  
{ .change-ifc2x}  
> IFC2x CHANGE The data type of the attribute _RelatedElements_ has been
> changed from _IfcElement_ to its supertype _IfcProduct_ with upward
> compatibility for file based exchange.  
[ _bSI
Documentation_](https://standards.buildingsmart.org/IFC/DEV/IFC4_2/FINAL/HTML/schema/ifcproductextension/lexical/ifcrelcontainedinspatialstructure.htm)


