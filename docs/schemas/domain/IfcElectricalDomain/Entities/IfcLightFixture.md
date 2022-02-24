# IfcLightFixture

A light fixture is a container that is designed for the purpose of housing one or more lamps and optionally devices that control, restrict or vary their emission.

> HISTORY  New entity in IFC4

{ .note}
>

## Attributes

### PredefinedType


## Formal Propositions

### CorrectPredefinedType
Either the _PredefinedType_ attribute is unset (e.g. because an _IfcLightFixtureType_ is associated), or the inherited attribute _ObjectType_ shall be provided, if the _PredefinedType_ is set to USERDEFINED.

### CorrectTypeAssigned
Either there is no light fixture type object associated, i.e. the _IsTypedBy_ inverse relationship is not provided, or the associated type object has to be of type _IfcLightFixtureType_.

## Concepts

### Connection


### Lighting Geometry

This represents the light emission of the item having IfcShapeRepresentation.RepresentationType of 'LightSource' and containing one or more IfcLightSource subtypes.


### Material


### Object Typing


### Port


### Property Sets for Objects


### Quantity Sets


