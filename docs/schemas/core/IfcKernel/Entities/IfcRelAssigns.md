# IfcRelAssigns

The assignment relationship, _IfcRelAssigns_, is a generalization of "link" relationships among instances of _IfcObject_ and its various 1<sup>st</sup> level subtypes. A link denotes the specific association through which one object (the client) applies the services of other objects (the suppliers), or through which one object may navigate to other objects.
<!-- end of short definition -->

The client is denoted as the relating object and is established at the level of the specific, instantiable subtypes of _IfcRelAssigns_. The suppliers are denoted as the related objects and they are established by the _RelatedObjects_ attribute.

> NOTE The terms "client" and "supplier" are used in a general concept and do not imply any meaning for implementations of systems (like client-server).

> EXAMPLE A resource may receive information about its nature of representing real building products by establishing a link between _IfcResource_ and _IfcBuiltElement_ (subtype of _IfcProduct_) through the assignment relationship _IfcRelAssignsToResource_. The resource is then the client that applies the services of other objects (here building elements) to express the particular view of elements to be consumed as a resource in a process.

The assignment relationship establishes a bi-directional relationship among the participating objects and does not imply any dependency. The subtypes of _IfcRelAssigns_ establish the particular semantic meaning of the assignment relationship.

> NOTE The RelatingObject attribute is defined at the level of each subtype of _IfcRelAssigns_. 

> HISTORY New entity in IFC2x.

## Attributes

### RelatedObjects
Related objects, which are assigned to a single object. The type of the single (or relating) object is defined in the subtypes of IfcRelAssigns.

### RelatedObjectsType
Particular type of the assignment relationship. It can constrain the applicable object types, used within the role of _RelatedObjects_.

> IFC4 DEPRECATION The attribute is deprecated and shall no longer be used. A NIL value should always be assigned.

> IFC4.3.0.1 CHANGE The attribute type has been changed to IfcStrippedOptional given that IfcObjectTypeEnum has been deleted.
