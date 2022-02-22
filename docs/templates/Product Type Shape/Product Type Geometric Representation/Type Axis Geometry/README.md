Type Axis Geometry
==================

The Axis representation may be defined on product types that have a concept of a linear representation, which may also correspond to structural axis or distribution flow path.

For distribution elements, this represents the 3D flow path of the item having _IfcShapeRepresentation.RepresentationType_ of 'Curve3D' and containing a single _IfcBoundedCurve_ subtype such as _IfcPolyline_, _IfcTrimmedCurve_, or _IfcCompositeCurve_. For elements containing directional ports (_IfcDistributionPort_ with _FlowDirection_ of _SOURCE_ or _SINK_), the direction of the curve indicates direction of flow where a _SINK_ port is positioned at the start of the curve and a _SOURCE_ port is positioned at the end of the curve. This representation is most applicable to flow segment types (pipes, ducts, cables), however may be used at other elements to define a primary flow path if applicable.

If an element type is defined parametrically (such as a flow segment type defining common material profile but no particular length or path), then no representations shall be asserted at the type.

> NOTE  The product representations are defined as representation maps (at the level of the supertype _IfcTypeProduct_, which get assigned by an element occurrence instance through the _IfcShapeRepresentation.Item[1]_ being an _IfcMappedItem_.

```
concept {
    IfcElementType:RepresentationMaps -> IfcRepresentationMap
    IfcRepresentationMap:MappedRepresentation -> IfcShapeRepresentation
    IfcRepresentationMap:MappingOrigin -> IfcAxis2Placement3D
    IfcRepresentationMap:MappingOrigin -> IfcAxis2Placement2D
    IfcShapeRepresentation:ContextOfItems -> IfcGeometricRepresentationContext
    IfcShapeRepresentation:RepresentationIdentifier -> IfcLabel_0
    IfcShapeRepresentation:RepresentationType -> IfcLabel_1
    IfcShapeRepresentation:Items -> IfcBoundedCurve
    IfcShapeRepresentation:RepresentationType[binding="Type"]
    IfcShapeRepresentation:Items[binding="Geometry"]
}
```
