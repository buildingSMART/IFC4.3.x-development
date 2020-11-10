IfcSpatialStructureElement
==========================
A spatial structure element is the generalization of all spatial elements that
might be used to define a spatial structure. That spatial structure is often
used to provide a project structure to organize a building project.  
A spatial project structure might define as many levels of decomposition as
necessary for the building project. Elements within the spatial project
structure are:  

  

  * site as [_IfcSite_]($element://{2E1AEFD9-0C13-4c37-ADD3-F1FF076F7A3C})
  

  

  

  * facility as _IfcFacility_, or any of its specific subtypes. REMOVE {specifically  
building as IfcBuilding  
bridge as IfcBridge }

  

  

  

  * facility part as [_IfcFacilityPart_]($element://{61C7E8E9-D8A6-4955-ACCB-2865F2D81503}), REMOVE { or specifically  
storey as IfcBuildingStorey  
bridge part as IfcBridgePart }

  

  

  

  * space as [_IfcSpace_]($element://{51F70274-0484-4e6b-899A-1D0445F25124})
  

  
or aggregations or parts thereof. The composition type declares an element to
be either an element itself, or an aggregation (complex) or a decomposition
(part). The interpretation of these types is given at each subtype of
[_IfcSpatialStructureElement_]($element://{30E08EC3-5B14-45f4-8246-B4811D2ECF1B}).  
The [_IfcRelAggregates_]($element://{12F56CBC-A6CE-493c-8A50-E301CE73BBA5}) is
defined as an 1-to-many relationship and used to establish the relationship
between exactly two levels within the spatial project structure. Finally the
highest level of the spatial structure is assigned to
[_IfcProject_]($element://{261F430C-03B3-4a9e-A414-1452166DEDA0}) using the
[_IfcRelAggregates_]($element://{12F56CBC-A6CE-493c-8A50-E301CE73BBA5}).  
The subtypes of
[_IfcSpatialStructureElement_]($element://{30E08EC3-5B14-45f4-8246-B4811D2ECF1B})
relate to other elements and systems by establishing the following
relationships:  

  

  * **Containment of elements** : [_IfcRelContainedInSpatialStructure_]($element://{4BA66984-EDFC-415d-BB2E-DE5369370756}) by inverse attribute _ContainsElements_, used to assign any element, like building elements, MEP elements, etc. to the spatial structure element in which they are primarily contained.
  

  * **Reference of elements** : [_IfcRelReferencedInSpatialStructure_]($element://{415054A4-1479-4c32-9A58-BC1E36A488CC}) by inverse attribute ReferencesElements, used to reference any element, like building elements, MEP elements, etc. in spatial structure elements, other then the one, where it is contained.
  

  

  

  * **Reference of systems** : REMOVE {IfcRelServicesBuildings by inverse attribute _ServicedBySystems_, used to reference a sytem,} [_IfcRelReferencedInSpatialStructure_]($element://{415054A4-1479-4c32-9A58-BC1E36A488CC}) by inverse attribute ReferencesElements, used to reference a system, like a building service or electrical distribution system, a zonal system, or a structural analysis system, that is assigned to this spatial structure element.
  

  
The subtypes of
[_IfcSpatialStructureElement_]($element://{30E08EC3-5B14-45f4-8246-B4811D2ECF1B})
relate to each other by using the
[_IfcRelAggregates_]($element://{12F56CBC-A6CE-493c-8A50-E301CE73BBA5})
relationship to build the project spatial structure. Figure 1 shows the use of
[_IfcRelAggregates_]($element://{12F56CBC-A6CE-493c-8A50-E301CE73BBA5}) to
establish a spatial structure including site, building, building section and
storey. More information is provided at the level of the subtypes.  
[ _Spatial Structure
composition_]($imageman://id=597667808;mdg=Global;name=Spatial Structure
composition;type=Bitmap;)  
Figure — Spatial structure element composition  
HISTORY New entity in IFC2x.  
  
 **Informal Propositions:**  

  

  1. The spatial project structure, established by the _IfcRelAggregates_, shall be acyclic.
  

  2. A site should not be (directly or indirectly) associated to a building, storey or space.
  

  3. A building should not be (directly or indirectly) associated to a storey or space.
  

  4. A storey should not be (directly or indirectly) associated to a space.
  

  
[ _bSI
Documentation_](https://standards.buildingsmart.org/IFC/DEV/IFC4_2/FINAL/HTML/schema/ifcproductextension/lexical/ifcspatialstructureelement.htm)


Attribute definitions
---------------------
| Attribute       | Description                                                                                                                                                                                                                                                                                                                                                  |
|-----------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| CompositionType | Denotes, whether the predefined spatial structure element represents itself, or an aggregate (complex) or a part (part). The interpretation is given separately for each subtype of spatial structure element. If no _CompositionType_ is asserted, the dafault value ''ELEMENT'' applies.\X\0D{ .change-ifc2x4}\X\0D> IFC4 CHANGE  Attribute made optional. |

