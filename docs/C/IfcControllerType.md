IfcControllerType
=================
The distribution control element type **IfcControllerType** defines commonly
shared information for occurrences of controllers. The set of shared
information may include:  
  
* common properties with shared property sets  
* common representations  
* common materials  
* common composition of elements  
* common ports  
  
It is used to define a controller type specification indicating the specific
product information that is common to all occurrences of that product type.
The **IfcControllerType** may be declared within _IfcProject_ or
_IfcProjectLibrary_ using _IfcRelDeclares_ and may be exchanged with or
without occurrences of the type. Occurrences of **IfcControllerType** are
represented by instances of _IfcController_. Refer to the documentation at
_IfcController_ for supported property sets, materials, composition, and
ports.  
  
> HISTORY  New entity in IFC2x2  
[ _bSI
Documentation_](https://standards.buildingsmart.org/IFC/DEV/IFC4_2/FINAL/HTML/schema/ifcbuildingcontrolsdomain/lexical/ifccontrollertype.htm)


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

