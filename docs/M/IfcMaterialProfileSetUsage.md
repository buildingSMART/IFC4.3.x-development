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


