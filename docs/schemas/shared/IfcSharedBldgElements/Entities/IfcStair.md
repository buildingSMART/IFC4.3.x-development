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

## WhereRules

### CorrectPredefinedType
Either the _PredefinedType_ attribute is unset (e.g. because an _IfcStairType_ is associated), or the inherited attribute _ObjectType_ shall be provided, if the _PredefinedType_ is set to USERDEFINED.

### CorrectTypeAssigned
Either there is no stair type object associated, i.e. the _IsTypedBy_ inverse relationship is not provided, or the associated type object has to be of type _IfcStairType_.
