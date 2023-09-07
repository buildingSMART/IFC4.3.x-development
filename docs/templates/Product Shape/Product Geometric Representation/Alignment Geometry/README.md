Alignment Geometry
==================

Supported shape representations of _IfcAlignment_ are:

* _IfcCompositeCurve_ as a 2D horizontal alignment (represented by its horizontal alignment segments), without a vertical layout.
* _IfcGradientCurve_ as a 3D horizontal and vertical alignment (represented by their alignment segments), without a cant layout.
* _IfcSegmentedReferenceCurve_ as a 3D curve defined relative to an _IfcGradientCurve_ to incorporate the application of cant.
* _IfcOffsetCurveByDistances_ as a 2D or 3D curve defined relative to an _IfcGradientCurve_ or another _IfcOffsetCurveByDistances_.
* _IfcPolyline_ or _IfcIndexedPolyCurve_ as a 3D alignment by a 3D polyline representation (such as coming from a survey).
* _IfcPolyline_ or _IfcIndexedPolyCurve_ as a 2D horizontal alignment by a 2D polyline representation (such as in very early planning phases or as a map representation).

Refer to the following Alignment Geometry concept templates to know which _RepresentationIdentifier_ and _RepresentationType_ shall be set for the different representations and the different layouts' configurations of _IfcAlignment_.
