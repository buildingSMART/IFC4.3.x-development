# IfcStair

A stair is a vertical passageway allowing occupants to walk (step) from one floor level to another floor level at a different elevation. It may include a landing as an intermediate floor slab.

{ .extDef}
> NOTE&nbsp; Definition according to ISO 6707-1: Construction comprising a succession of horizontal stages (steps or landings) that make it possible to pass on foot to other levels.

The _IfcStair_ shall either be represented:

* as a stair assembly entity that aggregates all parts (stair flight, landing, etc. with own representations), or
* as a single stair entity without decomposition including all representation directly at the stair entity.

> NOTE&nbsp; In case of an _IfcStair_ being the aggregate of all parts of the stair the aggregation is handled by the _IfcRelAggregates_ relationship, relating an _IfcStair_ with the related _IfcStairFlight_ and landings, _IfcSlab_ with PredefinedType=LANDING. _IfcRailing_'s belonging to the stair may also be included into the aggregation.

> NOTE&nbsp; Model View Definitions and implementer agreements may restrict the _IfcStair_ being an assembly to not have an independent shape representation, but to always require that the decomposed parts have a shape representation. In this case, at least the 'Body' geometric representations shall not be provided directly at _IfcStair_ if it is an assembly. The 'Body' geometric representation of the _IfcStair_ is then the sum of the 'Body' shape representation of the parts within the decomposition structure.

> HISTORY&nbsp; New entity in IFC2.0.

{ .change-ifc2x4}
> IFC4 CHANGE Attribute _ShapeType_ renamed to _PredefinedType_.

## Attributes

### PredefinedType
Predefined generic type for a stair that is specified in an enumeration. There may be a property set given specifically for the predefined types.
> NOTE&nbsp; The _PredefinedType_ shall only be used, if no _IfcStairType_ is assigned, providing its own _IfcStairType.PredefinedType_.

{ .change-ifc2x4}
> IFC4 CHANGE The attribute has been renamed from _ShapeType_ and changed to be OPTIONAL with upward compatibility for file based exchange.

## Formal Propositions

### CorrectPredefinedType
Either the _PredefinedType_ attribute is unset (e.g. because an _IfcStairType_ is associated), or the inherited attribute _ObjectType_ shall be provided, if the _PredefinedType_ is set to USERDEFINED.

### CorrectTypeAssigned
Either there is no stair type object associated, i.e. the _IsTypedBy_ inverse relationship is not provided, or the associated type object has to be of type _IfcStairType_.

## Concepts

### Axis 2D Geometry

The walking line is represented by a two-dimensional open curve 
as the axis. The curve is directed into the upward direction 
(direction has to be interpreted as specified at the subtypes of
IfcCurve). 




> NOTE  The 'Axis' representation of IfcStair 
> may be provided even if the IfcStair has components with own
>  shape representations.



### Body SweptSolid Geometry


### Element Decomposition

Geometric representation by aggregated elements


If the IfcStair has components (referenced by
SELF\IfcObject.IsDecomposedBy) with own 'Body'
representation, then no 'Body' representation shall defined for the
IfcStair. The IfcStair shape is then represented by
the geometric representation of its components. The components are
accessed via
SELF\IfcObject.IsDecomposedBy[1].RelatedObjects.


Figure 272 illustrates stair placement, where the IfcStair defines the local placement for all components and the common 'Axis' representation, and each component has its own 'Body' representation.


![stair](../../../../figures/ifcstair-layout1.png)
Figure 272 — Stair placement



### Material Solid

The material of the IfcStair is defined by the
IfcMaterial and attached by the
IfcRelAssociatesMaterial.RelatingMaterial. It is
accessible by the inverse HasAssociations relationship.


Material information can also be given at the
IfcStairType, defining the common attribute data for all
occurrences of the same type. It is then accessible by the inverse
IsDefinedBy relationship pointing to
IfcStair.HasAssociations and via
IfcRelAssociatesMaterial.RelatingMaterial to
IfcMaterial. If both are given, then the material directly
assigned to IfcStair overrides the material assigned to
IfcStairType.



### Object Typing


### Placement

The following restriction may be imposed by view definitions or implementer agreements:


* If the IfcStair establishes an aggregate, then
all contained elements shall be placed relative to the
IfcStair.ObjectPlacement.



### Property Sets for Objects


### Spatial Containment

The IfcStair, as any subtype of IfcBuildingElement, 
may participate alternatively in one of the two different containment relationships:


* the Spatial Containment (defined here), or
* the Element Composition.



