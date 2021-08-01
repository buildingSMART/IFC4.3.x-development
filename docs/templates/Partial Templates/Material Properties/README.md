Material Properties
===================

Material properties may capture standard or user-defined parameters.

```
concept {
    IfcMaterialDefinition:HasProperties -> IfcMaterialProperties:Material
    IfcMaterialProperties:Name -> IfcIdentifier
    IfcMaterialProperties:Description -> IfcText
    IfcMaterialProperties:Properties -> IfcProperty
}
```
