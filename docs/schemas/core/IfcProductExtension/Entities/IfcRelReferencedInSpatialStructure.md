# IfcRelReferencedInSpatialStructure

The objectified relationship, [<font color="#0000ff"><u>IfcRelReferencedInSpatialStructure</u></font>]($element://{415054A4-1479-4c32-9A58-BC1E36A488CC}) is used to assign elements in addition to those levels of the project spatial\S\ structure, in which they are referenced, but not primarily contained. <font color="#ff0000">It is also used to connect a system to the relevant spatial element that it serves.</font>  
NOTE The primary containment relationship between an element and the spatial structure is handled by [<font color="#0000ff"><u>IfcRelContainedInSpatialStructure</u></font>]($element://{4BA66984-EDFC-415d-BB2E-DE5369370756}).  
Any element can be referenced to zero, one or several levels of the spatial structure. Whereas the [<font color="#0000ff"><u>IfcRelContainedInSpatialStructure</u></font>]($element://{4BA66984-EDFC-415d-BB2E-DE5369370756}) relationship is required to be hierarchical (an element can only be contained in exactly one spatial structure element), the [<font color="#0000ff"><u>IfcRelReferencedInSpatialStructure</u></font>]($element://{415054A4-1479-4c32-9A58-BC1E36A488CC}) is not restricted to be hierarchical.  
EXAMPLE A wall might be normally contained within a storey, and since it does not span through several stories, it is not referenced in any additional storey. However a curtain wall might span through several stories, in this case it can be contained within the ground floor, but it would be referenced by all additional stories, it spans.  
Predefined spatial structure elements to which elements can be assigned are  
* site as [<font color="#0000ff"><u>IfcSite</u></font>]($element://{2E1AEFD9-0C13-4c37-ADD3-F1FF076F7A3C})
* facility as [<font color="#0000ff"><u>IfcFacility</u></font>]($element://{BF7D2E47-9C5D-4d0e-873E-34760E593EAC}) or its subtypes [<font color="#0000ff"><u>IfcBridge</u></font>]($element://{0E1DDD89-891A-4501-94C0-776937C5A9B6}), [<font color="#0000ff"><u>IfcBuilding</u></font>]($element://{6A41B6BC-5685-455c-84F7-0CBCEAF26389}), [<font color="#0000ff"><u>IfcMarineFacility</u></font>]($element://{A52886FF-ABF1-486e-80BC-B8FA83F34756}), [<font color="#0000ff"><u>IfcRailway</u></font>]($element://{CA669BBF-23DC-4d50-B4A3-F34551C17181}) or [<font color="#0000ff"><u>IfcRoad</u></font>]($element://{2CF12FC5-92DB-4151-AA2F-D3D8644AC83A})
* part of facility as [<font color="#0000ff"><u>IfcFaciltityPart</u></font>]($element://{61C7E8E9-D8A6-4955-ACCB-2865F2D81503}), or more specifically as [<font color="#0000ff"><u>IfcBuildingStorey</u></font>]($element://{9AEF2BF9-C883-4d6d-9C97-3ECF9D333235}) or [<font color="#0000ff"><u>IfcSpace</u></font>]($element://{51F70274-0484-4e6b-899A-1D0445F25124})

  
Elements can also be references in a spatial zone that is provided as [<font color="#0000ff"><u>IfcSpatialZone</u></font>]($element://{C6BFC05D-09D4-4bed-92A9-1823739DE0C8}).  
Figure 167 shows the use of [<font color="#0000ff"><u>IfcRelContainedInSpatialStructure</u></font>]($element://{4BA66984-EDFC-415d-BB2E-DE5369370756}) and [<font color="#0000ff"><u>IfcRelReferencedInSpatialStructure</u></font>]($element://{415054A4-1479-4c32-9A58-BC1E36A488CC}) to assign an [<font color="#0000ff"><u>IfcCurtainWall</u></font>]($element://{7E90AAF4-3589-40ea-B862-A15B42B9B489}) to two different levels within the spatial structure. It is primarily contained within the ground floor, and additionally referenced within the first and second floor.  
[<font color="#0000ff"><u>Spatial_referencing</u></font>]($imageman://id=732726067;mdg=Global;name=Spatial_referencing;type=Bitmap;)  
Figure 167 � Relationship for spatial structure referencing  
HISTORY New entity in IFC2x3.

## Attributes

### RelatedElements


### RelatingStructure


## Formal Propositions

### AllowedRelatedElements
The relationship object shall not be used to include other spatial structure elements into a spatial structure element. The hierarchy of the spatial structure is defined using _IfcRelAggregates_. Exception: an _IfcSpace_ can be referenced by another spatial structure element, in particular by an _IfcSpatialZone_.
{ .change-ifc2x4}
> IFC4 CHANGE&nbsp; The relaxation to allow _IfcSpace_ has been included.
