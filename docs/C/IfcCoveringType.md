IfcCoveringType
===============
The element type _IfcCoveringType_ defines commonly shared information for
occurrences of coverings. The set of shared information may include:  
  
* common properties within shared property sets  
* common material (layer set) information  
* common shape representations  
  
It is used to define an covering specification or covering style (i.e. the
specific product information, that is common to all occurrences of that
product type). Covering types may be exchanged without being already assigned
to occurrences.  
  
The occurrences of the _IfcCoveringType_ are represented by instances of
_IfcCovering_  
  
> HISTORY  New entity in IFC2x2.  
  
{ .spec-head}  
Informal Propositions:  
  
1\. The material assignment, if provided using the _IfcRelAssociatesMaterial_
relationship, shall not reference _IfcMaterialLayerSetUsage_ or
_IfcMaterialProfileSetUsage_.  
[ _bSI
Documentation_](https://standards.buildingsmart.org/IFC/DEV/IFC4_2/FINAL/HTML/schema/ifcsharedbldgelements/lexical/ifccoveringtype.htm)


Attribute definitions
---------------------
| Attribute      | Description   |
|----------------|---------------|
| PredefinedType |               |

