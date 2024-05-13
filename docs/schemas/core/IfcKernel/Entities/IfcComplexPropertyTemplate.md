# IfcComplexPropertyTemplate

The _IfcComplexPropertyTemplate_ defines the template for all complex properties, either the _IfcComplexProperty_'s, or the _IfcPhysicalComplexQuantity_'s. The individual complex property templates are interpreted according to their _Name_ attribute and and optional _UsageName_ attribute.<!-- end of definition -->

> HISTORY  New entity in IFC4.

## Attributes

### UsageName
Usage description of the _IfcComplexPropertyTemplate_.

### TemplateType
Property type defining whether the property template defines a property as a IfcComplexProperty or IfcPhysicalComplexQuantity

### HasPropertyTemplates
Reference to a set of property templates. It should only be provided, if the _PropertyType_ is set to COMPLEX.

## Formal Propositions

### UniquePropertyNames
Every individual _IfcPropertyTemplate_ within the complex property template shall have a unique _Name_ attribute value.

### NoSelfReference
The _IfcComplexPropertyTemplate_ should not reference itself within the set of _HasPropertyTemplates_.