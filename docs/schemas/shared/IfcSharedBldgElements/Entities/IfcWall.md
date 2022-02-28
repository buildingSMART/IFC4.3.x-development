# IfcWall

The wall represents a vertical construction that may bound or subdivide spaces. Wall are usually vertical, or nearly vertical, planar elements, often designed to bear structural loads. A wall is however not required to be load bearing.

{ .extDef}
> NOTE  Definition according to ISO 6707-1: vertical construction usually in masonry or in concrete which bounds or subdivides a construction works and fulfils a load bearing or retaining function.

> NOTE  An arbitrary planar element to which this semantic information is not applicable (is not predominantly vertical), shall be modeled as _IfcPlate_.

A wall may have openings, such as wall openings, openings used for windows or doors, or niches and recesses. They are defined by an _IfcOpeningElement_ attached to the wall using the inverse relationship _HasOpenings_ pointing to _IfcRelVoidsElement_.

> NOTE  Walls with openings that have already been modeled within the enclosing geometry may use the relationship _IfcRelConnectsElements_ to associate the wall with embedded elements such as doors and windows.

There are two main representations for all occurrences:

- _IfcWall_ with _IfcMaterialLayerSetUsage_ is used for all occurrences of walls, that have a non-changing thickness along the wall path and where the thickness parameter can be fully described by a material layer set. These walls are always represented geometrically by an 'Axis' and a 'SweptSolid' shape representation (or by a 'Clipping' geometry based on 'SweptSolid'), if a 3D geometric representation is assigned.

- _IfcWall_ without _IfcMaterialLayerSetUsage_ is used for all other occurrences of wall, particularly for walls with changing thickness along the wall path (e.g. polygonal walls), or walls with a non-rectangular cross sections (e.g. L-shaped retaining walls), and walls having an extrusion axis that is unequal to the global Z axis of the project (i.e. non-vertical walls), or walls having only 'Brep', or 'SurfaceModel' geometry, or if a more parametric representation is not intended.

> NOTE  The entity _IfcWallStandardCase_ has been deprecated, _IfcWall_ with _IfcMaterialLayerSetUsage_ is used instead. The entity _IfcWallElementedCase_ has been deprecated, _IfcWall_ with _IfcRelAggregates_ is used to describe occurrences of wall which are aggregated from subordinate elements, such as wall panels.

> NOTE  There is a representation of walls for structural analysis provided by a proper subtype of _IfcStructuralMember_ being part of the _IfcStructuralAnalysisModel_.

> HISTORY  New entity in IFC1.0

## Attributes

### PredefinedType
Predefined generic type for a wall that is specified in an enumeration. There may be a property set given specifically for the predefined types.
> NOTE  The _PredefinedType_ shall only be used, if no _IfcWallType_ is assigned, providing its own _IfcWallType.PredefinedType_.

{ .change-ifc2x4}
> IFC4 CHANGE The attribute has been added at the end of the entity definition.

## Formal Propositions

### CorrectPredefinedType
Either the _PredefinedType_ attribute is unset (e.g. because an _IfcWallType_ is associated), or the inherited attribute _ObjectType_ shall be provided, if the _PredefinedType_ is set to USERDEFINED.

### CorrectTypeAssigned
Either there is no wall type object associated, i.e. the _IsTypedBy_ inverse relationship is not provided, or the associated type object has to be of type _IfcWallType_.

## Concepts

### Axis 2D Geometry

> NOTE&nbsp; The 'Axis' is not used to locate the material layer set, only the subtype IfcWallStandardCase provides this capability.

#### Axis_IfcBoundedCurve_Curve2D

The wall axis of the wall.

### Body Clipping Geometry



### Body SweptSolid Geometry

The following additional constraints apply to the 'SweptSolid' representation:

* **Solid**: IfcExtrudedAreaSolid is required,
* **Profile**: IfcArbitraryClosedProfileDef is required.
* **Extrusion**: All extrusion directions shall be supported.

> NOTE&nbsp; If the wall body can be described by a vertical extrusion of a polygonal footprint with constant thickness along the axis (where vertical = into the direction of the global Z axis), the subtype IfcWallStandardCase should be used. If the extrusion is not equal to global Z, then the IfcWall should be used.

### Material Layer Set

The material of the IfcWall is defined by IfcMaterialLayerSet, or as fallback by IfcMaterial, and it is attached either directly or at the IfcWallType.

> NOTE&nbsp; It is illegal to assign an IfcMaterialLayerSetUsage to an IfcWall. Only the subtype IfcWallStandardCase supports this concept.

### Object Typing



### Path Connectivity



#### IfcWall

Walls with equal or lower priority are connected at RelatedElement.

### Product Assignment



#### IfcStructuralSurfaceMember

An idealized structural member corresponding to the wall.

#### IfcTask

A task for operating on the wall.

### Property Sets for Objects



### Quantity Sets



### Spatial Containment

The IfcWall, as any subtype of IfcBuildingElement, may participate alternatively in one of the two different containment relationships:

* the _Spatial Containment_ (defined here), or
* the _Element Composition_.

#### IfcBuildingStorey

Default spatial container

#### IfcBuilding

Spatial container for the element if it cannot be assigned to a building storey

#### IfcSite

Spatial container for the element in case that it is placed on site (outside of building)

### Surface Geometry

> NOTE&nbsp; The 'Surface' can be used to define a surfacic model of the building (e.g. for analytical purposes, or for reduced Level of Detail representation).

