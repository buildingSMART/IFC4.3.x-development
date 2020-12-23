# IfcStairFlight

A stair flight is an assembly of building components in a single "run" of stair steps (not interrupted by a landing). The stair steps and any stringers are included in the stair flight. A winder is also regarded a part of a stair flight.

An _IfcStairFlight_ is normally aggregated by an _IfcStair_ through the _IfcRelAggregates_ relationship, the stair flight is then included in the set of _IfcRelAggregates.RelatedObjects_. An _IfcStairFlight_ normally connects the floor slab of zero to two different storeys (or partial storeys, or landings) within a building. The connection relationship between the _IfcStairFlight_ and the _IfcSlab_ can be expressed using the _IfcRelConnectsElements_ relationship.

> HISTORY&nbsp; New entity in IFC2.0.

## Attributes

### NumberOfRisers
Number of the risers included in the stair flight
{ .change-ifc2x4}
> IFC4 CHANGE The attribute has been deprecated it shall only be exposed with a NIL value. Use _Pset_StairFlightCommon.NumberOfRisers_ instead.

### NumberOfTreads
Number of treads included in the stair flight.
{ .change-ifc2x4}
> IFC4 CHANGE The attribute has been deprecated it shall only be exposed with a NIL value. Use _Pset_StairFlightCommon.NumberOfTreads_ instead.

### RiserHeight
Vertical distance from tread to tread. The riser height is supposed to be equal for all stairs in a stair flight.
  
{ .change-ifc2x4}
> IFC4 CHANGE The attribute has been deprecated it shall only be exposed with a NIL value. Use _Pset_StairFlightCommon.RiserHeight_ instead.

### TreadLength
Horizontal distance from the front to the back of the tread. The tread length is supposed to be equal for all steps of the stair flight.
  
{ .change-ifc2x4}
> IFC4 CHANGE The attribute has been deprecated it shall only be exposed with a NIL value. Use _Pset_StairFlightCommon.TreadLength_ instead.

### PredefinedType
Predefined generic type for a stair flight that is specified in an enumeration. There may be a property set given specificly for the predefined types.
> NOTE&nbsp; The _PredefinedType_ shall only be used, if no _IfcStairFlightType_ is assigned, providing its own _IfcStairFlightType.PredefinedType_.

{ .change-ifc2x4}
> IFC4 CHANGE The attribute has been added at the end of the entity definition.

## WhereRules

### CorrectPredefinedType
Either the _PredefinedType_ attribute is unset (e.g. because an _IfcStairFlightType_ is associated), or the inherited attribute _ObjectType_ shall be provided, if the _PredefinedType_ is set to USERDEFINED.

### CorrectTypeAssigned
Either there is no stair flight type object associated, i.e. the _IsTypedBy_ inverse relationship is not provided, or the associated type object has to be of type _IfcStairFlightType_.
