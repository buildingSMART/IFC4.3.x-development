Material Single
===============

Materials are directly associated with products and product types to indicate a uniform material for the entire object.

```
concept {
    IfcObjectDefinition:HasAssociations -> IfcRelAssociatesMaterial:RelatedObjects
    IfcRelAssociatesMaterial:RelatingMaterial -> IfcMaterial
}
```
