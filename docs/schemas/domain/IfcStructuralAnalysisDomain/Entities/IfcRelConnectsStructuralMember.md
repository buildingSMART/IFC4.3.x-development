# IfcRelConnectsStructuralMember

The entity _IfcRelConnectsStructuralMember_ defines all needed properties describing the connection between structural members and structural connection objects (nodes or supports).
<!-- end of short definition -->


> HISTORY New entity in IFC2x2.

**Use Definition**

_Point Connection_
Instances of the entity _IfcRelConnectsStructuralMember_ shall be used to describe a connection between an instance of _IfcStructuralPointConnection_ and either an instance of _IfcStructuralCurveMember_ or _IfcStructuralSurfaceMember_. The _RelatedStructuralConnection_ for point connections has to be of type _IfcStructuralPointConnection_.

_Curve Connection_
Instances of the entity _IfcRelConnectsStructuralMember_ shall be used to describe a connection between an instance of _IfcStructuralCurveConnection_ and an instance of either _IfcStructuralCurveMember_ or _IfcStructuralSurfaceMember_. The _RelatedStructuralConnection_ for curve connections has to be of type _IfcStructuralCurveConnection_.

_Surface Connection_
Instances of the entity _IfcRelConnectsStructuralMember_ shall be used to describe a connection between an instance of _IfcStructuralSurfaceConnection_ and an instance of _IfcStructuralSurfaceMember_. The _RelatedStructuralConnection_ for curve connections has to be of type _IfcStructuralSurfaceConnection_.

_Coordinate System for Applied Conditions_
All values defined by _AppliedCondition_ or _AdditionalConditions_ are given within the coordinate system provided by _ConditionCoordinateSystem_, which is defined relative to the local coordinate system of the structural member. If the _ConditionCoordinateSystem_ is not defined, the local coordinate system of the structural member is used instead.

_Supported Length_
Optionally a supported length can be given, which specifies the length (or width) of the physical connection along a curve connection.

Figure 1 illustrates the appropriate definition of support lengths.

![supported length](../../../../figures/ifcrelconnectsstructuralmember-fig1.gif)

Figure 1 — Structural member support lengths

## Attributes

### RelatingStructuralMember
Reference to an instance of IfcStructuralMember (or its subclasses) which is connected to the specified structural connection.

### RelatedStructuralConnection
Reference to an instance of IfcStructuralConnection (or its subclasses) which is connected to the specified structural member.

### AppliedCondition
Conditions which define the connections properties. Connection conditions are often called "release" but are not only used to define mechanisms like hinges but also rigid, elastic, and other conditions.

### AdditionalConditions
Describes additional connection properties.

### SupportedLength
Defines the 'supported length' of this structural connection. See Fig. for more detail.

### ConditionCoordinateSystem
Defines a coordinate system used for the description of the connection properties in _ConnectionCondition_ relative to the local coordinate system of _RelatingStructuralMember_. If left unspecified, the placement _IfcAxis2Placement3D_((x,y,z), ?, ?) is implied with x,y,z being the local member coordinates where the connection is made and the default axes directions being in parallel with the local axes of _RelatingStructuralMember_.
