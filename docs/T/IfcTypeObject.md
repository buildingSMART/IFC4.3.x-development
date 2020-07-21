IfcTypeObject
=============
The object type defines the specific information about a type, being common to
all occurrences of this type. It refers to the specific level of the well
recognized _generic - specific - occurrance_ modeling paradigm. The
_IfcTypeObject_ gets assigned to the individual object instances (the
occurrences) via the _IfcRelDefinesByType_ relationship.  
  
> NOTE  The terms ''Type'' and ''Style'' are often used interchangeably.  
  
The object type is represented by a set of property set definitions. The
attached property sets describe the available alpha-numeric information about
the object type. and are used to define all common properties that apply to
all object occurrences of that type.  
  
> NOTE  If a property having having the same name is used within the
> _IfcPropertySet_ assigned to an _IfcTypeObject_ (and subtypes) and to an
> occurrence of that type, then the occurrence property overrides the type
> property. See _IfcRelDefinesByType_ for an explanatory figure.  
  
Object types may be exchanged without being already assigned to objects. An
object type may have an indication of the library (or catalogue) from which
its definition originates. This association is handled by the inherited
_HasAssociations_ relationship pointing to _IfcRelAssociatesLibrary_.  
  
> HISTORY  New entity in IFC2x  
  
{ .change-ifc2x3}  
> IFC2x3 CHANGE  The _IfcTypeObject_ is now subtyped from the new supertype
> _IfcObjectDefinition_, and the attribute _HasPropertySets_ has been changed
> from a LIST into a SET.  
  
{ .change-ifc2x4}  
> IFC4 CHANGE  The entity _IfcTypeObject_ shall not be instantiated from IFC4
> onwards. It will be changed into an ABSTRACT supertype in future releases of
> IFC. The inverse attribute _Types_ has been renamed from _ObjectTypeOf_.  
[ _bSI
Documentation_](https://standards.buildingsmart.org/IFC/DEV/IFC4_2/FINAL/HTML/schema/ifckernel/lexical/ifctypeobject.htm)


Attribute definitions
---------------------
| Attribute            | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
|----------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ApplicableOccurrence | The attribute optionally defines the data type of the occurrence object, to which the assigned type object can relate. If not present, no instruction is given to which occurrence object the type object is applicable. The following conventions are used:\X\0D* The IFC entity name of the applicable occurrence using the IFC naming convention, CamelCase with IFC prefix\X\0D* It can be optionally followed by the predefined type after the separator "/" (forward slash), using uppercase\X\0D* If one type object is applicable to many occurrence objects, then those occurrence object names should be separate by comma "," forming a comma separated string. \X\0D\X\0D> EXAMPLE Refering to a furniture as applicable occurrence entity would be expressed as ''IfcFurnishingElement'', refering to a brace as applicable entity would be expressed as ''IfcMember/BRACE'', refering to a wall and wall standard case would be expressed as ''IfcWall, IfcWallStandardCase''. |

Formal Propositions
-------------------
| Rule                   | Description   |
|------------------------|---------------|
| NameRequired           |               |
| UniquePropertySetNames |               |

Associations
------------
| Attribute       | Description   |
|-----------------|---------------|
| HasPropertySets |               |
| Types           |               |

