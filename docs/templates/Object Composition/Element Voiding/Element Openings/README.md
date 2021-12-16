Element Openings
================

Elements may have openings (geometric voids) defined, which may be a partial recess or extend the full depth. Openings may optionally be filled by another element such as a door or window.

The 'Body' representation of an element does not account for voids, for which CSG operations are required to produce the resulting shape.

The 'Mesh' representation of an element does account for voids, such that no additional operations are required.

```
concept {
    IfcElement:HasOpenings -> IfcRelVoidsElement:RelatingBuildingElement
    IfcRelVoidsElement:RelatedOpeningElement -> IfcOpeningElement
    IfcOpeningElement:PredefinedType -> IfcOpeningElementTypeEnum
    IfcOpeningElement:FillsVoids -> IfcRelFillsElement:RelatedBuildingElement
    IfcRelFillsElement:RelatedBuildingElement -> IfcDoor
    IfcRelFillsElement:RelatedBuildingElement -> IfcWindow
    IfcElement:HasOpenings[binding="HasOpenings"]
    IfcRelVoidsElement:RelatedOpeningElement[binding="RelatedOpeningElement"]
    IfcOpeningElement:PredefinedType[binding="OpeningElementType"]
    IfcOpeningElement:FillsVoids[binding="FillsVoids"]
    IfcRelFillsElement:RelatedBuildingElement[binding="RelatedBuiltElement"]
}
```
