Reference Geometry
==================

A specific form of geometry representation is the 'Reference' geometry. It is used to provide a geometry used for various forms of assessments (like for quantities, etc.) but not for display and also not for implicit Boolean operations in a voiding relationship.

> EXAMPLE&nbsp; An example is the use of 'Reference' representation is for opening elements that shall not be used to create a void using the _IfcRelVoidsElement_ relationship, since the voids are already part of the 'Body' representation of the voided element. The representation identifier of the representation is:
> 
> * _IfcShapeRepresentation_._RepresentationIdentifier_ = 'Reference'

```
concept {
    IfcProduct:Representation -> IfcProductDefinitionShape
    IfcProductDefinitionShape:Representations -> IfcShapeRepresentation
    IfcShapeRepresentation:ContextOfItems -> IfcGeometricRepresentationContext
    IfcShapeRepresentation:RepresentationIdentifier -> IfcLabel_0
    IfcShapeRepresentation:RepresentationType -> IfcLabel_1
    IfcLabel_0 -> constraint_0
    constraint_0[label="=Reference"]
    IfcShapeRepresentation:RepresentationIdentifier[binding="Identifier"]
    IfcShapeRepresentation:RepresentationType[binding="Type"]
}
```
