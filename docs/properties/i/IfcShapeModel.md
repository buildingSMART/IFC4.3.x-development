IfcShapeModel
=============

_IfcShapeModel_ represents the concept of a particular geometric and/or topological representation of a product's shape or a product component's shape within a representation context. This representation context has to be a geometric representation context (with the exception of topology representations without associated geometry). The two subtypes are _IfcShapeRepresentation_ to cover geometric models that represent a shape, and _IfcTopologyRepresentation_ to cover the conectivity of a product or product component. The topology may or may not have geometry associated.

The _IfcShapeModel_ can be a shape representation (geometric and/or topologogical) of a product (via _IfcProductDefinitionShape_), or a shape representation (geometric and/or topologogical) &nbsp;of a component of a product shape (via _IfcShapeAspect_).

> HISTORY&nbsp; New entity in IFC2x3.
