The element type _IfcTrackElementType_ defines commonly shared information for occurrences of track elements. The set of shared information may include:
* common properties within shared property sets
* common material information
* common profile definitions
* common shape representations



<!-- end of short definition -->

It is used to define a track element specification (the specific product information that is common to all occurrences of that track element type). Track element types may be exchanged without being already assigned to occurrences.
Occurrences of the _IfcTrackElementType_ are represented by instances of _IfcTrackElement_.

## Attributes

### PredefinedType


## Formal Propositions

### CorrectPredefinedType
The inherited attribute _ElementType_ shall be provided, if the _PredefinedType_ is set to USERDEFINED.
