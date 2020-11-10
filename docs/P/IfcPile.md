IfcPile
=======
A pile is a slender timber, concrete, or steel structural element, driven,
jetted, or otherwise embedded on end in the ground for the purpose of
supporting a load. A pile is also characterized as deep foundation, where the
loads are transfered to deeper subsurface layers.  
  
{ .extDef}  
> NOTE  Definition according to ISO 6707-1: slender structural member,
> substantially underground, intended to transmit force(s) into loadbearing
> strata below the surface of the ground.  
  
> NOTE  Shallow foundations, which transfer the loads to the ground near its
> surface, are represented by _IfcFooting_.  
  
> HISTORY  New entity in IFC2x2.  
[ _bSI
Documentation_](https://standards.buildingsmart.org/IFC/DEV/IFC4_2/FINAL/HTML/schema/ifcstructuralelementsdomain/lexical/ifcpile.htm)


Attribute definitions
---------------------
| Attribute        | Description                                                                                                                                                                                                                                                                                                                                                                                  |
|------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| PredefinedType   |                                                                                                                                                                                                                                                                                                                                                                                              |
| ConstructionType | Deprecated.\X\0D\X\0D{ .change-ifc2x4}\X\0D> IFC4 CHANGE  Material profile association capability by means of _IfcRelAssociatesMaterial_ has been added. The attribute _ConstructionType_ should not be used whenever its information can be provided by a material profile set, either associated with the _IfcPile_ object or, if present, with a corresponding instance of _IfcPileType_. |

