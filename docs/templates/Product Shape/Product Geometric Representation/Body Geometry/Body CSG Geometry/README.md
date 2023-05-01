Body CSG Geometry
=================

The _Body CSG Geometry_ is the representation of the 3D shape of a product by Constructive Solid Geometry models.

The following attribute values for the _IfcShapeRepresentation_ holding this geometric representation shall be used:

* _IfcShapeRepresentation_._RepresentationIdentifier_ = 'Body'
* _IfcShapeRepresentation_._RepresentationType_ = 'CSG'
* _IfcShapeRepresentation_._Items_ = _IfcCSGSolid_

> NOTE  The _Items_ _IfcBooleanResult_ and _IfcPrimitive3D_ shall also be allowed for compatibility with previous releases of the standard.

```
concept {
    IfcElement:Representation -> IfcProductDefinitionShape
    IfcProductDefinitionShape:Representations -> IfcShapeRepresentation
    IfcShapeRepresentation:ContextOfItems -> IfcGeometricRepresentationContext
    IfcShapeRepresentation:RepresentationIdentifier -> IfcLabel_0
    IfcShapeRepresentation:RepresentationType -> IfcLabel_1
    IfcShapeRepresentation:Items -> IfcCsgSolid
    IfcLabel_0 -> constraint_0
    constraint_0[label="=Body"]
    IfcLabel_1 -> constraint_1
    constraint_1[label="=CSG"]
    IfcShapeRepresentation:RepresentationIdentifier[binding="Identifier"]
    IfcShapeRepresentation:RepresentationType[binding="Type"]
}
```
