Material Constituent Set
========================

Material constituents may be associated to arbitrary geometry using _IfcShapeAspect_. This association is done by
comparing the name of the material constituent with the name of an _IfcShapeAspect_ assigned to a portion of the
product's representation.

```
concept {
    IfcProduct:HasAssociations -> IfcRelAssociatesMaterial:RelatedObjects

    IfcProduct:Representation -> IfcProductDefinitionShape:ShapeOfProduct
    IfcProductDefinitionShape:Representations -> IfcShapeRepresentation:OfProductRepresentation
    IfcShapeAspect:PartOfProductDefinitionShape -> IfcProductDefinitionShape:HasShapeAspects
    IfcShapeAspect:ShapeRepresentations -> IfcShapeRepresentation:OfShapeAspect
    IfcShapeAspect:Name[binding="ShapeAspectName"]
    IfcShapeAspect:Name -> IfcLabel_0

    IfcRelAssociatesMaterial:RelatingMaterial -> IfcMaterialConstituentSet
    IfcMaterialConstituentSet:MaterialConstituents -> IfcMaterialConstituent
    IfcMaterialConstituentSet:Name -> IfcLabel_2
    IfcMaterialConstituentSet:Description -> IfcText_1
    IfcMaterialConstituent:Name -> IfcLabel_0
    IfcMaterialConstituent:Description -> IfcText_0
    IfcMaterialConstituent:Material -> IfcMaterial
    IfcMaterialConstituent:Category -> IfcLabel_1
    IfcMaterialConstituent:Fraction -> IfcNormalisedRatioMeasure
    IfcMaterial -> Material
    IfcMaterialConstituent:Name[binding="ConstituentName"]
}
```
