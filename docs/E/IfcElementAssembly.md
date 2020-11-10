IfcElementAssembly
==================
The [_IfcElementAssembly_]($element://{37A21453-AB05-44b6-8887-DD9BF7647B60})
represents complex element assemblies aggregated from several elements, such
as discrete elements, building elements, or other elements.  
> EXAMPLE Steel construction assemblies, such as trusses and different kinds
> of frames, can be represented by the
> [_IfcElementAssembly_]($element://{37A21453-AB05-44b6-8887-DD9BF7647B60})
> entity. Other examples include slab fields aggregated from a number of
> precast concrete slabs or reinforcement units made from several
> reinforcement bars. Also bathroom units, staircase sections and other
> premanufactured or precast elements are examples of the general
> [_IfcElementAssembly_]($element://{37A21453-AB05-44b6-8887-DD9BF7647B60})
> entity  
> NOTE The
> [_IfcElementAssembly_]($element://{37A21453-AB05-44b6-8887-DD9BF7647B60}) is
> a general purpose entity that is required to be decomposed. Also other
> subtypes of IfcElement can be decomposed. REMOVE {with some dedicated
> entities such as _IfcWallElementedCase_ and _IfcSlabElementedCase_.}  
The assembly structure can be nested, i.e. an
[_IfcElementAssembly_]($element://{37A21453-AB05-44b6-8887-DD9BF7647B60})
could be an aggregated part within another
[_IfcElementAssembly_]($element://{37A21453-AB05-44b6-8887-DD9BF7647B60}).  
> NOTE View definitions and/or implementer agreements may restrict the number
> of allowed levels of nesting.  
The geometry of an
[_IfcElementAssembly_]($element://{37A21453-AB05-44b6-8887-DD9BF7647B60}) is
generally formed from its components, in which case it does not need to have
an explicit geometric representation. In some cases it may be useful to also
expose an own explicit representation of the aggregate.  
> NOTE View definitions or implementer agreements may further constrain the
> applicability of certain shape representations at the
> [_IfcElementAssembly_]($element://{37A21453-AB05-44b6-8887-DD9BF7647B60}) in
> respect of the shape representations of its parts.  
> HISTORY New entity in IFC2x2.  
  
 **Informal Propositions:**  

  

  1. The [_IfcElementAssembly_]($element://{37A21453-AB05-44b6-8887-DD9BF7647B60}) shall have an aggregation relationship to the contained parts, i.e. the (INV) IsDecomposedBy relationship shall be utilized.
  

  
[ _bSI
Documentation_](https://standards.buildingsmart.org/IFC/DEV/IFC4_2/FINAL/HTML/schema/ifcproductextension/lexical/ifcelementassembly.htm)


Attribute definitions
---------------------
| Attribute      | Description                                                                       |
|----------------|-----------------------------------------------------------------------------------|
| AssemblyPlace  | A designation of where the assembly is intended to take place defined by an Enum. |
| PredefinedType |                                                                                   |

