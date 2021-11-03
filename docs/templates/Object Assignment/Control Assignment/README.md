Control Assignment
==================

Controls may have assignments indicating objects that must observe the established requirements. An example of such assignment is a labor resource assigned to a calendar.

```
concept {
    IfcControl:Controls -> IfcRelAssignsToControl:RelatingControl
    IfcRelAssignsToControl:RelatedObjects -> IfcObject
    IfcRelAssignsToControl:RelatedObjects[binding="Type"]
}
```
