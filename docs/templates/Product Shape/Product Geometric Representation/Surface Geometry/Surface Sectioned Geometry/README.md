Surface Sectioned Geometry
==========================

The _Surface Sectioned Geometry_ is the representation for elements having a 'Surface' representation, where the surface is specified using two or more open profiles that are swept between specified positions along the directrix, e.g. for defining the upper boundary of an _IfcCourse_.

The following attribute values for the _IfcShapeRepresentation_ holding this geometric representation shall be used:

* _IfcShapeRepresentation_._RepresentationIdentifier_ = 'Surface'
* _IfcShapeRepresentation_._RepresentationType_ = 'SectionedSurface'
* _IfcShapeRepresentation_._Items_ = _IfcSectionedSurface_

```
concept {
    IfcElement:Representation -> IfcProductDefinitionShape
    IfcProductDefinitionShape:Representations -> IfcShapeRepresentation
    IfcShapeRepresentation:ContextOfItems -> IfcGeometricRepresentationContext
    IfcShapeRepresentation:RepresentationIdentifier -> IfcLabel_0
    IfcShapeRepresentation:RepresentationType -> IfcLabel_1
    IfcShapeRepresentation:Items -> IfcSectionedSurface
    IfcLabel_0 -> constraint_0
    constraint_0[label="=Surface"]
    IfcLabel_1 -> constraint_1
    constraint_1[label="=SectionedSurface"]
    IfcSectionedSurface:Directrix -> IfcBoundedCurve
    IfcSectionedSurface:CrossSections -> IfcProfileDef
    IfcShapeRepresentation:RepresentationIdentifier[binding="Identifier"]
    IfcShapeRepresentation:RepresentationType[binding="Type"]
    IfcShapeRepresentation:Items[binding="Items"]
    IfcSectionedSurface:Directrix[binding="Directrix"]
    IfcSectionedSurface:CrossSections[binding="CrossSections"]
}
```
