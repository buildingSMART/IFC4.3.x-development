# IfcRelPositions

An _IfcRelPositions_ relationship informs on the positioning dependency between a product and a positioning element.
<!-- end of short definition -->

This relationship does not affect the geometric representation of a product nor its geometrical placement, which is done through subtypes of _IfcObjectPlacement_. 

> EXAMPLE To geometrically place an _IfcReferent_ along an alignment curve, the _IfcReferent.ObjectPlacement_ is used. To inform that an _IfcReferent_ is positioned along an alignment curve, maybe referring to a certain stationing value, _IfcRelPositions_ is used. This is **independent from the actual geometrical placement** of the referent. For this reason, the semantics of _IfcRelPositions_ shall not be used to calculate the geometry of the placement, but just to inform on the position of the referent on the alignment curve.

## Attributes

### RelatingPositioningElement
Positioning element defining the source of the relative position.

### RelatedProducts
Relatively positioned product.

## Formal Propositions

### NoSelfReference
The instance of the _PositionedElement_ shall not be the same instance as the _Product_.