# IfcBuiltElementType

The _Ifc<font color="#ff0000">Built</font>ElementType_ provides the type information for _Ifc<font color="#ff0000">Built</font>Element_ occurrences.  
> NOTE The product representations are defined as representation maps (at the level of the supertype [<font color="#0000ff"><u>IfcTypeProduct</u></font>]($element://{BA61CFBF-8CD7-44c2-AD99-072068F55C99}) , which gets assigned by an element occurrence instance through the _IfcShapeRepresentation.Item[1]_ being an _IfcMappedItem_.  
A <font color="#ff0000">built</font> element type is used to define the common properties of a certain type of <font color="#ff0000">built</font> element that are applied to all occurrences of that type. It is used to define a <font color="#ff0000">built</font> element specification (i.e. the specific product information, that is common to all occurrences of that product type). <font color="#ff0000">Built</font> element types (or the instantiable subtypes) may be exchanged without being already assigned to occurrences.  
<font color="#ff0000">REMOVE{ </font>The _IfcBuildingElementType_ is an abstract type that cannot be instantiated. For arbitrary building element types, that cannot be expressed by a subtype of _IfcBuildingElementType_, use _IfcBuildingElementProxyType_.<font color="#ff0000">}</font>  
<font color="#ff0000">The IfcBuiltElementType can be instantiated in the case when arbitrary built element types cannot be expressed by a subtype of IfcBuiltElementType .</font>  
Occurrences of subtypes of the _IfcBuildingElementType_ are represented by instances of the appropriate subtypes of _IfcBuildingElement_.  
> HISTORY New entity in IFC2x2.
