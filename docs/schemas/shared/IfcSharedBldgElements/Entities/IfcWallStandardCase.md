# IfcWallStandardCase

The _IfcWallStandardCase_ defines a wall with certain constraints for the provision of parameters and with certain constraints for the geometric representation. The _IfcWallStandardCase_ handles all cases of walls, that are extruded vertically:

* along the positive z axis of the wall object coordinate system, and
* along the positive z axis of the global (world) coordinate system

and have a single thickness along the path for each wall layer, i.e.:

* parallel sides for straight walls
* co-centric sides for curved walls.

and have either:

* a straight line axis (straight wall), or
* a circular arc axis (round wall).

and shall not have:

* aggregated components, that is, parts aggregated to a wall by _IfcRelAggregates_
* shape representation for 'Body' not being an extrusion, or clipped extrusion

<!-- end of short definition -->

The following parameter have to be provided:

* Wall height, taken from the depth of extrusion, provided by the geometric representation.
* Wall thickness, taken from the material layer set usage, attached to the wall
* Wall offset from axis, taken from the material layer set usage, attached to the wall

The _IfcWallStandardCase_ requires the provision of the wall axis either a straight line that is parallel to the x-axis of the object coordinate system, or a circular arc where the tangent at start is parallel to the x-axis of the object coordinate system. The direction of the wall axis shall be the positive direction of that x-axis.

The material of the wall is defined by the _IfcMaterialLayerSetUsage_ and is attached by the _IfcRelAssociatesMaterial_ objectified relationship. It is accessible by the inverse _HasAssociations_ relationship. The material layer set usage has to be given (enforced by where rule).

An 'Axis' and a 'Body' shape representation has to be provided, and it is invalid to exchange a 'Tessellation', 'SurfaceModel', 'Brep' or 'MappedRepresentation' representation for the 'Body' shape representation of the _IfcWallStandardCase_.

> HISTORY New entity in IFC2x.

## Formal Propositions

### HasMaterialLayerSetUsage
A valid instance of _IfcWallStandardCase_ relies on the provision of an _IfcMaterialLayerSetUsage_.

## Concepts

### Axis 2D Geometry

The wall axis is represented by a two-dimensional open curve
within a particular shape representation. The wall axis is used to
apply the material layer set usage parameter to the wall geometry.



* Axis
	+ _IfcPolyline_ having two _Points_, or
	_IfcTrimmedCurve_ with _BasisCurve_ of _Type_
	_IfcLine_ for the 'SweptSolid' provided as
	_IfcExtrudedAreaSolid_. The axis curve lies on the x/y plane and is parallel to the x-axis of
	 the object coordinate system.
	+ _IfcTrimmedCurve_ with _BasisCurve_ of _Type_
	_IfcCircle_ for 'SweptSolid' provided as
	 _IfcExtrudedAreaSolid_. The axis curve lies on the x/y plane
	 of the object coordinate system, the tangent at the start is along
	the positive x-axis.


 


![straight wall axis](../../../../figures/ifcwallstandard_straigthwall_01-layout1.gif)

> EXAMPLE  Figure 289 illustrates an axis representation for a straight wall. In case of a straight wall, the set of items shall
> include a single geometric representation item of type _IfcPolyline_ or _IfcTrimmedCurve_ with the _BasisCurve_ being an _IfcLine_. The _IfcPolyline_ or _IfcTrimmedCurve_ shall be parallel (here in a special case co-linear) to the x-axis
> of the object coordinate system. The direction shall be identical to the direction of the x-axis.


Figure 289 — Wall axis straight

![curved wall axis](../../../../figures/ifcwallstandard_curvedwall_01-layout1.gif)

> EXAMPLE  Figure 290 illustrates an axis representation for a curved wall. In case of a curved wall, the set of items shall include
> a single geometric representation item of type _IfcTrimmedCurve_. The curve shall have a _BasisCurve_ of type _IfcCircle_. The tangent of the _IfcTrimmedCurve_ shall be parallel at start to the x-axis of the object coordinate system. The direction shall be identical to the direction of the x-axis.


Figure 290 — Wall axis curved


 



### Body Clipping Geometry

The following constraints apply to the 'Clipping'
representation:


* Solid: see standard geometric representation
* Profile: see standard geometric representation
* Extrusion: see standard geometric representation
* Boolean result: The _IfcBooleanClippingResult_
shall be supported, allowing for Boolean differences between the
swept solid (here _IfcExtrudedAreaSolid_) and one or several
_IfcHalfSpaceSolid_ (or subtypes).


Figure 293 illustrates a clipping for a straight wall using an _IfcPolygonalBoundedHalfSpace_ as _SecondOperand_ in
the _IfcBooleanClippingResult_.


Figure 294 illustrates a clipping for a curved wall using an _IfcHalfSpaceSolid_ as _SecondOperand_ in the
_IfcBooleanClippingResult_.


![straight wall clipping](../../../../figures/ifcwallstandard_straigthwall_03-layout1.gif)
![curved wall clipping](../../../../figures/ifcwallstandard_curvedwall_03-layout1.gif)
Figure 293 — Wall body clipping straight


Figure 294 — Wall body clipping curved



### Body SweptSolid Geometry

The following additional constraints apply to the 'SweptSolid'
representation:


* Solid: _IfcExtrudedAreaSolid_ is required,
* Profile: _IfcArbitraryClosedProfileDef_ and
_IfcRectangleProfileDef_ shall be supported.
* Extrusion: The profile shall be extruded vertically,
i.e., in the direction of the z-axis of the co-ordinate system of
the referred spatial structure element. It might be further
constraint to be in the direction of the global z-axis in
implementers agreements. The extrusion axis shall be perpendicular
to the swept profile, i.e. pointing into the direction of the
z-axis of the _Position_ of the _IfcExtrudedAreaSolid_.


The profile of a wall is described in the ground view and extruded vertically. The profile (also identical with the foot print of the wall) is defined by the _IfcArbitraryClosedProfileDef_ (excluding its subtypes). The profile is given with all wall connections already resolved.


Figure 291 illustrates a body representation for a straight wall. In case of a straight wall, the two sides of the profile shall be parallel to the wall axis, that is, the wall has a single unchanged thickness.


Figure 292 illustrates a body representation for a curved wall. In case of a curved wall, the two sides of the profile shall be parallel (with defined offset) to the wall axis, that is, the wall has a single unchanged thickness.


![straight wall body](../../../../figures/ifcwallstandard_straigthwall_02-layout1.gif)

Figure 291 — Wall body extrusion straight

![curved wall body](../../../../figures/ifcwallstandard_curvedwall_02-layout1.gif)

Figure 292 — Wall body extrusion curved

### Material Layer Set Usage


Multi-layer walls can be represented by referring to several
_IfcMaterialLayer_'s within the _IfcMaterialLayerSet_
that is referenced from the
_IfcMaterialLayerSetUsage_.


Material information can also be given at the
_IfcWallType_, defining the common attribute data for all
occurrences of the same type. It is then accessible by the
inverse _IsDefinedBy_ relationship pointing to
_IfcSlabType.HasAssociations_ and via
_IfcRelAssociatesMaterial.RelatingMaterial_.

 The _IfcWallType_ should then have a unique
 _IfcMaterialLayerSet_, that is referenced by
the _IfcMaterialLayerSetUsage_ assigned to all
occurrences of this _IfcWallType_.



![Material layer set and usage](../../../../figures/ifcwallstandardcase_materialusage-01.png)

Figure 287 — Wall Standard Object Typing


> EXAMPLE  Figure 287 illustrates assignment of _IfcMaterialLayerSetUsage_ and _IfcMaterialLayerSet_ to the wall type and the wall occurrence.

Figure 288 illustrates material layer usage, where the following conventions shall be met:


* The reference coordinate system is the local coordinate system established by the _ObjectPlacement_ of the _IfcWallStandardCase_.
* The reference axis is the axis defined by the _IfcShapeRepresentation_ with _RepresentationType_='Axis' as one of the
_Representation.Representations_ of the _IfcWallStandardCase_.
* The _IfcMaterialLayerSetUsage.OffsetFromReferenceLine_ is given as a distance from this axis.
* The _IfcMaterialLayerSetUsage.OffsetFromReferenceLine_ is the distance parallel to the reference axis and always within the base
(XY) plane of the reference coordinate system. A positive value of _IfcMaterialLayerSetUsage.OffsetFromReferenceLine_ would
then point into the positive y-axis of the reference coordinate system.
* The _IfcMaterialLayerSetUsage.DirectionSense_ defines how the _IfcMaterialLayer_'s are assigned to the reference axis. POSITIVE means in direction to the positive y-axis of the reference coordinate system.
* The _Thickness_ of each _IfcMaterialLayer_ is provided starting from the _OffsetFromReferenceLine_ and in the direction given by _DirectionSense_. It is applied without any gap or overlap between two consecutive layers. The _TotalThickness_ of the _IfcMaterialLayerSet_ is the sum of all layer thicknesses.
* The _IfcMaterialLayerSetUsage.LayerSetDirection_ is always AXIS2.


![wall material layer set](../../../../figures/ifcmateriallayersetusage_wall-01.png)

Figure 288 — Wall material layers



### Product Placement

The following restriction is imposed:


* The local placement shall provide the location and directions
for the standard wall, the x/y plane is the plane for the
profile, and the z-axis is the extrusion axis for the wall body.




