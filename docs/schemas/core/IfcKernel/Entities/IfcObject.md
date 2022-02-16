# IfcObject

An _IfcObject_ is the generalization of any semantically treated thing or process. Objects are things as they appear - i.e. occurrences.

> NOTE&nbsp; Examples of _IfcObject_ include physically tangible items such as wall, beam or covering, physically existing items such as spaces, or conceptual items such as grids or virtual boundaries. It also stands for processes such as work tasks, for controls such as cost items, or for actors such as persons involved in the design process.

Objects can be named, using the inherited _Name_ attribute, which should be a user recognizable label for the object occurrance. Further explanations to the object can be given using the inherited _Description_ attribute. The _ObjectType_ attribute is used:

* to store the user defined value for all subtypes of _IfcObject_, where a _PredefinedType_ attribute is given, and its value is set to USERDEFINED.
* to provide a type information (could be seen as a very lightweight classifier) of the subtype of _IfcObject_, if no _PredefinedType_ attribute is given. This is often the case, if no comprehensive list of predefined types is available.

Objects are independent pieces of information that might contain or reference other pieces of information. There are several relationships in which objects can be involved:

* **Association to external/internal resource information** - an association relationship that refers to external/internal sources of information. See supertype _IfcObjectDefinition_ for more information.
* **Assignment of other objects** - an assignment relationship that refers to other types of objects. See supertype _IfcObjectDefinition_ for more information.
* **Aggregation of other objects** - an aggregation relationship that establishes a whole/part relation. Objects can either be a whole, or a part, or both. See supertype _IfcObjectDefinition_ for more information.
* **Assignment of a type** : _IsTypedBy_ - a definition relationship _IfcRelDefinesByType_ that uses a type definition to define the common characteristics of this occurrences, potentially including the common shape representation and common properties of all object occurrences assigned to this type. It is a specific - occurrence relationship with implied dependencies (as the occurrence properties depend on the properties of the type, but may override them).
* **Assignment of a partial type** : _IsDeclaredBy_, _Declares_ - a definition relationship _IfcRelDefinesByObject_ that uses a component of a type definition (a part of a type, called the "declaring part") to define a component of an occurence (part of occurrence, called the "reflected part"). This is also refered to as a "deep copy". The common characteristics of all parts in the occurrence are defined by parts in the type. It is a specific - occurrence relationship with implied dependencies (as the occurrence properties depend on the properties of the type, but may override them).  
* **Assignment of property sets** : _IsDefinedBy_ - a definition relationship _IfcRelDefinesByProperties_ that assignes property set definitions to the object occurrence.

> NOTE&nbsp; See _IfcRelDefinesByType_ for an explanatory figure. Also see there for how to override type properties by occurrence properties. See _IfcRelDefinesByObject_ for an explanatory figure for the assignment of a partial type.

> HISTORY&nbsp; New entity in IFC1.0

{ .change-ifc2x4}
> IFC4 CHANGE&nbsp; The inverse relationships _Declares_, _IsDeclaredBy_, and _IsTypedBy_ have been added, types are not longer included in the _IsDefinesBy_ relationship. _IfcProject_ has been promoted to be a subtype of _IfcObjectDefinition_ -> _IfcContext_.

{ .spec-head}
Informal Propositions:

1. A partial type assignment, i.e. the inverse attribute _IsDeclaredBy_, or _Declares_ shall only be used, if the object is part of a decomposition, i.e. if either _IsDecomposedBy_, or _Decomposes_ is exerted.

## Attributes

### ObjectType
The type denotes a particular type that indicates the object further. The use has to be established at the level of instantiable subtypes. In particular it holds the user defined type, if the enumeration of the attribute _PredefinedType_ is set to USERDEFINED.

### IsDeclaredBy
Link to the relationship object pointing to the declaring object that provides the object definitions for this object occurrence. The declaring object has to be part of an object type decomposition. The associated _IfcObject_, or its subtypes, contains the specific information (as part of a type, or style, definition), that is common to all reflected instances of the declaring _IfcObject_, or its subtypes. 
{ .change-ifc2x4}
> IFC4 CHANGE&nbsp; New inverse relationship, change made with upward compatibility for file based exchange.

### Declares
Link to the relationship object pointing to the reflected object(s) that receives the object definitions. The reflected object has to be part of an object occurrence decomposition. The associated _IfcObject_, or its subtypes, provides the specific information (as part of a type, or style, definition), that is common to all reflected instances of the declaring _IfcObject_, or its subtypes. 
{ .change-ifc2x4}
> IFC4 CHANGE&nbsp; New inverse relationship, change made with upward compatibility for file based exchange.

### IsTypedBy
Set of relationships to the object type that provides the type definitions for this object occurrence. The then associated _IfcTypeObject_, or its subtypes, contains the specific information (or type, or style), that is common to all instances of _IfcObject_, or its subtypes, referring to the same type. 
{ .change-ifc2x4}
> IFC4 CHANGE&nbsp; New inverse relationship, the link to _IfcRelDefinesByType_ had previously be included in the inverse relationship _IfcRelDefines_. Change made with upward compatibility for file based exchange.

### IsDefinedBy
Set of relationships to property set definitions attached to this object. Those statically or dynamically defined properties contain alphanumeric information content that further defines the object. 
{ .change-ifc2x4}
> IFC4 CHANGE&nbsp; The data type has been changed from _IfcRelDefines_ to _IfcRelDefinesByProperties_ with upward compatibility for file based exchange.

## Formal Propositions

### UniquePropertySetNames


## Concepts

### Object Predefined Type


### Object Typing

Any object occurrence can be typed by being assigned to a common object type utilizing this concept. A particular rule, restricting the applicable subtypes of IfcTypeObject that can be assigned, is introduced by overriding this concept at the level of subtypes of IfcObject.

 


### Object User Identity

An attribute Name and optionally Description can be used for all subypes of IfcObject. For those subtypes, that have an object type definition, such as ifcBeam - IfcBeamType, the common Name and optionally Description is associated with the object type.


### Property Sets for Objects

Any object occurrence can hold property sets, each being a set of individual properties having name, description, value(s) and unit(s). A reference to applicable property sets, being part of this specification, is introduced at the level of sub types of IfcObject.


### Property Sets with Override

Any object occurrence can hold property sets, either directly at the object occurrence as element specific property sets, or at the object type, as type property sets. In this case, the properties that are provided to the object occurrence are the combinations of element specific and type properties. In case, that the same property (within the same property set, is defined both, in occurrence and type properties, the property value of the occurrence property overrides the property value of the type property.


