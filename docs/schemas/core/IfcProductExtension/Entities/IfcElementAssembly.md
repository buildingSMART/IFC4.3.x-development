# IfcElementAssembly

The _IfcElementAssembly_ represents complex element assemblies aggregated from several elements, such as discrete elements, building elements, or other elements.  

> EXAMPLE Steel construction assemblies, such as trusses and different kinds of frames, can be represented by the _IfcElementAssembly_ entity. Premanufactured or precast elements are examples of the general _IfcElementAssembly_ entity 

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

## Concepts

### Aggregation

The IfcElementAssembly shall represent an aggregate,
i.e. it should have other elements, being subtypes of
IfcElement, 
as contained (sub)parts. The table above only represents a selection of subtypes of IfcElement that are legitimate as parts in an 
IfcElementAssembly


* The IfcElementAssembly is an aggregate i.e. being
composed by other elements and acting as an assembly using the
objectified relationship IfcRelAggregates, refering to it
by its inverse attribute
SELF\IfcObjectDefinition.IsDecomposedBy. Components of an
assembly are described by instances of subtypes of
IfcElement.
* In this case, the contained subtypes of IfcElement
shall not be additionally contained in the project spatial
hierarchy, i.e. the inverse attribute
SELF\IfcElement.ContainedInStructure of those
IfcElement's shall be NIL.


Figure 151 illustrates spatial containment and element aggregation relationships.


![containment relationships](../../../../figuresifcelementassembly-containment.png)
Figure 151 — Element assembly containment



### Object Typing


### Spatial Containment

The IfcElementAssembly should have a relationship for its 
containment in the hierachical spatial structure of the project. Only if the IfcElementAssembly is itself a part of another assembly this relationship should be omitted.



