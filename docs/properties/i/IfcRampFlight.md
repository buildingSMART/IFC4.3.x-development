IfcRampFlight
=============

A ramp comprises a single inclined segment, or several inclined segments that are connected by a horizontal segment, refered to as a landing. A ramp flight is the single inclined segment and part of the ramp construction. In case of single flight ramps, the ramp flight and the ramp are identical.

> NOTE&nbsp; A single flight ramp is represented by an _IfcRamp_ instance without using aggregation and by utilizing the product shape representation directly at _IfcRamp_.

An _IfcRampFlight_ is an aggregated part of an _IfcRamp_ realized through the _IfcRelAggregates_ relationship, the ramp flight is therefore included in the set of _IfcRelAggregates.RelatedObjects_.

An _IfcRampFlight_ connects the floor slab of zero to two different storeys (or partial storeys or landings) within a building. The connection relationship between the _IfcRampFlight_ and the _IfcSlab_ can be expressed using the _IfcRelConnectsElements_ relationship.

> HISTORY&nbsp; New entity in IFC2.0.
