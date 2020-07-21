IfcContext
==========
_IfcContext_ is the generalization of a project context in which objects, type
objects, property sets, and properties are defined. The _IfcProject_ as
subtype of _IfcContext_ provides the context for all information on a
construction project, it may include one or several _IfcProjectLibrary_''s as
subtype of _IfcContext_ to register the included libraries for the project. A
library of products that is referenced is declared within the
_IfcProjectLibrary_ as the context of that library.  
  
Context definitions can be named, using the inherited _Name_ attribute, which
should be a user recognizable key or number for the context. The _LongName_
can add a full name. Further explanations to the context can be given using
the inherited _Description_ attribute.  
  
A Context is declared by the relationship object _IfcRelDeclares_ that refers
to the corresponding objects within the context. More specific relationships
are introduced at the level of subtypes.  
  
> HISTORY  New abstract entity in IFC4.  
[ _bSI
Documentation_](https://standards.buildingsmart.org/IFC/DEV/IFC4_2/FINAL/HTML/schema/ifckernel/lexical/ifccontext.htm)


Attribute definitions
---------------------
| Attribute   | Description                                                                                                                                                                                                                                                                                                                                                      |
|-------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ObjectType  | The object type denotes a particular type that indicates the object further. The use has to be established at the level of instantiable subtypes. \X\0D> NOTE  Subtypes of _IfcContext_ do not introduce a _PredefinedType_ attribute, therefore the usage of _ObjectType_ is not bound to the selection of USERDEFINED within the _PredefinedType_ enumaration. |
| LongName    | Long name for the context as used for reference purposes.                                                                                                                                                                                                                                                                                                        |
| Phase       | Current project phase, or life-cycle phase of this project. Applicable values have to be agreed upon by view definitions or implementer agreements.                                                                                                                                                                                                              |

Associations
------------
| Attribute              | Description   |
|------------------------|---------------|
| RepresentationContexts |               |
| UnitsInContext         |               |
| Declares               |               |
| IsDefinedBy            |               |

