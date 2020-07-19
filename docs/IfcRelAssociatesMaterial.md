IfcRelAssociatesMaterial
========================
_IfcRelAssociatesMaterial_ is an objectified relationship between a material
definition and elements or element types to which this material definition
applies.  
  
The material definition can be:  
  
* assigned to an element occurrence as a specific usage of a layer set or profile set  
* assigned to an element occurrence or element type as a layer set, profile set, constituent set or a single material  
  
Materials can be arranged by layers and applied to layered elements. Typical
elements are walls and slabs.  
  
* An _IfcMaterialLayerSet_, for layered elements with an indication of the layering direction and individual layer thicknesses  
* An _IfcMaterialLayerSetUsage_, i.e. a material layer set with positioning information along the reference axis or surface of the element.   
>> NOTE  As a material layer set usage is an occurrence based information,
that applies to each individual element, it cannot be assigned to an element
type.  
  
Material can be applied to profiles. Typical elements using profile material
are beam, column, member  
  
* An _IfcMaterialProfileSet_, i.e. a set of material assigned to a set of profiles, with a single material assigned to a single profile as the default.  
* An _IfcMaterialProfileSetUsage_, i.e. a material profile set with positioning information relative to the element axis, also refered to as cardinal point.   
>> NOTE  As a material profile set usage is an occurrence based information,
that applies to each individual element, it cannot be assigned to an element
type.  
  
Materials can be arranged by identified parts of a component based element.
Typical elements are dorrs/windows (with components such as lining, framing
and glazing), or distribution elements.  
  
* An _IfcMaterialConstituentSet_, for component based elements with an indication of the component by keyword to which the material consituent applies.   
>> NOTE  See the material use definitions at each applicable subtype of
_IfcElement_ or _IfcElementType_ for a provision of these keywords.  
  
As a fallback, or in cases where only a single material information is needed,
material information can be directly associated  
  
* A single _IfcMaterial_ for any element where the material use definition does not prohibits its direct association  
* An _IfcMaterialList_, e.g. for composite elements, without an information, how the different materials are arranged.   
>> DEPRECATED  The use of _IfcMaterialList_ is deprecated in IFC4 onwards. Use
_IfcMaterialConstituentSet_ instead.  
  
The _IfcRelAssociatesMaterial_ relationship is a special type of the
_IfcRelAssociates_ relationship. It can be applied to subtypes of _IfcElement_
and subtypes of _IfcElementType_.  
  
* The _IfcElement_ has an inverse relation to its material definition by the _HasAssociations_ attribute, inherited from _IfcObject_.  
* The _IfcElementType_ has an inverse relation to its material definition by the _HasAssociations_ attribute, inherited from _IfcPropertyDefinition_.  
  
If both, the element occurrence (by an instance of _IfcElement_) and the
element type (by an instance of _IfcElementType_, connected through
_IfcRelDefinesByType_) have an associated material, then the material
associated to the element occurrence overrides the material associated to the
element type.  
  
> HISTORY  New entity in IFC2x.  
  
{ .spec-head}  
Informal Propositions:  
  
1\. An _IfcMaterialLayerSetUsage_ shall not be associated with a subtype of
_IfcElementType_, it should only be associated with individual occurrences  
2\. An _IfcMaterialProfileSetUsage_ shall not be associated with a subtype of
_IfcElementType_, it should only be associated with individual occurrences  
[ _bSI
Documentation_](https://standards.buildingsmart.org/IFC/DEV/IFC4_2/FINAL/HTML/schema/ifcproductextension/lexical/ifcrelassociatesmaterial.htm)


