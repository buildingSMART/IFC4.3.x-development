# IfcStructuralCurveActivityTypeEnum

This enumeration defines the distribution of load values in a curve action or reaction.<!-- end of definition -->

> HISTORY  New enumeration in IFC4

## Items

### CONST
The load has a constant value over its entire extent.

### LINEAR
The load value is linearly distributed over the load's extent.

### POLYGONAL
The load consists of several consecutive linear sections.

### EQUIDISTANT
The load consists of n consecutive sections of same length and is specified by n+1 load samples.  The interpolation type over the segments is not defined by this distribution type but may be qualified in _IfcObject.ObjectType_ based on additional agreements.

### SINUS
The load value is distributed as a sinus half wave.

### PARABOLA
The load value is distributed as a half wave described by a symmetric quadratic parabola.

### DISCRETE
The load is specified as a series of discrete load points.

### USERDEFINED
The load distribution is user-defined.

### NOTDEFINED
The load distribution is undefined.
