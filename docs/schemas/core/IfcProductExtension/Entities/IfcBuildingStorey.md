The building storey has an elevation and typically represents a (nearly) horizontal aggregation of spaces that are vertically bound.

<!-- end of short definition -->


> NOTE Definition from ISO 6707-1:
> space between two consecutive floors or between a floor and a roof

A storey is (if specified) associated to a building. A storey may span over several connected storeys. Therefore storey complex provides for a collection of storeys included in a building. A storey can also be decomposed in (horizontal) parts, where each part defines a partial storey. This is defined by the composition type attribute of the supertype _IfcSpatialStructureElement_ which is interpreted as follow:

* **COMPLEX**: building storey complex
* **ELEMENT**: building storey
* **PARTIAL**: partial building storey

> EXAMPLE In split level houses, a storey is split into two or more partial storeys, each with a different elevation. It can be handled by defining a storey, which includes two or more partial storeys with the individual elevations.

The _IfcBuildingStorey_ is used to build the spatial structure of a building (that serves as the primary project breakdown and is required to be hierarchical). The spatial structure elements are linked together by using the objectified relationship _IfcRelAggregates_.

Figure 1 shows the _IfcBuildingStorey_ as part of the spatial structure. It also serves as the spatial container for building and other elements.

> NOTE Detailed requirements on mandatory element containment and placement structure relationships are provided in model view definitions.

![IfcBuildingStorey as part of a spatial structure](../../../../figures/ifcbuildingstorey-spatialstructure.png "Figure 1 — Building storey composition")

Figure 1 — Building storey composition

Figure 2 describes the heights and elevations of the _IfcBuildingStorey_.

* elevation of the structural slab level: provided by _Pset_BuildingStoreyCommon_ with Name="ElevationOfSSLRelative"
* elevation of the finish floor level: provided by _Pset_BuildingStoreyCommon_ with Name="ElevationOfFFLRelative"
* gross height of storey, also referred to as total height or system height (top of construction slab to top of construction slab above): provided by _Qto_BuildingStoreyBaseQuantities_ with Name="GrossHeight"
* net height of storey (top of construction slab to bottom of construction slab above): provided by _Qto_BuildingStoreyBaseQuantities_ with Name="NetHeight"

![space heights](../../../../figures/ifcbuildingstorey_heights.png "Figure 2 — Building storey elevations")

Figure 2 — Example showing the use of base quantities for building storeys

> HISTORY New entity in IFC1.0

## Attributes

### Elevation
Elevation of the base of this storey, relative to the 0,00 internal reference height of the building. The 0.00 level is given by the absolute above sea level height by the _ElevationOfRefHeight_ attribute given at _IfcBuilding_.

> NOTE The local placement of the _IfcBuildingStorey_ is determined by the _ObjectPlacement_. The value of _Elevation_ is for informational purposes only.

> IFC4.3.0.0 DEPRECATION This attribute is deprecated and shall no longer be used. Within Pset_BuildingStoreyCommon use ElevationOfSSLRelative or ElevationOfFFLRelative instead.

## Concepts

### Body Geometry

### FootPrint GeomSet Geometry

The foot print representation of _IfcBuildingStorey_ is given by either a single 2D curve (such as _IfcPolyline_ or _IfcCompositeCurve_), or by a list of 2D curves (in case of inner boundaries), if the building storey has an independent geometric representation.

> NOTE The independent geometric representation of _IfcBuildingStorey_ may not be allowed in certain model view definitions. In those cases only the contained elements and spaces have an independent geometric representation.

### Product Local Placement

The local placement for _IfcBuildingStorey_ is defined in its supertype _IfcProduct_. It is defined by the _IfcLocalPlacement_, which defines the local coordinate system that is referenced by all geometric representations.

* The _PlacementRelTo_ relationship of _IfcLocalPlacement_ shall point (if relative placement is used) to the _IfcSpatialStructureElement_ of type _IfcBuilding_, or of type _IfcBuildingStorey_ (e.g. to position a building storey relative to a building storey complex, or a partial building storey to a building storey).
* If the relative placement is not used, the absolute placement is defined within the world coordinate system.

### Property Sets for Objects



### Quantity Sets



### Spatial Composition

> NOTE By using the inverse relationship _IfcBuildingStorey.Decomposes_ it references (_IfcBuilding_ || _IfcBuildingStorey_) through _IfcRelAggregates.RelatingObject_, the referenced _IfcBuildingStorey_ needs to have a different and higher CompositionType, i.e. _COMPLEX_ (if the other _IfcBuildingStorey_ has _ELEMENT_), or _ELEMENT_ (if the other _IfcBuildingStorey_ has _PARTIAL_).

### Spatial Container

If there are building elements and/or other elements directly related to the _IfcBuildingStorey_ (like most building elements, such as walls, columns, etc.), they are associated with the _IfcBuildingStorey_ by using the objectified relationship _IfcRelContainedInSpatialStructure_. The _IfcBuildingStorey_ references them by its inverse relationship:

* _IfcBuildingStorey.ContainsElements_ -- referencing any subtype of _IfcProduct_ (with the exception of other spatial structure elements) by _IfcRelContainedInSpatialStructure.RelatedElements_.

Elements can also be referenced in an _IfcBuildingStorey_, for example, if they span through several storeys. This is expressed by using the objectified relationship _IfcRelReferencedInSpatialStructure_. Systems, such as building service or electrical distribution systems, zonal systems, or structural analysis systems, relate to _IfcBuildingStorey_ by using the objectified relationship _IfcRelServicesBuildings_.

### Spatial Decomposition

> NOTE By using the inverse relationship _IfcBuildingStorey.IsDecomposedBy_ it references _IfcBuildingStorey_ || _IfcSpace_ through _IfcRelAggregates.RelatedObjects_. If it refers to another instance _of IfcBuildingStorey_, the referenced _IfcBuildingStorey_ needs to have a different and lower _CompositionType_, i.e. _ELEMENT_ (if the other _IfcBuildingStorey_ has _COMPLEX_), or _PARTIAL_ (if the other IfcBuildingStorey has _ELEMENT_).

> NOTE Multi storey spaces shall be spatially contained by only a single building storey, usually it is the building storey where the base of the space lies.

### Storey Attributes
