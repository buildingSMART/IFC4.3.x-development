IfcSimplePropertyTemplateTypeEnum
=================================
This enumeration defines the correct subtype of instances of
_IfcSimpleProperty_ or _IfcPhysicalSimpleQuantity_ that are created and are
assigned to this _IfcSimplePropertyTemplate_. It also determines how the
attributes of _IfcPropertyTemplate_, _PrimaryUnit_, _SecondaryUnit_,
_Enumerators_, _PrimaryDataType_, _SecondaryDataType_, should be used.  
  
> HISTORY  New enumeration in IFC4.  
[ _bSI
Documentation_](https://standards.buildingsmart.org/IFC/DEV/IFC4_2/FINAL/HTML/schema/ifckernel/lexical/ifcsimplepropertytemplatetypeenum.htm)


Attribute definitions
---------------------
| Attribute         | Description                                                                                    |
|-------------------|------------------------------------------------------------------------------------------------|
| P_SINGLEVALUE     | The properties defined by this _IfcPropertyTemplate_ are of type _IfcPropertySingleValue_.     |
| P_TABLEVALUE      | The properties defined by this _IfcPropertyTemplate_ are of type _IfcPropertyTableValue_.      |
| Q_WEIGHT          | The properties defined by this _IfcPropertyTemplate_ are of type _IfcQuantityWeight_.          |
| Q_COUNT           | The properties defined by this _IfcPropertyTemplate_ are of type _IfcQuantityCount_.           |
| P_LISTVALUE       | The properties defined by this _IfcPropertyTemplate_ are of type _IfcPropertyListValue_.       |
| Q_TIME            | The properties defined by this _IfcPropertyTemplate_ are of type _IfcQuantityTime_.            |
| Q_LENGTH          | The properties defined by this _IfcPropertyTemplate_ are of type _IfcQuantityLength_.          |
| P_ENUMERATEDVALUE | The properties defined by this _IfcPropertyTemplate_ are of type _IfcPropertyEnumeratedValue_. |
| Q_VOLUME          | The properties defined by this _IfcPropertyTemplate_ are of type _IfcQuantityVolume_.          |
| P_BOUNDEDVALUE    | The properties defined by this _IfcPropertyTemplate_ are of type _IfcPropertyBoundedValue_.    |
| P_REFERENCEVALUE  | The properties defined by this _IfcPropertyTemplate_ are of type _IfcPropertyReferenceValue_.  |
| Q_AREA            | The properties defined by this _IfcPropertyTemplate_ are of type _IfcQuantityArea_.            |

