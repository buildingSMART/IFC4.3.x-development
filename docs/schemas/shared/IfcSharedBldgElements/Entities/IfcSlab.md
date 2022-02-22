# IfcSlab

A slab is a component of the construction that may enclose a space vertically. The slab may provide the lower support (floor) or upper construction (roof slab) in any space in a building.

> NOTE  Definition according to ISO 6707-1  
> thick, flat or shaped component, usually larger than 300 mm square, used to form a covering or projecting from a building.

Only the core or constructional part of this construction is considered to be a slab. The upper finish (flooring, roofing) and the lower finish (ceiling, suspended ceiling) are considered to be coverings. A special type of slab is the landing, described as a floor section to which one or more stair flights or ramp flights connect.

> NOTE  An arbitrary planar element to which this semantic information is not applicable or irrelevant shall be modeled as _IfcPlate_.

A slab may have openings, such as floor openings, or recesses. They are defined by an _IfcOpeningElement_ attached to the slab using the inverse relationship _HasOpenings_ pointing to _IfcRelVoidsElement_.

> NOTE  Slabs with openings that have already been modeled within the enclosing geometry may use the relationship _IfcRelConnectsElements_ to associate the wall with embedded elements such as trap doors.

There are two main representations for slab occurrences:

- _IfcSlab_ with _IfcMaterialLayerSetUsage_ is used for all occurrences of slabs, that are prismatic and where the thickness parameter can be fully described by the _IfcMaterialLayerSetUsage_. These slabs are always represented geometrically by a 'SweptSolid' geometry (or by a 'Clipping' geometry based on 'SweptSolid'), if a 3D geometric representation is assigned.

- _IfcSlab_ without _IfcMaterialLayerSetUsage_ is used for all other occurrences of slabs, particularly for slabs with changing thickness, or slabs with non planar surfaces, and slabs having only 'SweptSolid' or 'Brep' geometry, or if a more parametric representation is not intended.

> NOTE The entity _IfcSlabStandardCase_ has been deprecated, _IfcSlab_ with _IfcMaterialLayerSetUsage_ is used instead. The entity _IfcSlabElementedCase_ has been deprecated, _IfcSlab_ with _IfcRelAggregates_ is used to describe occurrences of slabs which are aggregated from subordinate elements.

> NOTE There is a representation of slabs for structural analysis provided by a proper subtype of _IfcStructuralMember_ being part of the _IfcStructuralAnalysisModel_.

> HISTORY  New entity in IFC2.0; it is a merger of the two previous entities IfcFloor, IfcRoofSlab, introduced in IFC1.0

## Attributes

### PredefinedType
Predefined generic type for a slab that is specified in an enumeration. There may be a property set given specifically for the predefined types.
> NOTE  The _PredefinedType_ shall only be used, if no _IfcSlabType_ is assigned, providing its own _IfcSlabType.PredefinedType_.

{ .change-ifc2x}
> IFC2x CHANGE The attribute has been changed into an OPTIONAL attribute.

## Formal Propositions

### CorrectPredefinedType
Either the _PredefinedType_ attribute is unset (e.g. because an _IfcSlabType_ is associated), or the inherited attribute _ObjectType_ shall be provided, if the _PredefinedType_ is set to USERDEFINED.

### CorrectTypeAssigned
Either there is no slab type object associated, i.e. the _IsTypedBy_ inverse relationship is not provided, or the associated type object has to be of type _IfcSlabType_.

## Concepts

### Body Clipping Geometry

The following constraints apply to the 'Clipping'
representation:


* Solid: see 'SweptSolid' shape representation,
* Profile: see 'SweptSolid' shape representation,
* Extrusion: see 'SweptSolid' shape representation,
* Boolean result: The IfcBooleanClippingResult
shall be supported, allowing for Boolean differences between the
swept solid (here IfcExtrudedAreaSolid) and one or several
IfcHalfSpaceSolid.


Figure 266 illustrates a 'Clipping' geometric representation with definition of a roof slab using advanced
geometric representation. The profile is extruded non-perpendicular and the slab body is clipped at the eave.


![advanced slab](../../../../figures/ifcslab_advanced-layout1.gif)
Figure 266 — Slab body clipping


The following constraints apply to the 'Clipping'
representation, when an IfcMaterialLayerSetUsage is assigned to the IfcSlab:


* Solid: see 'SweptSolid' shape representation,
* Profile: see 'SweptSolid' shape
representation,
* Extrusion: see 'SweptSolid' shape
representation,
* Material: see 'SweptSolid' shape
representation,
* Boolean result: The IfcBooleanClippingResult
 shall be supported, allowing for Boolean differences between the
swept solid (here IfcExtrudedAreaSolid) and one or several
IfcHalfSpaceSolid.


 


![advanced slab](../../../../figures/ifcslab_advanced-layout1.gif)

> EXAMPLE  Figure 267 illustrates a 'Clipping' geometric representation with definition of a roof slab using advanced geometric representation. The profile is extruded non-perpendicular and the slab body is clipped at the eave.


Figure 267 — Slab body clipping


 



### Body SweptSolid Geometry

The following constraints apply to the 'SweptSolid'
representation:


* Solid: IfcExtrudedAreaSolid is required,
* Profile: IfcArbitraryClosedProfileDef,
IfcRectangleProfileDef, IfcCircleProfileDef ,
IfcEllipseProfileDef shall be supported.
* Extrusion: The profile can be extruded perpendicularly
or non-perpendicularly to the plane of the swept profile.


Figure 264 illustrates a 'SweptSolid' geometric representation.



> NOTE  The following interpretation of dimension parameter applies for polygonal slabs (in ground floor view):
> * IfcArbitraryClosedProfileDef.OuterCurve: closed bounded curve interpreted as area (or foot print) of the slab.
>
>
>


![standard slab](../../../../figures/ifcslab_standard-layout1.gif)
Figure 264 — Slab body extrusion


The following additional constraints apply to the 'SweptSolid'
representation, when an IfcMaterialLayerSetUsage is assigned to the IfcSlab:


* Solid: IfcExtrudedAreaSolid is required,
* Profile: IfcArbitraryClosedProfileDef,
IfcRectangleProfileDef, IfcCircleProfileDef,
IfcEllipseProfileDef shall be supported.
* Extrusion: The profile can be extruded perpendicularly
or non-perpendicularly to the plane of the swept profile.
* Material: The definition of the
 IfcMaterialLayerSetUsage, particularly of the
OffsetFromReferenceLine and the
ForLayerSet.TotalThickness, has to be consistent to the
'SweptSolid' representation.


 


![standard slab](../../../../figures/ifcslab_standard-layout1.gif)

> EXAMPLE  Figure 265 illustrates a 'SweptSolid' geometric representation. The following interpretation of dimension parameter applies for polygonal slabs (in ground floor view):
>  IfcArbitraryClosedProfileDef.OuterCurve: closed bounded curve interpreted as area (or foot print) of the slab.


Figure 265 — Slab body extrusion


 



### Material Layer Set

The material information of the IfcSlab is defined by
 IfcMaterialLayerSet, or as fallback by IfcMaterial, and it is attached either directly or at the IfcSlabType. In this case, the material information does not allow to construct a shape by applying the layer definition to the plane of the shape representation, to enable this parametric definition, the IfcMaterialLayerSetUsage has to be used instead.



### Material Layer Set Usage

The material of IfcSlab can be defined by
IfcMaterialLayerSetUsage and attached by
IfcRelAssociatesMaterial.RelatingMaterial. It is
 accessible by the inverse HasAssociations relationship.
 Multi-layer slabs can be represented by refering to several
IfcMaterialLayer's within the IfcMaterialLayerSet
that is referenced from th e
IfcMaterialLayerSetUsage.


When assigning an
IfcMaterialLayerSetUsage to IfcSlab it shall imply that the
 IfcSlabType should have a unique
 IfcMaterialLayerSet, that is referenced by IfcMaterialLayerSetUsage assigned to all
occurrences of this IfcSlabType.


![Material layer set and usage](../../../../figures/ifcslab_materialusage-01.png)

> EXAMPLE  Figure 262 illustrates assignment of IfcMaterialLayerSetUsage and IfcMaterialLayerSet to the IfcSlab as the slab occurrence and to the IfcSlabType. The same IfcMaterialLayerSet shall be shared by many occurrences of IfcMaterialLayerSetUsage. This relationship shall be consistent to the relationship between the IfcSlabType and the IfcSlabStandardCase.


Figure 262 — Slab type definition


 


Figure 263 illustrates slab material usage, where the following conventions shall be met:


* The reference coordinate system is the coordinate system established by the IfcExtrudedAreaSolid.Position.
* The reference plane is the plane defined by the extruded profile of IfcExtrudedAreaSolid.SweptSolid. The IfcMaterialLayerSetUsage.OffsetFromReferenceLine is given as a distance from this plane.
* The IfcMaterialLayerSetUsage.DirectionSense defines how the IfcMaterialLayer's are assigned to the reference plane. POSITIVE means in direction to the positive z-axis of the reference coordinate system.
* The IfcMaterialLayerSetUsage.OffsetFromReferenceLine is the distance parallel to the reference plane and always perpendicular to the base (XY) plane of the reference coordinate system. This is independent of a potential non-perpendicular extrusion given by IfcExtrudedAreaSolid.ExtrudedDirection <> 0.,0.,1. A positive value of IfcMaterialLayerSetUsage.OffsetFromReferenceLine would then point into the positive z-axis of the reference coordinate system.
* The Thickness of each IfcMaterialLayer shall be the parallel distance (measured perpendicular to the base plane). The TotalThickness of the IfcMaterialLayerSet is the sum of all layer thicknesses and in case of a perpendicular extrusion identical with IfcExtrudedAreaSolid.Depth
* The IfcMaterialLayerSetUsage.LayerSetDirection is always AXIS3.


![slab material layer set](../../../../figures/ifcmateriallayersetusage_slab-01.png)
![roof slab material layer set](../../../../figures/ifcmateriallayersetusage_roofslab-01.png)
Figure 263 — Slab material layers



### Object Typing


### Property Sets for Objects


### Quantity Sets


### Spatial Containment

The IfcSlab, as any subtype of IfcBuildingElement,
may participate alternatively in one of the two different containment relationships:


* the Spatial Containment (defined here), or
* the Element Composition.

### Surface Geometry


> NOTE  The 'Surface' can be used to define a
> surfacic model of the building (e.g. for analytical purposes, or
> for reduced Level of Detail representation).
