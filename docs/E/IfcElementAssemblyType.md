IfcElementAssemblyType
======================
The
[_IfcElementAssemblyType_]($element://{B6122156-9E6E-44c9-9D83-B9817B3F8EDD})
defines a list of commonly shared property set definitions of an element and
an optional set of product representations. It is used to define an element
specification (i.e. the specific product information, that is common to all
occurrences of that product type).  
> NOTE The product representations are defined as representation maps (at the
> level of the supertype
> [_IfcTypeProduct_]($element://{BA61CFBF-8CD7-44c2-AD99-072068F55C99}) ,
> which gets assigned by an element occurrence instance through the
> IfcShapeRepresentation.Item[1] being an
> [_IfcMappedItem_]($element://{F1BD66A5-8531-41ca-BD3B-E02D0F1BE3C1}).  
An element assembly type is used to define the common properties of a certain
type of an element assembly that may be applied to many instances of that type
to assign a specific style. An element assembly types (or the instantiable
subtypes) may be exchanged without being already assigned to occurrences.  
The occurrences of the
[_IfcElementAssemblyType_]($element://{B6122156-9E6E-44c9-9D83-B9817B3F8EDD})
are represented by instances of
[_IfcElementAssembly_]($element://{37A21453-AB05-44b6-8887-DD9BF7647B60}).  
> HISTORY\S\ New entity in IFC4.  
[ _bSI
Documentation_](https://standards.buildingsmart.org/IFC/DEV/IFC4_2/FINAL/HTML/schema/ifcproductextension/lexical/ifcelementassemblytype.htm)


Attribute definitions
---------------------
| Attribute      | Description   |
|----------------|---------------|
| PredefinedType |               |

