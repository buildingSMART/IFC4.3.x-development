IfcRelAssignsToControl
======================
The objectified relationship _IfcRelAssignsToControl_ handles the assignment
of a control (represented by subtypes of _IfcControl_) to other objects
(represented by subtypes of _IfcObject_, with the exception of controls).  
  
> EXAMPLE  The assignment of a performance history (as subtype of
> _IfcControl_) for a building service element (as subtype of _IfcObject_) is
> an application of this generic relationship.  
  
> HISTORY  New entity in IFC2.0.  
  
{ .change-ifc2x}  
> IFC2x CHANGE Entity has been renamed from _IfcRelControls_.  
[ _bSI
Documentation_](https://standards.buildingsmart.org/IFC/DEV/IFC4_2/FINAL/HTML/schema/ifckernel/lexical/ifcrelassignstocontrol.htm)


Formal Propositions
-------------------
| Rule            | Description   |
|-----------------|---------------|
| NoSelfReference |               |

Associations
------------
| Attribute       | Description   |
|-----------------|---------------|
| RelatingControl |               |

