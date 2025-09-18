# IfcRelDefinesByTemplate

The objectified relationship _IfcRelDefinesByTemplate_ defines the relationship between a property set template and property sets. Common information about property sets (e.g., the applicable name, description and contained properties) is defined by a property set template and assigned to all relevant property sets.
<!-- end of short definition -->

> NOTE The assignment of an _IfcPropertySetTemplate_ is supported for _IfcPropertySet_ and _IfcQuantitySet_.

The _IfcRelDefinesByTemplate_ is a 1-to-N relationship, as it allows one property set template to be assigned to one or many property sets or quantity sets. Those property sets then share the same property set template definition.

> HISTORY New entity in IFC4.

## Attributes

### RelatedPropertySets
One or many property sets or quantity sets that obtain their definitions from the single property set template.

### RelatingTemplate
Property set template that provides the common definition of related property sets.
