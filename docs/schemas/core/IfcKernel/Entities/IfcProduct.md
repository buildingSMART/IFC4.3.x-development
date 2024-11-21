# IfcProduct

The _IfcProduct_ is an abstract representation of any object that relates to a geometric or spatial context. An _IfcProduct_ occurs at a specific location in space if it has a geometric representation assigned. It can be placed relatively to other products, but ultimately relative to the project coordinate system. The _ObjectPlacement_ attribute establishes the coordinate system in which all points and directions used by the geometric representation items under _Representation_ are founded. The _Representation_ is provided by an _IfcProductDefinitionShape_ being either a geometric shape representation, or a topology representation (with or without underlying geometry of the topological items).
<!-- end of short definition -->

Products include manufactured, supplied or created objects (referred to as elements) for incorporation into an AEC/FM project. This also includes objects that are created indirectly by other products, as spaces are defined by bounding elements. Products can be designated for permanent use or temporary use, an example for the latter is formwork. Products are defined by their properties and representations.

In addition to physical products (covered by the subtype _IfcElement_) and spatial items (covered by the subtype _IfcSpatialElement_) the _IfcProduct_ also includes non-physical items, that relate to a geometric or spatial contexts, such as grid, port, annotation, structural actions, etc.

Any instance of _IfcProduct_ defines a particular occurrence of a product. The common type information, that relates to many similar (or identical) occurrences of _IfcProduct_, is handled by the _IfcTypeProduct_ (and its subtypes), assigned to one or many occurrences of _IfcProduct_ by using the objectified relationship _IfcRelDefinesByType_. The _IfcTypeProduct_ may provide, in addition to common properties, also a common geometric representation for all occurrences.

> NOTE See _IfcTypeProduct_ for how to use a common geometric representation and _IfcRelDefinesByType_ for using and overriding common properties.

On a generic level products can be assigned to processes, controls, resources, project by using the relationship objects that refer to the corresponding object:

* **Having a control applied**: assigned using _IfcRelAssignsToControl_ linking the _IfcProduct_ to an _IfcControl_
* **Being assigned to a process**: assigned using _IfcRelAssignsToProcess_ linking the _IfcProduct_ to an _IfcProcess_
* **Being assigned to a resource**: assigned using _IfcRelAssignsToResource_ linking the _IfcProduct_ to an _IfcResource_

> EXAMPLE An example of the control relationship is the assignment of a performance history to a distribution element. An example of process assignment relationship is the assignment of products like wall, slab, column to a construction task for construction planning. And an example of resource assignment relationship is the assignment of products to a construction resource that consumes the product.

> HISTORY New entity in IFC1.0

## Attributes

### ObjectPlacement
This establishes the object coordinate system and placement of the product in space. The placement can either be absolute (relative to the world coordinate system), relative (relative to the object placement of another product), or constrained (e.g. relative to grid axes, or to a linear positioning element). The type of placement is determined by the various subtypes of _IfcObjectPlacement_. An object placement must be provided if a representation is present.

### Representation
Reference to the representations of the product, being either a representation (_IfcProductRepresentation_) or as a special case of a shape representation (_IfcProductDefinitionShape_). The product definition shape provides for multiple geometric representations of the shape property of the object within the same object coordinate system, defined by the object placement.

### ReferencedBy
Reference to the _IfcRelAssignsToProduct_ relationship, by which other products, processes, controls, resources or actors (as subtypes of _IfcObjectDefinition_) can be related to this product.

### PositionedRelativeTo
Reference to the _IfcRelPositions_ relationship, which defines its relationship with a positioning element.

### ReferencedInStructures
Reference to the objectified relationship _IfcRelReferencedInSpatialStructure_ may be used to relate a product to one or more spatial structure elements in addition to the one in which it is primarily contained.

## Formal Propositions

### PlacementForShapeRepresentation
If a _Representation_ is given being an _IfcProductDefinitionShape_, then also an _ObjectPlacement_ has to be given. The _ObjectPlacement_ defines the object coordinate system in which the geometric representation items of the _IfcProductDefinitionShape_ are founded.

> NOTE If the _Representation_ of several subtypes of _IfcProduct_ have the same coordinate system it is permitted to share an instance of _IfcObjectPlacement_.

## Concepts

### Body Geometry

The body or solid model geometric representation of an _IfcProduct_ is typically defined using a Tessellation or Brep. Subtypes may provide recommendations on other representation types that may be used. The following attribute values for the _IfcShapeRepresentation_ holding this geometric representation shall be used:

* _IfcShapeRepresentation.RepresentationIdentifier_ = 'Body'
* _IfcShapeRepresentation.RepresentationType_ = Typically 'Tessellation' or 'Brep'

### Product Geometric Representation

The geometric representation of any _IfcProduct_ is provided by the _IfcProductDefinitionShape_ allowing multiple geometric representations. It uses the _Product Placement_ concept utilizing _IfcLocalPlacement_ to establish an object coordinate system, in which all geometric representations are founded.

> NOTE A detailed specification of how to apply the local placement and which shape representations are applicable is provided at the level of subtypes of _IfcProduct_ and is further determined by the model view definition and implementer agreements.

### Product Geometry Colour



### Product Geometry Layer



### Product Relative Positioning

If the _IfcProduct_ _Product Placement_ is placed relative to an _IfcPositioningElement_ this relationship covers the information on which _IfcPositioningElement_ positions the _IfcProduct_.

### Product Span Positioning



