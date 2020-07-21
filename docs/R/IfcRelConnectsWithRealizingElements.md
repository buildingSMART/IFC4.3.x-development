IfcRelConnectsWithRealizingElements
===================================
_IfcRelConnectsWithRealizingElements_ defines a generic relationship that is
made between two elements that require the realization of that relationship by
means of further realizing elements.  
  
An _IfcRelConnectsWithRealizingElements_ is a specialization of
_IfcRelConnectsElement_ where the connecting operation has the additional
attribute of (one or many) realizing elements that may be used to realize or
further qualify the relationship. It is defined as a ternary relationship.  
  
> EXAMPLE  It may be used to describe the attachment of one element to another
> where the attachment is realized by a ''fixing'' element such as a bracket.
> It may also be used to describe the mounting of one element onto another
> such as the requirement for the mounting major plant items onto builders
> work bases and/or anti-vibration isolators.  
  
> HISTORY  New entity in IFC2x2.  
  
> NOTE  Regarding bridge prestressing, the tendon conduits and the tendon
> anchors are aggregated into the concrete elements, but not always the tendon
> itself (as the tendon may pass through several elements). Therefore, it is
> good practise to use RelConnects relationships between the tendon and the
> tendon conduits and the tendon anchors.  
  
The connection types for bridges include:  
  
* TrussJoint: Joint between truss members.  
* ExpansionJoint: Joint allowing movement, usually due to thermal expansion difference in structures, with DiscreteAccessory of type EXPANSION_JOINT_DEVICE as RealizingElement.  
* EmbeddedPartsJoint: Joint for auxiliary parts to structure, with appropriate RealizingElements, such as DiscreteAccessories of type ANCHORPLATE, BRACKET or SHOE.   
* ConstructionJoint: Joint for phasing of construction, typically in in-situ concrete structures.  
[ _bSI
Documentation_](https://standards.buildingsmart.org/IFC/DEV/IFC4_2/FINAL/HTML/schema/ifcproductextension/lexical/ifcrelconnectswithrealizingelements.htm)


Attribute definitions
---------------------
| Attribute      | Description                                                                                                                              |
|----------------|------------------------------------------------------------------------------------------------------------------------------------------|
| ConnectionType | The type of the connection given for informal purposes, it may include labels, like ''joint'', ''rigid joint'', ''flexible joint'', etc. |

Associations
------------
| Attribute         | Description   |
|-------------------|---------------|
| RealizingElements |               |

