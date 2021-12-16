Property Sets with Override
===========================



```
concept {
    IfcObject:IsDefinedBy -> IfcRelDefinesByProperties:RelatedObjects
    IfcObject:IsTypedBy -> IfcRelDefinesByType:RelatedObjects
    IfcRelDefinesByProperties:RelatingPropertyDefinition -> IfcPropertySet_0
    IfcPropertySet_0:HasProperties -> IfcPropertySingleValue_0
    IfcPropertySet_0:HasProperties -> IfcPropertyBoundedValue_0
    IfcPropertySet_0:HasProperties -> IfcPropertyEnumeratedValue_0
    IfcPropertySet_0:HasProperties -> IfcPropertyListValue_0
    IfcPropertySet_0:HasProperties -> IfcPropertyTableValue_0
    IfcPropertySingleValue_0 -> Single_Value
    IfcPropertyBoundedValue_0 -> Bounded_Value
    IfcPropertyEnumeratedValue_0 -> Enumerated_Value
    IfcPropertyListValue_0 -> List_Value
    IfcPropertyTableValue_0 -> Table_Value
    IfcRelDefinesByType:RelatingType -> IfcTypeObject
    IfcTypeObject:HasPropertySets -> IfcPropertySet_1
    IfcPropertySet_1:HasProperties -> IfcPropertySingleValue_1
    IfcPropertySet_1:HasProperties -> IfcPropertyBoundedValue_1
    IfcPropertySet_1:HasProperties -> IfcPropertyEnumeratedValue_1
    IfcPropertySet_1:HasProperties -> IfcPropertyListValue_1
    IfcPropertySet_1:HasProperties -> IfcPropertyTableValue_1
    IfcPropertySingleValue_1 -> Single_Value
    IfcPropertyBoundedValue_1 -> Bounded_Value
    IfcPropertyEnumeratedValue_1 -> Enumerated_Value
    IfcPropertyListValue_1 -> List_Value
    IfcPropertyTableValue_1 -> Table_Value
    IfcObject:PredefinedType[binding="PredefinedType"]
    IfcPropertySet_0:Name[binding="PsetName"]
    IfcPropertySet_0:HasProperties[binding="Properties"]
    IfcPropertySet_1:Name[binding="TypePsetName"]
    IfcPropertySet_1:HasProperties[binding="TypeProperties"]
}
```
