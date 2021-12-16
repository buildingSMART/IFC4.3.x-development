Element Voiding
===============

Elements may have voids defined, which may be partial recess or extending full depth. Voids for openings may optionally be filled by another element such as a door, window, earthen or aggregate fill, or may represent a voiding feature without fillings.

The 'Body' representation of an element does not account for voids, for which CSG operations are required to produce the resulting shape.

The 'Mesh' representation of an element does account for voids, such that no additional operations are required.

```
concept {
    IfcElement:HasOpenings -> IfcRelVoidsElement:RelatingBuildingElement
    IfcElement:HasOpenings[binding="HasOpenings"]
}
```
