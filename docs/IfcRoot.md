IfcRoot
=======
_IfcRoot_ is the most abstract and root class for all entity definitions that
roots in the kernel or in subsequent layers of the IFC specification. It is
therefore the common supertype of all IFC entities, beside those defined in an
IFC resource schema. All entities that are subtypes of _IfcRoot_ can be used
independently, whereas resource schema entities, that are not subtypes of
_IfcRoot_, are not supposed to be independent entities.  
  
> NOTE  View definitions and implementation agreement may impose additional
> restrictions on the use of the _OwnerHistory_ to handle object versioning.  
  
> HISTORY  New entity in IFC1.0  
  
{ .change-ifc2x4}  
> IFC4 CHANGE  The attribute _OwnerHistory_ has been made OPTIONAL.  
[ _bSI
Documentation_](https://standards.buildingsmart.org/IFC/DEV/IFC4_2/FINAL/HTML/schema/ifckernel/lexical/ifcroot.htm)


