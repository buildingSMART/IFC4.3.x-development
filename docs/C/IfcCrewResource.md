IfcCrewResource
===============
_IfcCrewResource_ represents a collection of internal resources used in
construction processes.  
  
> HISTORY  New entity in IFC2.0.  
  
Identification of people and equipment of a crew is achieved through their
specification at the level of the component. Therefore, knowing which persons
are within a crew is achieved through identifying the persons assigned to each
_IfcLaborResource_ within the _IfcCrewResource_. Similarly, identifying that a
screwing machine for pipe fitting forms part of the crew is achieved by
relating an appropriate instance of _IfcElementComponent_ to the
_IfcConstructionEquipmentResource_ forming an element of the
_IfcCrewResource_.  
[ _bSI
Documentation_](https://standards.buildingsmart.org/IFC/DEV/IFC4_2/FINAL/HTML/schema/ifcconstructionmgmtdomain/lexical/ifccrewresource.htm)


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

