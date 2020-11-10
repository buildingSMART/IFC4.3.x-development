IfcRelReferencedInSpatialStructure
==================================
The objectified relationship,
[_IfcRelReferencedInSpatialStructure_]($element://{415054A4-1479-4c32-9A58-BC1E36A488CC})
is used to assign elements in addition to those levels of the project
spatial\S\ structure, in which they are referenced, but not primarily
contained. It is also used to connect a system to the relevant spatial element
that it serves.  
NOTE The primary containment relationship between an element and the spatial
structure is handled by
[_IfcRelContainedInSpatialStructure_]($element://{4BA66984-EDFC-415d-BB2E-DE5369370756}).  
Any element can be referenced to zero, one or several levels of the spatial
structure. Whereas the
[_IfcRelContainedInSpatialStructure_]($element://{4BA66984-EDFC-415d-BB2E-DE5369370756})
relationship is required to be hierarchical (an element can only be contained
in exactly one spatial structure element), the
[_IfcRelReferencedInSpatialStructure_]($element://{415054A4-1479-4c32-9A58-BC1E36A488CC})
is not restricted to be hierarchical.  
EXAMPLE A wall might be normally contained within a storey, and since it does
not span through several stories, it is not referenced in any additional
storey. However a curtain wall might span through several stories, in this
case it can be contained within the ground floor, but it would be referenced
by all additional stories, it spans.  
Predefined spatial structure elements to which elements can be assigned are  

  

  * site as [_IfcSite_]($element://{2E1AEFD9-0C13-4c37-ADD3-F1FF076F7A3C})
  

  * facility as [_IfcFacility_]($element://{BF7D2E47-9C5D-4d0e-873E-34760E593EAC}) or its subtypes [_IfcBridge_]($element://{0E1DDD89-891A-4501-94C0-776937C5A9B6}), [_IfcBuilding_]($element://{6A41B6BC-5685-455c-84F7-0CBCEAF26389}), [_IfcMarineFacility_]($element://{A52886FF-ABF1-486e-80BC-B8FA83F34756}), [_IfcRailway_]($element://{CA669BBF-23DC-4d50-B4A3-F34551C17181}) or [_IfcRoad_]($element://{2CF12FC5-92DB-4151-AA2F-D3D8644AC83A})
  

  * part of facility as [_IfcFaciltityPart_]($element://{61C7E8E9-D8A6-4955-ACCB-2865F2D81503}), or more specifically as [_IfcBuildingStorey_]($element://{9AEF2BF9-C883-4d6d-9C97-3ECF9D333235}) or [_IfcSpace_]($element://{51F70274-0484-4e6b-899A-1D0445F25124})
  

  
Elements can also be references in a spatial zone that is provided as
[_IfcSpatialZone_]($element://{C6BFC05D-09D4-4bed-92A9-1823739DE0C8}).  
Figure 167 shows the use of
[_IfcRelContainedInSpatialStructure_]($element://{4BA66984-EDFC-415d-BB2E-DE5369370756})
and
[_IfcRelReferencedInSpatialStructure_]($element://{415054A4-1479-4c32-9A58-BC1E36A488CC})
to assign an
[_IfcCurtainWall_]($element://{7E90AAF4-3589-40ea-B862-A15B42B9B489}) to two
different levels within the spatial structure. It is primarily contained
within the ground floor, and additionally referenced within the first and
second floor.  
[
_Spatial_referencing_]($imageman://id=732726067;mdg=Global;name=Spatial_referencing;type=Bitmap;)  
Figure 167 — Relationship for spatial structure referencing  
HISTORY New entity in IFC2x3.  
[ _bSI
Documentation_](https://standards.buildingsmart.org/IFC/DEV/IFC4_2/FINAL/HTML/schema/ifcproductextension/lexical/ifcrelreferencedinspatialstructure.htm)


Attribute definitions
---------------------
| Attribute         | Description   |
|-------------------|---------------|
| RelatedElements   |               |
| RelatingStructure |               |

