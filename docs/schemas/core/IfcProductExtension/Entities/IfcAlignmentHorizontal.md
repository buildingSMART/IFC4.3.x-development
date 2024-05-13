# IfcAlignmentHorizontal

An _IfcAlignmentHorizontal_ is a linear reference projected onto the horizontal x/y plane. Points along a horizontal alignment have two coordinate values, x and y in the local Cartesian engineering system.<!-- end of definition -->

The horizontal alignment is defined by segments that are connected end-to-start. The transition at the segment connection is not enforced to be tangential, if the “tangential continuity” flag is set to false, otherwise a tangential continuity shall be preserved. Based on the context of the project, they are geo-referenced and convertible into Northing and Easting values.

> NOTE  Georeferencing is provided by _IfcMapConversion_ through the _IfcGeometricRepresentationContext_ defined at _IfcProject_.

## Concepts

### Alignment Horizontal Attributes



