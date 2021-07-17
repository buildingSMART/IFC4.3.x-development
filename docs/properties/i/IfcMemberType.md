IfcMemberType
=============

The element type _IfcMemberType_ defines commonly shared information for occurrences of members. Members are predominately linear building elements, often forming part of a structural system. The orientation of the member (being horizontal, vertical or sloped) is not relevant to its definition (in contrary to beam and column). The set of shared information may include:

* common properties within shared property sets
* common material information
* common profile definitions
* common shape representations

It is used to define a member specification, or member style (the specific product information that is common to all occurrences of that member type). Member types may be exchanged without being already assigned to occurrences.

Occurrences of the _IfcMemberType_ within building models are represented by instances of _IfcMemberStandardCase_ if the _IfcMemberType_ has a single associated _IfcMaterialProfileSet_; otherwise they are represented by instances of _IfcMember_. Occurrences of the _IfcMemberType_ within structural analysis models are represented by instances of _IfcStructuralCurveMember_, or its applicable subtypes.

> HISTORY&nbsp; New entity in IFC2x2 Addendum 1.
