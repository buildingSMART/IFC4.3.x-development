Lighting Geometry
=================

Elements emitting light provide a 'Lighting' representation. Examples of such elements include lamps and light fixtures. Such representation may be used for 3D rendering or lighting design.

The representation identifier and type and the only allowed single representation item of the 'Lighting' representation are:

* _IfcShapeRepresentation_._RepresentationIdentifier_ = 'Lighting'
* _IfcShapeRepresentation_._RepresentationType_ : 'LightSource'
* _IfcShapeRepresentation_._Items_ = _IfcLightSource_

```
concept {
    IfcElement:Representation -> IfcProductDefinitionShape
    IfcProductDefinitionShape:Representations -> IfcShapeRepresentation
    IfcShapeRepresentation:ContextOfItems -> IfcGeometricRepresentationContext
    IfcShapeRepresentation:RepresentationIdentifier -> IfcLabel
    IfcShapeRepresentation:RepresentationType -> IfcLabel
    IfcShapeRepresentation:Items -> IfcLightSource
    IfcLightSource:LightColour -> IfcColourRgb
    IfcShapeRepresentation:RepresentationIdentifier[binding="Identifier"]
    IfcShapeRepresentation:RepresentationType[binding="Type"]
    IfcShapeRepresentation:Items[binding="Items"]
}
```
