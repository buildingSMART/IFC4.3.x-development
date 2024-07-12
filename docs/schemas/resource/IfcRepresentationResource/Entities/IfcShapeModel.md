# IfcShapeModel

_IfcShapeModel_ represents the concept of a particular geometric and/or topological representation of a product's shape or a product component's shape within a representation context. This representation context has to be a geometric representation context (with the exception of topology representations without associated geometry). The two subtypes are _IfcShapeRepresentation_ to cover geometric models that represent a shape, and _IfcTopologyRepresentation_ to cover the connectivity of a product or product component. The topology may or may not have geometry associated.
<!-- end of short definition -->

The _IfcShapeModel_ can be a shape representation (geometric and/or topologogical) of a product (via _IfcProductDefinitionShape_), or a shape representation (geometric and/or topologogical) of a component of a product shape (via _IfcShapeAspect_).

> HISTORY New entity in IFC2x3.

## Attributes

### OfShapeAspect
Reference to the shape aspect, for which it is the shape representation.

## Formal Propositions

### WR11
The _IfcShapeModel_ shall be used by an _IfcProductRepresentation_, by an _IfcRepresentationMap_ or by an _IfcShapeAspect_.
