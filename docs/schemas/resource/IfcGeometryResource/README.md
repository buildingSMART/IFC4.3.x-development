IfcGeometryResource
===================

The schema _IfcGeometryResource_ defines the resources used for geometric representations. The primary application of this resource is for representation of the shape or geometric form of an element. The geometric representation items defined here are also used to describe geometric models within the schema _IfcGeometricModelResource_.

The following is within the scope of the geometry resource:

* definition of points directly by their coordinate values and by parameter values on curves and surfaces
* definition of directions, vectors, and axis placements
* definition of transformation operators, both uniform and non-uniform
* definition of parametric curves
* definition of conic curves
* definition of curves defined on a parametric surface
* definition of offset curves
* definition of elementary surfaces
* definition of swept surfaces
* definition of parametric spline curves and surfaces
* definition of mapped items mapping source representations using transformation operators

> NOTE&nbsp; Many definitions of this schema are adapted from definitions defined within [ISO 10303-42](../../bibliography.htm#iso-10303-42){ .int-ref}. The _IfcGeometryResource_ refers to clause 4, "Geometry" of the standard. The definitions of geometric and topological representation, when quoted from [ISO 10303-42](../../bibliography.htm#iso-10303-42){ .int-ref}, are explicitly excluded from the copyright of this specification.

&nbsp;

{ .extDef}
> NOTE&nbsp; Definition according to ISO 10303-42  
> **Placement coordinate system**  
> A rectangular Cartesian coordinate system associated with the placement of a geometric entity in space, used to describe the interpretation of the attributes and to associate a unique parameterization with curve and surface entities."

{ .extDef}
> NOTE&nbsp; Definition according to ISO 10303-42  
> **Space Dimensionality**  
> All geometry shall be defined in a right-handed rectangular Cartesian coordinate system with the same units on each axis. A common scheme has been used for the definition of both two-dimensional and three-dimensional geometry. Points and directions exists in both a two-dimensional and a three-dimensional form, these forms are distinguished solely by the presence, or absence, of a third coordinate value. Complex geometric entities are all defined using points and directions from which their space dimensionality can be deduced.

{ .extDef}
> NOTE&nbsp; Definition according to ISO 10303-42  
> **Parameterization of analytic curves and surfaces**  
> Each curve on surface specified here has a defined parameterization. In some instances the definitions are in parametric terms. In others, the conic curves and elementary surfaces, the definitions are in geometric terms. In this latter case a placement coordinate system is used to define the parameterization. The geometric definitions contain some, but not all, of the data required for this. The relevant data to define this placement coordinate system is contained in the axis2 placement associated with the individual curve and surface entities.

{ .extDef}
> NOTE&nbsp; Definition according to ISO 10303-42  
> **Curves**  
> The curve entities include lines, some elementary conics, and some referentially or procedurally defined curves. All the curves have a well defined parameterization which makes it possible to trim a curve or identify points on the curve by parameter value. For the conic curves a method of representation is used which separates their geometric form from their orientation and position in space. In each case, the position and orientation information is conveyed by an axis2 placement. A composite curve entity, which includes the facility to communicate continuity information at the curve-to-curve transition points, is provided for the construction of more complex curves. The offset curve type is a curve defined with reference to other geometry. Separate offset curves entities exist for 2D and 3D applications.

{ .extDef}
> NOTE&nbsp; Definition according to ISO 10303-42  
> **Surfaces**  
> The simple surfaces are the planar surface, a surface of revolution and a surface of linear extrusion. As with curves, all surfaces have an associated standard parameterization. In many cases the surfaces, as defined, are unbounded; it is assumed that they will be bounded either explicitly or implicitly. Explicit bounding is achieved with the bounded surface; implicit bounding requires the association of additional topological information to define a face.
