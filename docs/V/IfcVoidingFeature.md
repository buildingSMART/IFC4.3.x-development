IfcVoidingFeature
=================
A voiding feature is a modification of an element which reduces its volume.
Such a feature may be manufactured in different ways, for example by cutting,
drilling, or milling of members made of various materials, or by inlays into
the formwork of cast members made of materials such as concrete.  
  
The standard use of instances of _IfcVoidingFeature_ is as a part of element
type objects (instances of subtypes of _IfcElementType_). The part-whole
relationship is established by an aggregation relationship object, expressing
the decomposition of an element type into one or more additive elements
(element parts) and zero or more feature elements.  
  
> HISTORY  New entity in IFC4.  
  
{ .use-head}  
Containment Use Definition  
  
Voiding features shall have no spatial containment relationship to the spatial
structure since they are dependent on element types without spatial
containment relationships or on an element occurrence with own spatial
containment relationship.  
  
* The _SELF\\\IfcElement.ContainedInStructure_ relationship shall be NIL.  
[ _bSI
Documentation_](https://standards.buildingsmart.org/IFC/DEV/IFC4_2/FINAL/HTML/schema/ifcstructuralelementsdomain/lexical/ifcvoidingfeature.htm)


Formal Propositions
-------------------
| Rule          | Description   |
|---------------|---------------|
| HasObjectType |               |

Associations
------------
| Attribute      | Description   |
|----------------|---------------|
| PredefinedType |               |

