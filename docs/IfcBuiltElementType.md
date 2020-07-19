IfcBuiltElementType
===================
The _IfcBuiltElementType_ provides the type information for _IfcBuiltElement_
occurrences.  
> NOTE The product representations are defined as representation maps (at the
> level of the supertype
> [_IfcTypeProduct_]($element://{BA61CFBF-8CD7-44c2-AD99-072068F55C99}) ,
> which gets assigned by an element occurrence instance through the
> _IfcShapeRepresentation.Item[1]_ being an _IfcMappedItem_.  
A built element type is used to define the common properties of a certain type
of built element that are applied to all occurrences of that type. It is used
to define a built element specification (i.e. the specific product
information, that is common to all occurrences of that product type). Built
element types (or the instantiable subtypes) may be exchanged without being
already assigned to occurrences.  
REMOVE{ The _IfcBuildingElementType_ is an abstract type that cannot be
instantiated. For arbitrary building element types, that cannot be expressed
by a subtype of _IfcBuildingElementType_, use _IfcBuildingElementProxyType_.}  
The IfcBuiltElementType can be instantiated in the case when arbitrary built
element types cannot be expressed by a subtype of IfcBuiltElementType .  
Occurrences of subtypes of the _IfcBuildingElementType_ are represented by
instances of the appropriate subtypes of _IfcBuildingElement_.  
> HISTORY New entity in IFC2x2.  
[ _bSI
Documentation_](https://standards.buildingsmart.org/IFC/DEV/IFC4_2/FINAL/HTML/schema/ifcproductextension/lexical/ifcbuildingelementtype.htm)


