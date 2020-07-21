IfcTypeProduct
==============
_IfcTypeProduct_ defines a type definition of a product without being already
inserted into a project structure (without having a placement), and not being
included in the geometric representation context of the project.\S\ It is used
to define a product specification, that is, the specific product information
that is common to all occurrences of that product type.  
  
An _IfcTypeProduct_ may have a list of property set attached and an optional
set of product representations. Values of these properties and the
representation maps are common to all occurrences\S\ of that product type.\S\
The type-occurrence relationship is realized using the objectified
relationship _IfcRelDefinesByType_.  
  
> NOTE  The product representations are defined as representation maps, which
> may be assigned by a product instance through the representation item(s)
> being an _IfcShapeRepresentation_ and having _Items_ of type\S\
> _IfcMappedItem_.  
  
The representations at the occurrence level (represented by subtypes of
_IfcProduct_) can override the specific representations at the type level:  
  
* for geometric representations, a Cartesian transformation operator can be applied at the occurrence level.  
* for property sets, a property within an occurrence property set, assigned at the product occurrence, overrides the same property assigned to the product type.  
  
An _IfcTypeProduct_ may be exchanged without being already assigned to
subtypes of _IfcProduct_.  
  
> HISTORY  New entity in IFC2x.  
  
{ .change-ifc2x4}  
> IFC4 CHANGE  The entity _IfcTypeProduct_ shall not be instantiated from IFC4
> onwards. It will be changed into an ABSTRACT supertype in future releases of
> IFC.  
[ _bSI
Documentation_](https://standards.buildingsmart.org/IFC/DEV/IFC4_2/FINAL/HTML/schema/ifckernel/lexical/ifctypeproduct.htm)


Attribute definitions
---------------------
| Attribute   | Description                                                                                                                                            |
|-------------|--------------------------------------------------------------------------------------------------------------------------------------------------------|
| Tag         | The tag (or label) identifier at the particular type of a product, e.g. the article number (like the EAN). It is the identifier at the specific level. |

Formal Propositions
-------------------
| Rule                 | Description   |
|----------------------|---------------|
| ApplicableOccurrence |               |

Associations
------------
| Attribute          | Description   |
|--------------------|---------------|
| RepresentationMaps |               |
| ReferencedBy       |               |

