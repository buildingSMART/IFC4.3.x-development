Project Template Definitions
============================

Declaration of property set templates, including the property templates that are used as property definitions. Such templates define the applicable properties, their names, descriptions, measure types and property type (single, enumerated, bounded list or table value).

> HISTORY  New concept template enabled by schema enhancements in IFC4.

```
concept {
    IfcContext:Declares -> IfcRelDeclares:RelatingContext
    IfcContext:Phase -> IfcLabel_4
    IfcContext:ObjectType -> IfcLabel_5
    IfcContext:LongName -> IfcLabel_6
    IfcRelDeclares:RelatedDefinitions -> IfcPropertySetTemplate
    IfcPropertySetTemplate:TemplateType -> IfcPropertySetTemplateTypeEnum
    IfcPropertySetTemplate:ApplicableEntity -> IfcIdentifier
    IfcPropertySetTemplate:HasPropertyTemplates -> IfcSimplePropertyTemplate
    IfcSimplePropertyTemplate:TemplateType -> IfcSimplePropertyTemplateTypeEnum
    IfcSimplePropertyTemplate:PrimaryMeasureType -> IfcLabel_0
    IfcSimplePropertyTemplate:SecondaryMeasureType -> IfcLabel_1
    IfcSimplePropertyTemplate:Enumerators -> IfcPropertyEnumeration
    IfcSimplePropertyTemplate:AccessState -> IfcStateEnum
    IfcSimplePropertyTemplate:PrimaryUnit -> IfcUnit_0
    IfcSimplePropertyTemplate:SecondaryUnit -> IfcUnit_1
    IfcSimplePropertyTemplate:Expression -> IfcLabel_3
    IfcPropertyEnumeration:Name -> IfcLabel_2
    IfcPropertyEnumeration:EnumerationValues -> IfcValue
    IfcRelDeclares:RelatedDefinitions[binding="Type"]
}
```
