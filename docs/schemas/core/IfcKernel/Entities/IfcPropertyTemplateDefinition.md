# IfcPropertyTemplateDefinition

_IfcPropertyTemplateDefinition_ is a generalization of all property and property set templates. Templates define the collection, types, names, applicable measure types and units of individual properties used in a project. The property template definition can be either:

* **Property set template** - _IfcPropertySetTemplate_, a collection of property templates that determine the definition of properties used within a project context.
* **Property template** - _IfcPropertyTemplate_, a single template that determines the definition of a particular property used in the same project context. The template may determine the name, description, data type, the unit, or a standard expression for each property that is based on that template.
<!-- end of short definition -->

The subtypes of _IfcPropertyTemplateDefinition_ are declared within a project context. The uppermost template definition (e.g. the _IfcPropertySetTemplate_ including several _IfcPropertyTemplate_'s) should be related to the context, either _IfcProject_, or _IfcProjectLibrary_, using the inherited _HasContext_ inverse attribute.

> HISTORY New entity in IFC4.
