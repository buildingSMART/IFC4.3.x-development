# IfcAlignment2DHorizontal

An _IfcAlignment2DHorizontal_ is a linear reference projected onto the horizontal x/y plane. Points along a horizontal alignment have two coordinate values, x and y in the local Cartesian engineering system.

The horizontal alignment is defined by segments that are connected end-to-start. The transition at the segment connection is not enforced to be tangential, if the “tangential continuity” flag is set to false, otherwise a tangential continuity shall be preserved. Based on the context of the project, they are geo-referenced and convertible into Northing and Easting values.

> NOTE&nbsp; Georeferencing is provided by _IfcMapConversion_ through the _IfcGeometricRepresentationContext_ defined at _IfcProject_.

## Attributes

### StartDistAlong
The value of the distance along at the start of the horizontal alignment. If omited (standard) it is set to zero.

### Segments
An ordered list of unique horizontal alignment segments, each (but the last) are joint end to start

### ToAlignmentCurve

