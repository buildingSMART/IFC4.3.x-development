The _IfcIndexedPolygonalFaceWithVoids_ is a compact representation of a planar face with inner loops, being part of a face set.

<!-- end of short definition -->


> HISTORY New entity in IFC4 Addendum 2.

## Attributes

### InnerCoordIndices
Two-dimensional list, where the first dimension represents each inner loop (from 1 to N) and the second dimension the indices to three or more points that define the vertices of each inner loop. If the tessellated face set is closed, indicated by _SELF\IfcTessellatedFaceSet.Closed_, then the points, defining the inner loops, shall connect clockwise, as seen from the outside of the body.
> NOTE The coordinates of the vertices are provided by the indexed list of _SELF\IfcTessellatedFaceSet.Coordinates.CoordList_. If the _SELF\IfcTessellatedFaceSet.PnIndex_ is provided, the indices point into it, otherwise directly into the _IfcCartesianPointList3D_.
