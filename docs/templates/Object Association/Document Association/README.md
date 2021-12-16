Document Association
====================

The concept _Document Association_ describes how objects or object types can have associated documents indicating external files. Documents may be referenced in their entirety such as to capture product brochures, data sheets, multimedia content, or thumbnail images. Contents within documents may be referenced from any object, and may be used to synchronize information in other files such as work schedules for project management applications.

Typical document meta data, such as issue date, editor, and similar, can be captured with the association, the document content however remains with the external files.

```
concept {
    IfcObjectDefinition:HasAssociations -> IfcRelAssociatesDocument:RelatedObjects
    IfcRelAssociatesDocument:Name -> IfcLabel_0
    IfcRelAssociatesDocument:RelatingDocument -> IfcDocumentReference
    IfcDocumentReference:Location -> IfcURIReference
    IfcDocumentReference:Identification -> IfcIdentifier
    IfcDocumentReference:Name -> IfcLabel_1
    IfcDocumentReference:Description -> IfcText
    IfcRelAssociatesDocument:Name[binding="Name"]
}
```
