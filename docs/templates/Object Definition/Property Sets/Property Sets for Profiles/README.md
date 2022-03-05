Property Sets for Profiles
==========================

The concept template _Property Sets for Profiles_ describes how a material can be related to a single or multiple property sets. A property set contains a single or multiple properties. The data type of an individual property can be one of single, enumerated, value, table, reference or list value, and combination of property occurrences.

NOTE: An IfcProfileDef is not an IfcObject. For legacy reasons, this concept is listed under _Object Definition_. In future versions of the standard the various property set association mechanisms will likely be unified.

Property Sets applicable to this template will carry the IfcPropertySetTemplateTypeEnum "PSET_PROFILEDRIVEN".

```
concept {
    IfcProfileDef:HasProperties -> IfcProfileProperties:ProfileDefinition
    
    IfcProfileProperties:Name -> IfcIdentifier
    IfcProfileProperties:Description -> IfcText
    IfcProfileProperties:Properties -> IfcPropertySingleValue
    IfcProfileProperties:Properties -> IfcPropertyBoundedValue
    IfcProfileProperties:Properties -> IfcPropertyEnumeratedValue
    IfcProfileProperties:Properties -> IfcPropertyListValue
    IfcProfileProperties:Properties -> IfcPropertyTableValue
    
    IfcPropertySingleValue -> Single_Value
    IfcPropertyBoundedValue -> Bounded_Value
    IfcPropertyEnumeratedValue -> Enumerated_Value
    IfcPropertyListValue -> List_Value
    IfcPropertyTableValue -> Table_Value
    
    IfcProfileProperties:Name[binding="PsetName"]
    IfcProfileProperties:Properties[binding="Properties"]
}
```
