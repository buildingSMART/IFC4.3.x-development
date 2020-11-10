IfcRelNests
===========
The nesting relationship _IfcRelNests_ is a special type of the general
composition/decomposition (or whole/part) relationship _IfcRelDecomposes_. The
nesting relationship can be applied to all non physical subtypes of object and
object types, namely processes, controls (like cost items), and resources. It
can also be applied to physical subtypes of object and object types, namely
elements having ports. The nesting implies an order among the nested parts.  
  
> EXAMPLE  A nesting of costs items in an _IfcCostSchedule_ is the composition
> of complex cost items from other cost items. The order of the nested cost
> items underneath the parent cost item is determined by the order of the list
> of _RelatedObjects_.  
  
> EXAMPLE  A nesting of _IfcTask_''s within a work schedule is the composition
> of a parent work task from more specific sub work tasks. The order of the
> sub tasks underneath the parent task is determined by the order of the list
> of _RelatedObjects_.  
  
> EXAMPLE  A series of _IfcDistributionPort_''s can be nested within an
> _IfcDistributionElement_. They decompose the distribution element and have
> an implied order.  
  
Decompositions imply a dependency, i.e. the definition of the whole depends on
the definition of the parts and the parts depend on the existence of the
whole. The behaviour that is implied from the dependency has to be established
inside the applications.  
  
> HISTORY  New entity in IFC2.0  
  
{ .change-ifc2x4}  
> IFC4 CHANGE  The attributes _RelatingObject_ and _RelatedObjects_ are
> demoted from the supertype _IfcRelDecomposes_, and _RelatedObjects_ is
> refined to be a list. The use of _IfcRelNests_ is repurposed to be a nesting
> of an ordered collections of parts.  
[ _bSI
Documentation_](https://standards.buildingsmart.org/IFC/DEV/IFC4_2/FINAL/HTML/schema/ifckernel/lexical/ifcrelnests.htm)


Attribute definitions
---------------------
| Attribute      | Description   |
|----------------|---------------|
| RelatingObject |               |
| RelatedObjects |               |

