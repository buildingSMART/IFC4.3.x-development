IfcFixedReferenceSweptAreaSolid
===============================
An _IfcFixedReferenceSweptAreaSolid_ is a type of swept area solid which is
the result of sweeping an area along a _Directrix_. The swept area is provided
by a subtype of _IfcProfileDef_. The profile is placed by an implicit
cartesian transformation operator at the start point of the sweep, where the
profile normal agrees to the tangent of the directrix at this point, and the
profile''s x-axis agrees to the _FixedReference_ direction. The orientation of
the curve during the sweeping operation is controlled by the _FixedReference_
direction.  
  
The _SweptArea_ is swept along the _Directrix_ in such a way that the origin
of the local coordinate system used to define the _SweptArea_ is on the
_Directrix_ and the local X axis is in the direction of the projection of
_FixedReference_ onto the normal plane to the directrix at this point. The
resulting solid has the property that the cross section of the surface by the
normal plane to the _Directrix_ at any point is a copy of the _SweptArea_. The
resulting swept solid is placed by the _Position_ coordinate system.  
  
The _Directrix_ and the _ReferenceSurface_ are positioned within the object
coordinate system. The start of the sweeping operation is at the _StartParam_,
the parameter value is provided based on the curve parameterization. If no
_StartParam_ is provided the start defaults to the begin of the directrix. The
end of the sweeping operation is at the _EndParam_, the parameter value is
provided based on the curve parameterization. If no _EndParam_ is provided the
end defaults to the end of the directrix.  
  
> NOTE  The _StartParam_ and the _EndParam_ are not normalized by default,
> they depend upon the parameterization of the curve. However using the
> _IfcReparametrisedCompositeCurveSegment_ within an _IfcCompositeCurve_ as
> the directrix allows to explicitly reparameterize the underlying sweeping
> curve.  
  
> EXAMPLE  The reference surface is any surface (plane, cylindric, composite)
> situated in 3D space and positioned in the object coordinate system. In many
> cases, it is a surface of extrusion. The directrix lies on the surface,
> often defined as a p-curve at this reference surface. At any point of the
> directrix, a plane can be constructed. The origin of the position coordinate
> system lies at the directrix. The Axis3 (the z-axis, or normal) of the
> position coordinate system is identical to the tangent of the directrix at
> this point, the Axis1 (the x axis, or u) of the position coordinate system
> is identical to the _FixedReference_ direction. The Axis2 (the y axis, or v)
> is constructed. In this case the resulting swept solid is not repositioned.  
  
The orientation of the _SweptArea_ as it sweeps along the _Directrix_ is
precisely defined by a _CartesianTransformationOperator3d_ with attributes:  
  
* _LocalOrigin_ as point (0; 0; 0),  
* _Axis1_ as the _FixedReference_.  
* _Axis3_ as the direction of the tangent vector **t** at the point of the _Directrix_ with parameter **u**.  
  
The remaining attributes are defaulted to define a corresponding
transformation matrix **T(u)**, which varies with the _Directrix_ parameter
**u**.  
  
> NOTE  The geometric shape of the solid is not dependent upon the curve
> parameterization; the volume depends upon the area swept and the length of
> the _Directrix_.  
  
> NOTE  Entity adapted from **fixed_reference_swept_surface** defined in ISO
> 10303-42.  
  
> HISTORY  New entity in IFC4.  
  
{ .spec-head}  
Informal Propositions:  
  
1\. The _SweptArea_ shall lie in the plane z = 0.  
2\. The _FixedReference_ shall not be parallel to a tangent vector to the
directrix at any point along this curve.  
3\. The _Directrix_ curve shall be tangent continuous.  
[ _bSI
Documentation_](https://standards.buildingsmart.org/IFC/DEV/IFC4_2/FINAL/HTML/schema/ifcgeometricmodelresource/lexical/ifcfixedreferencesweptareasolid.htm)


