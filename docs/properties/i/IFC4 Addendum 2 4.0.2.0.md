IFC4 Addendum 2 4.0.2.0
=======================

{ .std}
The Second Addendum of the IFC4 release has the main scope to provide improvements to geometry issues that had been reported during the implementation of IFC4 and IFC4 Addendum 1. It resolves these issues and addresses further implementation issues and concerns.

The main changes incorporated into IFC4 ADD2 schema are:

* Improvement of the tessellated geometry to allow for more complex tessellations then triangulation and to enable an point index for sharing Cartesian point lists. 
    * new entities _IfcPolygonalFaceSet_, _IfcIndexedPolygonalFace_, _IfcIndexedPolygonalFaceWithVoids_,
    * changing the normal index to a point index at _IfcTriangulatedFaceSet_,
    * adding _IfcPolygonalFaceSet_ and _IfcTriangulatedFaceSet_ to _IfcBooleanOperand_ with the rule that only closed tessellations can be used,
    * extensive improvement of documentation and new figures to explain the use of tessellated face sets. 
* Improvement of advanced boundary representation, particularly for using elementary surfaces. 
    * new entities for elementary surfaces _IfcSphericalSurface_, _IfcToroidalSurface_,
    * new entities for intersection curves to enable curves defined in u,v parametric space _IfcSurfaceCurve_, _IfcIntersectionCurve_, _IfcSeamCurve_,
    * new enumeration _IfcPreferredSurfaceCurveRepresentation_ 
    * extensive improvement of documentation and new figures to explain the use of advanced boundary representations. 

Minor corrections and improvements to the IFC4 ADD1 schema include:

* additional enumerator for _IfcBuildingElementProxyTypeEnum_ to describe a provision for space,
* additional enumerator for _IfcSensorTypeEnum_ to describe a CO Sensor,
* additional property sets, where a common property set was missing,
* further improvements of property set definitions and rationalizations,
* general documentation updates and improvements in the generation of the documentation.

&nbsp;

___
**Minor corrections after release of IFC4 Add2 schema include:**

* 01. Aug 16 - add _IfcSurfaceCurve_ to select type _IfcCurveOnSurface_ to correct the use of the function _IfcGetBasisSurface_ in where rule CurveIsNotPcurve in _IfcSurfaceCurve_
