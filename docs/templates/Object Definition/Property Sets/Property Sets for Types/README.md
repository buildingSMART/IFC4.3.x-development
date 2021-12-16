Property Sets for Types
=======================

The concept template _Property Sets for Objects_ describes how an object type can be related to a single or multiple property sets. A property set contains a single or multiple properties. The data types of an individual property are single value, enumerated value, bounded value, table value, reference value, list value, and combination of property occurrences.

The property values assigned to an object type apply equally to all occurrences of this object type, see concept _Object Typing_, unless it is overriden by a property with same name within a property set with the same name at an individual object occurrence.

```
concept {
    IfcTypeObject:HasPropertySets -> IfcPropertySet
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
}
```
