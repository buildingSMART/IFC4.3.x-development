The _IfcConveyorSegmentType_ provides the type information for _IfcConveyorSegment_ occurrences.

<!-- end of short definition -->

A conveyor segment defines an occurrence of a flow segment/ continuous run within a conveyor system that joins two sections of the system. these can utilise different carrying methods such as belt, rope, chain, screw etc.

## Attributes

### PredefinedType
Identifies the predefined type of a conveyor segment.

## Formal Propositions

### CorrectPredefinedType
The inherited attribute _ElementType_ shall be provided, if the _PredefinedType_ is set to USERDEFINED.
