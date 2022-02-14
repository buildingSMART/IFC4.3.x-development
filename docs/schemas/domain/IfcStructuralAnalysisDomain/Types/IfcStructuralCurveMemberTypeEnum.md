# IfcStructuralCurveMemberTypeEnum

This enumeration distinguishes between different types of structural 'curve' members, such as cables.

> HISTORY&nbsp; New enumeration in IFC2x2.

{ .change-ifc2x4}
> IFC4 CHANGE&nbsp; Renamed from _IfcStructuralCurveTypeEnum_.

## Items

### RIGID_JOINED_MEMBER
A member with capacity to carry transverse and axial loads, i.e. a beam. Its actual joints may be rigid or pinned. Typically used in rigid frames.

### PIN_JOINED_MEMBER
A member with capacity to carry axial loads only, i.e. a link. Typically used in trusses.

### CABLE
A tension member which is able to carry transverse loads only under large deflection.

### TENSION_MEMBER
A member without compressional stiffness.

### COMPRESSION_MEMBER
A member without tensional stiffness.

### USERDEFINED
A specially defined member.

### NOTDEFINED
A member without further categorization.
