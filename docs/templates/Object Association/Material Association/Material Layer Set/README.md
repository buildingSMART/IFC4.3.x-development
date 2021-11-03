Material Layer Set
==================

Material layer sets are associated with products or product types to indicate a parametric specification of layers having specified thickness filling a boundary defined on the product, or the occurrences of the product type. Examples of such products or product types are slabs, walls, and plates.

```
concept {
    IfcObjectDefinition:HasAssociations -> IfcRelAssociatesMaterial:RelatedObjects
    IfcRelAssociatesMaterial:RelatingMaterial -> IfcMaterialLayerSet
    IfcMaterialLayerSet:MaterialLayers -> IfcMaterialLayer
    IfcMaterialLayerSet:LayerSetName -> IfcLabel
    IfcMaterialLayerSet:Description -> IfcText
    IfcMaterialLayer:Name -> IfcLabel
    IfcMaterialLayer:Description -> IfcText
    IfcMaterialLayer:Material -> IfcMaterial
    IfcMaterialLayer:LayerThickness -> IfcNonNegativeLengthMeasure
    IfcMaterialLayer:IsVentilated -> IfcLogical
    IfcMaterialLayer:Category -> IfcLabel
    IfcMaterialLayer:Priority -> IfcNormalisedRatioMeasure
    IfcMaterialLayerSet:MaterialLayers[binding="HasLayer"]
    IfcMaterialLayer:Name[binding="LayerName"]
    IfcMaterialLayer:LayerThickness[binding="LayerThickness"]
    IfcMaterialLayer:IsVentilated[binding="AirGap"]
    IfcMaterialLayer:Category[binding="Category"]
}
```
