# IfcProjectionElement

The projection element is a specialization of the general feature element to represent projections applied to building elements. It represents a solid attached to any element that has physical manifestation.

> EXAMPLE  A wall projection such as a pilaster strip is handled by _IfcProjectionElement_

> NOTE  View definitions or implementer agreements may restrict the types of elements to which _IfcProjectionElement_ can be applied.

An _IfcProjectionElement_ has to be linked to a element (all subtypes of _IfcElement_) by using the _IfcRelProjectsElement_ relationship. Its existence depends on the existence of the master element. The relationship implies a Boolean union operation between the volume of the projection element and the volume of the element.

The _IfcProjectionElement_ shall not participate in the containment relationship, i.e. it is not linked directly to the spatial structure of the project. It has a mandatory _ProjectsElements_ inverse relationship pointing to the _IfcElement_ that is contained in the spatial structure.

* The inverse relationship _ContainedInStructure_ shall be NIL.

> HISTORY  New entity in IFC2x2.

{ .change-ifc2x4}
> IFC4 CHANGE  The attribute _PredefinedType_ has been added at the end of attribute list.

## Attributes

### PredefinedType
Predefined generic type for a projection element that is specified in an enumeration. There may be a property set given specifically for the predefined types.
{ .change-ifc2x4}
> IFC4 CHANGE The attribute has been added at the end of the entity definition.

## Formal Propositions

### CorrectPredefinedType
Either _PredefinedType_ is unset or the inherited attribute _ObjectType_ shall be provided, if the _PredefinedType_ is set to USERDEFINED or _PredefinedType_.

## Concepts

### Body Geometry

The geometric representation of IfcProjectionElement can be defined using the swept area solid geometry. The following attribute values for the IfcShapeRepresentation holding this geometric representation shall be used:

* _IfcShapeRepresentation.RepresentationIdentifier_: 'Body'
* _IfcShapeRepresentation.RepresentationType_: 'SweptSolid'

The following constraints are recommended:

* _IfcShapeRepresentation.Items_ may include a single, or multiple, instances of IfcExtrudedAreaSolid.
* _IfcExtrudedAreaSolid.SweptArea_ shall support IfcRectangleProfileDef, IfcCircleProfileDef and IfcArbitraryClosedProfileDef.
* _IfcExtrudedAreaSolid.ExtrudedDirection_ shall extrude the profile in a direction non-parallel to the element it is projecting. This may be horizontal for wall projections or vertically for floor projections.
* If multiple instances of IfcExtrudedAreaSolid are used, the extrusion direction of each extrusion should be equal.

As shown in Figure PROJECTIONREP, the following interpretation of dimension parameters applies for rectangular projection:

* _IfcRectangleProfileDef.YDim_ interpreted as projection width
* _IfcRectangleProfileDef.XDim_ interpreted as projection height
* _IfcExtrudedAreaSolid.Depth_ is interpreted as projection depth

> NOTE  Rectangles are now defined centric, the placement location has to be set: > * IfcCartesianPoint(XDim/2,YDim/2)

> NOTE  The local placement directions for the IfcProjectionElement are only given as an example, other directions are valid as well.

![projection](../../../../figures/ifcprojectionelement-layout1.png )

Figure PROJECTIONREP &mdash; Projection representation

The general geometric representation of IfcProjectionElement can also be defined using the Brep or Tesselation geometry. The Brep or Tessellation representation allows for the representation of complex element shapes. The following attribute values for the IfcShapeRepresentation holding this geometric representation shall be used:

* _IfcShapeRepresentation.RepresentationIdentifier_: 'Body'
* _IfcShapeRepresentation.RepresentationType_: 'Tessellation' or 'Brep'

### Product Local Placement

The local placement for IfcProjectionElement is defined in its supertype IfcProduct. It is defined by the IfcLocalPlacement, which defines the local coordinate system that is referenced by all geometric representations.

* The PlacementRelTo relationship of IfcLocalPlacement should point to the local placement of the same element, to which the projection adds, i.e. referred to by _ProjectsElement.RelatingBuildingElement_.

### Property Sets for Objects



### Quantity Sets



