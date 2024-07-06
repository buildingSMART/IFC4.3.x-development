The function gets the representation type and the assigned set of representation items as input and verifies whether the correct items are assigned according to the representation type given.

<!-- end of short definition -->


> HISTORY New function in IFC2x.

> IFC2x3 CHANGE The check for _MappedRepresentation_ has been changed to allow multiple mapped items, and the _Annotation2D_ has been added.

> IFC2x4 CHANGE The check for _Curve3D_, _Surface2D_, _Surface3D_, _Tessellation_, _AdvancedBrep_, and _AdvancedSweptSolid_ has been added and _CSG_ enhanced.

> IFC4.3.0.0 CHANGE The check for _Segment_, and _SectionedSurface_ has been added

> IFC4.3.2.0 CHANGE The check for _Point_ has been broadened to also include subtypes of IfcCartesianPointList. The identifier _PointCloud_ has been kept for backwards compatibility.
