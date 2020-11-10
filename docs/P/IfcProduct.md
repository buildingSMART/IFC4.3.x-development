IfcProduct
==========
The _IfcProduct_ is an abstract representation of any object that relates to a
geometric or spatial context. An _IfcProduct_ occurs at a specific location in
space if it has a geometric representation assigned. It can be placed
relatively to other products, but ultimately relative to the project
coordinate system. The _ObjectPlacement_ attribute establishes the coordinate
system in which all points and directions used by the geometric representation
items under _Representation_ are founded. The _Representation_ is provided by
an _IfcProductDefinitionShape_ being either a geometric shape representation,
or a topology representation (with or without underlying geometry of the
topological items).  
  
Products include manufactured, supplied or created objects (referred to as
elements) for incorporation into an AEC/FM project. This also includes objects
that are created indirectly by other products, as spaces are defined by
bounding elements. Products can be designated for permanent use or temporary
use, an example for the latter is formwork. Products are defined by their
properties and representations.  
  
In addition to physical products (covered by the subtype _IfcElement_) and
spatial items (covered by the subtype _IfcSpatialElement_) the _IfcProduct_
also includes non-physical items, that relate to a geometric or spatial
contexts, such as grid, port, annotation, structural actions, etc.  
  
Any instance of _IfcProduct_ defines a particular occurrence of a product, the
common type information, that relates to many similar (or identical)
occurrences of _IfcProduct_, is handled by the _IfcTypeProduct_ (and its
subtypes), assigned to one or many occurrences of _IfcProduct_ by using the
objectified relationship _IfcRelDefinesByType_. The _IfcTypeProduct_ may
provide, in addition to common properties, also a common geometric
representation for all occurrences.  
  
> NOTE  See _IfcTypeProduct_ for how to use a common geometric representation
> and _IfcRelDefinesByType_ for using and overriding common properties.  
  
On a generic level products can be assigned to processes, controls, resources,
project by using the relationship objects that refer to the corresponding
object:  
  
* **Having a control applied**: assigned using _IfcRelAssignsToControl_ linking the _IfcProduct_ to an _IfcControl_  
* **Being assigned to a process**: assigned using _IfcRelAssignsToProcess_ linking the _IfcProduct_ to an _IfcProcess_  
* **Being assigned to a resource**: assigned using _IfcRelAssignsToResource_ linking the _IfcProduct_ to an _IfcResource_  
  
> EXAMPLE  An example of the control relationship is the assignment of a
> performance history to a distribution element. An example of process
> assignment relationship is the assignment of products like wall, slab,
> column to a contruction task for construction planning. And an example of
> resource assignment relationship is the assignment of products to a
> construction resource that consumes the product.  
  
> HISTORY  New entity in IFC1.0  
[ _bSI
Documentation_](https://standards.buildingsmart.org/IFC/DEV/IFC4_2/FINAL/HTML/schema/ifckernel/lexical/ifcproduct.htm)


Attribute definitions
---------------------
| Attribute              | Description   |
|------------------------|---------------|
| ObjectPlacement        |               |
| Representation         |               |
| ReferencedBy           |               |
| ReferencedInStructures |               |
| PositionedRelativeTo   |               |

