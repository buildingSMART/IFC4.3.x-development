Product Type Assignment
=======================

Product types may have assignments indicating re-usable process types for which occurrences may operate on occurrences of the product type. An example of such assignment is a task type for placing concrete in slabs on grade.

```
concept {
    IfcTypeProduct:ReferencedBy -> IfcRelAssignsToProduct:RelatingProduct
    IfcRelAssignsToProduct:RelatedObjects -> IfcTypeProcess
}
```
