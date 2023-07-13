# IfcBuildingStorey

The building storey has an elevation and typically represents a (nearly) horizontal aggregation of spaces that are vertically bound.

> NOTE  Definition from ISO 6707-1:
> space between two consecutive floors or between a floor and a roof

A storey is (if specified) associated to a building. A storey may span over several connected storeys. Therefore storey complex provides for a collection of storeys included in a building. A storey can also be decomposed in (horizontical) parts, where each part defines a partial storey. This is defined by the composition type attribute of the supertype _IfcSpatialStructureElement_ which is interpreted as follow:

* **COMPLEX**: building storey complex
* **ELEMENT**: building storey
* **PARTIAL**: partial building storey

> EXAMPLE  In split level houses, a storey is split into two or more partial storeys, each with a different elevation. It can be handled by defining a storey, which includes two or more partial storeys with the individual elevations.

The _IfcBuildingStorey_ is used to build the spatial structure of a building (that serves as the primary project breakdown and is required to be hierarchical). The spatial structure elements are linked together by using the objectified relationship _IfcRelAggregates_.

Figure 1 shows the _IfcBuildingStorey_ as part of the spatial structure. It also serves as the spatial container for building and other elements.

> NOTE  Detailed requirements on mandatory element containment and placement structure relationships are provided in model view definitions.

![IfcBuildingStorey as part of a spatial structure](../../../../figures/ifcbuildingstorey-spatialstructure.png "Figure 1 &mdash; Building storey composition")

Figure 1 &mdash; Building storey composition

Figure 2 describes the heights and elevations of the _IfcBuildingStorey_.

* elevation of the structural slab level: provided by _Pset_BuildingStoreyCommon_ with Name="ElevationOfSSLRelative"
* elevation of the finish floor level: provided by _Pset_BuildingStoreyCommon_ with Name="ElevationOfFFLRelative"
* gross height of storey, also referred to as total height or system height (top of construction slab to top of construction slab above): provided by _Qto_BuildingStoreyBaseQuantities_ with Name="GrossHeight"
* net height of storey (top of construction slab to bottom of construction slab above): provided by _Qto_BuildingStoreyBaseQuantities_ with Name="NetHeight"

![space heights](../../../../figures/ifcbuildingstorey_heights.png "Figure 2 &mdash; Building storey elevations")

Figure 2 &mdash; Example showing the use of base quantities for building storeys

> HISTORY  New entity in IFC1.0

## Attributes

### Elevation
Elevation of the base of this storey, relative to the 0,00 internal reference height of the building. The 0.00 level is given by the absolute above sea level height by the _ElevationOfRefHeight_ attribute given at _IfcBuilding_.

> NOTE  The local placement of the _IfcBuildingStorey_ is determined by the _ObjectPlacement_. The value of _Elevation_ is for informational purposes only.

> IFC4.3.0.0 DEPRECATION This attribute is deprecated and shall no longer be used. Within Pset_BuildingStoreyCommon use ElevationOfSSLRelative or ElevationOfFFLRelative instead.

## Concepts

### Body Geometry

### FootPrint GeomSet Geometry

The foot print representation of IfcBuildingStorey is given by either a single 2D curve (such as IfcPolyline or IfcCompositeCurve), or by a list of 2D curves (in case of inner boundaries), if the building storey has an independent geometric representation.

> NOTE  The independent geometric representation of IfcBuildingStorey may not be allowed in certain model view definitions. In those cases only the contained elements and spaces have an independent geometric representation.

### Product Local Placement

The local placement for IfcBuildingStorey is defined in its supertype IfcProduct. It is defined by the IfcLocalPlacement, which defines the local coordinate system that is referenced by all geometric representations.

* The PlacementRelTo relationship of IfcLocalPlacement shall point (if relative placement is used) to the IfcSpatialStructureElement of type IfcBuilding, or of type IfcBuildingStorey (e.g. to position a building storey relative to a building storey complex, or a partial building storey to a building storey).
* If the relative placement is not used, the absolute placement is defined within the world coordinate system.

### Property Sets for Objects



### Quantity Sets



### Spatial Composition

> NOTE  By using the inverse relationship _IfcBuildingStorey.Decomposes_ it references (IfcBuilding || IfcBuildingStorey) through _IfcRelAggregates.RelatingObject_IfcBuildingStorey_, the referenced
IfcBuildingStorey needs to have a different and higher
 CompositionType, i.e. COMPLEX (if the other IfcBuildingStorey has ELEMENT), or ELEMENT (if the other
 IfcBuildingStorey has PARTIAL)._

### Spatial Container

If there are building elements and/or other elements directly related to the IfcBuildingStorey (like most building elements, such as walls, columns, etc.), they are associated with the IfcBuildingStorey by using the objectified relationship IfcRelContainedInSpatialStructure. The IfcBuildingStorey references them by its inverse relationship:

* _IfcBuildingStorey.ContainsElements_ -- referencing any subtype of IfcProduct (with the exception of other spatial structure element) by _IfcRelContainedInSpatialStructure.RelatedElements_.

Elements can also be referenced in an IfcBuildingStorey, for example, if they span through several storeys. This is expressed by using the objectified relationship IfcRelReferencedInSpatialStructure. Systems, such as building service or electrical distribution systems, zonal systems, or structural analysis systems, relate to IfcBuildingStorey by using the objectified relationship IfcRelServicesBuildings.

### Spatial Decomposition

> NOTE  By using the inverse relationship _IfcBuildingStorey.IsDecomposedBy_ it references IfcBuildingStorey || IfcSpace through _IfcRelAggregates.RelatedObjects_. If it refers to another instance of IfcBuildingStorey, the referenced IfcBuildingStorey needs to have a different and lower CompositionType, i.e. ELEMENT (if the other IfcBuildingStorey has COMPLEX), or PARTIAL (if the other IfcBuildingStorey has ELEMENT).

> NOTE  Multi storey spaces shall be spatially contained by only a single building storey, usually it is the building storey where the base of the space lies.

### Storey Attributes
