Material Profile Set Usage
==========================

When the occurrence has an associated IfcObjectType, that object type may define the material profile set (no usage). In this scenario, all occurrences of that type must use that profile set.

> EXAMPLE A beam type may define a material profile. A beam of that beam type will then have a geometry correlating to that profile, extruded along an axis.

The usage may parametrically define an 'Axis' reference curve, an offset, alignment, and extent of the profile to extend along the axis.

Profiles will typically be parametrically defined and named according to a standard, and have material properties that assist in usecases such as structural simulations.

```
concept {
    IfcProduct:HasAssociations -> IfcRelAssociatesMaterial:RelatedObjects

    IfcProduct:IsTypedBy -> IfcRelDefinesByType:RelatedObjects
    IfcRelDefinesByType:RelatingType -> IfcTypeProduct
    IfcTypeProduct:HasAssociations -> IfcRelAssociatesMaterial_1:RelatedObjects
    IfcRelAssociatesMaterial_1:RelatingMaterial -> IfcMaterialProfileSet_0

    IfcRelAssociatesMaterial:RelatingMaterial -> IfcMaterialProfileSetUsage
    IfcMaterialProfileSetUsage:ForProfileSet -> IfcMaterialProfileSet_0
    IfcMaterialProfileSetUsage:CardinalPoint -> IfcCardinalPointReference_0
    IfcMaterialProfileSetUsage:ReferenceExtent -> IfcPositiveLengthMeasure
    IfcMaterialProfileSet_0:MaterialProfiles -> IfcMaterialProfile
    IfcMaterialProfile:Material -> IfcMaterial
    IfcMaterialProfile:Profile -> IfcProfileDef
    IfcMaterialProfile:Name[binding="Name"]
    IfcProfileDef:ProfileName[binding="ProfileName"]
    IfcProfileDef:ProfileName -> IfcLabel_1
}
```
