Element Voiding Features
========================

Elements may have voiding features defined, which may be achieved though cutting, drilling, or milling of members made of various materials, or by inlays into the formwork of cast members made of materials such as concrete.

The 'Body' representation of an element does not account for voids, for which CSG operations are required to produce the resulting shape.

The 'Mesh' representation of an element does account for voids, such that no additional operations are required.

```
concept {
    IfcElement:HasOpenings -> IfcRelVoidsElement:RelatingBuildingElement
    IfcRelVoidsElement:RelatedOpeningElement -> IfcVoidingFeature
    IfcVoidingFeature:PredefinedType -> IfcVoidingFeatureTypeEnum
    IfcElement:HasOpenings[binding="HasOpenings"]
    IfcRelVoidsElement:RelatedOpeningElement[binding="RelatedVoidingFeature"]
    IfcVoidingFeature:PredefinedType[binding="VoidingFeatureType"]
}
```
