Material Set
============

Composite or multiple materials may be described using a material set. There are three types of material sets to choose from:

 * Layer sets - layered materials with a thickness that fills a boundary
 * Profile sets - when materials that are extruded along a profiled shape
 * Constituent sets - when materials are either homogenously mixed, or arbitrarily placed

> EXAMPLE A wall or slab may use a layer set. A beam, column, pipe, or duct may use a profile set, even if it only has one profile. Composite beams may be made out of multiple profiles. Concrete may use a constituent set for portions of sand and cement. A window frame may also use a constituent set for one material for its frame and another material for its glazing portion.

The material is defined by either _IfcMaterialLayerSet_, _IfcMaterialProfileSet_, or _IfcMaterialConstituentSet_ and related using _IfcRelAssociatesMaterial_.RelatingMaterial. Independent of the material used, each each layer, profile, or constituent within the set may be identified using a name and category.

```
concept {
    IfcObjectDefinition:HasAssociations -> IfcRelAssociatesMaterial:RelatedObjects
    IfcRelAssociatesMaterial:RelatingMaterial -> IfcMaterialLayerSet
    IfcRelAssociatesMaterial:RelatingMaterial -> IfcMaterialProfileSet
    IfcRelAssociatesMaterial:RelatingMaterial -> IfcMaterialConstituentSet

    IfcMaterialLayerSet:MaterialLayers -> IfcMaterialLayer
    IfcMaterialLayer:Name -> IfcLabel_0
    IfcMaterialLayer:Material -> IfcMaterial_0
    IfcMaterialLayer:Name[binding="Name"]

    IfcMaterialProfileSet:MaterialProfiles -> IfcMaterialProfile
    IfcMaterialProfile:Name -> IfcLabel_1
    IfcMaterialProfile:Material -> IfcMaterial_1
    IfcMaterialProfile:Name[binding="Name"]

    IfcMaterialConstituentSet:MaterialConstituents -> IfcMaterialConstituent
    IfcMaterialConstituent:Name -> IfcLabel_2
    IfcMaterialConstituent:Material -> IfcMaterial_2
    IfcMaterialConstituent:Name[binding="Name"]

}
```
