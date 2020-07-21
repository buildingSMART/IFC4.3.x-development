IfcBuildingElementPart
======================
[_IfcBuildingElementPart_]($element://{9D8E729C-E134-42d6-A098-4EB19D03B8EB})
represents major components as subordinate parts of a building element.
Typical usage examples include precast concrete sandwich walls, where the
layers may have different geometry representations. In this case the layered
material representation does not sufficiently describe the element. Each layer
is represented by an own instance of the
[_IfcBuildingElementPart_]($element://{9D8E729C-E134-42d6-A098-4EB19D03B8EB})
with its own geometry description.  
The kind of building element part is further specified by a corresponding
instance of
[_IfcBuildingElementPartType_]($element://{D5FF49E6-0638-4407-962C-5C7551B7B8EB}),
referred to by
[_IfcRelDefinesByType_]($element://{8FEACB46-E1AA-4065-BC99-1175273FEBAC}).  
> HISTORY New entity in IFC2x2.  
[ _bSI
Documentation_](https://standards.buildingsmart.org/IFC/DEV/IFC4_2/FINAL/HTML/schema/ifcsharedcomponentelements/lexical/ifcbuildingelementpart.htm)


Attribute definitions
---------------------
| Attribute      | Description   |
|----------------|---------------|
| PredefinedType |               |

Formal Propositions
-------------------
| Rule                  | Description   |
|-----------------------|---------------|
| CorrectPredefinedType |               |
| CorrectTypeAssigned   |               |

Associations
------------
| Attribute      | Description   |
|----------------|---------------|
| PredefinedType |               |

