Body SectionedSolidHorizontal
=============================

The _Body SectionedSolidHorizontal_ is the representation of the 3D body of a product by using two or more closed profiles, possibly with varying dimensions,  that are swept between specified positions along the directrix.

The following attribute values for the _IfcShapeRepresentation_ holding this geometric representation shall be used:

* _IfcShapeRepresentation_._RepresentationIdentifier_ = 'Body'
* _IfcShapeRepresentation_._RepresentationType_ = 'AdvancedSweptSolid'
* _IfcShapeRepresentation_._Items_ = _IfcSectionedSolidHorizontal_

```
concept {
    IfcElement:Representation -> IfcProductDefinitionShape
    IfcProductDefinitionShape:Representations -> IfcShapeRepresentation
    IfcShapeRepresentation:ContextOfItems -> IfcGeometricRepresentationContext
    IfcShapeRepresentation:RepresentationIdentifier -> IfcLabel_0
    IfcShapeRepresentation:RepresentationType -> IfcLabel_1
    IfcShapeRepresentation:Items -> IfcSectionedSolidHorizontal
    IfcLabel_0 -> constraint_0
    constraint_0[label="=Body"]
    IfcLabel_1 -> constraint_1
    constraint_1[label="=AdvancedSweptSolid"]
    IfcSectionedSolidHorizontal:Directrix -> IfcBoundedCurve
    IfcSectionedSolidHorizontal:CrossSections -> IfcProfileDef
    IfcShapeRepresentation:RepresentationIdentifier[binding="Identifier"]
    IfcShapeRepresentation:RepresentationType[binding="Type"]
    IfcShapeRepresentation:Items[binding="Items"]
    IfcSectionedSolidHorizontal:Directrix[binding="Directrix"]
    IfcSectionedSolidHorizontal:CrossSections[binding="CrossSections"]
}
```
