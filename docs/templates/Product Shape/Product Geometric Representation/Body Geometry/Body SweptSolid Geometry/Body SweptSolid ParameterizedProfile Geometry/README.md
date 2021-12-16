Body SweptSolid ParameterizedProfile Geometry
=============================================



```
concept {
    IfcElement:Representation -> IfcProductDefinitionShape
    IfcProductDefinitionShape:Representations -> IfcShapeRepresentation
    IfcShapeRepresentation:ContextOfItems -> IfcGeometricRepresentationContext
    IfcShapeRepresentation:RepresentationIdentifier -> IfcLabel_0
    IfcShapeRepresentation:RepresentationType -> IfcLabel_1
    IfcShapeRepresentation:Items -> IfcSweptAreaSolid
    IfcLabel_0 -> constraint_0
    constraint_0[label="=Body"]
    IfcSweptAreaSolid -> Extruded_Area_Standardized_Profile
    IfcSweptAreaSolid -> Revolved_Area_Standardized_Profile
    IfcSweptAreaSolid -> Extruded_Area_Basic_Profile
    IfcSweptAreaSolid -> Revolved_Area_Basic_Profile
    IfcShapeRepresentation:RepresentationIdentifier[binding="Identifier"]
    IfcShapeRepresentation:RepresentationType[binding="Type"]
    IfcShapeRepresentation:Items[binding="Geometry"]
}
```
