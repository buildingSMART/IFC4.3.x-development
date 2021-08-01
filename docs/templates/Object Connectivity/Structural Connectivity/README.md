Structural Connectivity
=======================

Structural items may be connected within an analysis model.

```
concept {
    IfcStructuralMember:ConnectedBy -> IfcRelConnectsStructuralMember:RelatingStructuralMember
    IfcRelConnectsStructuralMember:RelatedStructuralConnection -> IfcStructuralConnection
}
```
