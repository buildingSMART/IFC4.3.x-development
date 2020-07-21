IfcIndexedPolygonalFace
=======================
The _IfcIndexedPolygonalFace_ is a compact representation of a planar face
being part of a face set. The vertices of the polygonal planar face are
provided by 3 or more Cartesian points, defined by indices that point into an
_IfcCartesianPointList3D_, either direcly, or via the _PnIndex_, if provided
at _IfcPolygonalFaceSet_.  
  
Figure 1 shows an _IfcIndexedPolygonalFace_ at an _IfcPolygonalFaceSet_ not
using _PnIndex_ (the default).  
  
!["IfcIndexedPolygonalFace"](../figures/ifcindexedpolygonalface_01.png "Figure
1 -- Polygonal face geometry provided by indices into a point list")  
  
  
  
Figure 2 shows an _IfcIndexedPolygonalFace_ at an _IfcPolygonalFaceSet_ using
_PnIndex_.  
  
!["IfcIndexedPolygonalFace us  
ing PnIndex"](../figures/ifcindexedpolygonalface_02.png "Figure 2 -- Polygonal
face geometry provided by indices into a point list")  
  
> HISTORY  New entity in IFC4 Addendum 2.  
[ _bSI
Documentation_](https://standards.buildingsmart.org/IFC/DEV/IFC4_2/FINAL/HTML/schema/ifcgeometricmodelresource/lexical/ifcindexedpolygonalface.htm)


Attribute definitions
---------------------
| Attribute   | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
|-------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| CoordIndex  | One-dimensional list with the indices for the three or more points, that define the vertices of the outer loop. If the tessellated face set is closed, indicated by _SELF\\\IfcTessellatedFaceSet.Closed_, then the points, defining the outer loop, shall connect counter clockwise, as seen from the outside of the body, so that the resulting normal will point outwards.\X\0D> NOTE  The coordinates of the vertices are provided by the indexed list of _SELF\\\IfcTessellatedFaceSet.Coordinates.CoordList_. If the _SELF\\\IfcTessellatedFaceSet.PnIndex_ is provided, the indices point into it, otherwise directly into the _IfcCartesianPointList3D_. |

Associations
------------
| Attribute   | Description   |
|-------------|---------------|
| ToFaceSet   |               |

