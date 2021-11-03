Type Element Aggregation
========================

Product types may define aggregated components.

Placement of such components may be explicitly defined using _IfcLocalPlacement_ relative to the enclosing _IfcElementType_, or implicitly defined if _IfcElement_._ObjectPlacement_ is null.

If an occurrence is instantiated of the given _IfcElementType_, then such occurrence must include equivalent aggregated elements with names corresponding to those within the element type.

```
concept {
    IfcElementType:IsDecomposedBy -> IfcRelAggregates
    IfcRelAggregates:RelatedObjects -> IfcElement
    IfcElementType:PredefinedType[binding="PredefinedType"]
    IfcRelAggregates:RelatedObjects[binding="RelatedObjects"]
}
```
