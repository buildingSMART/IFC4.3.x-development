IfcObject
=========
An _IfcObject_ is the generalization of any semantically treated thing or
process. Objects are things as they appear - i.e. occurrences.  
  
> NOTE  Examples of _IfcObject_ include physically tangible items such as
> wall, beam or covering, physically existing items such as spaces, or
> conceptual items such as grids or virtual boundaries. It also stands for
> processes such as work tasks, for controls such as cost items, or for actors
> such as persons involved in the design process.  
  
Objects can be named, using the inherited _Name_ attribute, which should be a
user recognizable label for the object occurrance. Further explanations to the
object can be given using the inherited _Description_ attribute. The
_ObjectType_ attribute is used:  
  
* to store the user defined value for all subtypes of _IfcObject_, where a _PredefinedType_ attribute is given, and its value is set to USERDEFINED.  
* to provide a type information (could be seen as a very lightweight classifier) of the subtype of _IfcObject_, if no _PredefinedType_ attribute is given. This is often the case, if no comprehensive list of predefined types is available.  
  
Objects are independent pieces of information that might contain or reference
other pieces of information. There are several relationships in which objects
can be involved:  
  
* **Association to external/internal resource information** - an association relationship that refers to external/internal sources of information. See supertype _IfcObjectDefinition_ for more information.  
* **Assignment of other objects** - an assignment relationship that refers to other types of objects. See supertype _IfcObjectDefinition_ for more information.  
* **Aggregation of other objects** - an aggregation relationship that establishes a whole/part relation. Objects can either be a whole, or a part, or both. See supertype _IfcObjectDefinition_ for more information.  
* **Assignment of a type** : _IsTypedBy_ - a definition relationship _IfcRelDefinesByType_ that uses a type definition to define the common characteristics of this occurrences, potentially including the common shape representation and common properties of all object occurrences assigned to this type. It is a specific - occurrence relationship with implied dependencies (as the occurrence properties depend on the properties of the type, but may override them).  
* **Assignment of a partial type** : _IsDeclaredBy_, _Declares_ - a definition relationship _IfcRelDefinesByObject_ that uses a component of a type definition (a part of a type, called the "declaring part") to define a component of an occurence (part of occurrence, called the "reflected part"). This is also refered to as a "deep copy". The common characteristics of all parts in the occurrence are defined by parts in the type. It is a specific - occurrence relationship with implied dependencies (as the occurrence properties depend on the properties of the type, but may override them).   
* **Assignment of property sets** : _IsDefinedBy_ - a definition relationship _IfcRelDefinesByProperties_ that assignes property set definitions to the object occurrence.  
  
> NOTE  See _IfcRelDefinesByType_ for an explanatory figure. Also see there
> for how to override type properties by occurrence properties. See
> _IfcRelDefinesByObject_ for an explanatory figure for the assignment of a
> partial type.  
  
> HISTORY  New entity in IFC1.0  
  
{ .change-ifc2x4}  
> IFC4 CHANGE  The inverse relationships _Declares_, _IsDeclaredBy_, and
> _IsTypedBy_ have been added, types are not longer included in the
> _IsDefinesBy_ relationship. _IfcProject_ has been promoted to be a subtype
> of _IfcObjectDefinition_ -> _IfcContext_.  
  
{ .spec-head}  
Informal Propositions:  
  
1\. A partial type assignment, i.e. the inverse attribute _IsDeclaredBy_, or
_Declares_ shall only be used, if the object is part of a decomposition, i.e.
if either _IsDecomposedBy_, or _Decomposes_ is exerted.  
[ _bSI
Documentation_](https://standards.buildingsmart.org/IFC/DEV/IFC4_2/FINAL/HTML/schema/ifckernel/lexical/ifcobject.htm)


