IfcPhysicalComplexQuantity
==========================
The complex physical quantity, _IfcPhysicalComplexQuantity_, is an entity that
holds a set of single quantity measure value (as defined at the subtypes of
_IfcPhysicalSimpleQuantity_), that all apply to a given component or aspect of
the element.  
  
> EXAMPLE: A layered element, like a wall, may have several material layers,
> each having individual quantities, like footprint area, side area and
> volume. An instance of _IfcPhysicalComplexQuantity_ would group these
> individual quantities (given by a subtype of _IfcPhysicalSimpleQuantity_)
> and name them according to the material layer name by using the _Name_
> attribute. The _Discrimination_ attribute would then be ''layer''.  
  
A section "Quantity Use Definition" at individual entities as subtypes of
_IfcBuildingElement_ gives guidance to the usage of the _Name_ and
_Discrimination_ attribute to characterize the complex quantities.  
  
> HISTORY  New entity in IFC2x2 Addendum 1.  
  
{ .change-ifc2x2}  
> IFC2x2 ADDENDUM 1 CHANGE  The entity _IfcPhysicalComplexQuantity_ has been
> added. Upward compatibility for file based exchange is guaranteed.  
[ _bSI
Documentation_](https://standards.buildingsmart.org/IFC/DEV/IFC4_2/FINAL/HTML/schema/ifcquantityresource/lexical/ifcphysicalcomplexquantity.htm)


