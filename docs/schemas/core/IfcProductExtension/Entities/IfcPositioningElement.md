# IfcPositioningElement

New and abstract entity definition for positioning and annotating elements that are used to position other elements relatively.

> EXAMPLE  A grid is a positioning element to position building components mainly in vertical structures, an alignment is a linear positioning element to position geographic and civil elements mainly in infrastructure works.

> EXAMPLE  An alignment is a linear positioning element for using a linear referencing method to position other items. See ISO 19148 “Linear referencing” for general information about linear referencing methods and expressions.

## Attributes

### ContainedInStructure
Relationship to a spatial structure element, to which the positioning element is primarily associated.
{ .change-ifc2x}
> IFC2x CHANGE  The inverse relationship has been added to _IfcGrid_ with upward compatibility

{ .change-ifc4}
> IFC4 CHANGE  The inverse relationship has been promoted from _IfcGrid_ to this new supertype with upward compatibility

### Positions


## Formal Propositions

### HasPlacement
The placement for the grid has to be given.
