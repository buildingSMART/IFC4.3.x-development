Mapped Geometry
===============

Elements may have a 'Mapped Geometry' representation that reuses the concept _Product Type Shape_ at the corresponding product type, as defined by the concept _Object Typing_.

The representation identifier of the mapped geometry representation is any of the other valid geometric representation identifiers, such as 'Body', 'FootPrint', or 'Axis'.

* _IfcShapeRepresentation_._RepresentationIdentifier_ = (any, see above)
* _IfcShapeRepresentation_._RepresentationType_ = 'MappedRepresentation'

```
concept {
    IfcProduct:Representation -> IfcProductDefinitionShape
    IfcProductDefinitionShape:Representations -> IfcShapeRepresentation
    IfcShapeRepresentation:ContextOfItems -> IfcGeometricRepresentationContext
    IfcShapeRepresentation:RepresentationIdentifier -> IfcLabel
    IfcShapeRepresentation:RepresentationType -> IfcLabel
    IfcShapeRepresentation:Items -> IfcMappedItem
    IfcMappedItem:MappingSource -> IfcRepresentationMap
    IfcMappedItem:MappingTarget -> IfcCartesianTransformationOperator3D
    IfcMappedItem:MappingTarget -> IfcCartesianTransformationOperator3DnonUniform
    IfcRepresentationMap:MappingOrigin -> IfcAxis2Placement3D
    IfcRepresentationMap:MappedRepresentation -> IfcShapeRepresentation
    IfcAxis2Placement3D:Location -> IfcCartesianPoint
    IfcAxis2Placement3D:Axis -> IfcDirection
    IfcAxis2Placement3D:RefDirection -> IfcDirection
    IfcCartesianTransformationOperator3D:Axis1 -> IfcDirection
    IfcCartesianTransformationOperator3D:Axis2 -> IfcDirection
    IfcCartesianTransformationOperator3D:LocalOrigin -> IfcCartesianPoint
    IfcCartesianTransformationOperator3D:Axis3 -> IfcDirection
    IfcShapeRepresentation:RepresentationIdentifier[binding="Identifier"]
    IfcShapeRepresentation:RepresentationType[binding="Type"]
}
```
