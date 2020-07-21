IfcMember
=========
An _IfcMember_ is a structural member designed to carry loads between or
beyond points of support. It is not required to be load bearing. The
orientation of the member (being horizontal, vertical or sloped) is not
relevant to its definition (in contrary to _IfcBeam_ and _IfcColumn_). An
_IfcMember_ represents a linear structural element from an architectural or
structural modeling point of view and shall be used if it cannot be expressed
more specifically as either an _IfcBeam_ or an _IfcColumn_.  
> NOTE The representation of a member in a structural analysis model is
> provided by _IfcStructuralCurveMember_ being part of an
> _IfcStructuralAnalysisModel_.  
The IFC specification provides two entities for member occurrences:  

  

  * _IfcMemberStandardCase_ used for all occurrences of members, that have a profile defined that is swept along a directrix. The profile might be changed uniformly by a taper definition along the directrix. The profile parameter and its cardinal point of insertion can be fully described by the _IfcMaterialProfileSetUsage_. These beams are always represented geometricly by an ''Axis'' and a ''SweptSolid'' or ''AdvancedSweptSolid'' shape representation (or by a ''Clipping'' geometry based on the swept solid), if a 3D geometric representation is assigned. In addition they have to have a corresponding _IfcMaterialProfileSetUsage_ assigned.   
  
> NOTE View definitions and implementer agreements may further constrain the
> applicable geometry types, such as by excluding tapering from an
> _IfcMemberStandardCase_ implementation.
  

  * _IfcMember_ used for all other occurrences of members, particularly for members with changing profile sizes along the extrusion, or members defined by non-linear extrusion, or members having only ''Brep'', or ''SurfaceModel'' geometry.
  

  
> HISTORY New entity in IFC2x2 Addendum 1.  
[ _bSI
Documentation_](https://standards.buildingsmart.org/IFC/DEV/IFC4_2/FINAL/HTML/schema/ifcsharedbldgelements/lexical/ifcmember.htm)


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

