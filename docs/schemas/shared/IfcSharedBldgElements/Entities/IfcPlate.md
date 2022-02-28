# IfcPlate

An _IfcPlate_ is a planar and often flat part with constant thickness. A plate may carry loads between or beyond points of support, or provide stiffening. The location of the plate (being horizontal, vertical or sloped) is not relevant to its definition (in contrary to _IfcWall_ and _IfcSlab_ (as floor slab)).

> NOTE  Definition according to ISO 6707-1: thin, rigid, flat, metal product, of a thickness greater than that of a sheet.

Plates are normally made of steel, other metallic material, or by glass panels. However the definition of _IfcPlate_ is material independent and specific material information shall be handled by using _IfcAssociatesMaterial_ to assign a material specification to the _IfcPlate_.

> NOTE  Although not necessarily, plates are often add-on parts. This is represented by the _IfcRelAggregates_ decomposition mechanism used to aggregate parts, such as _IfcPlate_, into a container element such as _IfcElementAssembly_ or _IfcCurtainWall_.

An instance of _IfcPlate_ should preferably get its geometric representation and material assignment through the type definition by _IfcPlateType_ assigned using the _IfcRelDefinesByType_ relationship. This allows identical plates in a construction to be represented by the same instance of _IfcPlateType_.

A plate may have openings, such as voids or recesses. They are defined by an _IfcOpeningElement_ attached to the plate using the inverse relationship _HasOpenings_ pointing to _IfcRelVoidsElement_. The position number of a plate as often used in steel construction is assigned through the attribute _IfcElement.Tag_

There are two main representations for plate occurrences:

- _IfcPlate_ with _IfcMaterialLayerSetUsage_ is used for all occurrences of plates, that are prismatic and where the thickness parameter can be fully described by the _IfcMaterialLayerSetUsage_. These plates are always represented geometrically by a 'SweptSolid' geometry (or by a 'Clipping' geometry based on 'SweptSolid'), if a 3D geometric representation is assigned.

- _IfcPlate_ without _IfcMaterialLayerSetUsage_ is used for all other occurrences of plates, particularly for plates with changing thickness, or plates with non planar surfaces, and plates having only 'SurfaceModel' or 'Brep' geometry or if a more parametric representation is not intended.

> NOTE  The representation of a plate in a structural analysis model is provided by _IfcStructuralSurfaceMember_ being part of an _IfcStructuralAnalysisModel_.

> HISTORY  New entity in IFC2x2


## Attributes

### PredefinedType
Predefined generic type for a plate that is specified in an enumeration. There may be a property set given specifically for the predefined types.
> NOTE  The _PredefinedType_ shall only be used, if no _IfcPlateType_ is assigned, providing its own _IfcPlateType.PredefinedType_.

{ .change-ifc2x4}
> IFC4 CHANGE The attribute has been added at the end of the entity definition.

## Formal Propositions

### CorrectPredefinedType
Either the _PredefinedType_ attribute is unset (e.g. because an _IfcPlateType_ is associated), or the inherited attribute _ObjectType_ shall be provided, if the _PredefinedType_ is set to USERDEFINED.

### CorrectTypeAssigned
Either there is no plate type object associated, i.e. the _IsTypedBy_ inverse relationship is not provided, or the associated type object has to be of type _IfcPlateType_.

## Concepts

### Body Clipping Geometry



### Body SweptSolid Geometry

The following additional constraints apply to the 'SweptSolid' representation:

* **Solid**: IfcExtrudedAreaSolid is required,
* **Profile**: _IfcArbitraryClosedProfileDef, IfcArbitraryProfileDefWithVoids, IfcRectangleProfileDef, IfcCircleProfileDef, IfcEllipseProfileDef_ shall be supported.
* **Extrusion**: The profile can be extruded perpendicularly or non-perpendicularly to the plane of the swept profile.

### Material Layer Set

The material of the IfcPlate is defined by IfcMaterialLayerSet, or by IfcMaterial, and it is attached either directly or at the IfcPlateType.

> NOTE&nbsp; It is illegal to assign an IfcMaterialLayerSetUsage to an IfcPlate. Only the subtype IfcPlateStandardCase supports this concept.

### Object Typing



### Product Assignment



#### IfcStructuralSurfaceMember

An idealized structural member corresponding to the plate.

#### IfcTask

A task for operating on the plate.

### Property Sets for Objects



### Quantity Sets



### Spatial Containment

The IfcPlate, as any subtype of IfcBuildingElement, may participate alternatively in one of the two different containment relationships:

* the _Spatial Containment_ (defined here), or
* the _Element Composition_.

#### IfcBuildingStorey

Default spatial container

#### IfcBuilding

Spatial container for the element if it cannot be assigned to a building storey

#### IfcSite

Spatial container for the element in case that it is placed on site (outside of building)

### Surface 3D Geometry

> NOTE&nbsp; The 'Surface' can be used to define a surfacic model of the building (e.g. for analytical purposes, or for reduced Level of Detail representation).

