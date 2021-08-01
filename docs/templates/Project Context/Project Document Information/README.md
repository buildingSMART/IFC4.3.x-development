Project Document Information
============================

Projects may define external documents, which may be used to attach arbitrary information to objects contained within the same project or referencing projects.

```
concept {
    IfcContext:HasAssociations -> IfcRelAssociatesDocument
    IfcContext:Phase -> IfcLabel
    IfcContext:ObjectType -> IfcLabel
    IfcContext:LongName -> IfcLabel
    IfcRelAssociatesDocument:RelatingDocument -> IfcDocumentInformation
    IfcDocumentInformation:Location -> IfcURIReference
    IfcDocumentInformation:ElectronicFormat -> IfcDocumentElectronicFormat
    IfcDocumentInformation:Identification -> IfcIdentifier
    IfcDocumentInformation:Name -> IfcLabel
    IfcDocumentInformation:Description -> IfcText
}
```
