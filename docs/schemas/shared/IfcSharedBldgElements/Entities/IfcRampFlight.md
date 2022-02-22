# IfcRampFlight

A ramp comprises a single inclined segment, or several inclined segments that are connected by a horizontal segment, refered to as a landing. A ramp flight is the single inclined segment and part of the ramp construction. In case of single flight ramps, the ramp flight and the ramp are identical.

> NOTE  A single flight ramp is represented by an _IfcRamp_ instance without using aggregation and by utilizing the product shape representation directly at _IfcRamp_.

An _IfcRampFlight_ is an aggregated part of an _IfcRamp_ realized through the _IfcRelAggregates_ relationship, the ramp flight is therefore included in the set of _IfcRelAggregates.RelatedObjects_.

An _IfcRampFlight_ connects the floor slab of zero to two different storeys (or partial storeys or landings) within a building. The connection relationship between the _IfcRampFlight_ and the _IfcSlab_ can be expressed using the _IfcRelConnectsElements_ relationship.

> HISTORY  New entity in IFC2.0.

## Attributes

### PredefinedType
Predefined generic type for a ramp flight that is specified in an enumeration. There may be a property set given specifically for the predefined types.
> NOTE  The _PredefinedType_ shall only be used, if no _IfcRampFlightType_ is assigned, providing its own _IfcRampFlightType.PredefinedType_.

{ .change-ifc2x4}
> IFC4 CHANGE The attribute has been added at the end of the entity definition.

## Formal Propositions

### CorrectPredefinedType
Either the _PredefinedType_ attribute is unset (e.g. because an _IfcRampFlightType_ is associated), or the inherited attribute _ObjectType_ shall be provided, if the _PredefinedType_ is set to USERDEFINED.

### CorrectTypeAssigned
Either there is no ramp flight type object associated, i.e. the _IsTypedBy_ inverse relationship is not provided, or the associated type object has to be of type _IfcRampFlightType_.

## Concepts

### Axis 2D Geometry

The walking line is represented by a two-dimensional open curve
as the axis. The curve is directed into the upward direction
(direction has to be interpreted as specified at the subtypes of
IfcCurve). 


Figure 254 illustrates the axis representation which has the following constraints:


* In case of straight flights the curve shall be a single item of type IfcPolyline.
* In case of winding flights the curve shall be a single item of type IfcCompositeCurve.
* In case of a curved flight or a spiral flight the curve shall be a single item of type IfcTrimmedCurve.


![walking line](../../../../figures/ifcstairflight_01-layout1.gif)
Figure 254 — Ramp flight axis



### Body Clipping Geometry


### Body SweptSolid Geometry

The following additional constraints apply to the 'SweptSolid'
representation type:


* Solid: IfcExtrudedAreaSolid is required,
* Profile: IfcRectangleProfileDef and
IfcArbitraryClosedProfileDef shall be supported.
* Extrusion: The profile shall be extruded in any
direction relative to the XY plane of the position coordinate
system of the IfcExtrudedAreaSolid. Therefore
non-perpendicular sweep operation has to be supported. It might be
further constrained to be in the direction of the global z-axis in
implementers agreements.


Figure 256 illustrates the body representation.


![fig1](../../../../figures/ifcrampflight-layout1.gif)
Figure 256 — Ramp flight body



### Footprint Geometry

The flight foot print, including the flight boundary is represented by a two-dimensional geometric curve set.


Figure 255 illustrates the footprint representation which has the following constraints:


* In case of straight flights the curve set shall consist of a single item of type IfcPolyline.
* In case of winding flights or curved flights the curve set shall consists of a single item of type
IfcCompositeCurve.
* In case of a spiral flight the curve set shall consists of a single item of type IfcConic or
IfcPolyline.


![boundary](../../../../figures/ifcstairflight_02-layout1.gif)
Figure 255 — Ramp flight footprint



### Material Solid

The material of the IfcRampFlight is defined by the
IfcMaterial and attached by the
IfcRelAssociatesMaterial.RelatingMaterial. It is
accessible by the inverse HasAssociations relationship.



### Object Typing


### Property Sets for Objects


### Quantity Sets


### Spatial Containment

The IfcRampFlight, as any subtype of IfcBuildingElement, 
may participate alternatively in one of the two different containment relationships:


* the Spatial Containment (defined here), or
* the Element Composition.



> NOTE  Model view definitions or implementer agreements may force an IfcRampFlight to be solely used as a part within an IfcRamp container. In this case, no Spatial containment shall be used.
> 


