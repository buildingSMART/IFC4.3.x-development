Property Sets for Objects
=========================

The concept template _Property Sets for Objects_ describes how an object occurrence can be related to a single or multiple property sets. A property set contains a single or multiple properties. The data types of an individual property are single value, enumerated value, bounded value, table value, reference value, list value, and combination of property occurrences.

Property sets can also be related to an object type, see concept _Property Sets for Types_. They then define the common properties for all occurrences of the same type. If the same property (by name) is provided by the same property set (by name), then the properties directly assigned to the object occurrence override the properties assigned to the object type.

```
concept {
    IfcObject:IsDefinedBy -> IfcRelDefinesByProperties:RelatedObjects
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
    IfcObject:PredefinedType[binding="PredefinedType"]
    IfcPropertySet:Name[binding="PsetName"]
    IfcPropertySet:HasProperties[binding="Properties"]
}
```
