# IfcConnectionPointEccentricity

_IfcConnectionPointEccentricity_ is used to describe the geometric constraints that facilitate the physical connection of two objects at a point or vertex point with associated point coordinates. There is a physical distance, or eccentricity, etween the connection points of both object. The eccentricity can be either given by:

* providing the _PointOnRelatingElement_ and the _PointOnRelatedElement_, where both point coordinates are not identical within a common parent coordinate system (latestly within the world coordinate system),
* providing the _PointOnRelatingElement_ and the three distance measures, _EccentricityInX_, _EccentricityInY_, and _EccentricityInZ_ (or only _EccentricityInX_, and _EccentricityInY_ if the underlying coordinate system is two-dimensional), or
* providing both.

<!-- end of short definition -->

> NOTE  If both, _PointOnRelatedElement_, and _EccentricityInX_, _EccentricityInY_, (_EccentricityInZ_) are provided, the values should be consistent. In case of any non-consistency, the calculated distance between _PointOnRelatingElement_ and _PointOnRelatedElement_ takes precedence.

The _IfcPoint_ (or the _IfcVertexPoint_ with an associated _IfcPoint_) at the _PointOnRelatingElement_ attribute defines the point where the basic geometry items of the connected elements connects. The point coordinates are provided within the local coordinate system of the _RelatingElement_, as specified at the _IfcRelConnects_ subtype that utilizes the _IfcConnectionPointGeometry_. Optionally, the same point coordinates can also be provided within the local coordinate system of the _RelatedElement_ by using the _PointOnRelatedElement_ attribute, otherwise the distance to the point at the RelatedElement has to be given by the three eccentricity values.

The explicit values for _EccentricityInX_, _EccentricityInY_, and _EccentricityInZ_ are always measured in the following direction and coordinate system (defining when the value is positive or negative):

* from the _PointOnRelatedElement_ to _PointOnRelatingElement_ within the coordinate system of the _RelatingElement_.
* in addition: when used to specify connections in structural analysis models, the _IfcStructuralMember_ is to be used as the _RelatingElement_ of the relationship object utilizing _IfcConnectionPointEccentricity_, and the _IfcStructuralConnection_ is the _RelatedElement_.

> HISTORY New entity in IFC2x3.

## Attributes

### EccentricityInX
Distance in x direction between the two points (or vertex points) engaged in the point connection.

### EccentricityInY
Distance in y direction between the two points (or vertex points) engaged in the point connection.

### EccentricityInZ
Distance in z direction between the two points (or vertex points) engaged in the point connection.
