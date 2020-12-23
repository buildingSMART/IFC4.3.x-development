# IfcPropertySetTemplate

_IfcPropertySetTemplate_ defines the template for all dynamically extensible property sets represented by _IfcPropertySet_. The property set template is a container of property templates within a property tree. The individual property templates are interpreted according to their _Name_ attribute and shall have no values assigned.

> NOTE&nbsp; By convention an _IfcPropertySetTemplate_ can also be used as a template for an _IfcElementQuantity_, being a particular type of a property set definition.

Property set templates can form part of a property library used and declared within a project. Depending on the _TemplateType_ the _IfcPropertySetTemplate_ defines a template for:

* "Pset_" - occurrences of _IfcPropertySet_
* "QTO_" - occurrences of _IfcElementQuantity_

The inherited _HasContext_ inverse relation to _IfcRelDeclares_ is used to declare the _IfcPropertySetTemplate_ within a project library. If included in an exchange data set it can then be traversed through the _IfcProjectLibrary_. The _Defines_ inverse relation to _IfcRelDefinesByTemplate_ is provided to keep the definition relationship between the _IfcPropertySetTemplate_ and the one to many _IfcPropertySet_'s, for which it provides the template. Figure 1 illustrates relationships used for property set templates.

&nbsp;

!["property set template"](../../../../../../figures/ifcpropertysettemplate_fig-1.png "Figure 1 &mdash; Property set template relationships")

Between _IfcProperty_'s within the _HasProperties_ set of _IfcPropertySet_ having the same _Name_ attribute value as the _IfcPropertyTemplate_'s within the _HasPropertyTemplates_ set of _IfcPropertySetTemplate_ an implicit definition relationship is established that assigns the template to the individual properties.

> HISTORY&nbsp; New entity in IFC4.

## Attributes

### TemplateType
Property set type defining whether the property set is applicable to a type (subtypes of _IfcTypeObject_), to an occurrence (subtypes of _IfcObject_), or as a special case to a performance history.  
  
The attribute _ApplicableEntity_ may further refine the applicability to a single or multiple entity type(s).

### ApplicableEntity
The attribute optionally defines the data type of the applicable type or occurrence object, to which the assigned property set template can relate. If not present, no instruction is given to which type or occurrence object the property set template is applicable. The following conventions are used:
* The IFC entity name of the applicable entity using the IFC naming convention, CamelCase with IFC prefix
* It can be optionally followed by the predefined type after the separator "/" (forward slash), using upper case
* If a performance history object of a particular distribution object is attributes by the property set template, then the entity name (and potentially amended by the predefined type) is expanded by adding '[PerformanceHistory]' 
* If one property set template is applicable to many type and/or occurrence objects, then those object names should be separate by comma "," forming a comma separated string. 

> EXAMPLE Refering to a boiler type as applicable entity would be expressed as 'IfcBoilerType', refering to a steam boiler type as applicable entity would be expressed as 'IfcBoilerType/STEAM', refering to a wall and wall standard case and a wall type would be expressed as 'IfcWall, IfcWallStandardCase, IfcWallType'. An applicable _IfcPerformanceHistory_ assigned to an occurrence or type object would be indicated by IfcBoilerType[PerformanceHistory], or respectively IfcBoilerType/STEAM[PerformanceHistory].

### HasPropertyTemplates
Set of _IfcPropertyTemplate_'s that are defined within the scope of the _IfcPropertySetTemplate_.

### Defines
Relation to the property sets, via the objectified relationship _IfcRelDefinesByTemplate_, that, if given, utilize the definition template.

## WhereRules

### ExistsName
The _Name_ attribute has to be provided. The attribute is used to specify the signifier of the property set template. The properties that are allowed to be attached to a particular property set template may be given within the property set definition part of the IFC specification.

### UniquePropertyNames
Every individual _IfcPropertyTemplate_ within the property set template shall have a unique _Name_ attribute value.
