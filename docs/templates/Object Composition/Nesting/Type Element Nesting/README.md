Type Element Nesting
====================

Hosted components may be specified on types, following the same rules as defined for corresponding occurrences.

On type objects, hosted components do not have types defined, but serve as placeholders indicating that occurrences of the enclosing type object shall use a duplicate list of hosted components, where the types are defined at each occurrence.

This relationship differs from _IfcRelAggregates_, which is used to define explicit decomposition of elements at specified placement; this nesting relationship indicates an arbitrary composition of elements, where placement is defined parametrically -- either implicitly (material profile, layer, or constituent association) or explicitly (constraint association).

The order and naming of components may be significant based on parameterized material association. For example, if the _IfcElementType_ has an associated _IfcMaterialLayerSet_, then layers are constructed according to material associations of each nested _IfcElement_, and the _Name_ of each _IfcMaterialLayer_ must correspond to the _Name_ of each _IfcElement_.

```
concept {
    IfcElementType:IsNestedBy -> IfcRelNests
    IfcRelNests:RelatedObjects -> IfcElement
    IfcElement:Name -> IfcLabel
}
```
