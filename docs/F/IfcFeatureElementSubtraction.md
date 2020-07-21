IfcFeatureElementSubtraction
============================
The _IfcFeatureElementSubtraction_ is specialization of the general feature
element, that represents an existence dependent elements which modifies the
shape and appearance of the associated master element. The
_IfcFeatureElementSubtraction_ offers the ability to handle shape modifiers as
semantic objects within the IFC object model that subtract from the shape of
the master element.  
  
> NOTE  A single subtraction feature such as the subtype _IfcOpeningElement_
> is assigned by a single subtraction relationship _IfcRelVoidsElement_ to one
> occurrences of _IfcElement_. It establishes a 1:1 relationship between the
> opening and the element. An element may have several _IfcRelVoidsElement_
> relationships, enabling several voids.  
  
The voiding relationship between a master element and a subtraction feature is
geometrically resolved by a Boolean difference operation.  
  
The local placement for _IfcFeatureElementSubtraction_ is defined in its
supertype _IfcProduct_. It is defined by the _IfcLocalPlacement_, which
defines the local coordinate system that is referenced by all geometric
representations. The local placement is always defined in relation to the
local placement of the building element from which the feature element
substration is substracted:  
  
* The _PlacementRelTo_ relationship of _IfcLocalPlacement_ shall point (if given) to the local placement of the same _IfcElement_, which is used in the _VoidsElements.RelatingElement_ inverse attribute.  
  
> HISTORY  New entity in IFC2x2.  
  
{ .change-ifc2x2}  
> IFC2x2 CHANGE  The entity is introduced as an upward compatible extension of
> the IFC2x platform. It is an intermediate abstract supertype without
> defining its own explicit attributes.  
[ _bSI
Documentation_](https://standards.buildingsmart.org/IFC/DEV/IFC4_2/FINAL/HTML/schema/ifcproductextension/lexical/ifcfeatureelementsubtraction.htm)


Formal Propositions
-------------------
| Rule             | Description   |
|------------------|---------------|
| HasNoSubtraction |               |
| IsNotFilling     |               |

Associations
------------
| Attribute     | Description   |
|---------------|---------------|
| VoidsElements |               |

