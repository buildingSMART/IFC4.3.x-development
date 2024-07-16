# IfcReinforcingBarType

The reinforcing element type **IfcReinforcingBarType** defines commonly shared information for occurrences of reinforcing bars. The set of shared information may include:

* common properties with shared property sets
* common representations
* common materials
* common composition of elements
<!-- end of short definition -->

It is used to define a reinforcing bar type specification indicating the specific product information that is common to all occurrences of that product type. The **IfcReinforcingBarType** may be declared within _IfcProject_ or _IfcProjectLibrary_ using _IfcRelDeclares_ and may be exchanged with or without occurrences of the type. Occurrences of **IfcReinforcingBarType** are represented by instances of _IfcReinforcingBar_.

> HISTORY New entity in IFC4.

## Attributes

### PredefinedType
Subtype of reinforcing bar.

### NominalDiameter
The nominal diameter defining the cross-section size of the reinforcing bar.

### CrossSectionArea
The effective cross-section area of the reinforcing bar.

### BarLength
The total length of the reinforcing bar. The total length of bended bars are calculated according to local standards with corrections for the bends.

### BarSurface
Indicator for whether the bar surface is plain or textured.

### BendingShapeCode
Shape code per a standard like ACI 315, ISO 3766, or a similar standard. It is presumed that a single standard for defining the bar bending is used throughout the project and that this standard is referenced from the _IfcProject_ object through the _IfcDocumentReference_ mechanism.

### BendingParameters
Bending shape parameters. Their meaning is defined by the bending shape code and the respective standard.

## Formal Propositions

### CorrectPredefinedType
The inherited attribute _ElementType_ shall be provided if the _PredefinedType_ is set to USERDEFINED.

### BendingShapeCodeProvided
Bending parameters must be accompanied by a shape code.

## Concepts

### Reinforcing Bar Type Attributes



