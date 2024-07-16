# Pset_ControllerTypeMultiPosition

Properties for discrete inputs, outputs, and values within a programmable logic controller.
<!-- end of short definition -->

 HISTORY: New in IFC4, replaces Pset_MultiStateInput and Pset_MultiStateOutput.


## Comments

### ControlType

INPUT: Controller element is a dedicated input.
OUTPUT: Controller element is a dedicated output.
VARIABLE: Controller element is an in-memory variable.

### Value

The expected range and default value. The LowerLimitValue and UpperLimitValue must fall within the physical Range.

### Labels

Each entry corresponds to an integer within the ValueRange.