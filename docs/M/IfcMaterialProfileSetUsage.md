IfcMaterialProfileSetUsage
==========================
_IfcMaterialProfileSetUsage_ determines the usage of _IfcMaterialProfileSet_
in terms of its location relative to the associated element geometry. The
location of a material profile set shall be compatible with the building
element geometry (that is, material profiles shall fit inside the element
geometry). The rules to ensure the compatibility depend on the type of the
building element. For building elements with shape representations which are
based on extruded solids, this is accomplished by referring to the identical
profile definition in the shape model as in the material profile set.  
  
> NOTE  Model view definitions or implementer agreements may provide more
> instructions on matching between building element geometry and material
> profile set usage.  
  
> NOTE  The referenced _IfcMaterialProfileSet_ may represent a single material
> profile, or a composite profile with two or more material profiles.  
  
> HISTORY\S\ New entity in IFC4.  
[ _bSI
Documentation_](https://standards.buildingsmart.org/IFC/DEV/IFC4_2/FINAL/HTML/schema/ifcmaterialresource/lexical/ifcmaterialprofilesetusage.htm)


Attribute definitions
---------------------
| Attribute       | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
|-----------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ForProfileSet   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| CardinalPoint   | Index reference to a significant point in the section profile. Describes how the section is aligned relative to the (longitudinal) axis of the member it is associated with. This parametric specification of profile alignment can be provided redundantly to the explicit alignment defined by ForProfileSet.MaterialProfiles[\\\\*].Profile.                                                                                                                                                                                                                                                                                                                                               |
| ReferenceExtent | Extent of the extrusion of the elements body shape representation to which the _IfcMaterialProfileSetUsage_ applies. It is used as the reference value for the upper _OffsetValues[2]_ provided by the _IfcMaterialProfileSetWithOffsets_ subtype for included material profiles.\X\0D\X\0D> NOTE  The attribute _ReferenceExtent_ shall be asserted if an _IfcMaterialProfileSetWithOffsets_ is included in the _ForProfileSet.MaterialProfiles_ list of material layers.\X\0D\X\0D> NOTE  The _ReferenceExtent_ for _IfcBeamStandardCase_, _IfcColumnStandardCase_, and _IfcMemberStandardCase_ is the reference length starting at z=0 being the XY plane of the object coordinate system. |

