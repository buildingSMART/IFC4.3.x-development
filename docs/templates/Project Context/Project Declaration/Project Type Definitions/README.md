Project Type Definitions
========================

Declaration of object types, such as element types utilized by the element occurrences within this project, within the context of the project. It provides a directory of all object types independently if and where they are used by object occurrences.

> HISTORY&nbsp; New concept template enabled by schema enhancements in IFC4.

```
concept {
    IfcContext:Declares -> IfcRelDeclares:RelatingContext
    IfcContext:Phase -> IfcLabel_0
    IfcContext:ObjectType -> IfcLabel_1
    IfcContext:LongName -> IfcLabel_2
    IfcRelDeclares:RelatedDefinitions -> IfcTypeObject
    IfcRelDeclares:RelatedDefinitions[binding="RelatedTypes"]
}
```
