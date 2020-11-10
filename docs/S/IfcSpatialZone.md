IfcSpatialZone
==============
A spatial zone is a non-hierarchical and potentially overlapping decomposition
of the project under some functional consideration. A spatial zone might be
used to represent a thermal zone, a construction zone, a lighting zone, a
usable area zone. A spatial zone might have its independent placement and
shape representation.  
The [_IfcSpatialZone_]($element://{C6BFC05D-09D4-4bed-92A9-1823739DE0C8})
inherits and declares these attributes that shall have the following meaning:  

  

  * _Name_ : A number or designator provided by the user or system for the spatial element, e.g. a space number "1-003", could also be a running number provided by default by the application
  

  * _LongName_ : Name of the spatial element provided by the user, e.g. a space name "Office".
  

  * _Description_ : Any additional description provided by the user, e.g. a space description "Corner office with habour view".
  

  * _ObjectType_ : reserved for typing of spatial elements in case of _PredefinedType_ = .USERDEFINED., restrictions on applicable values might be published in view definitions or implementer agreements.
  

  
Physical elements that are referenced by this spatial zone are related using
the
[_IfcRelReferencedInSpatialStructure_]($element://{415054A4-1479-4c32-9A58-BC1E36A488CC})
relationship as it is a non-hierarchical assignment in addition to the
hierarchical spatial containment within a subtype of
[_IfcSpatialStructureElement_]($element://{30E08EC3-5B14-45f4-8246-B4811D2ECF1B}).
Also spaces, that referenced by this spatial zone are related using the
[_IfcRelReferencedInSpatialStructure_]($element://{415054A4-1479-4c32-9A58-BC1E36A488CC})
relationship. The
[_IfcSpatialZone_]($element://{C6BFC05D-09D4-4bed-92A9-1823739DE0C8}) itself
can also be referenced by another spatial element using
[_IfcRelReferencedInSpatialStructure_]($element://{415054A4-1479-4c32-9A58-BC1E36A488CC})
.  
NOTE The [_IfcSpatialZone_]($element://{C6BFC05D-09D4-4bed-92A9-1823739DE0C8})
is different to the
[_IfcZone_]($element://{F02CE4C4-BC52-4eb7-8FFD-A44181BDDF63}) entity by
allowing an own placement and shape representation, whereas
[_IfcZone_]($element://{F02CE4C4-BC52-4eb7-8FFD-A44181BDDF63}) is only a
grouping of [_IfcSpace_]($element://{51F70274-0484-4e6b-899A-1D0445F25124})'s.  
HISTORY New entity in IFC4.  
[ _bSI
Documentation_](https://standards.buildingsmart.org/IFC/DEV/IFC4_2/FINAL/HTML/schema/ifcproductextension/lexical/ifcspatialzone.htm)


Attribute definitions
---------------------
| Attribute      | Description   |
|----------------|---------------|
| PredefinedType |               |

