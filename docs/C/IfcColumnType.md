IfcColumnType
=============
The element type _IfcColumnType_ defines commonly shared information for
occurrences of columns. The set of shared information may include:  
  
* common properties within shared property sets  
* common material information  
* common profile definitions  
* common shape representations  
  
It is used to define a column specification, or column style (i.e. the
specific product information that is common to all occurrences of that column
type). Column types may be exchanged without being already assigned to
occurrences.  
  
Occurrences of the _IfcColumnType_ within building models are represented by
instances of _IfcColumnStandardCase_ if the _IfcColumnType_ has a single
associated _IfcMaterialProfileSet_; otherwise they are represented by
instances of _IfcColumn_. Occurrences of the _IfcColumnType_ within structural
analysis models are represented by instances of _IfcStructuralCurveMember_, or
its applicable subtypes.  
  
> HISTORY  New entity in IFC2x2.  
[ _bSI
Documentation_](https://standards.buildingsmart.org/IFC/DEV/IFC4_2/FINAL/HTML/schema/ifcsharedbldgelements/lexical/ifccolumntype.htm)


