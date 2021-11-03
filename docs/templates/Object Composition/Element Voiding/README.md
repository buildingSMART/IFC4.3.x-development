Element Voiding
===============

Elements may have voids defined, which may be partial recess or extending full depth. Voids for openings may optionally be filled by another element such as a door or window, or may represent a voiding feature without fillings.

The 'Body' representation of an element does not account for voids, for which CSG operations are required to produce the resulting shape.

The 'Mesh' representation of an element does account for voids, such that no additional operations are required.

```
concept {
    IfcElement:HasOpenings -> IfcRelVoidsElement:RelatingBuildingElement
    IfcRelVoidsElement:RelatedOpeningElement -> IfcOpeningElement
    IfcOpeningElement:PredefinedType -> IfcOpeningElementTypeEnum
    IfcOpeningElement:HasFillings -> IfcRelFillsElement:RelatingOpeningElement
    IfcRelFillsElement:RelatedBuildingElement -> IfcDoor
    IfcRelFillsElement:RelatedBuildingElement -> IfcWindow
    IfcElement:HasOpenings[binding="HasOpenings"]
    IfcOpeningElement:HasFillings[binding="HasFillings"]
    IfcRelFillsElement:RelatedBuildingElement[binding="RelatedFillings"]
    IfcDoor[binding="ElementName"]
    IfcWindow[binding="ElementName"]
}
```
