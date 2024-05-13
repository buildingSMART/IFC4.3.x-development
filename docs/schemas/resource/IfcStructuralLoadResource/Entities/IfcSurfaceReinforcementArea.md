# IfcSurfaceReinforcementArea

Describes required or provided reinforcement area of surface members.<!-- end of definition -->

> NOTE  Member design parameters like concrete cover, effective depth, orientation of meshes or rebars (two, optionally three directions) etc. are not specified in _IfcStructuralLoadResource_ schema. They shall be specified at the level of structural members.

> HISTORY  New entity in IFC4.

## Attributes

### SurfaceReinforcement1
Reinforcement at the face of the member which is located at the side of the positive local z direction of the surface member.  Specified as area per length, e.g. square metre per metre (hence length measure, e.g. metre).  The reinforcement area may be specified for two or three directions of reinforcement bars.

### SurfaceReinforcement2
Reinforcement at the face of the member which is located at the side of the negative local z direction of the surface member.  Specified as area per length, e.g. square metre per metre (hence length measure, e.g. metre).  The reinforcement area may be specified for two or three directions of reinforcement bars.

### ShearReinforcement
Shear reinforcement.  Specified as area per area, e.g. square metre per square metre (hence ratio measure, i.e. unitless).

## Formal Propositions

### SurfaceAndOrShearAreaSpecified
At least one of the reinforcement area attributes shall be specified.

### NonnegativeArea1
Surface reinforcement area must not be less than 0.

### NonnegativeArea2
Surface reinforcement area must not be less than 0.

### NonnegativeArea3
Shear reinforcement area must not be less than 0.
