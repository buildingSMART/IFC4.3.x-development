Resource Assignment
===================

Resources may have assignments indicating sources available to be used. An example of such assignment is a person fulfilling a carpenter labor resource.

```
concept {
    IfcResource:ResourceOf -> IfcRelAssignsToResource:RelatingResource
    IfcRelAssignsToResource:RelatedObjects -> IfcActor
    IfcRelAssignsToResource:RelatedObjects -> IfcProduct
}
```
