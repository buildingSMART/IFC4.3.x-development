IfcTypeProcess
==============
_IfcTypeProcess_ defines a specific (or type) definition of a process or
activity without being assigned to a schedule or a time.\S\ It is used to
define a process or activity specification, that is, the specific process or
activity information that is common to all occurrences that are defined for
that process or activity type.  
  
An _IfcTypeProcess_ may have a list of property set attached. Values of these
properties are common to all occurrences of that process or activity type. The
type occurrence relationship is realized using the objectified relationship
_IfcRelDefinesByType_.  
  
Subtypes of _IfcTypeProcess_ may be exchanged without being already assigned
to subtypes of _IfcProcess_.  
  
> HISTORY  New entity in IFC4.  
[ _bSI
Documentation_](https://standards.buildingsmart.org/IFC/DEV/IFC4_2/FINAL/HTML/schema/ifckernel/lexical/ifctypeprocess.htm)


Attribute definitions
---------------------
| Attribute       | Description                                                                                                                                                                                                                                                             |
|-----------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| OperatesOn      |                                                                                                                                                                                                                                                                         |
| Identification  | An identifying designation given to a process type.                                                                                                                                                                                                                     |
| LongDescription | An long description, or text, describing the activity in detail.\X\0D> NOTE  The inherited _SELF\\\IfcRoot.Description_ attribute is used as the short description.                                                                                                     |
| ProcessType     | The type denotes a particular type that indicates the process further. The use has to be established at the level of instantiable subtypes. In particular it holds the user defined type, if the enumeration of the attribute ''PredefinedType'' is set to USERDEFINED. |

