Body AdvancedSwept Directrix Geometry
=====================================



```
concept {
    IfcElement:Representation -> IfcProductDefinitionShape
    IfcProductDefinitionShape:Representations -> IfcShapeRepresentation
    IfcShapeRepresentation:ContextOfItems -> IfcGeometricRepresentationContext
    IfcShapeRepresentation:RepresentationIdentifier -> IfcLabel_0
    IfcShapeRepresentation:RepresentationType -> IfcLabel_1
    IfcShapeRepresentation:Items -> IfcSurfaceCurveSweptAreaSolid
    IfcShapeRepresentation:Items -> IfcFixedReferenceSweptAreaSolid
    IfcLabel_0 -> constraint_0
    constraint_0[label="=Body"]
    IfcLabel_1 -> constraint_1
    constraint_1[label="=AdvancedSweptSolid"]
    IfcSurfaceCurveSweptAreaSolid -> SurfaceCurve_SweptArea_PolyCurve_Profile
    IfcFixedReferenceSweptAreaSolid -> FixedReference_SweptArea_PolyCurve_Profile
    IfcShapeRepresentation:RepresentationIdentifier[binding="Identifier"]
    IfcShapeRepresentation:RepresentationType[binding="Type"]
    IfcShapeRepresentation:Items[binding="Items"]
}
```
