# IfcCoordinateOperation

The coordinate operation is an abstract supertype to handle any operation (transformation or conversion) between two coordinate reference systems. It is meant to provide expandability for future versions, since currently only the conversion of a local engineering coordinate system into a map coordinate reference system is dealt with by the subtype _IfcMapConversion_.

By convention, a coordinate operation is given between the _SourceCRS_ being the more local, or child coordinate reference system, and the _TargetCRS_ being the more remote or parent coordinate reference system, in the special case the coordinate operation between the local engineering coordinate system of the construction project and any map or other coordinate reference system.

{ .extDef}
> NOTE  Definition from OpenGIS Abstract Specification, Topic 2:  
> If the relationship between any two coordinate reference systems is known, coordinates can be transformed or converted to another coordinate reference system. Coordinate operations are divided into two subtypes: { .note}
> * _Coordinate conversion_ &ndash; mathematical operation on coordinates that does not include any change of datum. The best-known example of a coordinate conversion is a map projection. The parameters describing coordinate conversions are defined rather than empirically derived. Note that some conversions have no parameters.
> * _Coordinate transformation_ &ndash; mathematical operation on coordinates that usually includes a change of datum. The parameters of a coordinate transformation are empirically derived from data containing the coordinates of a series of points in both coordinate reference systems. This computational process is usually &lsquo;over-determined&rsquo;, allowing derivation of error (or accuracy) estimates for the transformation. Also, the stochastic nature of the parameters may result in multiple (different) versions of the same coordinate transformation. Because of this several transformations may exist for a given pair of coordinate reference systems, differing in their transformation method, parameter values and accuracy characteristics.

> HISTORY  New entity in IFC4.

## Attributes

### SourceCRS
Source coordinate reference system for the operation.

### TargetCRS
Target coordinate reference system for the operation.
