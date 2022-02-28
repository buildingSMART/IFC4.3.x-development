# IfcColumn

An _IfcColumn_ is a vertical structural member which often is aligned with a structural grid intersection. It represents a vertical, or nearly vertical, structural member that transmits, through compression, the weight of the structure above to other structural elements below. It represents such a member from an architectural point of view. It is not required to be load bearing.

> NOTE  Definition according to ISO 6707-1
> structural member of slender form, usually vertical, that transmits to its base the forces, primarily in compression, that are applied to it.

There are two main representations for column occurrences:

- _IfcColumn_ with _IfcMaterialProfileSetUsage_ is used for all occurrences of columns, that have a profile defined that is swept along a directrix. The profile might be changed uniformly by a taper definition along the directrix. The profile parameter and its cardinal point of insertion can be fully described by the _IfcMaterialProfileSetUsag_e. These columns are always represented geometricly by an 'Axis' and a 'SweptSolid' or 'AdvancedSweptSolid' shape representation (or by a 'Clipping' geometry based on the swept solid), if a 3D geometric representation is assigned.

- _IfcColumn_ is used for all other occurrences of columns, particularly for columns with changing profile sizes along the extrusion, or columns defined by non-linear extrusion, or columns having only 'Brep', or 'SurfaceModel' geometry, or if a more parametric representation is not intended.

> NOTE  The entity IfcColumnStandardCase has been deprecated, IfcColumn with IfcMaterialProfileSetUsage is used instead.

For any longitudial structural member, not constrained to be predominately horizontal nor vertical, or where this semantic information is irrelevant, the entity _IfcMember_ exists.

> NOTE  The representation of a column in a structural analysis model is provided by _IfcStructuralCurveMember_ being part of an _IfcStructuralAnalysisModel_.

> HISTORY  New entity in IFC1.0

## Attributes

### PredefinedType
Predefined generic type for a column that is specified in an enumeration. There may be a property set given specifically for the predefined types.
> NOTE  The _PredefinedType_ shall only be used, if no _IfcColumnType_ is assigned, providing its own _IfcColumnType.PredefinedType_.

{ .change-ifc2x4}
> IFC4 CHANGE The attribute has been added at the end of the entity definition.

## Formal Propositions

### CorrectPredefinedType
Either the _PredefinedType_ attribute is unset (e.g. because an _IfcColumnType_ is associated), or the inherited attribute _ObjectType_ shall be provided, if the _PredefinedType_ is set to USERDEFINED.

### CorrectTypeAssigned
Either there is no column type object associated, i.e. the _IsTypedBy_ inverse relationship is not provided, or the associated type object has to be of type _IfcColumnType_.

## Concepts

### Axis 3D Geometry

The axis representation can be used to represent the system length of a column that may extent the body length of the column.

> NOTE&nbsp; The 'Axis' is not used to locate the material profile set, only the subtype IfcColumnStandardCase provides this capability.

#### Axis_IfcBoundedCurve_Curve3D

Three-dimensional reference curve for the column.

### Body AdvancedSweptSolid Geometry

The following additional constraints apply to the 'AdvancedSweptSolid' representation type:

* **Solid**: IfcSurfaceCurveSweptAreaSolid, IfcFixedReferenceSweptAreaSolid, IfcExtrudedAreaSolidTapered, IfcRevolvedAreaSolidTapered shall be supported. 
>> NOTE&nbsp; View definitions and implementer agreements can further constrain the allowed swept solid types. 
* **Profile**: see 'SweptSolid' geometric representation
* **Extrusion**: not applicable

### Body Clipping Geometry

The following constraints apply to the 'Clipping' representation:

* **Solid**: see 'SweptSolid' geometric representation
* **Profile**: see 'SweptSolid' geometric representation
* **Extrusion**: see 'SweptSolid' geometric representation
* **Boolean result**: The IfcBooleanClippingResult shall be supported, allowing for Boolean differences between the swept solid (here IfcExtrudedAreaSolid) and one or several IfcHalfSpaceSolid.

Figure 1 illustrates a 'Clipping' geometric representation with use of IfcBooleanClippingResult between an IfcExtrudedAreaSolid and an IfcHalfSpaceSolid to create a clipped body.

!["advanced column"](../../../../figures/ifccolumn_advanced-2-layout1.png "Figure 1 &mdash; Column clipping")

### Body SweptSolid Geometry

The following additional constraints apply to the 'SweptSolid' representation:

* **Solid**: IfcExtrudedAreaSolid, IfcRevolvedAreaSolid shall be supported
* **Profile**: all subtypes of IfcProfileDef (with exception of IfcArbitraryOpenProfileDef) 
* **Extrusion**: All extrusion directions shall be supported

Figure 1 illustrates a 'SweptSolid' geometric representation. There are no restrictions or conventions on how to use the local placement (black), solid of extrusion placement (red) and profile placement (green).

!["standard column"](../../../../figures/ifccolumn_standard-layout1.gif "Figure 1 &mdash; Column swept solid")

Figure 2 illustrates use of a special profile type (here IfcIShapeProfileDef) for the definition of the IfcExtrudedAreaSolid.

!["advanced column"](../../../../figures/ifccolumn_advanced-1-layout1.png "Figure 2 &mdash; Column extrusion of I-Shape")

### Material Profile Set

The material of the IfcColumn is defined by the IfcMaterialProfileSet or as fallback by IfcMaterial, and it is attached either directly or at the IfcColumnType.

> NOTE&nbsp; It is illegal to assign an IfcMaterialProfileSetUsage to an IfcColumn. Only the subtype IfcColumnStandardCase supports this concept.

### Object Typing



### Product Assignment



#### IfcStructuralCurveMember

An idealized structural member corresponding to the column.

#### IfcTask

A task for operating on the column.

### Property Sets for Objects



### Quantity Sets



### Spatial Containment

The IfcColumn, as any subtype of IfcBuildingElement, may participate alternatively in one of the two different containment relationships:

* the _Spatial Containment_ (defined here), or
* the _Element Composition_.

#### IfcBuildingStorey

Default spatial container

#### IfcBuilding

Spatial container for the element if it cannot be assigned to a building storey

#### IfcSite

Spatial container for the element in case that it is placed on site (outside of building)

