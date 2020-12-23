# IfcComplexPropertyTemplate

The _IfcComplexPropertyTemplate_ defines the template for all complex properties, either the _IfcComplexProperty_'s, or the _IfcPhysicalComplexQuantity_'s. The individual complex property templates are interpreted according to their _Name_ attribute and and optional _UsageName_ attribute.

> HISTORY&nbsp; New entity in IFC4.

## Attributes

### UsageName


### TemplateType


### HasPropertyTemplates
Reference to a set of property templates. It should only be provided, if the _PropertyType_ is set to <small>COMPLEX</small>.

## Formal Propositions

### UniquePropertyNames
Every individual _IfcPropertyTemplate_ within the complex property template shall have a unique _Name_ attribute value.

### NoSelfReference

