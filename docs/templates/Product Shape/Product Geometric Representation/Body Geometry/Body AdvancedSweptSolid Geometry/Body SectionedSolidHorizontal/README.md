Body SectionedSolidHorizontal
=============================



```
concept {
    IfcElement:Representation -> IfcProductDefinitionShape
    IfcProductDefinitionShape:Representations -> IfcShapeRepresentation
    IfcShapeRepresentation:ContextOfItems -> IfcGeometricRepresentationContext
    IfcShapeRepresentation:RepresentationIdentifier -> IfcLabel
    IfcShapeRepresentation:RepresentationType -> IfcLabel
    IfcShapeRepresentation:Items -> IfcSectionedSolidHorizontal
    IfcSectionedSolidHorizontal:Directrix -> IfcBoundedCurve
    IfcSectionedSolidHorizontal:CrossSections -> IfcProfileDef
    IfcSectionedSolidHorizontal:FixedAxisVertical -> IfcBoolean
    IfcShapeRepresentation:RepresentationIdentifier[binding="Identifier"]
    IfcShapeRepresentation:RepresentationType[binding="Type"]
    IfcShapeRepresentation:Items[binding="Items"]
    IfcSectionedSolidHorizontal:Directrix[binding="Directrix"]
    IfcSectionedSolidHorizontal:CrossSections[binding="CrossSections"]
    IfcSectionedSolidHorizontal:FixedAxisVertical[binding="FixedAxisVertical"]
}
```
