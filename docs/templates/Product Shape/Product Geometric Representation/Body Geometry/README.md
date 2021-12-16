Body Geometry
=============

Elements may have a 'Body' representation describing the volumetric shape of the object. Such representation may be used for 3D coordination, rendering or quantity take-off. Geometry may be based on boundary representations describing outer faces, primitives such as spheres or cones, swept solids such as profile extrusions or revolutions, Constructive Solid Geometry (CSG) such as clippings or subtractions of other shapes, or Non-Uniform Rational B-Spline (NURBS) geometry. Surface styles may indicate particular colors, textures, and reflectance for 3D rendering.

The representation identifier of the body representation is:

* _IfcShapeRepresentation_._RepresentationIdentifier_ = 'Body'

```
concept {
    IfcElement:Representation -> IfcProductDefinitionShape
    IfcProductDefinitionShape:Representations -> IfcShapeRepresentation
    IfcShapeRepresentation:ContextOfItems -> IfcGeometricRepresentationContext
    IfcShapeRepresentation:RepresentationIdentifier -> IfcLabel_0
    IfcShapeRepresentation:RepresentationType -> IfcLabel_1
    IfcLabel_0 -> constraint_0
    constraint_0[label="=Body"]
    IfcShapeRepresentation:RepresentationIdentifier[binding="Identifier"]
    IfcShapeRepresentation:RepresentationType[binding="Type"]
}
```
