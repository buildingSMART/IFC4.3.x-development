Body AdvancedSwept Tapered Geometry
===================================



```
concept {
    IfcElement:Representation -> IfcProductDefinitionShape
    IfcProductDefinitionShape:Representations -> IfcShapeRepresentation
    IfcShapeRepresentation:ContextOfItems -> IfcGeometricRepresentationContext
    IfcShapeRepresentation:RepresentationIdentifier -> IfcLabel_0
    IfcShapeRepresentation:RepresentationType -> IfcLabel_1
    IfcShapeRepresentation:Items -> IfcExtrudedAreaSolidTapered
    IfcShapeRepresentation:Items -> IfcRevolvedAreaSolidTapered
    IfcLabel_0 -> constraint_0
    constraint_0[label="=Body"]
    IfcLabel_1 -> constraint_1
    constraint_1[label="=AdvancedSweptSolid"]
    IfcExtrudedAreaSolidTapered -> Extruded_Area_Tapered_PolyCurve_Profile
    IfcExtrudedAreaSolidTapered -> Extruded_Area_Tapered_Parameterized_Profile
    IfcRevolvedAreaSolidTapered -> Revolved_Area_Tapered_PolyCurve_Profile
    IfcRevolvedAreaSolidTapered -> Revolved_Area_Tapered_Parameterized_Profile
    IfcShapeRepresentation:RepresentationIdentifier[binding="Identifier"]
    IfcShapeRepresentation:RepresentationType[binding="Type"]
    IfcShapeRepresentation:Items[binding="Items"]
}
```
