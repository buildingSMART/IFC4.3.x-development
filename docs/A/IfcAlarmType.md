IfcAlarmType
============
The distribution control element type **IfcAlarmType** defines commonly shared
information for occurrences of alarms. The set of shared information may
include:  
  
* common properties with shared property sets  
* common representations  
* common materials  
* common composition of elements  
* common ports  
  
It is used to define a alarm type specification indicating the specific
product information that is common to all occurrences of that product type.
The **IfcAlarmType** may be declared within _IfcProject_ or
_IfcProjectLibrary_ using _IfcRelDeclares_ and may be exchanged with or
without occurrences of the type. Occurrences of **IfcAlarmType** are
represented by instances of _IfcAlarm_. Refer to the documentation at
_IfcAlarm_ for supported property sets, materials, composition, and ports.  
  
> HISTORY  New entity in IFC2x2  
[ _bSI
Documentation_](https://standards.buildingsmart.org/IFC/DEV/IFC4_2/FINAL/HTML/schema/ifcbuildingcontrolsdomain/lexical/ifcalarmtype.htm)


Formal Propositions
-------------------
| Rule                  | Description   |
|-----------------------|---------------|
| CorrectPredefinedType |               |

Associations
------------
| Attribute      | Description   |
|----------------|---------------|
| PredefinedType |               |

