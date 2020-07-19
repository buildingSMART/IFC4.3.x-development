IfcColumn
=========
  
{ .extDef}  
> NOTE  Definition according to ISO 6707-1  
> structural member of slender form, usually vertical, that transmits to its
> base the forces, primarily in compression, that are applied to it.  
  
> NOTE  The representation of a column in a structural analysis model is
> provided by _IfcStructuralCurveMember_ being part of an
> _IfcStructuralAnalysisModel_.  
  
> NOTE  For any longitudial structural member, not constrained to be
> predominately horizontal nor vertical, or where this semantic information is
> irrelevant, the entity _IfcMember_ exists.  
  
The IFC specification provides two entities for column occurrences:  
  
* _IfcColumnStandardCase_ used for all occurrences of columns, tthat have a profile defined that is swept along a directrix. The profile might be changed uniformly by a taper definition along the directrix. The profile parameter and its cardinal point of insertion can be fully described by the _IfcMaterialProfileSetUsage_. These beams are always represented geometricly by an ''Axis'' and a ''SweptSolid'' or ''AdvancedSweptSolid'' shape representation (or by a ''Clipping'' geometry based on the swept solid), if a 3D geometric representation is assigned. In addition they have to have a corresponding _IfcMaterialProfileSetUsage_ assigned.   
>> NOTE  View definitions and implementer agreements may further constrain the
applicable geometry types, for example by excluding tapering from an
_IfcColumnStandardCase_ implementation.  
* _IfcColumn_ used for all other occurrences of columns, particularly for columns with changing profile sizes along the extrusion, or columns defined by non-linear extrusion, or columns having only ''Brep'', or ''SurfaceModel'' geometry.  
  
> HISTORY  New entity in IFC1.0  
[ _bSI
Documentation_](https://standards.buildingsmart.org/IFC/DEV/IFC4_2/FINAL/HTML/schema/ifcsharedbldgelements/lexical/ifccolumn.htm)


