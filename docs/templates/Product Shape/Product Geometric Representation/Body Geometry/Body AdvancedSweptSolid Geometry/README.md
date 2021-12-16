Body AdvancedSweptSolid Geometry
================================

The _Body AdvancedSweptSolid Geometry_ is the representation of the 3D shape of a product by swept solid models, including advanced sweeping operations, such as sweeping along any directrix and tapering.

The following attribute values for the _IfcShapeRepresentation_ holding this geometric representation shall be used:

* _IfcShapeRepresentation_._RepresentationIdentifier_ = 'Body'
* _IfcShapeRepresentation_._RepresentationType_ = 'AdvancedSweptSolid'
* _IfcShapeRepresentation_._Items_ = _IfcSweptAreaSolid_, _IfcSweptDiskSolid_

```
concept {
    IfcElement:Representation -> IfcProductDefinitionShape
    IfcProductDefinitionShape:Representations -> IfcShapeRepresentation
    IfcShapeRepresentation:ContextOfItems -> IfcGeometricRepresentationContext
    IfcShapeRepresentation:RepresentationIdentifier -> IfcLabel_0
    IfcShapeRepresentation:RepresentationType -> IfcLabel_1
    IfcLabel_0 -> constraint_0
    constraint_0[label="=Body"]
    IfcLabel_1 -> constraint_1
    constraint_1[label="=AdvancedSweptSolid"]
    IfcShapeRepresentation:RepresentationIdentifier[binding="Identifier"]
    IfcShapeRepresentation:RepresentationType[binding="Type"]
    IfcShapeRepresentation:Items[binding="Items"]
}
```
