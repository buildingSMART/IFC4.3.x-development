# IfcPropertyTemplate

The _IfcPropertyTemplate_ is an abstract supertype comprising the templates for all dynamically extensible properties, either as an _IfcComplexPropertyTemplate_, or an _IfcSimplePropertyTemplate_. These templates determine the structure of:

* in case of _IfcComplexPropertyTemplate_
    * an _IfcComplexProperty_
    * an _IfcPhysicalComplexQuantity_
* in case of _IfcSimplePropertyTemplate_
    * a subtype of _IfcSimpleProperty_
    * a subtype of _IfcPhysicalSimpleQuantity_

The individual property templates are interpreted according to their _Name_ attribute and may have a predefined property type, property unit, and property data type. A template however shall not have measure values, or quantity values assigned.

> NOTE  Property templates can form part of a property library used and attached as part of a project library. In general the _IfcPropertySetTemplate_, containing the subtypes of _IfcPropertyTemplate_ would be directly linked to the _IfcProjectLibrary_.

> HISTORY  New entity in IFC4.

## Attributes

### PartOfComplexTemplate
Reference to a complex property template. It should only be provided, if the _PropertyType_ of the referenced complex property template is set to COMPLEX.

### PartOfPsetTemplate
Reference to the _IfcPropertySetTemplate_ that defines the scope for the _IfcPropertyTemplate_. A single _IfcPropertyTemplate_ can be defined within the scope of zero, one or many _IfcPropertySetTemplate_ entities.
