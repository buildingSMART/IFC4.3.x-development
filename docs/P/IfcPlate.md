IfcPlate
========
An _IfcPlate_ is a planar and often flat part with constant thickness. A plate
may carry loads between or beyond points of support, or provide stiffening.
The location of the plate (being horizontal, vertical or sloped) is not
relevant to its definition (in contrary to _IfcWall_ and _IfcSlab_ (as floor
slab)).  
  
{ .extDef}  
> NOTE  Definition according to ISO 6707-1: thin, rigid, flat, metal product,
> of a thickness greater than that of a sheet.  
  
Plates are\S\ normally made of steel, other metallic material, or by glass
panels. However the definition of _IfcPlate_ is material independent and
specific material information shall be handled by using
_IfcAssociatesMaterial_ to assign a material specification to the _IfcPlate_.  
  
> NOTE \S\ Although not necessarily, plates are often add-on parts. This is
> represented by the _IfcRelAggregates_ decomposition mechanism used to
> aggregate parts, such as _IfcPlate_, into a container element such as
> _IfcElementAssembly_ or _IfcCurtainWall_.  
  
> NOTE  The representation of a plate in a structural analysis model is
> provided by _IfcStructuralSurfaceMember_ being part of an
> _IfcStructuralAnalysisModel_.  
  
An instance _IfcPlate_ should preferably get its geometric representation and
material assignment through the type definition by _IfcPlateType_ assigned
using the _IfcRelDefinesByType_ relationship. This allows identical plates in
a construction to be represented by the same instance of _IfcPlateType_.  
  
A plate may have openings, such as voids or recesses. They are defined by an
_IfcOpeningElement_ attached to the plate using the inverse relationship
_HasOpenings_ pointing to _IfcRelVoidsElement_. The position number of a plate
as often used in steel construction is assigned through the attribute
_IfcElement.Tag_  
  
The IFC specification provides two entities for plate occurrences:  
  
* _IfcPlateStandardCase_ used for all occurrences of plates, that are prismatic and where the thickness parameter can be fully described by the _IfcMaterialLayerSetUsage_. These plates are always represented geometrically by a ''SweptSolid'' geometry (or by a ''Clipping'' geometry based on ''SweptSolid''), if a 3D geometric representation is assigned. In addition they have to have a corresponding _IfcMaterialLayerSetUsage_ assigned.  
* _IfcPlate_ used for all other occurrences of plates, particularly for plates with changing thickness, or plates with non planar surfaces, and plates having only ''SurfaceModel'' or ''Brep'' geometry.  
  
> HISTORY  New entity in IFC2x2  
[ _bSI
Documentation_](https://standards.buildingsmart.org/IFC/DEV/IFC4_2/FINAL/HTML/schema/ifcsharedbldgelements/lexical/ifcplate.htm)


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

