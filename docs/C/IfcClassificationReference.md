IfcClassificationReference
==========================
An _IfcClassificationReference_ is a reference into a classification system or
source (see _IfcClassification_) for a specific classification key (or
notation).  
  
The inherited attributes have the following meaning:  
  
* _Identification_: holds the key provided for a specific references to classification items (or tables).  
* _Name_: allows for a human interpretable designation of a classification notation.  
* _Location_: optionally holds a direct URI link into the classification system (or source) to hyperlink the classification key.  
  
The _IfcClassificationReference_ can either be assigned directly to the
_IfcClassification_, such as if no classification hierarchy has to be
included, or it references the parent classification notation, if the fully
classification hierarchy is included in the data set. The first is refered to
as "lightweight classification", and the second as "full classification". The
attribute _ReferencedSource_ then holds the following information (choice by
_IfcClassificationReferenceSelect_):  
  
1\. being of type _IfcClassification_: direct reference to the classification
system (with meta information provided);  
2\. being of type _IfcClassificationReference_: reference to the parent
classification notation within the classification hierarchy.  
  
> EXAMPLE  The _IfcClassificationReference_ can be used as a form of
> ''lightweight'' classification through the ''_Identification_'' attribute
> inherited from the abstract _IfcExternalReference_ class. In this case, the
> ''_Identification_'' could take (for instance) the Uniclass notation "L6814"
> which, if the classification was well understood by all parties and was
> known to be taken from a particular classification source, would be
> sufficient. The _Name_ attribute could be the title "Tanking". This would
> remove the need for the overhead of the more complete classification
> structure of the model.  
  
> HISTORY  New entity in IFC2x.  
  
{ .change-ifc2x4}  
> IFC4 CHANGE  The attribute _Description_ and inverse attribute
> _HasReferences_ are added. The attribute _Identification_ has been renamed
> from ItemReference.  
[ _bSI
Documentation_](https://standards.buildingsmart.org/IFC/DEV/IFC4_2/FINAL/HTML/schema/ifcexternalreferenceresource/lexical/ifcclassificationreference.htm)


