Profile Properties
==================

Profile properties may capture standard or user-defined parameters.

```
concept {
    IfcProfileDef:ProfileType -> IfcProfileTypeEnum
    IfcProfileDef:ProfileName -> IfcLabel
    IfcProfileDef:HasProperties -> IfcProfileProperties:ProfileDefinition
    IfcProfileProperties:Name -> IfcIdentifier
    IfcProfileProperties:Description -> IfcText
    IfcProfileProperties:Properties -> IfcProperty
}
```
