Spatial Container
=================

The _Spatial Container_ concept defines a spatial element as being the spatial container for physical elements, or other elements being directly related to the spatial container, such as annotations or grids.

> EXAMPLE  A building story is a logical spatial container of building elements, distribution elements, or furnishing elements.

The _Spatial Container_ concept is realized by using the _IfcRelContainedInSpatialStructure_ objectified relationship between subtypes of _IfcSpatialElement_ and the elements contained. The inverse relationship _ContainsElements_ at the subtypes of _IfcSpatialElement_ refers to the contained physical elements.

```
concept {
    IfcSpatialElement:ContainsElements -> IfcRelContainedInSpatialStructure:RelatingStructure
    IfcRelContainedInSpatialStructure:RelatedElements -> IfcProduct
    IfcRelContainedInSpatialStructure:RelatedElements[binding="Type"]
}
```
