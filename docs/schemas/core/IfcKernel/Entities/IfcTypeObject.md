# IfcTypeObject

The object type defines the specific information about a type, being common to all occurrences of this type. It refers to the specific level of the well recognized _generic - specific - occurrence_ modeling paradigm. The _IfcTypeObject_ gets assigned to the individual object instances (the occurrences) via the _IfcRelDefinesByType_ relationship.<!-- end of definition -->

> NOTE The terms 'Type' and 'Style' are often used interchangeably.

The object type is represented by a set of property set definitions. The attached property sets describe the available alpha-numeric information about the object type and are used to define all common properties that apply to all object occurrences of that type.

> NOTE If a property having the same name is used within the _IfcPropertySet_ assigned to an _IfcTypeObject_ (and subtypes) and to an occurrence of that type, then the occurrence property overrides the type property. See _IfcRelDefinesByType_ for an explanatory figure.

Object types may be exchanged without being already assigned to objects. An object type may have an indication of the library (or catalogue) from which its definition originates. This association is handled by the inherited _HasAssociations_ relationship pointing to _IfcRelAssociatesLibrary_.

> HISTORY New entity in IFC2x

{ .change-ifc2x3}
> IFC2x3 CHANGE The _IfcTypeObject_ is now subtyped from the new supertype _IfcObjectDefinition_, and the attribute _HasPropertySets_ has been changed from a LIST into a SET.

{ .change-ifc2x4}
> IFC4 CHANGE The entity _IfcTypeObject_ shall not be instantiated from IFC4 onwards. It will be changed into an ABSTRACT supertype in future releases of IFC. The inverse attribute _Types_ has been renamed from _ObjectTypeOf_.

## Attributes

### ApplicableOccurrence
The attribute optionally defines the data type of the occurrence object, to which the assigned type object can relate. If not present, no instruction is given to which occurrence object the type object is applicable. The following conventions are used:

* The IFC entity name of the applicable occurrence using the IFC naming convention, CamelCase with "Ifc" prefix
* It can be optionally followed by the predefined type after the separator "/" (forward slash), using uppercase
* If one type object is applicable to many occurrence objects, then those occurrence object names should be separate by comma "," forming a comma separated string.

> EXAMPLE Referring to a furniture as applicable occurrence entity would be expressed as 'IfcFurnishingElement', referring to a brace as applicable entity would be expressed as 'IfcMember/BRACE'.

### HasPropertySets
Set of unique property sets, that are associated with the object type and are common to all object occurrences referring to this object type.
{ .change-ifc2x3}
> IFC2x3 CHANGE The attribute aggregate type has been changed from LIST to SET.

### Types
Reference to the relationship IfcRelDefinesByType and thus to those occurrence objects, which are defined by this type.

## Formal Propositions

### NameRequired
A Name attribute has to be provided. The name can be declared within the IFC specification as part of the property set agreements.

### UniquePropertySetNames
Every individual _IfcPropertySetDefinition_ assigned to the instance in the attribute _HasPropertySets_ shall have a unique _Name_ attribute value.

