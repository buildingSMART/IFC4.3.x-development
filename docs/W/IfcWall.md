IfcWall
=======
The wall represents a vertical construction that may bound or subdivide
spaces. Wall are usually vertical, or nearly vertical, planar elements, often
designed to bear structural loads. A wall is however\S\ not required to be
load bearing.

Test
  
> NOTE  Definition according to ISO 6707-1: vertical construction usually in
> masonry or in concrete which bounds or subdivides a construction works and
> fulfils a load bearing or retaining function.  
  
> NOTE  There is a representation of walls for structural analysis provided by
> a proper subtype of _IfcStructuralMember_ being part of the
> _IfcStructuralAnalysisModel_.  
  
> NOTE  An arbitrary planar element to which this semantic information is not
> applicable (is not predominantly vertical), shall be modeled as _IfcPlate_.  
  
A wall may have openings, such as wall openings, openings used for windows or
doors, or niches and recesses. They are defined by an _IfcOpeningElement_
attached to the wall using the inverse relationship _HasOpenings_ pointing to
_IfcRelVoidsElement_.  
  
> NOTE  Walls with openings that have already been modeled within the
> enclosing geometry may use the relationship _IfcRelConnectsElements_ to
> associate the wall with embedded elements such as doors and windows.  
  
There are three entities for wall occurrences:  
  
* _IfcWallStandardCase_ \S\ used for all occurrences of walls, that have a non-changing thickness along the wall path and where the thickness parameter can be fully described by a material layer set. These walls are always represented geometrically by an ''Axis'' and a ''SweptSolid'' shape representation (or by a ''Clipping'' geometry based on ''SweptSolid''), if a 3D geometric representation is assigned. In addition they have to have a corresponding _IfcMaterialProfileSetUsage_ assigned.  
* _IfcWallElementedCase_ used for occurrences of walls which are aggregated from subordinate elements, following specific decomposition rules expressed by the mandatory use of _IfcRelAggregates_ relationship.  
* _IfcWall_ \S\ used for all other occurrences of wall, particularly for walls with changing thickness along the wall path (e.g. polygonal walls), or walls with a non-rectangular cross sections (e.g. L-shaped retaining walls), and walls having an extrusion axis that is unequal to the global Z axis of the project (i.e. non-vertical walls), or walls having only ''Brep'', or ''SurfaceModel'' geometry.  
  
> HISTORY  New entity in IFC1.0  
[ _bSI
Documentation_](https://standards.buildingsmart.org/IFC/DEV/IFC4_2/FINAL/HTML/schema/ifcsharedbldgelements/lexical/ifcwall.htm)


Formal Propositions
-------------------
| Rule                  | Description   |
|-----------------------|---------------|
| CorrectPredefinedType |               |
| CorrectTypeAssigned   |               |

Associations
------------
| Attribute      | Description   |
|----------------|---------------|
| PredefinedType |               |

