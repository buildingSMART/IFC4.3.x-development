Element Openings
================

Elements may have openings (geometric voids) defined, which may be a partial recess or extend the full depth. Openings may optionally be filled by another element such as a door or window.

The 'Body' representation of an element does not account for voids upon export, for which CSG operations are required at import to produce the resulting shape.

The 'Reference' representation of an element does account for voids at export, such that no additional operations are required at import.

```
concept {
    IfcElement:HasOpenings -> IfcRelVoidsElement:RelatingBuildingElement
    IfcRelVoidsElement:RelatedOpeningElement -> IfcOpeningElement:VoidsElements
    IfcOpeningElement:PredefinedType -> IfcOpeningElementTypeEnum
    IfcOpeningElement:HasFillings -> IfcRelFillsElement:RelatingOpeningElement
    IfcRelFillsElement:RelatedBuildingElement -> IfcElement_1:FillsVoids

    IfcElement_1:FillsVoids[binding="FillsVoids"]
    IfcRelVoidsElement:RelatedOpeningElement[binding="RelatedOpeningElement"]
    IfcOpeningElement:PredefinedType[binding="OpeningElementType"]
    IfcOpeningElement:HasFillings[binding="HasFillings"]
    IfcRelFillsElement:RelatedBuildingElement[binding="RelatedBuiltElement"]
}
```
