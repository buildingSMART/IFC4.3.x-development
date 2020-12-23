# IfcBeamType

The element type _IfcBeamType_ defines commonly shared information for occurrences of beams. The set of shared information may include:

* common properties within shared property sets
* common material information
* common profile definitions
* common shape representations

It is used to define a beam specification, or beam style (the specific product information that is common to all occurrences of that beam type). Beam types may be exchanged without being already assigned to occurrences.

Occurrences of the _IfcBeamType_ within building models are represented by instances of _IfcBeamStandardCase_ if the _IfcBeamType_ has a single associated _IfcMaterialProfileSet_; otherwise they are represented by instances of _IfcBeam_. Occurrences of the _IfcBeamType_ within structural analysis models are represented by instances of _IfcStructuralCurveMember_, or its applicable subtypes.

> HISTORY&nbsp; New entity in IFC2x2.

## Attributes

### PredefinedType
Identifies the predefined types of a beam element from which the type required may be set.

## Formal Propositions

### CorrectPredefinedType
The inherited attribute _ElementType_ shall be provided, if the _PredefinedType_ is set to USERDEFINED.
