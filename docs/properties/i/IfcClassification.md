IfcClassification
=================

An _IfcClassification_ is used for the arrangement of objects into a class or category according to a common purpose or their possession of common characteristics. A classification in the sense of _IfcClassification_ is taxonomy, or taxonomic scheme, arranged in a hierarchical structure. A category of objects relates to other categories in a generalization-specialization relationship. Therefore the classification items in an classification are organized in a tree structure.

The _IfcClassification_ identifies the classification system or source to which a classification reference refers to. Each classification reference may reference an instance of _IfcClassification_. A classification system declared may be either formally published, or it may be a locally defined method of classifiying information.

> NOTE&nbsp; Examples for such formally published classifications are Omniclass, Uniclass, Masterformat, or DIN277.

There are two methods to define and reference a classification system:

1. Including the classification system structure within the dataset: Here a hierarchical tree of _IfcClassificationReference_'s is included that defines the classification system including the relationship between the classification items. The _ReferencedSource_ attribute of _IfcClassificationReference_ links the classification item to the parent item, and the parent item finally to the _IfcClassification_.
2. Referencing the classification system by a classification key or id: Here the _IfcClassificationReference_ is used to assign a classification id or key as _Identification_ attribute and it may link by _ReferencedSource_ attribute directly to the _IfcClassification_.

> HISTORY&nbsp; New entity in IFC1.5

{ .change-ifc2x4}
> IFC 2x4 CHANGE&nbsp; Attribute _Edition_ made optional. Attributes: _Description_, _Location_, and _ReferenceTokens_ and inverse attribute _HasReferences_ added.
