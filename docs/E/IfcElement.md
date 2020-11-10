IfcElement
==========
An element is a generalization of all components that make up an AEC product.  
  
Elements are physically existent objects, although they might be void
elements, such as holes. Elements either remain permanently in the AEC
product, or only temporarily, as formwork does. Elements can be either
assembled on site or pre-manufactured and built in on site.  
  
> EXAMPLE  Examples of elements in a building construction context are walls,
> floors, windows and recesses.  
  
The elements can be logically contained by a spatial structure element that
constitutes a certain level within a project structure hierarchy (site,
building, storey or space). This is done by using the
_IfcRelContainedInSpatialStructure_ relationship. An element can have material
and quantity information assigned through the _IfcRelAssociatesMaterial_ and
_IfcRelDefinesByProperties_ relationship.  
  
In addition an element can be declared to be a specific occurrence of an
element type (and thereby be defined by the element type properties) using the
_IfcRelDefinesByType_ relationship. An element can also be defined as an
element assembly that is a group of semantically and topologically related
elements that form a higher level part of the AEC product. Those element
assemblies are defined by virtue of the _IfcRelAggregates_ relationship.  
  
> EXAMPLE  Examples for element assembly are complete Roof Structures, made by
> several Roof Areas, or a Stair, composed by Flights and Landings.  
  
Elements that performs the same function may be grouped by an "Element Group
By Function". It is realized by an instance of _IfcGroup_ with the
_ObjectType_ =''ElementGroupByFunction''.  
  
> HISTORY  New entity in IFC1.0  
[ _bSI
Documentation_](https://standards.buildingsmart.org/IFC/DEV/IFC4_2/FINAL/HTML/schema/ifcproductextension/lexical/ifcelement.htm)


Attribute definitions
---------------------
| Attribute               | Description   |
|-------------------------|---------------|
| HasProjections          |               |
| HasOpenings             |               |
| IsConnectionRealization |               |
| HasCoverings            |               |
| ConnectedFrom           |               |
| ContainedInStructure    |               |
| ConnectedTo             |               |
| FillsVoids              |               |
| ProvidesBoundaries      |               |

