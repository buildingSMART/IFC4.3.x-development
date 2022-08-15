Material Single
===============

Materials are directly associated with products and product types to indicate a uniform material for the entire object.

Materials can also be associated with the _IfcTypeObject_, defining a material for occurrences of that type. If a material is associated at both the _IfcTypeObject_ and _IfcObject_, then the material directly assigned to _IfcObject_ takes priority.

```
concept {
    IfcObjectDefinition:HasAssociations -> IfcRelAssociatesMaterial:RelatedObjects
    IfcRelAssociatesMaterial:RelatingMaterial -> IfcMaterial
    IfcMaterial -> Material
}
```
