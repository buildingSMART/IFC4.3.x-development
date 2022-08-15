Material Constituent Set
========================

A material constituent set may have its constituents associated to arbitrary geometry using _IfcShapeAspect_. This
association is done by comparing the name of the material constituent with the name of an _IfcShapeAspect_ assigned to a portion of the product's representation.

> EXAMPLE A window's geometric representation may be split into two items: the frame, and the glazing. Each representation item would be given a name that correlates with the name of the material constituent.

```
concept {
    IfcProduct:HasAssociations -> IfcRelAssociatesMaterial:RelatedObjects

    IfcProduct:Representation -> IfcProductDefinitionShape:ShapeOfProduct
    IfcProductDefinitionShape:Representations -> IfcShapeRepresentation:OfProductRepresentation
    IfcShapeRepresentation:Items -> IfcRepresentationItem
    IfcShapeRepresentation_0:Items -> IfcRepresentationItem
    IfcShapeAspect:PartOfProductDefinitionShape -> IfcProductDefinitionShape:HasShapeAspects
    IfcShapeAspect:ShapeRepresentations -> IfcShapeRepresentation_0:OfShapeAspect
    IfcShapeAspect:Name[binding="ShapeAspectName"]
    IfcShapeAspect:Name -> IfcLabel

    IfcRelAssociatesMaterial:RelatingMaterial -> IfcMaterialConstituentSet:AssociatedTo
    IfcMaterialConstituentSet:MaterialConstituents -> IfcMaterialConstituent:ToMaterialConstituentSet
    IfcMaterialConstituent:Name -> IfcLabel_0
    IfcMaterialConstituent:Material -> IfcMaterial
    IfcMaterialConstituent:Category -> IfcLabel_1
    IfcMaterialConstituent:Fraction -> IfcNormalisedRatioMeasure
    IfcMaterialConstituent:Name[binding="ConstituentName"]
}
```
