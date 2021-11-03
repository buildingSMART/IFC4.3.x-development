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
    IfcPropertySingleValue -> Single_Value
    IfcPropertySingleValue -> Single_Value
    IfcPropertyBoundedValue -> Bounded_Value
    IfcPropertyBoundedValue -> Bounded_Value
    IfcPropertyEnumeratedValue -> Enumerated_Value
    IfcPropertyEnumeratedValue -> Enumerated_Value
    IfcPropertyListValue -> List_Value
    IfcPropertyListValue -> List_Value
    IfcPropertyTableValue -> Table_Value
    IfcPropertyTableValue -> Table_Value
    IfcRelDefinesByType:RelatingType -> IfcTypeObject
    IfcTypeObject:HasPropertySets -> IfcPropertySet
    IfcObject:PredefinedType[binding="PredefinedType"]
    IfcPropertySet:Name[binding="TypePsetName"]
    IfcPropertySet:HasProperties[binding="TypeProperties"]
}
```
