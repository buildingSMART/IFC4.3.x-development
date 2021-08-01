Material Layer Set Usage
========================

Material layer set usage defines layout at occurrences to indicate a direction and offset from the 'Axis' reference curve, and a reference extent such as for a default wall height.

The concept of _Material Layer Set Usage_ is only applicable to certain product subtypes, refered to as "Standard case" elements. It supports a certain range of parametric definitions for those element configurations.

The material of those standard case elements is defined by _IfcMaterialLayerSetUsage_ and is attached by the _IfcRelAssociatesMaterial_._RelatingMaterial_. It is accessible by the inverse _HasAssociations_ relationship. Standard case elements with multiple layers can be represented by refering to several _IfcMaterialLayer_'s within the _IfcMaterialLayerSet_ that is referenced from the _IfcMaterialLayerUsage_.

```
concept {
    IfcProduct:HasAssociations -> IfcRelAssociatesMaterial
    IfcRelAssociatesMaterial:RelatingMaterial -> IfcMaterialLayerSetUsage
    IfcMaterialLayerSetUsage:ForLayerSet -> IfcMaterialLayerSet
    IfcMaterialLayerSetUsage:LayerSetDirection -> IfcLayerSetDirectionEnum
    IfcMaterialLayerSetUsage:DirectionSense -> IfcDirectionSenseEnum
    IfcMaterialLayerSetUsage:OffsetFromReferenceLine -> IfcLengthMeasure
    IfcMaterialLayerSetUsage:ReferenceExtent -> IfcPositiveLengthMeasure
    IfcMaterialLayerSet:MaterialLayers -> IfcMaterialLayer
    IfcMaterialLayerSet:MaterialLayers -> IfcMaterialLayerWithOffsets
    IfcMaterialLayer:Material -> IfcMaterial
    IfcMaterialLayer:LayerThickness -> IfcNonNegativeLengthMeasure
    IfcMaterial:HasRepresentation -> IfcMaterialDefinitionRepresentation:RepresentedMaterial
    IfcMaterialLayerWithOffsets:OffsetDirection -> IfcLayerSetDirectionEnum
    IfcMaterialLayerWithOffsets:OffsetValues -> IfcLengthMeasure
}
```
