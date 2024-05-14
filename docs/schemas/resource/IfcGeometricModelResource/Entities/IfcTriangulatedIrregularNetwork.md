# IfcTriangulatedIrregularNetwork

The _IfcTriangulatedIrregularNetwork_ is a triangulated face set for representing horizontal surfaces (one unique Z coordinate for all X and Y coordinates within domain) with additional flags for each face indicating breaklines between faces or designation as a hole or void. Triangles shall be defined with vertices in counterclockwise order as viewing from above (following right-hand rule).<!-- end of definition -->

For visualization, applications should not display faces where flags are set as negative (either a hole, void, or possible future extension).

The flag _Void_ shall be used to indicate that faces are to be excluded without falling back on any other geometry. Such designation could be used for portions of a site beneath a building or other structure.

The flag _Hole_ shall be used to indicate that faces are to be excluded but may fall back on other geometry. Such designation could be used for portions of a proposed site that are to remain unchanged (conforming to an existing site that may also be defined)

For scenarios where multiple surfaces used as input are to be combined, any triangles marked _Void_ shall be retained as voids, while any triangles marked as _Hole_ shall be overridden if another surface has visible geometry defined within the same horizontal location.

## Attributes

### Flags
Indicates attributes of each triangle in a compact form as follows: -2 = invisible void; -1 = invisible hole; 0 = no breaklines; 1 = breakline at edge 1; 2 = breakline at edge 2; 3 = breakline at edges 1 and 2; 4 = breakline at edge 3; 5 = breakline at edges 1 and 3; 6 = breakline at edges 2 and 3; 7 = breakline at edges 1, 2, and 3.

## Formal Propositions

### NotClosed
The triangulated face set shall not be closed.
