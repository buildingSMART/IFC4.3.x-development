# IfcAlignment2DVertical

An _IfcAlignment2DVertical_ is a height profile along the horizontal alignment. Points along a vertical alignment have two coordinate values. The first value is the distance along the horizontal alignment, the second value is the height according to the project engineering coordinate system. Based on the context of the project, they are geo-referenced and the height value is convertible into orthogonal height above/below the vertical datum.

> NOTE&nbsp; Georeferencing is provided by _IfcMapConversion_ through the _IfcGeometricRepresentationContext_ defined at _IfcProject_.

## Attributes

### Segments
An ordered list of unique vertical alignment segments, each (but the last) are joint end to start

### ToAlignmentCurve

