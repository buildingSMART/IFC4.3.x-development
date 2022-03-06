# IfcBeam

An _IfcBeam_ is typically a horizontal, or nearly horizontal, structural member that is capable of withstanding load primarily by resisting bending. It may also represent such a member from an architectural point of view. It is not required to be load bearing.

There are two main representations for beam occurrences:

 * _IfcBeam_ with _IfcMaterialProfileSetUsage_ is used for all occurrences of beams, that have a profile defined that is swept along a directrix. The profile might change uniformly by a taper definition along the directrix. The profile parameter and its cardinal point of insertion can be fully described by the _IfcMaterialProfileSetUsage_. These beams are always represented geometricly by an 'Axis' and a 'SweptSolid' or 'AdvancedSweptSolid' shape representation (or by a 'Clipping' geometry based on the swept solid), if a 3D geometric representation is assigned.
 * _IfcBeam_ without _IfcMaterialProfileSetUsage_ is used for all other occurrences of beams, particularly for beams with non-uniformly changing profile sizes along the sweep, or beams having only 'AdvancedBrep', 'Brep', or 'SurfaceModel' geometry, if a more parametric representation is not intended.

For any other longitudinal structural member, not constrained to be predominately horizontal nor vertical, or where this semantic information is irrelevant, the entity _IfcMember_ should be used.

> REFERENCE  Definition according to ISO 6707-1: structural member for carrying load(s) between or beyond points of support, usually narrow in relation to its length and horizontal or nearly so.

> NOTE  The entity IfcBeamStandardCase has been deprecated, IfcBeam with IfcMaterialProfileSetUsage is used instead.

> NOTE  The representation of load-bearing beams in a structural analysis model is provided by subtypes of _IfcStructuralMember_ (with _IfcStructuralCurveMember_ being mostly applicable) as part of an _IfcStructuralAnalysisModel_. The camber of a beam may be defined by assigning an _IfcStructuralCurveMember_ with displacement coordinates. Multiple sets of camber ordinates may be provided that are qualified by the particular load case, where full dead load would typically be used for fabrication, and other scenarios used for other loading conditions such as during construction.

> HISTORY  New entity in IFC1.0

## Attributes

### PredefinedType
Predefined generic type for a beam that is specified in an enumeration. There may be a property set given specifically for the predefined types.
> NOTE  The _PredefinedType_ shall only be used, if no _IfcBeamType_ is assigned, providing its own _IfcBeamType.PredefinedType_.

{ .change-ifc2x4}
> IFC4 CHANGE The attribute has been added at the end of the entity definition.

## Formal Propositions

### CorrectPredefinedType
Either the _PredefinedType_ attribute is unset (e.g. because an _IfcBeamType_ is associated), or the inherited attribute _ObjectType_ shall be provided, if the _PredefinedType_ is set to USERDEFINED.

### CorrectTypeAssigned
Either there is no beam type object associated, i.e. the _IsTypedBy_ inverse relationship is not provided, or the associated type object has to be of type _IfcBeamType_.

## Concepts

### Axis 3D Geometry

The axis representation can be used to represent the fundamental orientation and extents of a beams's body.

If an _IfcMaterialProfileSetUsage_ is used, the axis representation is used to locate the profile. In addition:

 * For a body representation using an _IfcExtrudedAreaSolid_, the axis may be an _IfcPolyline_ having two Points, or _IfcTrimmedCurve_ with BasisCurve of type _IfcLine_. The axis curve lies on the z axis of the object coordinate system.
 * For a body representation using an _IfcRevolvedAreaSolid_, the axis may be an _IfcTrimmedCurve_ with BasisCurve of type _IfcCircle_. The axis curve lies on the x/z plane of the object coordinate system, the tangent at the start is along the positive z-axis.

As shown in Figure 76, the axis shall be defined along the z axis of the object coordinate system.

![Axis](../../../../figures/ifcbeamstandardcase_axis-01.png)

Figure 76 — Beam axis representation

As shown in Figure 77, the axis representation must be positioned at the _IfcMaterialProfileSetUsage_.CardinalPoint, and parallel to the _IfcExtrudedAreaSolid_.ExtrudedDirection. This offset between the axis line and the _IfcExtrudedAreaSolid_.Position must correlate with the chosen _IfcMaterialProfileSetUsage_.CardinalPoint.

![Axis](../../../../figures/ifcbeamstandardcase_axis-02.png)

Figure 77 — Beam axis cardinal point

#### Axis_IfcBoundedCurve_Curve3D

Three-dimensional reference curve for the beam.

### Body AdvancedSweptSolid Geometry

* IfcSurfaceCurveSweptAreaSolid, IfcFixedReferenceSweptAreaSolid, IfcExtrudedAreaSolidTapered, IfcRevolvedAreaSolidTapered shall be supported.
* All subtypes of IfcProfileDef (with exception of IfcArbitraryOpenProfileDef)

### Body Clipping Geometry

* IfcExtrudedAreaSolid, IfcRevolvedAreaSolid shall be supported
* All subtypes of IfcProfileDef (with exception of IfcArbitraryOpenProfileDef)
* All extrusion directions shall be supported.
* The IfcBooleanClippingResult shall be supported, allowing for Boolean differences between the swept solid (here IfcExtrudedAreaSolid) and one or several IfcHalfSpaceSolid (or its subtypes).

Figure 201 illustrates use of IfcBooleanClippingResult between an IfcExtrudedAreaSolid and an IfcHalfSpaceSolid to create a clipped body.

![clipped beam](../../../../figures/ifcbeam_advanced-2-layout1.gif)
Figure 201 — Beam clipping

### Body SweptSolid Geometry

 * IfcExtrudedAreaSolid, IfcRevolvedAreaSolid shall be supported
 * All subtypes of IfcProfileDef
 * All extrusion directions shall be supported.
 * For all single profiles, the IfcParameterizedProfileDef.Position shall be NIL, or having Location = 0.,0. and RefDirection = 1.,0.
 * Orientation: The y-axis of the profile, as determined by IfcSweptAreaSolid.Position.P[2] shall point upwards. It indicates the "role" of the beam, a role=0° means y-axis of profile pointing upwards.

Figure 200 illustrates the 'SweptSolid' geometric representation. There are no restrictions or conventions on how to use the local placement (black), solid of extrusion placement (red) and profile placement (green).

![standard beam](../../../../figures/ifcbeam_standard-layout1.gif)

Figure 200 — Beam swept solid

Figure 201 illustrates the use of non-perpendicular extrusion to create the IfcExtrudedAreaSolid.

![non-perpendicular extrusion](../../../../figures/ifcbeam_advanced-1-layout1.gif)

Figure 201 — Beam non-perpendicular extrusion

If parametric profiles are used, the parameters may be interpreted to be the dimensions of the beam:

* IfcRectangleProfileDef.YDim interpreted as beam height
* IfcRectangleProfileDef.XDim interpreted as beam width
* IfcCircleProfileDef.Radius interpreted as beam radius.

![standard beam](../../../../figures/ifcbeamstandardcase_sweptsolid-01.png)

Figure 207 — Beam body extrusion using an IfcRectangleProfileDef

### Element Composition

#### IfcElementAssembly

Special purpose composite entity

#### IfcBuildingElement

Any building element can be a composite

### Material Profile Set

The material information of the IfcBeam is defined by
IfcMaterialProfileSet or as fallback by IfcMaterial, and it is attached either directly or at the IfcBeamType. In this case, the material information does not allow to construct a shape by applying the profile definition to the axis representation, to enable this parametric definition, the IfcMaterialProfileSetUsage has to be used instead.

### Material Profile Set Usage

The Material Profile Set Usage defines the assignment of an IfcMaterialProfileSetUsage to the
IfcBeamType providing a common profile definition to all
 occurrences of this IfcBeamType. Beams with composite profile can be represented by referring to
 several IfcMaterialProfile's within the
IfcMaterialProfileSet that is referenced from the
IfcMaterialProfileSetUsage.


![Material profile set and usage](../../../../figures/ifcbeam-01.png)

Figure 196 — Beam profile usage

> EXAMPLE  Figure 196 illustrates assignment of IfcMaterialProfileSetUsage and IfcMaterialProfileSet to the IfcBeam as the beam occurrence and to the IfcBeamType. The same IfcMaterialProfileSet shall be shared by many occurrences of IfcMaterialProfileSetUsage. This relationship shall be consistent to the relationship between the IfcBeamType and the IfcBeam.



![Cardinal point usage](../../../../figures/ifcbeam_cardinalpoint.png)

Figure 197 — Beam cardinal points

Figure 197 illustrates alignment of cardinal points. It has to be guaranteed that the use of IfcCardinalPointEnum is consistent to the placement of the extrusion body provided by IfcExtrudedAreaSolid.Position

The cardinal points 8 (top centre) and 6 (mid-depth right) are assigned according to the definition at IfcCardinalPointReference


![Material profile set and usage](../../../../figures/ifcbeam-02.png)

Figure 198 — Beam composite profiles

Figure 198 illustrates assignment of a composite profile by using IfcCompositeProfile for geometric representation and several IfcMaterialProfile's within the IfcMaterialProfileSet.

### Object Typing

### Product Assignment

#### IfcStructuralCurveMember

An idealized structural member corresponding to the beam.

### Property Sets for Objects

### Quantity Sets

### Spatial Containment

The IfcBeam, as any subtype of IfcBuildingElement, may participate alternatively in one of the two different containment relationships:

* the _Spatial Containment_ (defined here), or
* the _Element Composition_.

#### IfcBuildingStorey

Default spatial container

#### IfcBuilding

Spatial container for the element if it cannot be assigned to a building storey

#### IfcSite

Spatial container for the element in case that it is placed on site (outside of building)
