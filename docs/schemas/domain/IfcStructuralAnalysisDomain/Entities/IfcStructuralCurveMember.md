# IfcStructuralCurveMember

Instances of _IfcStructuralCurveMember_ describe edge members, i.e. structural analysis idealizations of beams, columns, rods etc.. Curve members may be straight or curved.

> HISTORY  New entity in IFC2x2.

{ .change-ifc2x4}
> IFC4 CHANGE  Attribute _Axis_ and WHERE rule added. Use definitions changed.

### Coordinate Systems

See definitions at _IfcStructuralItem_. The local coordinate system is established by the reference curve given by topology representation and by the attribute _Axis_. The local x axis is parallel with the tangent on the reference curve. The local z axis is located in the surface which is created by sweeping _Axis_ along the reference curve and is directed according to _Axis_. The local y axis is directed such that x,y,z form a right-handed Cartesian coordinate system.

## Attributes

### PredefinedType
Type of member with respect to its load carrying behavior in this analysis idealization.

### Axis
Direction which is used in the definition of the local z axis.  _Axis_ is specified relative to the so-called global coordinate system, i.e. the _SELF\IfcProduct.ObjectPlacement_.

> NOTE  It is desirable and usually possible that many instances of _IfcStructuralCurveConnection_ and _IfcStructuralCurveMember_ share a common instance of _IfcDirection_ as their _Axis_ attribute.

## Formal Propositions

### HasObjectType
The attribute ObjectType shall be given if the predefined type is set to USERDEFINED.

## Concepts

### Material Profile Set Usage

The material of direct instances IfcStructuralCurveMember (in contrast to instances of the subtype IfcStructuralCurveMemberVarying) is defined by IfcMaterialProfileSetUsage and attached by the _IfcRelAssociatesMaterial.RelatingMaterial_. It is accessible by the inverse HasAssociations relationship. Composite profile beams can be represented by refering to several _IfcMaterialProfile_s within the IfcMaterialProfileSet that is referenced from the IfcMaterialProfileSetUsage. In case of tapered members, the material profile usage subtype IfcMaterialProfileSetUsageDual is used which specifies _IfcMaterialProfileSet_s separately at the start and the end of the tapered member.

The material (IfcMaterial) in each IfcMaterialProfile(Set) is specified minimally by a name which corresponds with an agreed upon standardized structural material designation. An external reference to the source which specifies the material designation should be provided. Alternatively, structural material properties may be provided by means of IfcMechanicalMaterialProperties and IfcExtendedMaterialProperties.

The profile (IfcProfileDef) in each IfcMaterialProfile(Set) is specified minimally by a name which corresponds with an agreed upon standardized structural profile designation. An external reference to the source which specifies the profile designation should be provided. Alternatively or additionally, explicit profile geometry should be provided by using respective subtypes of IfcProfileDef. Alternatively or additionally, structural profile properties may be provided by means of subtypes of IfcProfileProperties.

An IfcProfileDef is a two-dimensional geometric object with a x~p~,y~p~ coordinate system. The profile is inserted into the curve member model thus that the origin of x~p~,y~p~ is located at the member's reference curve and that x~p~,y~p~ are parallel with and directed like the local y,z.

> NOTE&nbsp; Due to convention in structural mechanics, axis names of IfcStructuralCurveMember differ from axis names of building elements like IfcBeamStandardCase: The extrusion axis of IfcStructuralCurveMember is called x while the extrusion axis of IfcBeamStandardCase is called z. Hence x,y,z of IfcStructuralCurveMember correspond with z,x,y of IfcBeamStandardCase.

If the profile is meant to be inserted centrically in terms of structural section properties, it is necessary that the origin of x~p~,y~p~ is identical with the geometric centroid of the profile (commonly also called centre of gravity). If subtypes of IfcParameterizedProfileDef are used which are only singly symmetric or are asymmetric, an explicit translation by _IfcParameterizedProfileDef.Position.Location_ is required then.

If the profile is inserted at its geometric centroid, _IfcMaterialProfileSetUsage.CardinalPoint_ shall be set to 10.

Otherwise, the profile is inserted eccentrically and a different cardinal point should be set accordingly.

> NOTE&nbsp; Another eccentricity model is available independently of eccentric profile specification: The reference curve of the member may be located eccentrically relative to the reference points of the connected _IfcStructuralPointConnection_s. The connection relationship is then established by IfcRelConnectsWithEccentricity. Whether one or the other or both eccentricity models may be used is subject to information requirements and local agreements.

### Reference Topology

Direct instances of IfcStructuralCurveMember shall have a topology representation which consists of one instance of IfcEdge or a subtype, representing the reference curve of the curve member. See definitions at IfcStructuralItem for further specifications.

{ .spec-head}
Informal Propositions:

1. The reference curve must not be parallel with Axis at any point within the curve member's domain.

The local coordinate system is established by the reference curve given by topology representation and by the attribute Axis. The local x axis is parallel with the tangent on the reference curve. The local z axis is located in the surface which is created by sweeping Axis along the reference curve and is directed according to Axis. The local y axis is directed such that x,y,z form a right-handed Cartesian coordinate system.

### Structural Connectivity



#### IfcStructuralPointConnection

Point connections at each end of the member.

