# IfcGeographicElement

An _IfcGeographicElement_ is a generalization of all elements within a geographical landscape. It includes occurrences of typical geographical elements, often referred to as features, such as trees or terrain. Common type information behind several occurrences of _IfcGeographicElement_ is provided by the _IfcGeographicElementType_. 

> HISTORY New entity in IFC4.

## Attributes

### PredefinedType


## Formal Propositions

### CorrectPredefinedType
Either the _IfcGeographicElement_ attribute is unset (e.g. because an _IfcGeographicElementType_ is associated), or the inherited attribute _ObjectType_ shall be provided, if the _PredefinedType_ is set to USERDEFINED.

### CorrectTypeAssigned
Either there is no geographic element type object associated, i.e. the _IsTypedBy_ inverse relationship is not provided, or the associated type object has to be of type _IfcGeographicElementType_.
