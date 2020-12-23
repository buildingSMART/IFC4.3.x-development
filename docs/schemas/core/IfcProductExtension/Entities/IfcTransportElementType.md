# IfcTransportElementType

The element type [<font color="#0000ff"><u>IfcTransportElementType</u></font>]($element://{827AB441-28FB-4320-A57A-76E6CC5BA21D})  defines commonly shared information for occurrences of transport elements. The set of shared information may include:  
* common properties within shared property sets
* common material information
* common shape representations

  
It is used to define a transport element specification (i.e. the specific product information that is common to all occurrences of that beam type). Transport element types (or the instantiable subtypes) may be exchanged without being already assigned to occurrences.  
The occurrences of the [<font color="#0000ff"><u>IfcTransportElementType</u></font>]($element://{827AB441-28FB-4320-A57A-76E6CC5BA21D})  are represented by instances of [<font color="#0000ff"><u>IfcTransportElement</u></font>]($element://{9CF73480-06BE-4997-B578-8F3958E77111})  (or its subtypes).  
> HISTORY New entity in IFC2x2.

## Attributes

### PredefinedType


## WhereRules

### CorrectPredefinedType
The inherited attribute _ElementType_ shall be provided, if the _PredefinedType_ is set to USERDEFINED.
