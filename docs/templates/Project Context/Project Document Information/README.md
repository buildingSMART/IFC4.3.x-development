Project Document Information
============================

Projects may define external documents, which may be used to attach arbitrary information to objects contained within the same project or referencing projects.

```
concept {
    IfcContext:HasAssociations -> IfcRelAssociatesDocument:RelatedObjects
    IfcContext:Phase -> IfcLabel_1
    IfcContext:ObjectType -> IfcLabel_2
    IfcContext:LongName -> IfcLabel_3
    IfcRelAssociatesDocument:RelatingDocument -> IfcDocumentInformation
    IfcRelAssociatesDocument:RelatingDocument -> IfcDocumentReference
    IfcDocumentInformation:Location -> IfcURIReference
    IfcDocumentInformation:ElectronicFormat -> IfcIdentifier
    IfcDocumentInformation:Identification -> IfcIdentifier
    IfcDocumentInformation:Name -> IfcLabel_0
    IfcDocumentInformation:Description -> IfcText
}
```
