Material Constituent Set
========================

Material constituents are associated with products or product types where materials are placed arbitrarily (unlike 1D material profiles or 2D material layers). The mapping of materials to geometry may be accomplished using _IfcShapeAspect_.

```
concept {
    IfcObjectDefinition:HasAssociations -> IfcRelAssociatesMaterial:RelatedObjects
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
