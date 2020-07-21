IfcConstructionMaterialResource
===============================
_IfcConstructionMaterialResource_ identifies a material resource type in a
construction project.  
  
> HISTORY  New entity in IFC2.0.  
  
{ .change-ifc2x4}  
> IFC4 CHANGE  The attribute _Suppliers_ has been deleted; use
> _IfcRelAssignsToResource_ to assign an _IfcActor_ to fulfill the role as a
> supplier. The attribute _UsageRatio_ has been deleted; use
> _BaseQuantityConsumed_ and _BaseQuantityProduced_ to indicate material
> usage.  
  
Occurrences of _IfcConstructionMaterialResource_ are consumed (wholly or
partially), or occupied during a construction work task (_IfcTask_).  
  
Similar to _IfcConstructionProductResource_, sometimes things such as 5000kg
of gravel are already instantiated as an instance of an _IfcProduct_ subtype
because it is a result of a work task (for example, transporting gravel). In
this case, the instance of _IfcConstructionMaterialResource_ can be associated
with the product instance 5000kg of gravel to provide more information for
resource uses. Nevertheless, _IfcConstructionMaterialResource_ should only be
used to represent resource usage, but not product substances.  
  
> NOTE  This entity is not the same as _IfcMaterial_. One one hand,
> _IfcConstructionMaterialResource_ represents usage of bulk materials such as
> sand, gravels, nails and so on. Physical manifestations can be instantiated
> from _IfcProduct_ as well, depending on their uses in the system, and such
> an _IfcProduct_ object can be assigned to the
> _IfcConstructionMaterialResource_ object via _IfcRelAssignsToResource_. On
> the other hand, _IfcMaterial_ is about physical materials that a physical
> building element consists of, possibly with detailed material layering
> information."  
[ _bSI
Documentation_](https://standards.buildingsmart.org/IFC/DEV/IFC4_2/FINAL/HTML/schema/ifcconstructionmgmtdomain/lexical/ifcconstructionmaterialresource.htm)


Formal Propositions
-------------------
| Rule                  | Description   |
|-----------------------|---------------|
| CorrectPredefinedType |               |

Associations
------------
| Attribute      | Description   |
|----------------|---------------|
| PredefinedType |               |

