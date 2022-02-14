# IfcGeometricProjectionEnum

_IfcGeometricProjectionEnum_ defines the various representation types that can be semantically distinguished. Often different levels of detail of the shape representation are controlled by the representation type.

> HISTORY&nbsp; New enumeration in IFC2x2.

## Items

### GRAPH_VIEW
Geometric display representation that shows an abstract, often 1D element representation, e.g. representing a wall by its axis line.

### SKETCH_VIEW
Geometric display representation that shows an abstract, often 2D element representation, e.g. representing a wall by its two foot print edges, surpressing any inner layer representation.

### MODEL_VIEW
Geometric display representation that shows a full 3D element representation, e.g. representing a wall by its volumetric body.

### PLAN_VIEW
Geometric display representation that shows a full 2D element representation, the level of detail often depends on the target scale, e.g. representing a wall by its two foot print edges and the edges of all inner layers. The projection is shown in ground view as seen from above.

### REFLECTED_PLAN_VIEW
Geometric display representation that shows a full 2D element representation, the level of detail often depends on the target scale, e.g. representing a wall by its two foot print edges and the edges of all inner layers. The projection is shown in ground view as seen from below.

### SECTION_VIEW
Geometric display representation that shows a full 2D element representation, the level of detail often depends on the target scale, e.g. representing a wall by its two inner/outer edges and the edges of all inner layers, if the element is cut by the section line.

### ELEVATION_VIEW
Geometric display representation that shows a full 2D element representation, the level of detail often depends on the target scale, e.g. representing a wall by its bounding edges if the element is within an elevation view.

### USERDEFINED
A user defined specification is given by the value of the _UserDefinedTargetView_ attribute.

### NOTDEFINED
No specification given.
