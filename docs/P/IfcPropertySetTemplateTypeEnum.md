IfcPropertySetTemplateTypeEnum
==============================
This enumeration defines the general applicability of instances of
_IfcPropertySet_, or _IfcElementQuantity_ defined by this
_IfcPropertySetTemplate_, to subtypes of _IfcObjectDefinition_.  
  
> HISTORY  New enumeration in IFC4.  
[ _bSI
Documentation_](https://standards.buildingsmart.org/IFC/DEV/IFC4_2/FINAL/HTML/schema/ifckernel/lexical/ifcpropertysettemplatetypeenum.htm)


Attribute definitions
---------------------
| Attribute               | Description                                                                                                                                                                                                  |
|-------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| NOTDEFINED              |                                                                                                                                                                                                              |
| QTO_OCCURRENCEDRIVEN    | The element quantity defined by this _IfcPropertySetTemplate_ can only be\X\0Dassigned to subtypes of _IfcObject_.                                                                                           |
| QTO_TYPEDRIVENONLY      | The element quantity defined by this _IfcPropertySetTemplate_ can only be assigned to subtypes of _IfcTypeObject_.                                                                                           |
| PSET_TYPEDRIVENONLY     | The property sets defined by this _IfcPropertySetTemplate_ can only be assigned to subtypes of _IfcTypeObject_.                                                                                              |
| PSET_PERFORMANCEDRIVEN  | The property sets defined by this _IfcPropertySetTemplate_ can only be assigned to _IfcPerformanceHistory_.                                                                                                  |
| PSET_OCCURRENCEDRIVEN   | The property sets defined by this _IfcPropertySetTemplate_ can only be assigned to subtypes of _IfcObject_.                                                                                                  |
| QTO_TYPEDRIVENOVERRIDE  | The element quantity defined by this _IfcPropertySetTemplate_ can be\X\0Dassigned to subtypes of _IfcTypeObject_ and can be overridden\X\0Dby an element quantity with same name at subtypes of _IfcObject_. |
| PSET_TYPEDRIVENOVERRIDE | The property sets defined by this _IfcPropertySetTemplate_ can be assigned\X\0Dto subtypes of _IfcTypeObject_ and can be overridden by a\X\0Dproperty set with same name at subtypes of _IfcObject_.         |

