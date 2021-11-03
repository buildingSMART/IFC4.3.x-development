Material Profile Set
====================

Material profile sets are associated with products or product types where materials are placed in cross-sections of specified dimensions following a path defined at occurrences of the type. Examples of such products are beams, columns, members, reinforcing, footings, piles, pipe segments, duct segments, and cable segments.

> EXAMPLE&nbsp; Material profile sets can be provided at the _IfcColumnType_, defining the common material information for all occurrences of the same column type. It is then accessible by the inverse _IsTypedBy_ relationship at _IfcColumn_ pointing to _IfcColumnType_ having the _HasAssociations_ inverse relationship to _IfcRelAssociatesMaterial_ with _RelatingMaterial_ refering to the _IfcMaterialProfileSet_>. If an individual material association is provide at the _IfcColumn_ and the _IfcColumnType_, then the material directly assigned to _IfcColumn_ overrides the material assigned to _IfcColumnType_.

```
concept {
    IfcObjectDefinition:HasAssociations -> IfcRelAssociatesMaterial:RelatedObjects
    IfcRelAssociatesMaterial:RelatingMaterial -> IfcMaterialProfileSet
    IfcMaterialProfileSet:MaterialProfiles -> IfcMaterialProfile
    IfcMaterialProfileSet:Name -> IfcLabel
    IfcMaterialProfileSet:Description -> IfcText
    IfcMaterialProfile:Name -> IfcLabel
    IfcMaterialProfile:Description -> IfcText
    IfcMaterialProfile:Material -> IfcMaterial
    IfcMaterialProfile:Profile -> IfcProfileDef
    IfcMaterialProfile:Category -> IfcLabel
    IfcMaterialProfile:Priority -> IfcInteger
    IfcProfileDef:ProfileType -> IfcProfileTypeEnum
    IfcProfileDef:ProfileName -> IfcLabel
    IfcMaterialProfileSet:MaterialProfiles[binding="HasProfiles"]
    IfcProfileDef:ProfileName[binding="ProfileName"]
    IfcMaterialProfile:Category[binding="Category"]
}
```
