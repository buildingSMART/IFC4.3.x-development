IfcBeam
=======
An _IfcBeam_ is a horizontal, or nearly horizontal, structural member that is
capable of withstanding load primarily by resisting bending. It represents
such a member from an architectural point of view. It is not required to be
load bearing.  
  
{ .extDef}  
> NOTE  Definition according to ISO 6707-1: structural member for carrying
> load(s) between or beyond points of support, usually narrow in relation to
> its length and horizontal or nearly so.  
  
> NOTE  The representation of load-bearing beams in a structural analysis
> model is provided by subtypes of _IfcStructuralMember_ (with
> _IfcStructuralCurveMember_ being mostly applicable) as part of an
> _IfcStructuralAnalysisModel_.  
  
> NOTE  For any other longitudinal structural member, not constrained to be
> predominately horizontal nor vertical, or where this semantic information is
> irrelevant, the entity _IfcMember_ should be used.  
  
The camber of a beam may be defined by assigning a StructuralCurveMember with
displacement coordinates. Multiple sets of camber ordinates may be provided
that are qualified by the particular load case, where full dead load would
typically be used for fabrication, and other scenarios used for other loading
conditions such as during construction.  
  
There are two entities for beam occurrences:  
  
* _IfcBeamStandardCase_ used for all occurrences of beams, that have a profile defined that is swept along a directrix. The profile might be changed uniformly by a taper definition along the directrix. The profile parameter and its cardinal point of insertion can be fully described by the _IfcMaterialProfileSetUsage_. These beams are always represented geometricly by an ''Axis'' and a ''SweptSolid'' or ''AdvancedSweptSolid'' shape representation (or by a ''Clipping'' geometry based on the swept solid), if a 3D geometric representation is assigned. In addition they have to have a corresponding _IfcMaterialProfileSetUsage_ assigned.   
>> NOTE  Model view definitions and implementer agreements may further
constrain the applicable geometry types, for example, by excluding tapering
from an _IfcBeamStandardCase_ implementation.* _IfcBeam_ used for all other
occurrences of beams, particularly for beams with non-uniformly changing
profile sizes along the sweep, or beams having only ''AdvancedBrep'',
''Brep'', ''SurfaceModel'', or ''Tessellation'' geometry.  
>> NOTE  Model view definitions and implementer agreements may impose the use
of _IfcBeam_ in all cases by excluding _IfcBeamStandardCase_ from scope of the
model view.  
> HISTORY  New entity in IFC1.0  
[ _bSI
Documentation_](https://standards.buildingsmart.org/IFC/DEV/IFC4_2/FINAL/HTML/schema/ifcsharedbldgelements/lexical/ifcbeam.htm)


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

