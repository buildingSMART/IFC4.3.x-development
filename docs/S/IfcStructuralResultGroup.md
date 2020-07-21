IfcStructuralResultGroup
========================
Instances of the entity _IfcStructuralResultGroup_ are used to group results
of structural analysis calculations and to capture the connection to the
underlying basic load group. The basic functionality for grouping inherited
from _IfcGroup_ is used to collect instances from _IfcStructuralReaction_ or
its respective subclasses.  
  
> HISTORY  New entity in IFC2x2.  
  
{ .change-ifc2x4}  
> IFC4 CHANGE  WHERE rule added.  
[ _bSI
Documentation_](https://standards.buildingsmart.org/IFC/DEV/IFC4_2/FINAL/HTML/schema/ifcstructuralanalysisdomain/lexical/ifcstructuralresultgroup.htm)


Attribute definitions
---------------------
| Attribute   | Description                                                                                                                        |
|-------------|------------------------------------------------------------------------------------------------------------------------------------|
| TheoryType  | Specifies the analysis theory used to obtain the respective results.                                                               |
| IsLinear    | This value allows to easily recognize whether a linear analysis has been applied (allowing the superposition of analysis results). |

Formal Propositions
-------------------
| Rule          | Description   |
|---------------|---------------|
| HasObjectType |               |

Associations
------------
| Attribute          | Description   |
|--------------------|---------------|
| ResultGroupFor     |               |
| ResultForLoadGroup |               |

