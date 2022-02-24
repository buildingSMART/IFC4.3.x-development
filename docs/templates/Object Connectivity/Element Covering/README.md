Element Covering
================

Covering elements are assigned to their hosting elements using the _Element Covering_ concept.

> EXAMPLE  A cladding is assigned to a wall, a flooring is assigned to a slab, a wrapping is assigned to a duct using the _IfcRelCoversBldgElements_ relationship.

```
concept {
    IfcElement:HasCoverings -> IfcRelCoversBldgElements:RelatingBuildingElement
    IfcRelCoversBldgElements:RelatedCoverings -> IfcCovering
}
```
