IfcRelFillsElement
==================
_IfcRelFillsElement_ is an objectified relationship between an opening element
and an element that fills (or partially fills) the opening element. It is an
one-to-one relationship.  
  
> NOTE  View definitions or implementer agreements may restrict an opening to
> be filled by one filling element only.  
  
As shown in Figure 1, the insertion of a door into a wall is represented by
two separate relationships. First the door opening is created within the wall
by _IfcWall(StandardCase) <\-- IfcRelVoidsElement --> IfcOpeningElement_, then
the door is inserted within the opening by _IfcOpeningElement <\--
IfcRelFillsElement --> IfcDoor_.  
  
  
  
!["relationships for filling"](../figures/ifcrelfillselements-fig1.png "Figure
1 -- Relationships for element filling")  
  
> HISTORY  New entity in IFC1.0  
[ _bSI
Documentation_](https://standards.buildingsmart.org/IFC/DEV/IFC4_2/FINAL/HTML/schema/ifcproductextension/lexical/ifcrelfillselement.htm)


Attribute definitions
---------------------
| Attribute              | Description   |
|------------------------|---------------|
| RelatedBuildingElement |               |
| RelatingOpeningElement |               |

