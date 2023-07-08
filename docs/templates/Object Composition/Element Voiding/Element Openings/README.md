Element Openings
================

Elements may have openings (geometric voids) defined, which may be a partial recess or extend the full depth. Openings may optionally be filled by another element such as a door or window.

The 'Body' representation of an element does not account for voids upon export, for which CSG operations are required at import to produce the resulting shape.

The 'Reference' representation of an element does account for voids at export, such that no additional operations are required at import.

```
concept {
    IfcElement_0:HasOpenings -> IfcRelVoidsElement:RelatingBuildingElement
    IfcRelVoidsElement:RelatedOpeningElement -> IfcOpeningElement
IfcOpeningElement:PredefinedType -> IfcOpeningElementTypeEnum
    IfcOpeningElement:FillsVoids -> IfcRelFillsElement:RelatedBuildingElement
    IfcRelFillsElement:RelatedBuildingElement -> IfcElement_1

    IfcElement_1:HasOpenings[binding="HasOpenings"]
    IfcRelVoidsElement:RelatedOpeningElement[binding="RelatedOpeningElement"]
    IfcOpeningElement:PredefinedType[binding="OpeningElementType"]
    IfcOpeningElement:FillsVoids[binding="FillsVoids"]
    IfcRelFillsElement:RelatedBuildingElement[binding="RelatedBuiltElement"]
}
```
