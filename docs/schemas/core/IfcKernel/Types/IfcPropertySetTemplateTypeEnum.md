# IfcPropertySetTemplateTypeEnum

This enumeration defines the general applicability of instances of _IfcPropertySet_, or _IfcElementQuantity_ defined by this _IfcPropertySetTemplate_, to subtypes of _IfcObjectDefinition_.<!-- end of definition -->

> HISTORY  New enumeration in IFC4.

## Items

### PSET_TYPEDRIVENONLY
The property sets defined by this _IfcPropertySetTemplate_ can only be assigned to subtypes of _IfcTypeObject_.

### PSET_TYPEDRIVENOVERRIDE
The property sets defined by this _IfcPropertySetTemplate_ can be assigned
to subtypes of _IfcTypeObject_ and can be overridden by a
property set with same name at subtypes of _IfcObject_.

### PSET_OCCURRENCEDRIVEN
The property sets defined by this _IfcPropertySetTemplate_ can only be assigned to subtypes of _IfcObject_.

### PSET_PERFORMANCEDRIVEN
The property sets defined by this _IfcPropertySetTemplate_ can only be assigned to _IfcPerformanceHistory_, which is
related to the applicable object by means of IfcRelAssignsToControl.

### PSET_PROFILEDRIVEN
The property sets defined by this _IfcPropertySetTemplate_ are to be encoded in an IfcProfileProperties entity and assigned to an IfcProfileDef.

### PSET_MATERIALDRIVEN
The property sets defined by this _IfcPropertySetTemplate_ are to be encoded in an IfcMaterialProperties entity and assigned to an IfcMaterialDefinition.

### QTO_TYPEDRIVENONLY
The element quantity defined by this _IfcPropertySetTemplate_ can only be assigned to subtypes of _IfcTypeObject_.

### QTO_TYPEDRIVENOVERRIDE
The element quantity defined by this _IfcPropertySetTemplate_ can be
assigned to subtypes of _IfcTypeObject_ and can be overridden
by an element quantity with same name at subtypes of _IfcObject_.

### QTO_OCCURRENCEDRIVEN
The element quantity defined by this _IfcPropertySetTemplate_ can only be
assigned to subtypes of _IfcObject_.

### NOTDEFINED
No restriction provided, the property sets defined by this _IfcPropertySetTemplate_ can be assigned to any entity, if not
otherwise restricted by the _ApplicableEntity_ attribute.
