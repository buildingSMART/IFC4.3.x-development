Project Declaration
===================

The project provides a directory of object types and property templates contained within using declaration relationships.

> NOTE&nbsp; The actual object occurrences used within the context of a project, such as walls, beams, air outlets, are assigned to a spatial hierarchy that is linked to the project using the aggregation hierarchy. See concept _Spatial Decomposition_ for linking a spatial structure to the project.

> HISTORY&nbsp; New concept template enabled by schema enhancements in IFC4.

```
concept {
    IfcContext:Declares -> IfcRelDeclares:RelatingContext
    IfcContext:Phase -> IfcLabel_0
    IfcContext:ObjectType -> IfcLabel_1
    IfcContext:LongName -> IfcLabel_2
    IfcRelDeclares:RelatedDefinitions[binding="Type"]
}
```
