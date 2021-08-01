Project Template Definitions
============================

Declaration of property set templates, including the property templates that are used as property definitions. Such templates define the applicable properties, their names, descriptions, measure types and property type (single, enumerated, bounded list or table value).

> HISTORY&nbsp; New concept template enabled by schema enhancements in IFC4.

```
concept {
    IfcContext:Declares -> IfcRelDeclares:RelatingContext
    IfcContext:Phase -> IfcLabel
    IfcContext:ObjectType -> IfcLabel
    IfcContext:LongName -> IfcLabel
    IfcRelDeclares:RelatedDefinitions -> IfcPropertySetTemplate
    IfcPropertySetTemplate:TemplateType -> IfcPropertySetTemplateTypeEnum
    IfcPropertySetTemplate:ApplicableEntity -> IfcIdentifier
    IfcPropertySetTemplate:HasPropertyTemplates -> IfcSimplePropertyTemplate
    IfcSimplePropertyTemplate:TemplateType -> IfcSimplePropertyTemplateTypeEnum
    IfcSimplePropertyTemplate:PrimaryMeasureType -> IfcLabel
    IfcSimplePropertyTemplate:SecondaryMeasureType -> IfcLabel
    IfcSimplePropertyTemplate:Enumerators -> IfcPropertyEnumeration
    IfcSimplePropertyTemplate:AccessState -> IfcStateEnum
    IfcSimplePropertyTemplate:PrimaryUnit -> IfcUnit
    IfcSimplePropertyTemplate:SecondaryUnit -> IfcUnit
    IfcSimplePropertyTemplate:Expression -> IfcLabel
    IfcPropertyEnumeration:Name -> IfcLabel
    IfcPropertyEnumeration:EnumerationValues -> IfcValue
}
```
