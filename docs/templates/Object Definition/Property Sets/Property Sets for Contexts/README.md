Property Sets for Contexts
==========================

The concept template _Property Sets for Contexts_ describes how an context can be related to a single or multiple property sets. A property set contains a single or multiple properties. The data types of an individual property are single value, enumerated value, bounded value, table value, reference value, list value, and combination of property occurrences.

```
concept {
    IfcContext:IsDefinedBy -> IfcRelDefinesByProperties:RelatedObjects
    IfcRelDefinesByProperties:RelatingPropertyDefinition -> IfcPropertySet
    IfcPropertySet:HasProperties -> IfcPropertySingleValue
    IfcPropertySet:HasProperties -> IfcPropertyBoundedValue
    IfcPropertySet:HasProperties -> IfcPropertyEnumeratedValue
    IfcPropertySet:HasProperties -> IfcPropertyListValue
    IfcPropertySet:HasProperties -> IfcPropertyTableValue
    IfcPropertySingleValue -> Single_Value
    IfcPropertyBoundedValue -> Bounded_Value
    IfcPropertyEnumeratedValue -> Enumerated_Value
    IfcPropertyListValue -> List_Value
    IfcPropertyTableValue -> Table_Value
    IfcPropertySet:Name[binding="PsetName"]
    IfcPropertySet:HasProperties[binding="Properties"]
}
```
