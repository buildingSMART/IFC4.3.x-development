IfcLogicalOperatorEnum
======================
_IfcLogicalOperatorEnum_ is an enumeration that defines the logical operators
that may be applied for the satisfaction of one or more operands
(_IfcConstraint_) at a time.  
  
Table 1 illustrates application of _IfcLogicalOperatorEnum_ in a case of three
operands, A, B and C, for each operator.  
  
  
  
  
| LOGICALAND(A,B,C)  
  
|  **A**  
|  F  
| F  
| F  
| T  
| F  
| T  
| T  
| T  
  
---|---|---|---|---|---|---|---|---  
  
  
 **B**  
|  F  
| F  
| T  
| F  
| T  
| F  
| T  
| T  
  
  
 **C**  
|  F  
| T  
| F  
| F  
| T  
| T  
| F  
| T  
  
  
  
 **RESULT**  
|  F  
| F  
| F  
| F  
| F  
| F  
| F  
| T  
  
  
LOGICALOR(A,B,C)  
  
|  **A**  
|  F  
| F  
| F  
| T  
| F  
| T  
| T  
| T  
  
  
  
 **B**  
|  F  
| F  
| T  
| F  
| T  
| F  
| T  
| T  
  
  
 **C**  
|  F  
| T  
| F  
| F  
| T  
| T  
| F  
| T  
  
  
  
 **RESULT**  
|  F  
| T  
| T  
| T  
| T  
| T  
| T  
| T  
  
  
LOGICALXOR(A,B,C)  
  
|  **A**  
|  F  
| F  
| F  
| T  
| F  
| T  
| T  
| T  
  
  
  
 **B**  
|  F  
| F  
| T  
| F  
| T  
| F  
| T  
| T  
  
  
 **C**  
|  F  
| T  
| F  
| F  
| T  
| T  
| F  
| T  
  
  
  
 **RESULT**  
|  F  
| T  
| T  
| T  
| F  
| F  
| F  
| F  
  
  
LOGICALNOTAND(A,B,C)  
  
|  **A**  
|  F  
| F  
| F  
| T  
| F  
| T  
| T  
| T  
  
  
  
 **B**  
|  F  
| F  
| T  
| F  
| T  
| F  
| T  
| T  
  
  
 **C**  
|  F  
| T  
| F  
| F  
| T  
| T  
| F  
| T  
  
  
  
 **RESULT**  
|  T  
| T  
| T  
| T  
| T  
| T  
| T  
| F  
  
  
LOGICALNOTOR(A,B,C)  
  
|  **A**  
|  F  
| F  
| F  
| T  
| F  
| T  
| T  
| T  
  
  
  
 **B**  
|  F  
| F  
| T  
| F  
| T  
| F  
| T  
| T  
  
  
 **C**  
|  F  
| T  
| F  
| F  
| T  
| T  
| F  
| T  
  
  
  
 **RESULT**  
|  T  
| F  
| F  
| F  
| F  
| F  
| F  
| F  
  
  
  
  
  
  

Table 1 -- Logical operators  
  
  
  
  
> HISTORY  New enumeration in IFC2.0.  
  
{ .change-ifc2x4}  
> IFC4 CHANGE  Extended to include LOGICALXOR, LOGICALNOTAND and LOGICALNOTOR.  
[ _bSI
Documentation_](https://standards.buildingsmart.org/IFC/DEV/IFC4_2/FINAL/HTML/schema/ifcconstraintresource/lexical/ifclogicaloperatorenum.htm)


