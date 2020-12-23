# IfcMemberStandardCase

The standard member, _IfcMemberStandardCase_, defines a member with certain constraints for the provision of material usage, parameters and with certain constraints for the geometric representation. The _IfcMemberStandardCase_ handles all cases of members, that:

* have a reference to the _IfcMaterialProfileSetUsage_ defining the material profile association of the member with the cardinal point of its insertion relative to the local placement.
* are based on a sweep of a planar profile, or set of profiles, as defined by the _IfcMaterialProfileSet_
* have an 'Axis' shape representation with constraints provided below in the geometry use definition
* have a 'Body' shape representation with constraints provided below in the geometry use definition
* have a start profile, or set of profiles, that is swept along the directrix and might be changed uniformly by a taper definition
* are consistent in using the correct cardinal point offset of the profile as compared to the 'Axis' and 'Body' shape representation
* are extruded perpendicular to the profile definition plane

> NOTE&nbsp; View definitions and implementer agreements may further constrain the applicable geometry types, such as by excluding tapering from an _IfcMemberStandardCase_ implementation.

> HISTORY&nbsp; New entity in IFC4.

## Formal Propositions

### HasMaterialProfileSetUsage
A valid instance of _IfcMemberStandardCase_ relies on the provision of an _IfcMaterialProfileSetUsage_.
