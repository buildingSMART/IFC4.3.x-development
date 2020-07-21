IfcCostItem
===========
An _IfcCostItem_ describes a cost or financial value together with descriptive
information that describes its context in a form that enables it to be used
within a cost schedule. An _IfcCostItem_ can be used to represent the cost of
goods and services, the execution of works by a process, lifecycle cost and
more.  
  
Each instance of _IfcCostItem_ may have a name and a description. Depending on
the use for which the cost is intended, these values should be asserted on the
basis of agreement. For instance, the _Name_ attribute could be used to
provide a common value that enables distinct instances to be brought together
in a nesting arrangement (see below) while the Description attribute may be
used to provide text used for item description in a costing schedule.  
  
An _IfcCostItem_ can link one or many _IfcCostValue_''s representing a unit
cost, total cost, or a unit cost with one or many quantities used to generate
the total cost. The quantities can be given as individual quantities, or those
quantities are provided as element quantities by one or many building
elements. The _IfcCostValue.CostType_ attribute indicates the category of
cost, which may be used to present the value in a particular column. For
nested cost items (having _IfcRelNests_ relationship), _IfcCostValue.CostType_
is significant such that _IfcCostValue.AppliedValue_ is calculated as the sum
of all nested costs having the same _IfcCostValue.CostType_ or if set to an
asterisk (''\\\\*''), then the sum of all nested costs of all cost types. An
_IfcCostValue_ may represent an original value or a value derived from
formulas using _IfcAppliedValueRelationship_. For example, taxes may be
calculated as a percentage of a subtotal.  
  
> HISTORY  New entity in IFC2.0.  
  
{ .change-ifc2x4}  
> IFC4 CHANGE  Attribute _PredefinedType_, _CostValues_, and _CostQuantities_
> added.  
[ _bSI
Documentation_](https://standards.buildingsmart.org/IFC/DEV/IFC4_2/FINAL/HTML/schema/ifcsharedmgmtelements/lexical/ifccostitem.htm)


Associations
------------
| Attribute      | Description   |
|----------------|---------------|
| CostValues     |               |
| CostQuantities |               |
| PredefinedType |               |

