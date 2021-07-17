IfcRamp
=======

A ramp is a vertical passageway which provides a human or vehicle circulation link between one floor level and another floor level at a different elevation. It may include a landing as an intermediate floor slab. A ramp normally does not include steps.

{ .extDef}
> NOTE&nbsp; Definition according to ISO 6707-1: Inclined way or floor joining two surfaces at different levels.

The _IfcRamp_ shall either be represented:

* as a ramp assembly that aggregates all parts(ramp flight, landing, etc.) with own shape representations, or
* as a single ramp without decomposition including all shape representations directly at the ramp entity.

> NOTE&nbsp; In case of an _IfcRamp_ being the assembly of all parts of the ramp the aggregation is handled by the _IfcRelAggregates_ relationship, relating an _IfcRamp_ with the related _IfcRampFlight_ and landings, _IfcSlab_ with PredefinedType=LANDING. _IfcRailing_'s belonging to the ramp may also be included into the aggregation.

> NOTE&nbsp; Model View Definitions and implementer agreements may restrict the _IfcRamp_ being an assembly to not have an independent shape representation, but to always require that the decomposed parts have a shape representation. In this case, at least the 'Body' geometric representations shall not be provided directly at _IfcRamp_ if it is an assembly. The 'Body' geometric representation of the _IfcRamp_ is then the sum of the 'Body' shape representation of the parts within the decomposition structure.

> HISTORY&nbsp; New entity in IFC2.0.

{ .change-ifc2x4}
> IFC4 CHANGE Attribute _ShapeType_ renamed to _PredefinedType_
