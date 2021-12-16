Mapped Geometry
===============

Elements may have a 'Mapped Geometry' representation that reuses the concept _Product Type Shape_ at the corresponding product type, as defined by the concept _Object Typing_.

The representation identifier of the mapped geometry representation is any of the other valid geometric representation identifiers, such as 'Body', 'FootPrint', or 'Axis'.

* _IfcShapeRepresentation_._RepresentationIdentifier_ = (any, see above)
* _IfcShapeRepresentation_._RepresentationType_ = 'MappedRepresentation'

```
concept {
    IfcProduct:Representation -> IfcProductDefinitionShape
    IfcProductDefinitionShape:Representations -> IfcShapeRepresentation_0
    IfcShapeRepresentation_0:ContextOfItems -> IfcGeometricRepresentationContext
    IfcShapeRepresentation_0:RepresentationIdentifier -> IfcLabel_0
    IfcShapeRepresentation_0:RepresentationType -> IfcLabel_1
    IfcShapeRepresentation_0:Items -> IfcMappedItem
    IfcMappedItem:MappingSource -> IfcRepresentationMap
    IfcMappedItem:MappingTarget -> IfcCartesianTransformationOperator3D
    IfcMappedItem:MappingTarget -> IfcCartesianTransformationOperator3DnonUniform
    IfcRepresentationMap:MappingOrigin -> IfcAxis2Placement3D
    IfcRepresentationMap:MappedRepresentation -> IfcShapeRepresentation_1
    IfcAxis2Placement3D:Location -> IfcCartesianPoint_0
    IfcAxis2Placement3D:Axis -> IfcDirection_0
    IfcAxis2Placement3D:RefDirection -> IfcDirection_1
    IfcCartesianTransformationOperator3D:Axis1 -> IfcDirection_2
    IfcCartesianTransformationOperator3D:Axis2 -> IfcDirection_3
    IfcCartesianTransformationOperator3D:LocalOrigin -> IfcCartesianPoint_1
    IfcCartesianTransformationOperator3D:Axis3 -> IfcDirection_4
    IfcShapeRepresentation_0:RepresentationIdentifier[binding="Identifier"]
    IfcShapeRepresentation_0:RepresentationType[binding="Type"]
}
```
