Project Classification Information
==================================

Projects may define classification structures, which may be used to classify objects contained within the same project, or other referencing projects (incorporating the current project as _IfcProjectLibrary_).

The classification information can either be provided as an external classification reference, only referring to an _IfcClassification_, that holds the classification name, edition and a resource location, or to an _IfcClassification_ containing the _IfcClassificationReference_'s as the classification notations, and thereby allowing to include the classification system structure within the exchange structure.

```
concept {
    IfcContext:HasAssociations -> IfcRelAssociatesClassification:RelatedObjects
    IfcContext:Phase -> IfcLabel_3
    IfcContext:ObjectType -> IfcLabel_4
    IfcContext:LongName -> IfcLabel_5
    IfcRelAssociatesClassification:RelatingClassification -> IfcClassification
    IfcClassification:Source -> IfcLabel_0
    IfcClassification:Name -> IfcLabel_1
    IfcClassification:ReferenceTokens -> IfcIdentifier_0
    IfcClassification:HasReferences -> IfcClassificationReference_0:ReferencedSource
    IfcClassificationReference_0:HasReferences -> IfcClassificationReference_1:ReferencedSource
    IfcClassificationReference_0:Identification -> IfcIdentifier_1
    IfcClassificationReference_0:Name -> IfcLabel_2
    IfcClassificationReference_0:Description -> IfcText
    IfcClassificationReference_0:Sort -> IfcIdentifier_2
    IfcClassification:Source[binding="ClassificationSource"]
    IfcClassification:Name[binding="ClassificationName"]
    IfcClassification:ReferenceTokens[binding="ReferenceTokens"]
}
```
