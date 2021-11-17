# IfcOccupant

An occupant is a type of actor that defines the form of occupancy of a property.

The principal purpose of **IfcOccupant** is to determine the nature of occupancy of a property for a particular actor. All characteristics relating to the actor (name and organization details) are inherited from the _IfcActor_ entity.

> HISTORY&nbsp; New entity in IFC2x

## Attributes

### PredefinedType
Predefined occupant types from which that required may be set.

{ .change-ifc2x4}
> IFC4 CHANGE Attribute made optional.

## Formal Propositions

### WR31
The attribute ObjectType must be asserted when the value of the IfcOccupantTypeEnum is set to USERDEFINED.

## Concepts

### Actor Assignment


