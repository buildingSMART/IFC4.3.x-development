Material Layer Set
==================

Material layer sets are associated with products or product types to indicate a parametric specification of layers having specified thickness filling a boundary defined on the product, or the occurrences of the product type. Examples of such products or product types are slabs, walls, and plates.

```
concept {
    IfcObjectDefinition:HasAssociations -> IfcRelAssociatesMaterial:RelatedObjects
    IfcRelAssociatesMaterial:RelatingMaterial -> IfcMaterialLayerSet
    IfcMaterialLayerSet:MaterialLayers -> IfcMaterialLayer
    IfcMaterialLayerSet:LayerSetName -> IfcLabel_2
    IfcMaterialLayerSet:Description -> IfcText_1
    IfcMaterialLayer:Name -> IfcLabel_0
    IfcMaterialLayer:Description -> IfcText_0
    IfcMaterialLayer:Material -> IfcMaterial
    IfcMaterialLayer:LayerThickness -> IfcNonNegativeLengthMeasure
    IfcMaterialLayer:IsVentilated -> IfcLogical
    IfcMaterialLayer:Category -> IfcLabel_1
    IfcMaterialLayer:Priority -> IfcNormalisedRatioMeasure
    IfcMaterial -> Material
    IfcMaterialLayerSet:MaterialLayers[binding="HasLayer"]
    IfcMaterialLayer:Name[binding="LayerName"]
    IfcMaterialLayer:LayerThickness[binding="LayerThickness"]
    IfcMaterialLayer:IsVentilated[binding="AirGap"]
    IfcMaterialLayer:Category[binding="Category"]
}
```
