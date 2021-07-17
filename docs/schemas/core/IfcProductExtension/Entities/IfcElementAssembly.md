# IfcElementAssembly

The _IfcElementAssembly_ represents complex element assemblies aggregated from several elements, such as discrete elements, building elements, or other elements.  

> EXAMPLE Steel construction assemblies, such as trusses and different kinds of frames, can be represented by the _IfcElementAssembly_ entity. Other examples include slab fields aggregated from a number of precast concrete slabs or reinforcement units made from several reinforcement bars. Also bathroom units, staircase sections and other premanufactured or precast elements are examples of the general _IfcElementAssembly_ entity 

> NOTE&nbsp; The _IfcElementAssembly_ is a general purpose entity that is required to be decomposed. Also other subtypes of _IfcElement_ can be decomposed.    
The assembly structure can be nested, i.e. an _IfcElementAssembly_ could be an aggregated part within another _IfcElementAssembly_.  

> NOTE&nbsp; View definitions and/or implementer agreements may restrict the number of allowed levels of nesting.  

The geometry of an _IfcElementAssembly_ is generally formed from its components, in which case it does not need to have an explicit geometric representation. In some cases it may be useful to also expose an own explicit representation of the aggregate.  

> NOTE&nbsp; View definitions or implementer agreements may further constrain the applicability of certain shape representations at the _IfcElementAssembly_ in respect of the shape representations of its parts.  

> HISTORY&nbsp; New entity in IFC2x2.  

{ .spec-head}
Informal Propositions:

1. The _IfcElementAssembly_ shall have an aggregation relationship to the contained parts, i.e. the (INV) _IsDecomposedBy_ relationship shall be utilized.

## Attributes

### AssemblyPlace
A designation of where the assembly is intended to take place defined by an Enum.

### PredefinedType


## Formal Propositions

### CorrectPredefinedType
Either the _PredefinedType_ attribute is unset (e.g. because an _IfcElementAssemblyType_ is associated), or the inherited attribute _ObjectType_ shall be provided, if the _PredefinedType_ is set to USERDEFINED.

### CorrectTypeAssigned
Either there is no element assembly type object associated, i.e. the _IsTypedBy_ inverse relationship is not provided, or the associated type object has to be of type _IfcElementAssemblyType_.
