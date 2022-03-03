Library Association
===================

The concept _Library Association_ describes how object and object types can have associated library entities indicating the another source of data such as from a model server, product library, or external database or system that enriches the data with more details. Libraries may be referenced in their entirety from projects or project libraries indicating the master source and version of data. Contents within libraries may be referenced from any object, type object, property, and some resource schema entities within a project or project library.

```
concept {
    IfcObjectDefinition:HasAssociations -> IfcRelAssociatesLibrary:RelatedObjects
    IfcRelAssociatesLibrary:RelatingLibrary -> IfcLibraryReference
    IfcLibraryReference:Location -> IfcURIReference
    IfcLibraryReference:Identification -> IfcIdentifier
    IfcLibraryReference:Name -> IfcLabel
    IfcLibraryReference:Description -> IfcText
    IfcLibraryReference:Language -> IfcLanguageId
    IfcLibraryReference:ReferencedLibrary -> IfcLibraryInformation
    IfcRelAssociatesLibrary:RelatingLibrary[binding="RelatingLibrary"]
}
```
