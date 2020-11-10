IfcSlabType
===========
The element type _IfcSlabType_ defines commonly shared information for
occurrences of slabs. The set of shared information may include:  
  
* common properties within shared property sets  
* common material information  
* common material layer definitions  
* common shape representations  
  
> NOTE  It is illegal to share shape representations as representation maps
> for occurrences of _IfcSlabStandardCase_.  
  
It is used to define a slab specification (i.e. the specific product
information, that is common to all occurrences of that product type). Slab
types may be exchanged without being already assigned to occurrences.  
  
> NOTE  The product representations are defined as representation maps (at the
> level of the supertype _IfcTypeProduct_, which gets assigned by an element
> occurrence instance through the _IfcShapeRepresentation.Item[1]_ being an
> _IfcMappedItem_.  
  
The occurrences of the _IfcSlabType_ within building models are represented by
instances of _IfcSlabStandardCase_ if the _IfcSlabType_ has a single
associated _IfcMaterialLayerSet_; otherwise they are represented by instances
of _IfcSlab_, or _IfcSlabElementedCase_.  
  
> HISTORY  New entity in IFC2x2.  
  
{ .spec-head}  
Informal Propositions:  
  
1\. The material assignment, if provided using the _IfcRelAssociatesMaterial_
relationship, shall not reference the _IfcMaterialLayerSetUsage_.  
[ _bSI
Documentation_](https://standards.buildingsmart.org/IFC/DEV/IFC4_2/FINAL/HTML/schema/ifcsharedbldgelements/lexical/ifcslabtype.htm)


Attribute definitions
---------------------
| Attribute      | Description   |
|----------------|---------------|
| PredefinedType |               |

