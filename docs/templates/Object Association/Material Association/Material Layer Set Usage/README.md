Material Layer Set Usage
========================

A material layer set can be used to model the material of a product as a set of homogeneous layers with constant thickness.

Material layer set usage defines layout at occurrences to indicate a direction and offset from the 'Axis' reference curve or the coordinate system established by the IfcExtrudedAreaSolid.Position (provided by its representation).

When the occurrence has an associated IfcObjectType, that object type may define the material layer set (no usage). In this scenario, all occurrences of that type must use that layer set.

> EXAMPLE A wall type may define multiple layers of material (e.g brick - insulation - brick). A wall occurrence of that wall type will then have a geometry with a thickness that corresponds with the layers in the wall type.

> EXAMPLE A wall type may define multiple layers of material. A wall of that wall type will then have a geometry with a thickness that corresponds with the layers in the wall type.

The usage may parametrically define an 'Axis' reference curve, and a direction, offset, and extent of the layers to extend along the axis. This allows layers to slope or only extend up to a particular height.

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
