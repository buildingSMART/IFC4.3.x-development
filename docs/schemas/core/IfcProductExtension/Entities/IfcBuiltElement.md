# IfcBuiltElement

The built element comprises all elements that are primarily part of the construction of a built facility, i.e., its structural and space separating system. Built elements are all physically existent and tangible things.

This _IfcBuiltElement_ is a generalization of all elements that are major functional parts of the structural or space separation system of a built facility. Typical examples of _IfcBuiltElement_ entities are (among others):

* built elements within a space separation system
* built elements within an enclosure system (such as a facade)
* built elements within a fenestration system
* built elements within a load bearing system
* built elements within a foundation system
* built elements within an infrastructure facility

> EXAMPLE  built elements are curtain wall, doors, and others in case of buildings; walls, columns, pile, beams in case of buildings or infrastructure works; bearings in case of bridges; pavements in case of roads or rails in case of railways.

The _IfcBuiltElement_ can be instantiated in the case when arbitrary built elements cannot be expressed by a subtype of _IfcBuiltElement_.

> NOTE  The deprecated _IfcBuildingElementProxy_ shall not be used to represent any arbitrary built element. Use a direct instantiation of _IfcBuiltElement_ instead.

> HISTORY  New entity in IFC1.0

> IFC4.3.0.0 CHANGE  The entity has been renamed from IfcBuildingElement and made non abstract.

## Formal Propositions

### MaxOneMaterialAssociation
There should be only a maximum of one material association assigned to an building element.
> NOTE  The material association can assign a single material, a set of material constituents, a set of material layers, or a set of material profiles by a single association relationship.

{ .change-ifc2x4}
> IFC2x4 CHANGE The where rule has been promoted from the subtype _IfcWall_.

## Concepts

### Product Assignment



#### IfcTask

Task for operating upon the building element.

### Property Sets for Objects



### Spatial Containment



### Surface 3D Geometry

Some _IfcBuildingElement_ may be represented by an surface as an abstract geometric representation. See each subtype for specific guidance.

