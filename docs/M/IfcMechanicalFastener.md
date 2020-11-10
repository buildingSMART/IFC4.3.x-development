IfcMechanicalFastener
=====================
A mechanical fasteners connecting building elements or parts mechanically. A
single instance of this class may represent one or many of actual mechanical
fasteners, for example an array of bolts or a row of nails.  
> HISTORY New entity in IFC2x2  
IFC4 CHANGE Supertype changed from IfcFastener to IfcElementComponent.
Attribute PredefinedType added. Attributes NominalDiameter and NominalLength
deprecated.  
[ _bSI
Documentation_](https://standards.buildingsmart.org/IFC/DEV/IFC4_2/FINAL/HTML/schema/ifcsharedcomponentelements/lexical/ifcmechanicalfastener.htm)


Attribute definitions
---------------------
| Attribute       | Description                                                                                                                                                                                                               |
|-----------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| NominalDiameter | The nominal diameter describing the cross-section size of the fastener type.\X\0D\X\0D{ .change-ifc2x4}\X\0D> IFC4 CHANGE  Deprecated; the respective attribute of _IfcMechanicalFastenerType_ should be used instead.    |
| NominalLength   | The nominal length describing the longitudinal dimensions of the fastener type.\X\0D\X\0D{ .change-ifc2x4}\X\0D> IFC4 CHANGE  Deprecated; the respective attribute of _IfcMechanicalFastenerType_ should be used instead. |
| PredefinedType  |                                                                                                                                                                                                                           |

