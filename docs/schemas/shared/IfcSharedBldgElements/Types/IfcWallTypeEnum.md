# IfcWallTypeEnum

This enumeration defines the different types of walls that can further specify an _IfcWall_ or _IfcWallType_.

> HISTORY&nbsp; New enumeration in IFC2x2.

{ .change-ifc2x2}
> IFC2x2 CHANGE&nbsp; The enumerator _POLYGON_ has been changed to _POLYGONAL_.

{ .change-ifc2x3}
> IFC2x3 CHANGE&nbsp; The enumerators _ELEMENTEDWALL_ and _PLUMBINGWALL_ have been added.

{ .change-ifc2x4}
> IFC4 CHANGE&nbsp; New enumerators MOVABLE, PARAPET, PARTITIONING, and SOLIDWALL have been added.  
> IFC4 DEPRECATION&nbsp; The enumerators STANDARD, POLYGONAL and ELEMENTEDWALL are deprecated and shall no longer be used.

> NOTE&nbsp; The potentially misleading term _SHEAR_ shall not impose a particular resistance against shear forces, but a particular shape.

## Items

### MOVABLE
A movable wall that is either movable, such as folding wall or a sliding wall, or can be easily removed as a removable partitioning or mounting wall. Movable walls do normally not define space boundaries and often belong to the furnishing system.

### PARAPET
A wall-like barrier to protect human or vehicle from falling, or to prevent the spread of fires. Often designed at the edge of balconies, terraces or roofs, or along edges of bridges.

### PARTITIONING
A wall designed to partition spaces that often has a light-weight, sandwich-like construction (e.g. using gypsum board). Partitioning walls are normally non load bearing.

### PLUMBINGWALL
A pier, or enclosure, or encasement, normally used to enclose plumbing in sanitary rooms. Such walls often do not extent to the ceiling.

### SHEAR
A wall designed to withstand shear loads. Examples of shear wall are diaphragms inside a box girder, typically on a pier, to resist lateral forces and transfer them to the support.

### SOLIDWALL
A massive wall construction for the wall core being the single layer or having multiple layers attached. Such walls are often masonry or concrete walls (both cast in-situ or precast) that are load bearing and fire protecting.

### STANDARD
A standard wall, extruded vertically with a constant thickness along the wall path. 
{ .deprecated}
> The value is deprecated, it is expressed by choosing the subtype _IfcWallStandardCase_.

### POLYGONAL
A polygonal wall, extruded vertically, where the wall thickness varies along the wall path.

### ELEMENTEDWALL
A stud wall framed with studs and faced with sheetings, sidings, wallboard, or plasterwork. 
{ .deprecated}
> The value is deprecated, it is expressed by choosing the subtype _IfcWallElementedCase_.

### RETAININGWALL
A supporting wall used to protect against soil layers behind. Special types of a retaining wall may be e.g. Gabion wall and Grib wall. Examples of retaining walls are wing wall, headwall, stem wall, pierwall and protecting wall.

### WAVEWALL
Protective wall or screen to block overtopping and impact of waves across a breakwater

### USERDEFINED
User-defined wall element.

### NOTDEFINED
Undefined wall element.
