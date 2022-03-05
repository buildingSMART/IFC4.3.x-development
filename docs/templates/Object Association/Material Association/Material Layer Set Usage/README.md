Material Layer Set Usage
========================

A material layer set may be defined on an object type. In this scenario, occurrences of that type must use this layer set to parametrically define their geometry.

> EXAMPLE A wall type may define multiple layers of material. A wall of that wall type will then have a geometry with a thickness that corresponds with the layers in the wall type.

The usage may parametrically define an 'Axis' reference curve, and a direction, offset, and extent of the layers to extend along the axis. This allows layers to slope or only extend up to a particular height.

When the _IfcMaterialLayerSet_ is defined by the object type, this implies that all occurrences of that type must use the same instance of the material set via _IfcMaterialLayerSetUsage_.

```
concept {
    IfcProduct:HasAssociations -> IfcRelAssociatesMaterial:RelatedObjects

    IfcProduct:IsTypedBy -> IfcRelDefinesByType:RelatedObjects
    IfcRelDefinesByType:RelatingType -> IfcTypeProduct
    IfcTypeProduct:HasAssociations -> IfcRelAssociatesMaterial_1:RelatedObjects
    IfcRelAssociatesMaterial_1:RelatingMaterial -> IfcMaterialLayerSet

    IfcRelAssociatesMaterial:RelatingMaterial -> IfcMaterialLayerSetUsage
    IfcMaterialLayerSetUsage:ForLayerSet -> IfcMaterialLayerSet
    IfcMaterialLayerSetUsage:LayerSetDirection -> IfcLayerSetDirectionEnum_1
    IfcMaterialLayerSetUsage:DirectionSense -> IfcDirectionSenseEnum
    IfcMaterialLayerSetUsage:OffsetFromReferenceLine -> IfcLengthMeasure_1
    IfcMaterialLayerSetUsage:ReferenceExtent -> IfcPositiveLengthMeasure
    IfcMaterialLayerSet:MaterialLayers -> IfcMaterialLayer
    IfcMaterialLayer:Material -> IfcMaterial
    IfcMaterialLayer:LayerThickness -> IfcNonNegativeLengthMeasure
    IfcMaterialLayer:Name[binding="Name"]
}
```
