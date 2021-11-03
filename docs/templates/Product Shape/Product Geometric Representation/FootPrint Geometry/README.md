FootPrint Geometry
==================

Elements filling a boundary provide a 'Footprint' representation indicating a rectangle or any arbitrary set of outer and inner boundary curves. Examples of such elements include slabs and spaces. For elements that have a material layer set association indicating material thicknesses, a 'Body' representation may be generated based on the footprint and material layers. Fill area styles may indicate particular colors, tiles, or hatching for 2D rendering.

The representation identifier of the foot print representation is:

* _IfcShapeRepresentation_._RepresentationIdentifier_ = 'FootPrint'

```
concept {
    IfcProduct:Representation -> IfcProductDefinitionShape
    IfcProductDefinitionShape:Representations -> IfcShapeRepresentation
    IfcShapeRepresentation:RepresentationIdentifier -> IfcLabel
    IfcShapeRepresentation:ContextOfItems -> IfcGeometricRepresentationContext
    IfcShapeRepresentation:RepresentationType -> IfcLabel
    IfcShapeRepresentation:RepresentationIdentifier[binding="Identifier"]
    IfcShapeRepresentation:RepresentationType[binding="Type"]
    IfcShapeRepresentation:Items[binding="Items"]
}
```
