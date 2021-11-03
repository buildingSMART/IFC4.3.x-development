Material Profile Set Usage
==========================

Material profile set usage defines layout at occurrences to indicate the offset from the 'Axis' reference curve according to cardinal point, and a reference extent such as for a default column height.

The concept of _Material Profile Set Usage_ is only applicable to certain product subtypes, refered to as "standard case" elements. It supports a certain range of parametric definitions for those element configurations.

The material of those standard case elements is defined by _IfcMaterialProfileSetUsage_ and is attached by the _IfcRelAssociatesMaterial_._RelatingMaterial_. It is accessible by the inverse _HasAssociations_ relationship. Standard case elements with composite profiles can be represented by refering to several _IfcMaterialProfile_'s within the _IfcMaterialProfileSet_ that is referenced from the _IfcMaterialProfileSetUsage_.

```
concept {
    IfcProduct:HasAssociations -> IfcRelAssociatesMaterial
    IfcRelAssociatesMaterial:RelatingMaterial -> IfcMaterialProfileSetUsage
    IfcRelAssociatesMaterial:RelatingMaterial -> IfcMaterialProfileSetUsageTapering
    IfcMaterialProfileSetUsage:ForProfileSet -> IfcMaterialProfileSet
    IfcMaterialProfileSetUsage:CardinalPoint -> IfcCardinalPointReference
    IfcMaterialProfileSetUsage:ReferenceExtent -> IfcPositiveLengthMeasure
    IfcMaterialProfileSet:MaterialProfiles -> IfcMaterialProfile
    IfcMaterialProfileSet:MaterialProfiles -> IfcMaterialProfileWithOffsets
    IfcMaterialProfile:Material -> IfcMaterial
    IfcMaterialProfile:Profile -> IfcProfileDef
    IfcMaterial:HasRepresentation -> IfcMaterialDefinitionRepresentation:RepresentedMaterial
    IfcMaterialProfileWithOffsets:OffsetValues -> IfcLengthMeasure
    IfcMaterialProfileSetUsageTapering:ForProfileEndSet -> IfcMaterialProfileSet
    IfcMaterialProfileSetUsageTapering:CardinalEndPoint -> IfcCardinalPointReference
    IfcMaterialProfile:Name[binding="Name"]
}
```
