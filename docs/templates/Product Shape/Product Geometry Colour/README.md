Product Geometry Colour
=======================



```
concept {
    IfcProduct:Representation -> IfcProductDefinitionShape
    IfcProductDefinitionShape:Representations -> IfcShapeRepresentation
    IfcShapeRepresentation:Items -> IfcSolidModel
    IfcShapeRepresentation:Items -> IfcTessellatedFaceSet
    IfcSolidModel:StyledByItem -> IfcStyledItem:Item
    IfcStyledItem:Styles -> IfcSurfaceStyle
    IfcSurfaceStyle -> Surface_Color_Style
    IfcTessellatedFaceSet:HasColours -> IfcIndexedColourMap:MappedTo
    IfcIndexedColourMap:Opacity -> IfcNormalisedRatioMeasure
    IfcIndexedColourMap:Colours -> IfcColourRgbList
    IfcIndexedColourMap:ColourIndex -> IfcPositiveInteger
}
```
