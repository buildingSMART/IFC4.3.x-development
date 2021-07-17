# IfcBuilding

A building represents a structure that provides shelter for its occupants or contents and stands in one place. The building is also used to provide a basic element within the spatial structure hierarchy for the components of a building project (together with site, storey, and space).

{ .extDef}
> NOTE&nbsp; Definition from ISO 6707-1:  
> Construction work that has the provision of shelter for its occupants or contents as one of its main purpose and is normally designed to stand permanently in one place.

A building is (if specified) associated to a site. A building may span over several connected or disconnected buildings. Therefore building complex provides for a collection of buildings included in a site. A building can also be decomposed in (vertical) parts, where each part defines a building section. This is defined by the composition type attribute of the supertype _IfcSpatialStructureElements_ which is interpreted as follow:

* **COMPLEX**: building complex
* **ELEMENT**: building
* **PARTIAL**: building section

The _IfcBuilding_ is used to build the spatial structure of a building (that serves as the primary project breakdown and is required to be hierarchical). The spatial structure elements are linked together by using the objectified relationship _IfcRelAggregates_. Figure 1 shows the _IfcBuilding_ as part of the spatial structure. It also serves as the spatial container for building and other elements.

> NOTE&nbsp; Detailed requirements on mandatory element containment and placement structure relationships are given in view definitions and implementer agreements.

!["IfcBuildingStorey as part of a spatial structure"](../../../../figures/ifcbuilding-spatialstructure.png "Figure 1 &mdash; Building composition")

Systems, such as building service or electrical distribution systems, zonal systems, or structural analysis systems, relate to _IfcBuilding_ by using the objectified relationship _IfcRelServicesBuildings_.

Figure 2 describes the heights and elevations of the _IfcBuilding_. It is used to provide the height above sea level of the project height datum for this building, that is, the internal height 0.00. The height 0.00 is often used as a building internal reference height and equal to the floor finish level of the ground floor.

* base elevation of building provided by: _IfcBuilding.ElevationOfRefHeight_, it is usually the top of construction slab 
* base elevation of terrain at the perimeter of the building provided by: _IfcBuilding.ElevationOfTerrain_, it is usually the minimum elevation is sloped terrain 
* total height of building, also referred to as ridge height (top of roof structure, e.g the ridge against terrain): provided by BaseQuantity with Name="TotalHeight" 
* eaves height of building (base of roof structure, e.g the eaves against terrain): provided by BaseQuantity with Name="EavesHeight" 

<table border="0" cellpadding="2" cellspacing="2">
      <tbody>
        <tr valign="top">
          <td align="left" valign="top">
            <img src="../../../../figures/ifcbuilding_heights.png" alt="building heights" border="0" height="420" width="800">&nbsp;
          </td>
        </tr>
        <tr>
          <td>
            <p class="figure">Figure 2 &mdash; Building elevations
            </p>
          </td>
        </tr>
      </tbody>
    </table>

> HISTORY&nbsp; New entity in IFC1.0.

## Attributes

### ElevationOfRefHeight
Elevation above sea level of the reference height used for all storey elevation measures, equals to height 0.0. It is usually the ground floor level.

### ElevationOfTerrain
Elevation above the minimal terrain level around the foot print of the building, given in elevation above sea level.

### BuildingAddress

