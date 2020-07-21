IfcBuiltElement
===============
The built element comprises all elements that are primarily part of the
construction of a built facility, i.e., its structural and space separating
system. Built elements are all physically existent and tangible things  
> NOTE Definition from ISO 6707-1: Major functional part of a building,
> examples are foundation, floor, roof, wall.  
This _IfcBuiltElement_ is a generalization of all elements that participate in
a building system. Typical examples of __IfcBuiltElement__'s are (among
others):  

  

  * built elements within a space separation systems
  

  * built elements within an enclosure system (such as a facade)
  

  * built elements within a fenestration system
  

  * built elements within a load bearing system
  

  * built elements within a foundation system
  

  
> EXAMPLE built elements are walls, curtain wall, doors, columns, pile, and
> others.  
REMOVE{ The _IfcBuiltElement_ is an abstract entity that cannot be
instantiated. For arbitrary building elements, that cannot be expressed by a
subtype of _IfcBuiltElement_, use _IfcBuiltElementProxy_.}  
The IfcBuiltElement can be instantiated in the case when arbitrary built
elements cannot be expressed by a subtype of IfcBuiltElement.  
> HISTORY New entity in IFC1.0  
[ _bSI
Documentation_](https://standards.buildingsmart.org/IFC/DEV/IFC4_2/FINAL/HTML/schema/ifcproductextension/lexical/ifcbuildingelement.htm)


Formal Propositions
-------------------
| Rule                      | Description   |
|---------------------------|---------------|
| MaxOneMaterialAssociation |               |

