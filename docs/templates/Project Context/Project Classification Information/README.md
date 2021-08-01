Project Classification Information
==================================

Projects may define classification structures, which may be used to classify objects contained within the same project, or other referencing projects (incorporating the current project as _IfcProjectLibrary_).

The classification information can either be provided as an external classification reference, only refering to an _IfcClassification_, that holds the classification name, edition and a resource location, or to an _IfcClassification_ containing the _IfcClassificationReference_'s as the classification notations, and thereby allowing to include the classification system structure within the exchange structure.

```
concept {
    IfcContext:HasAssociations -> IfcRelAssociatesClassification
    IfcContext:Phase -> IfcLabel
    IfcContext:ObjectType -> IfcLabel
    IfcContext:LongName -> IfcLabel
    IfcRelAssociatesClassification:RelatingClassification -> IfcClassification
    IfcClassification:Source -> IfcLabel
    IfcClassification:Name -> IfcLabel
    IfcClassification:ReferenceTokens -> IfcIdentifier
    IfcClassification:HasReferences -> IfcClassificationReference:ReferencedSource
    IfcClassificationReference:HasReferences -> IfcClassificationReference:ReferencedSource
    IfcClassificationReference:Identification -> IfcIdentifier
    IfcClassificationReference:Name -> IfcLabel
    IfcClassificationReference:Description -> IfcText
    IfcClassificationReference:Sort -> IfcIdentifier
}
```
