IfcStructuralSurfaceMember
==========================

Instances of _IfcStructuralSurfaceMember_ describe face members, that is, structural analysis idealizations of slabs, walls, and shells. Surface members may be planar or curved.

> HISTORY&nbsp; New entity in IFC2x2.

{ .change-ifc2x4}
> IFC4 CHANGE&nbsp; Use definitions changed, WHERE rule added.

****Coordinate Systems****:

See definitions at _IfcStructuralItem_. The local coordinate system is established by the reference surface given by topology representation.

****Material Use Definition****

The material of direct instances _IfcStructuralSurfaceMember_ (in contrast to instances of the subtype _IfcStructuralSurfaceMemberVarying_) is defined by _IfcMaterial_ and attached by the _IfcRelAssociatesMaterial.RelatingMaterial_. It is accessible by the inverse _HasAssociations_ relationship.

The material is specified minimally by a name which corresponds with an agreed upon standardized structural material designation. An external reference to the source which specifies the material designation should be provided. Alternatively, structural material properties may be provided by means of _IfcMechanicalMaterialProperties_ and _IfcExtendedMaterialProperties_.

Direct instances of _IfcStructuralSurfaceMember_ are assumed to be located centrically relative to their reference surface. Their depth is provided in the attribute _Thickness_.
