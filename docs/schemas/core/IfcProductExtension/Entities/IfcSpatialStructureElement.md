# IfcSpatialStructureElement

A spatial structure element is the generalization of all spatial elements that might be used to define a spatial structure. That spatial structure is often used to provide a project structure to organize a building project.  
A spatial project structure might define as many levels of decomposition as necessary for the building project. Elements within the spatial project structure are:  
* site as [<font color="#0000ff"><u>IfcSite</u></font>]($element://{2E1AEFD9-0C13-4c37-ADD3-F1FF076F7A3C})

  
* facility as _IfcFacility_, or <font color="#ff0000">any of its specific subtypes. REMOVE {</font>specifically   building as IfcBuilding   bridge as IfcBridge<font color="#ff0000"> }</font>

  
* facility part as [<font color="#0000ff"><u>IfcFacilityPart</u></font>]($element://{61C7E8E9-D8A6-4955-ACCB-2865F2D81503}), <font color="#ff0000">REMOVE {</font> or specifically   storey as IfcBuildingStorey   bridge part as IfcBridgePart <font color="#ff0000">}</font>

  
* space as [<font color="#0000ff"><u>IfcSpace</u></font>]($element://{51F70274-0484-4e6b-899A-1D0445F25124})

  
or aggregations or parts thereof. The composition type declares an element to be either an element itself, or an aggregation (complex) or a decomposition (part). The interpretation of these types is given at each subtype of [<font color="#0000ff"><u>IfcSpatialStructureElement</u></font>]($element://{30E08EC3-5B14-45f4-8246-B4811D2ECF1B}).  
The [<font color="#0000ff"><u>IfcRelAggregates</u></font>]($element://{12F56CBC-A6CE-493c-8A50-E301CE73BBA5}) is defined as an 1-to-many relationship and used to establish the relationship between exactly two levels within the spatial project structure. Finally the highest level of the spatial structure is assigned to [<font color="#0000ff"><u>IfcProject</u></font>]($element://{261F430C-03B3-4a9e-A414-1452166DEDA0}) using the [<font color="#0000ff"><u>IfcRelAggregates</u></font>]($element://{12F56CBC-A6CE-493c-8A50-E301CE73BBA5}).  
The subtypes of [<font color="#0000ff"><u>IfcSpatialStructureElement</u></font>]($element://{30E08EC3-5B14-45f4-8246-B4811D2ECF1B}) relate to other elements and systems by establishing the following relationships:  
* **Containment of elements**: [<font color="#0000ff"><u>IfcRelContainedInSpatialStructure</u></font>]($element://{4BA66984-EDFC-415d-BB2E-DE5369370756}) by inverse attribute _ContainsElements_, used to assign any element, like building elements, MEP elements, etc. to the spatial structure element in which they are primarily contained.
* **Reference of elements**: [<font color="#0000ff"><u>IfcRelReferencedInSpatialStructure</u></font>]($element://{415054A4-1479-4c32-9A58-BC1E36A488CC}) by inverse attribute ReferencesElements, used to reference any element, like building elements, MEP elements, etc. in spatial structure elements, other then the one, where it is contained.

  
* **Reference of systems**: <font color="#ff0000">REMOVE {</font>IfcRelServicesBuildings by inverse attribute _ServicedBySystems_, used to reference a sytem,<font color="#ff0000">} </font>[<font color="#ff0000"><u>IfcRelReferencedInSpatialStructure</u></font>]($element://{415054A4-1479-4c32-9A58-BC1E36A488CC})<font color="#ff0000"> by inverse attribute ReferencesElements, used to reference a system,</font> like a building service or electrical distribution system, a zonal system, or a structural analysis system, that is assigned to this spatial structure element.

  
The subtypes of [<font color="#0000ff"><u>IfcSpatialStructureElement</u></font>]($element://{30E08EC3-5B14-45f4-8246-B4811D2ECF1B}) relate to each other by using the [<font color="#0000ff"><u>IfcRelAggregates</u></font>]($element://{12F56CBC-A6CE-493c-8A50-E301CE73BBA5}) relationship to build the project spatial structure. Figure 1 shows the use of [<font color="#0000ff"><u>IfcRelAggregates</u></font>]($element://{12F56CBC-A6CE-493c-8A50-E301CE73BBA5}) to establish a spatial structure including site, building, building section and storey. More information is provided at the level of the subtypes.  
[<font color="#0000ff"><u>Spatial Structure composition</u></font>]($imageman://id=597667808;mdg=Global;name=Spatial Structure composition;type=Bitmap;)  
Figure � Spatial structure element composition  
HISTORY New entity in IFC2x.  
  
**Informal Propositions:**  
1. The spatial project structure, established by the _IfcRelAggregates_, shall be acyclic.
2. A site should not be (directly or indirectly) associated to a building, storey or space.
3. A building should not be (directly or indirectly) associated to a storey or space.
4. A storey should not be (directly or indirectly) associated to a space.

## Attributes

### CompositionType
Denotes, whether the predefined spatial structure element represents itself, or an aggregate (complex) or a part (part). The interpretation is given separately for each subtype of spatial structure element. If no _CompositionType_ is asserted, the dafault value ''ELEMENT'' applies.\X\0D
{ .change-ifc2x4}\X\0D
> IFC4 CHANGE&nbsp; Attribute made optional.

## WhereRules

### WR41
All spatial structure elements shall be associated (using the IfcRelAggregates relationship) with another spatial structure element, or with IfcProject.
