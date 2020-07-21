IfcSimplePropertyTemplate
=========================
The _IfcSimplePropertyTemplate_ defines the template for all dynamically
extensible properties, either the subtypes of _IfcSimpleProperty_, or the
subtypes of _IfcPhysicalSimpleQuantity_. The individual property templates are
interpreted according to their _Name_ attribute and may have a predefined
template type, property units, and property measure types. The correct
interpretation of the attributes:  
  
* _PrimaryUnit_  
* _SecondaryUnit_  
* _PrimaryMeasureType_  
* _SecondaryMeasureType_  
  
is determined by the _TemplateType_. The attributes Enumerators and Expression
only apply to instances of _IfcSimplePropertyTemplate_ having a particular
_TemplateType_. The _TemplateType_ also controls, which subtype of either
_IfcSimpleProperty_ or _IfcPhysicalSimpleQuantity_ shall be used for property
occurrences corresponding to this template.  
  
The _IfcSimplePropertyTemplate_ is part of the set of templates included in
the _IfcPropertySetTemplate_. The template can be accessed throught the
inverse attribute _PartOfPsetTemplate_ The _IfcPropertySetTemplate_ may define
one or several instances of _IfcPropertySet_ (or _IfcElementQuantity_). The
definition assignment is established by the objectified relationship
_IfcRelDefinesByTemplate_ as shown in Figure 1. There is no direct link
between an _IfcSimplePropertyTemplate_ and a subtype of either
_IfcSimpleProperty_ or _IfcPhysicalSimpleQuantity_. The definition
relationship between the template and the individual properties (or
quantities) is established by the _Name_ attributes.  
  
> NOTE  Constraints at _IfcPropertySetTemplate_ and _IfcPropertySet_ (and
> _IfcElementQuantity_) guarantee that the _Name_ attributes of included
> property templates and individual properties are unique.  
  
!["IfcSimplePropertyTemplate figure
1"](../figures/ifcsimplepropertytemplate_fig-1.png "Figure 1 -- Property
template relationships")  
  
> HISTORY  New entity in IFC4.  
[ _bSI
Documentation_](https://standards.buildingsmart.org/IFC/DEV/IFC4_2/FINAL/HTML/schema/ifckernel/lexical/ifcsimplepropertytemplate.htm)


Attribute definitions
---------------------
| Attribute            | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
|----------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| PrimaryMeasureType   | Primary measure type assigned to the definition of the property. It should be provided, if the _PropertyType_ is set to:\X\0D* P_SINGLEVALUE: determining the measure type of _IfcPropertySingleValue.NominalValue_\X\0D* P_ENUMERATEDVALUE: determining the measure type of _IfcPropertyEnumeratedValue.EnumerationValues_\X\0D* P_BOUNDEDVALUE: determining the measure type of _IfcPropertyBoundedValue.LowerBoundValue_\X\0D* P_LISTVALUE: determining the measure type of _IfcPropertyListValue.ListValues_\X\0D* P_TABLEVALUE: determining the measure type of _IfcPropertyTableValue.DefiningValues_\X\0D* P_REFERENCEVALUE: determining the measure type of _IfcPropertyTableValue.PropertyReference_\X\0D\X\0D> NOTE  The value range of the measure type is within the select type _IfcValue_ for all _PropertyType_''s with the exeption of P_REFERENCEVALUE. Here it is within the select type _IfcObjectReferenceSelect_.                                                                                                                                                                                                                                                                                                             |
| SecondaryMeasureType | Secondary measure type assigned to the definition of the property. It should be provided, if the _PropertyType_ is set to:\X\0D* P_BOUNDEDVALUE: determining the measure type of _IfcPropertyBoundedValue.UpperBoundValue_\X\0D* P_TABLEVALUE: determining the measure type of _IfcPropertyTableValue.DefinedValues_\X\0D\X\0D\X\0DThe value range of the measure type is within the select type _IfcValue_ for all _PropertyType_''s with the exeption of P_ENUMERATEDVALUE. Here it is the comma delimited list of enumerators.\X\0D> NOTE  The measure type of _IfcPropertyEnumeration.EnumerationValues_ is provided as _PrimaryDataType_.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| PrimaryUnit          | Primary unit assigned to the definition of the property. It should be provided, if the _PropertyType_ is set to:\X\0D* P_SINGLEVALUE: determining the _IfcPropertySingleValue.Unit_\X\0D* P_ENUMERATEDVALUE: determining the _IfcPropertyEnumeration.Unit_\X\0D* P_BOUNDEDVALUE: determining the _IfcPropertyBoundedValue.Unit_\X\0D* P_LISTVALUE: determining the _IfcPropertyListValue.Unit_\X\0D* P_TABLEVALUE: determining the _IfcPropertyTableValue.DefiningUnit_                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| SecondaryUnit        | Secondary unit assigned to the definition of the property. It should be provided, if the _PropertyType_ is set to:\X\0D* P_TABLEVALUE: determining the _IfcPropertyTableValue.DefinedUnit_                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| Expression           | The expression used to store additional information for the property template depending on the _PropertyType_. It should the following definitions, if the _PropertyType_ is set to:\X\0D* P_TABLEVALUE: the expression that could be evaluated to define the correlation between the defining values and the defined values.\X\0D* Q_LENGTH, Q_AREA, Q_VOLUME, Q_COUNT, Q_WEIGTH, Q_TIME: the formula to be used to calculate the quantity\X\0D\X\0D> NOTE  No value shall be asserted if the _PropertyType_ is not listed above.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| AccessState          | Information about the access state of the property. It determines whether a property be viewed and/or modified by any receiving application without specific knowledge of it. \X\0D \X\0D**Attribute use definition for _IfcStateEnum_*** READWRITE: Properties of this template are readable and writable. They may be viewed and modified by users of any application. These are typical informational properties set by a user.\X\0D* READONLY: Properties of this template are read-only. They may be viewed but not modified by users of any application. (Applications may generate such values). These are typical automatically generated properties that should be displayed only, but not written back.\X\0D* LOCKED: Properties of this template are locked. They may only be accessed by the owning application (the publisher of the property set template). These are typically application depended, internal properties that should not be published.\X\0D* READWRITELOCKED: Properties of this template are locked, readable, and writable. They may only be accessed by the owning application.\X\0D* READONLYLOCKED: Properties of this template are locked and read-only. They may only be accessed by the owning application. |

Associations
------------
| Attribute    | Description   |
|--------------|---------------|
| Enumerators  |               |
| TemplateType |               |

