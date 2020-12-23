# IfcElementAssembly

The [<font color="#0000ff"><u>IfcElementAssembly</u></font>]($element://{37A21453-AB05-44b6-8887-DD9BF7647B60}) represents complex element assemblies aggregated from several elements, such as discrete elements, building elements, or other elements.  
> EXAMPLE Steel construction assemblies, such as trusses and different kinds of frames, can be represented by the [<font color="#0000ff"><u>IfcElementAssembly</u></font>]($element://{37A21453-AB05-44b6-8887-DD9BF7647B60}) entity. Other examples include slab fields aggregated from a number of precast concrete slabs or reinforcement units made from several reinforcement bars. Also bathroom units, staircase sections and other premanufactured or precast elements are examples of the general [<font color="#0000ff"><u>IfcElementAssembly</u></font>]($element://{37A21453-AB05-44b6-8887-DD9BF7647B60}) entity  
> NOTE The [<font color="#0000ff"><u>IfcElementAssembly</u></font>]($element://{37A21453-AB05-44b6-8887-DD9BF7647B60}) is a general purpose entity that is required to be decomposed. Also other subtypes of IfcElement can be decomposed.  <font color="#ff0000">REMOVE {</font>with some dedicated entities such as _IfcWallElementedCase_ and _IfcSlabElementedCase_.<font color="#ff0000">}</font>  
The assembly structure can be nested, i.e. an [<font color="#0000ff"><u>IfcElementAssembly</u></font>]($element://{37A21453-AB05-44b6-8887-DD9BF7647B60}) could be an aggregated part within another [<font color="#0000ff"><u>IfcElementAssembly</u></font>]($element://{37A21453-AB05-44b6-8887-DD9BF7647B60}).  
> NOTE View definitions and/or implementer agreements may restrict the number of allowed levels of nesting.  
The geometry of an [<font color="#0000ff"><u>IfcElementAssembly</u></font>]($element://{37A21453-AB05-44b6-8887-DD9BF7647B60}) is generally formed from its components, in which case it does not need to have an explicit geometric representation. In some cases it may be useful to also expose an own explicit representation of the aggregate.  
> NOTE View definitions or implementer agreements may further constrain the applicability of certain shape representations at the [<font color="#0000ff"><u>IfcElementAssembly</u></font>]($element://{37A21453-AB05-44b6-8887-DD9BF7647B60}) in respect of the shape representations of its parts.  
> HISTORY New entity in IFC2x2.  
  
**Informal Propositions:**  
1. The [<font color="#0000ff"><u>IfcElementAssembly</u></font>]($element://{37A21453-AB05-44b6-8887-DD9BF7647B60}) shall have an aggregation relationship to the contained parts, i.e. the (INV) IsDecomposedBy relationship shall be utilized.

## Attributes

### AssemblyPlace
A designation of where the assembly is intended to take place defined by an Enum.

### PredefinedType


## WhereRules

### CorrectPredefinedType
Either the _PredefinedType_ attribute is unset (e.g. because an _IfcElementAssemblyType_ is associated), or the inherited attribute _ObjectType_ shall be provided, if the _PredefinedType_ is set to USERDEFINED.

### CorrectTypeAssigned
Either there is no element assembly type object associated, i.e. the _IsTypedBy_ inverse relationship is not provided, or the associated type object has to be of type _IfcElementAssemblyType_.
