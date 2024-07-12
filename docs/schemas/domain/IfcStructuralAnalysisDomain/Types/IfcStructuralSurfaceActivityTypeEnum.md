# IfcStructuralSurfaceActivityTypeEnum

This enumeration defines the distribution of load values in a surface action or reaction.
<!-- end of short definition -->


> HISTORY New enumeration in IFC4

## Items

### CONST
The load has a constant value over its entire extent.

### BILINEAR
The load value is bilinearly distributed over the load's extent.

### DISCRETE
The load is specified as a series of discrete load points.

### ISOCONTOUR
The load is specified by a series of iso-curves (level sets), i.e. curves at which the load value is constant. These curves run perpendicularly to the load gradient.

### USERDEFINED
The load distribution is user-defined.

### NOTDEFINED
The load distribution is undefined.
