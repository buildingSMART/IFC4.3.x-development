In most cases the case the IfcDirectrixDerivedReferenceSweptAreaSolid has exactly the same behavior as IfcFixedReferenceSweptAreaSolid, except when the Directrix not only defines a tangent direction but a tangent plane for each point on the curve. Like for example in the case of a IfcSegmentReferenceCurve, the change in y direction of the tangent plane is added to the fixed reference. The change in y direction at the start of the directrix is defined to be 0 independent from StartParam value, this means the change can be non-zero at the start of the resulting Swept Area Solid.

<!-- end of short definition -->

