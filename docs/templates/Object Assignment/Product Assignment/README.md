Product Assignment
==================

Products may have assignments indicating processes that operate upon the product. An example of such assignment is a task to construct a wall.

```
concept {
    IfcProduct:ReferencedBy -> IfcRelAssignsToProduct:RelatingProduct
    IfcRelAssignsToProduct:RelatedObjects -> IfcObject
}
```
