Element Filling
===============

Elements such as doors and windows may be placed inside openings of walls, slabs, or other elements.

```
concept {
    IfcElement:FillsVoids -> IfcRelFillsElement:RelatedBuildingElement
    IfcRelFillsElement:RelatingOpeningElement -> IfcOpeningElement
    IfcOpeningElement:VoidsElements -> IfcRelVoidsElement
    IfcRelVoidsElement:RelatingElement -> IfcElement
}
```
