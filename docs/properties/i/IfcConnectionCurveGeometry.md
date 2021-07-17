IfcConnectionCurveGeometry
==========================

_IfcConnectionCurveGeometry_ is used to describe the geometric constraints that facilitate the physical connection of two objects at a curve or at an edge with curve geometry associated. It is envisioned as a control that applies to the element connection relationships.

The _IfcCurve_ (or the _IfcEdgeCurve_ with an associated _IfcCurve_) at the _CurveOnRelatingElement_ attribute defines the curve where the basic geometry items of the connected elements connects. The curve geometry and coordinates are provided within the local coordinate system of the _RelatingElement_, as specified at the _IfcRelConnects_ subtype that utilizes the _IfcConnectionCurveGeometry_. Optionally, the same curve geometry and coordinates can also be provided within the local coordinate system of the _RelatedElement_ by using the _CurveOnRelatedElement_ attribute.

> EXAMPLE&nbsp; The connection relationship between two walls has a geometric constraint which describes the end caps (or cut-off of the wall ends) by a _CurveOnRelatingElement_ for the first wall and a _CurveOnRelatedElement_ for the second wall. The exact usage of the _IfcConnectionCurveGeometry_ is further defined in the geometry use sections of the elements that use it.

The available geometry for the connection constraint may be further restricted to only allow straight segments by applying _IfcPolyline_ only. Such an usage constraint is provided at the object definition of the _IfcElement_ subtype, utilizing the element connection by referring to the subtype of _IfcRelConnects_ with the associated&nbsp;_IfcConnectionCurveGeometry._

> HISTORY&nbsp; New entity in IFC1.5.

{ .change-ifc2x}
> IFC2x CHANGE&nbsp; Renamed from IfcLineConnectionGeometry.

{ .change-ifc2x3}
> IFC2x3 CHANGE&nbsp; The provision of topology with associated geometry, _IfcEdgeCurve_, is enabled by using the _IfcCurveOrEdgeCurve_.
