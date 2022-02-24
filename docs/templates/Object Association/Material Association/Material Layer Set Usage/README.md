Material Layer Set Usage
========================

Material layer set usage defines layout at occurrences to indicate a direction and offset from the 'Axis' reference curve, and a reference extent such as for a default wall height.

The material is defined by _IfcMaterialLayerSetUsage_ and is attached by the _IfcRelAssociatesMaterial_._RelatingMaterial_. It is accessible by the inverse _HasAssociations_ relationship. Elements with multiple layers can be represented by referring to several _IfcMaterialLayer_'s within the _IfcMaterialLayerSet_ that is referenced from the _IfcMaterialLayerUsage_.

```
concept {
    IfcProduct:HasAssociations -> IfcRelAssociatesMaterial:RelatedObjects
    IfcRelAssociatesMaterial:RelatingMaterial -> IfcMaterialLayerSetUsage
    IfcMaterialLayerSetUsage:ForLayerSet -> IfcMaterialLayerSet
    IfcMaterialLayerSetUsage:LayerSetDirection -> IfcLayerSetDirectionEnum_1
    IfcMaterialLayerSetUsage:DirectionSense -> IfcDirectionSenseEnum
    IfcMaterialLayerSetUsage:OffsetFromReferenceLine -> IfcLengthMeasure_1
    IfcMaterialLayerSetUsage:ReferenceExtent -> IfcPositiveLengthMeasure
    IfcMaterialLayerSet:MaterialLayers -> IfcMaterialLayer
    IfcMaterialLayerSet:MaterialLayers -> IfcMaterialLayerWithOffsets
    IfcMaterialLayer:Material -> IfcMaterial
    IfcMaterialLayer:LayerThickness -> IfcNonNegativeLengthMeasure
    IfcMaterial:HasRepresentation -> IfcMaterialDefinitionRepresentation:RepresentedMaterial
    IfcMaterialDefinitionRepresentation -> Material_Surface_Color_Style
    IfcMaterialLayerWithOffsets:OffsetDirection -> IfcLayerSetDirectionEnum_0
    IfcMaterialLayerWithOffsets:OffsetValues -> IfcLengthMeasure_0
    IfcMaterialLayer:Name[binding="Name"]
}
```
