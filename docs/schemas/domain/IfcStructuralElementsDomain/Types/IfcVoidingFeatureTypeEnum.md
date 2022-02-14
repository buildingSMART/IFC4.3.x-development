# IfcVoidingFeatureTypeEnum

This enumeration qualifies a voiding feature regarding its shape and configuration relative to the voided element.

> HISTORY&nbsp; New type in IFC4.

## Items

### CUTOUT
An internal cutout (creating an opening) or external cutout (creating a recess) of arbitrary shape.  The edges between cutting planes may be overcut or undercut, i.e. rounded.

### NOTCH
An external cutout of with a mostly rectangular cutting profile.  The edges between cutting planes may be overcut or undercut, i.e. rounded.

### HOLE
A circular or slotted or threaded hole, typically but not necessarily of smaller dimension than what would be considered a cutout.

### MITER
A skewed plane end cut, removing material across the entire profile of the voided element.

### CHAMFER
A skewed plane end cut, removing material only across a part of the profile of the voided element.

### EDGE
A shape modification along an edge of the element with the edge length as the predominant dimension of the feature, and feature profile dimensions which are typically much smaller than the edge length.  Can for example be a chamfer edge (differentiated from a chamfer by its ratio of dimensions and thus usually manufactured differently), rounded edge (a convex edge feature), or fillet edge (a concave edge feature).

### USERDEFINED
A user-defined type of voiding feature.

### NOTDEFINED
An undefined type of voiding feature.
