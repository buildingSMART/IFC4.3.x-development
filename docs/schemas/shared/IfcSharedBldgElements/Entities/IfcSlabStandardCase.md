# IfcSlabStandardCase

The standard slab, _IfcSlabStandardCase_, defines a slab with certain constraints for the provision of material usage, parameters and with certain constraints for the geometric representation. The _IfcSlabStandardCase_ handles all cases of slabs, that:

* have a reference to the _IfcMaterialLayerSetUsage_ defining the material layers of the slab with thicknesses
* are based on an extrusion of a planar surface as defined by the slab profile
* have a constant thickness along the extrusion direction
* are consistent in using the correct material layer set offset to the base planar surface in regard to the shape representation
* are extruded either perpendicular or slanted to the plane surface

The definitions of slab openings and niches are the same as given at the supertype _IfcSlab_. The same agreements to the special types of slabs, as defined in the _PredefinedType_ attribute apply as well.

> NOTE&nbsp; If the _IfcSlabStandardCase_ is of type Landing and is used within an _IfcStair_ or _IfcRamp_, the special agreements to handle stair and ramp geometry will also affect the geometric representation of the _IfcSlabStandardCase_.

> HISTORY&nbsp; New entity in IFC4.

## Formal Propositions

### HasMaterialLayerSetusage
A valid instance of _IfcSlabStandardCase_ relies on the provision of an _IfcMaterialLayerSetUsage_.

## Concepts

### Body Clipping Geometry

The following constraints apply to the 'Clipping'
representation:


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

> EXAMPLE  Figure 271 illustrates a 'Clipping' geometric representation with definition of a roof slab using advanced geometric representation. The profile is extruded non-perpendicular and the slab body is clipped at the eave.


Figure 271 — Slab body clipping


 



### Body SweptSolid Geometry

The following additional constraints apply to the swept solid
representation:


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

> EXAMPLE  Figure 270 illustrates a 'SweptSolid' geometric representation. The following interpretation of dimension parameter applies for polygonal slabs (in ground floor view):
>  IfcArbitraryClosedProfileDef.OuterCurve: closed bounded curve interpreted as area (or foot print) of the slab.


Figure 270 — Slab body extrusion


 


### Material Layer Set Usage


Multi-layer slabs can be represented by refering to several
IfcMaterialLayer's within the IfcMaterialLayerSet
that is referenced from the
IfcMaterialLayerSetUsage. 


Material information can also be given at the
IfcSlabType, defining the common attribute data for all
occurrences of the same type. It is then accessible by the 
inverse IsDefinedBy relationship pointing to
IfcSlabType.HasAssociations and via
IfcRelAssociatesMaterial.RelatingMaterial. The IfcSlabStandardCase defines in addition that the
IfcSlabType should have a unique IfcMaterialLayerSet,
that is referenced by the IfcMaterialLayerSetUsage
assigned to all occurrences of this IfcSlabType.


 


![Material layer set and usage](../../../../figures/ifcslab_materialusage-01.png)

> EXAMPLE  Figure 269 illustrates assignment of IfcMaterialLayerSetUsage and IfcMaterialLayerSet to the IfcSlabStandardCase as the slab occurrence and to the IfcSlabType. The same IfcMaterialLayerSet shall be shared by many occurrences of IfcMaterialLayerSetUsage. This relationship shall be consistent to the relationship between the IfcSlabType and the IfcSlabStandardCase.


Figure 269 — Slab type definition


 


Figure 270 illustrates slab material usage, where the following conventions shall be met:


* The reference coordinate system is the coordinate system established by the IfcExtrudedAreaSolid.Position.
* The reference plane is the plane defined by the extruded profile of IfcExtrudedAreaSolid.SweptSolid. The IfcMaterialLayerSetUsage.OffsetFromReferenceLine is given as a distance from this plane.
* The IfcMaterialLayerSetUsage.DirectionSense defines how the IfcMaterialLayer's are assigned to the reference plane. POSITIVE means in direction to the positive z-axis of the reference coordinate system.
* The IfcMaterialLayerSetUsage.OffsetFromReferenceLine is the distance parallel to the reference plane and always perpendicular to the base (XY) plane of the reference coordinate system. This is independent of a potential non-perpendicular extrusion given by IfcExtrudedAreaSolid.ExtrudedDirection <> 0.,0.,1. A positive value of IfcMaterialLayerSetUsage.OffsetFromReferenceLine would then point into the positive z-axis of the reference coordinate system.
* The Thickness of each IfcMaterialLayer shall be the parallel distance (measured perpendicular to the base plane). The TotalThickness of the IfcMaterialLayerSet is the sum of all layer thicknesses and in case of a perpendicular extrusion identical with IfcExtrudedAreaSolid.Depth
* The IfcMaterialLayerSetUsage.LayerSetDirection is always AXIS3.


![slab material layer set](../../../../figures/ifcmateriallayersetusage_slab-01.png)
![roof slab material layer set](../../../../figures/ifcmateriallayersetusage_roofslab-01.png)
Figure 270 — Slab material layers



### Product Placement

The following restriction is imposed:


* The local placement shall provide the location and directions 
for the standard slab, the x/y plane is the plane for the 
profile, and the z-axis is the extrusion axis for the slab body.



