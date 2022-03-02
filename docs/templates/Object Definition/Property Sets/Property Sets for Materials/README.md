Property Sets for Materials
===========================

The concept template _Property Sets for Materials_ describes how a material can be related to a single or multiple property sets. A property set contains a single or multiple properties. The data types of an individual property are single value, enumerated value, bounded value, table value, reference value, list value, and combination of property occurrences.

NOTE: An IfcMaterial is not an IfcObject. For legacy reasons, this concept is listed under _Object Definition_. In future versions of the standard the various property set association mechanisms will likely be unified. In the current version of this template, there is no mechanism to further guide the applicability in a way similar to how applicability can be tailored to individual predefined types of leaf entities of IfcObject that feature the PredefinedType attribute. In future versions of the standard there will likely be the possibility to make property sets applicable to specific categories of IfcMaterial.

Property Sets applicable to this template will carry the IfcPropertySetTemplateTypeEnum "PSET_MATERIALDRIVEN".

```
concept {
    IfcMaterial:HasProperties -> IfcMaterialProperties:Material
    
    IfcMaterialProperties:Name -> IfcIdentifier
    IfcMaterialProperties:Description -> IfcText
    IfcMaterialProperties:Properties -> IfcPropertySingleValue
    IfcMaterialProperties:Properties -> IfcPropertyBoundedValue
    IfcMaterialProperties:Properties -> IfcPropertyEnumeratedValue
    IfcMaterialProperties:Properties -> IfcPropertyListValue
    IfcMaterialProperties:Properties -> IfcPropertyTableValue
    
    IfcPropertySingleValue -> Single_Value
    IfcPropertyBoundedValue -> Bounded_Value
    IfcPropertyEnumeratedValue -> Enumerated_Value
    IfcPropertyListValue -> List_Value
    IfcPropertyTableValue -> Table_Value
    
    IfcMaterialProperties:Name[binding="PsetName"]
    IfcMaterialProperties:Properties[binding="Properties"]
}
```
