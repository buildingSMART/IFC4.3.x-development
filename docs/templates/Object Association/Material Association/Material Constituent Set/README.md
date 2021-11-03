Material Constituent Set
========================

Material constituents are associated with products or product types where materials are placed arbitrarily (unlike 1D material profiles or 2D material layers). The mapping of materials to geometry may be accomplished using _IfcShapeAspect_.

```
concept {
    IfcObjectDefinition:HasAssociations -> IfcRelAssociatesMaterial:RelatedObjects
    IfcRelAssociatesMaterial:RelatingMaterial -> IfcMaterialConstituentSet
    IfcMaterialConstituentSet:MaterialConstituents -> IfcMaterialConstituent
    IfcMaterialConstituentSet:Name -> IfcLabel
    IfcMaterialConstituentSet:Description -> IfcText
    IfcMaterialConstituent:Name -> IfcLabel
    IfcMaterialConstituent:Description -> IfcText
    IfcMaterialConstituent:Material -> IfcMaterial
    IfcMaterialConstituent:Category -> IfcLabel
    IfcMaterialConstituent:Fraction -> IfcNormalisedRatioMeasure
    IfcMaterialConstituent:Name[binding="ConstituentName"]
}
```
