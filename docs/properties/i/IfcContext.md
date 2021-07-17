IfcContext
==========

_IfcContext_ is the generalization of a project context in which objects, type objects, property sets, and properties are defined. The _IfcProject_ as subtype of _IfcContext_ provides the context for all information on a construction project, it may include one or several _IfcProjectLibrary_'s as subtype of _IfcContext_ to register the included libraries for the project. A library of products that is referenced is declared within the _IfcProjectLibrary_ as the context of that library.

Context definitions can be named, using the inherited _Name_ attribute, which should be a user recognizable key or number for the context. The _LongName_ can add a full name. Further explanations to the context can be given using the inherited _Description_ attribute.

A Context is declared by the relationship object _IfcRelDeclares_ that refers to the corresponding objects within the context. More specific relationships are introduced at the level of subtypes.

> HISTORY&nbsp; New abstract entity in IFC4.
