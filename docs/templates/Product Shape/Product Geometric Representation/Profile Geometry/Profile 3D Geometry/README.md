Profile 3D Geometry
===================

The _Profile 3D Geometry_ is the standard representation of the outer profile for elements filling an opening. Examples of such elements include doors and windows. In the case of doors and windows the profile geometry is used to apply the parametric definition of lining and panel dimensions to the profile.

The following attribute values for the _IfcShapeRepresentation_ holding this geometric representation shall be used:

* _IfcShapeRepresentation_._RepresentationIdentifier_ = 'Profile'
* _IfcShapeRepresentation_._RepresentationType_ = 'Curve3D'
* _IfcShapeRepresentation_._Items_ = _IfcBoundedCurve_

```
concept {
    IfcElement:Representation -> IfcProductDefinitionShape
    IfcProductDefinitionShape:Representations -> IfcShapeRepresentation
    IfcShapeRepresentation:ContextOfItems -> IfcGeometricRepresentationContext
    IfcShapeRepresentation:RepresentationIdentifier -> IfcLabel
    IfcShapeRepresentation:RepresentationType -> IfcLabel
    IfcShapeRepresentation:Items -> IfcBoundedCurve
    IfcShapeRepresentation:RepresentationIdentifier[binding="Identifier"]
    IfcShapeRepresentation:RepresentationType[binding="Type"]
    IfcShapeRepresentation:Items[binding="Items"]
}
```
