Property Sets with Override
===========================



```
concept {
    IfcObject:IsDefinedBy -> IfcRelDefinesByProperties:RelatedObjects
    IfcObject:IsTypedBy -> IfcRelDefinesByType:RelatedObjects
    IfcRelDefinesByProperties:RelatingPropertyDefinition -> IfcPropertySet
    IfcPropertySet:HasProperties -> IfcPropertySingleValue
    IfcPropertySet:HasProperties -> IfcPropertyBoundedValue
    IfcPropertySet:HasProperties -> IfcPropertyEnumeratedValue
    IfcPropertySet:HasProperties -> IfcPropertyListValue
    IfcPropertySet:HasProperties -> IfcPropertyTableValue
    IfcPropertySet:HasProperties -> IfcPropertySingleValue
    IfcPropertySet:HasProperties -> IfcPropertyBoundedValue
    IfcPropertySet:HasProperties -> IfcPropertyEnumeratedValue
    IfcPropertySet:HasProperties -> IfcPropertyListValue
    IfcPropertySet:HasProperties -> IfcPropertyTableValue
    IfcPropertySet:HasProperties -> IfcPropertySingleValue
    IfcPropertySet:HasProperties -> IfcPropertyBoundedValue
    IfcPropertySet:HasProperties -> IfcPropertyEnumeratedValue
    IfcPropertySet:HasProperties -> IfcPropertyListValue
    IfcPropertySet:HasProperties -> IfcPropertyTableValue
    IfcPropertySet:HasProperties -> IfcPropertySingleValue
    IfcPropertySet:HasProperties -> IfcPropertyBoundedValue
    IfcPropertySet:HasProperties -> IfcPropertyEnumeratedValue
    IfcPropertySet:HasProperties -> IfcPropertyListValue
    IfcPropertySet:HasProperties -> IfcPropertyTableValue
    IfcRelDefinesByType:RelatingType -> IfcTypeObject
    IfcTypeObject:HasPropertySets -> IfcPropertySet
}
```
