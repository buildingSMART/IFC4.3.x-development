IfcReinforcingElement
=====================
A reinforcing element represents bars, wires, strands, meshes, tendons, and
other components embedded in concrete in such a manner that the reinforcement
and the concrete act together in resisting forces.  
  
{ .extDef}  
> NOTE  Definition according to ISO 6707-1: rod(s), bar(s), fabric, fibres,
> wires and cable(s) added to give additional strength or support to a
> material or component.  
  
One or several instances of subtypes of _IfcReinforcingElement_ should always
be accompanied by a defining instance of a respective subtype of
_IfcReinforcingElementType_. The type object holds shape and material
information.  
  
> HISTORY  New entity in IFC2x2  
  
{ .change-ifc2x4}  
> IFC4 CHANGE  Attribute _SteelGrade_ deprecated.  
[ _bSI
Documentation_](https://standards.buildingsmart.org/IFC/DEV/IFC4_2/FINAL/HTML/schema/ifcstructuralelementsdomain/lexical/ifcreinforcingelement.htm)


Attribute definitions
---------------------
| Attribute   | Description                                                                                                                                      |
|-------------|--------------------------------------------------------------------------------------------------------------------------------------------------|
| SteelGrade  | Deprecated.\X\0D\X\0D{ .change-ifc2x4}\X\0D> IFC4 CHANGE  Attribute deprecated. Use material association at _IfcReinforcingElementType_ instead. |

