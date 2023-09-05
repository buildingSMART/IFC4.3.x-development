Aggregation
===========

An aggregation indicates an internal unordered part composition relationship between the whole structure, referred to as the "composite", and the subordinate components, referred to as the "parts". The concept of aggregation is used in various ways. Examples are:

* Aggregation is used on building elements to indicate parts such as studs within a wall;
* Aggregation is used on spatial elements to indicate a spatial structure such as a storey within a building;
* Aggregation is used on systems to indicate subsystems such as branch circuits.

Aggregation is a bi-directional relationship, the relationship from the composite to its parts is called Decomposition, and the relationship from the part to its composite is called Composition.

```
concept {
    IfcObjectDefinition:IsDecomposedBy -> IfcRelAggregates:RelatingObject
}
```
