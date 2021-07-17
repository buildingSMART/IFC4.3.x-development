IfcRelSpaceBoundary
===================

The space boundary defines the physical or virtual delimiter of a space by the relationship _IfcRelSpaceBoundary_ to the surrounding elements.

* In the case of a physical space boundary, the placement and shape of the boundary may be given, and the building element, providing the boundary, is referenced,
* In the case of a virtual space boundary, the placement and shape of the boundary may be given, and a virtual element is referenced.

The _IfcRelSpaceBoundary_ is defined as an objectified relationship that handles the element to space relationship by objectifying the relationship between an element and the space it bounds. It is given as a one-to-one relationship, but allows each element (including virutal elements and openings) to define many such relationship and each space to be defined by many such relationships.

Space boundaries are always defined as seen from the space. In general two basic types of space boundaries are distinguished:

* 1^<small>st</small>^ level space boundary: defined as boundaries of the space, not taking into account any change in building element or spaces on the other side.
* 2^<small>nd</small>^ level space boundary: defined as boundary taking any change in building element or spaces on the other side into account. It can be further distinguished into 
    * 2^<small>nd</small>^ level type A: There is a space on the other side.
    * 2^<small>nd</small>^ level type B: There is a building element on the other side. 

> <small>The exact definition of how space boundaries are broken down depends on the view definition, more detailed conventions on how space boundaries are decomposed can only be given at the domain or application type level.</small>> * <small>In an architectural or FM related view, a space boundary is defined totally from inside the space. This is a 1<sup><small>st</small></sup> level space boundary.</small>
> * <small>In a thermal view, the decomposition of the space boundary depends on the material of the providing building element and the adjacent spaces behind. This is a 2<sup><small>nd</small></sup> level space boundary.</small>

<table summary="space boundary types" border="0">
<tr>
 <td><img src="../../../../../../figures/ifcrelspaceboundary_1stlevel.png" alt="1st level"></td>
 <td><img src="../../../../../../figures/ifcrelspaceboundary_2ndlevel.png" alt="2nd level"></td>
</tr>
<tr>
 <td><p class="figure">Figure 1 &mdash; Space boundary at first level</p></td>
 <td><p class="figure">Figure 2 &mdash; Space boundary at second level</p></td>
</tr>
<tr>
 <td><img src="../../../../../../figures/ifcrelspaceboundary_2ndlevel_typea.png" alt="2nd level type a"></td>
 <td><img src="../../../../../../figures/ifcrelspaceboundary_2ndlevel_typeb.png" alt="2nd level type b"></td>
</tr>
<tr>
 <td><p class="figure">Figure 3 &mdash; Space boundary at second level type A</p></td>
 <td><p class="figure">Figure 4 &mdash; Space boundary at second level type B</p></td>
</tr>
</table>

The differences between the 1^<small>st</small>^ and 2^<small>nd</small>^ level space boundaries is identified by:

* **1^<small>st</small>^ level:**   SELF\IfcRoot.Name = "1stLevel"   SELF\IfcRootDescription = NIL
* **2^<small>nd</small>^ level:**   SELF\IfcRoot.Name = "2ndLevel"   SELF\IfcRootDescription = "2a", or "2b"

Differentiation between physical and virtual space boundary is illustrated in Figure 1 and Figure 42.

As shown in Figure 41, if the _IfcRelSpaceBoundary_ is used to express a virtual boundary, the attribute _PhysicalOrVirtualBoundary_ has to be set to VIRTUAL. The attribute _RelatedBuildingElement_ shall point to an instance of _IfcVirtualElement_. If the correct location is of interest, the attribute _ConnectionGeometry_ is required.

> NOTE&nbsp; The connection geometry, either by a 2D curve or a 3D surface, is used to describe the portion of the "virtual wall" that separates the two spaces. All instances of _IfcRelSpaceBoundary_ given at the adjacent spaces share the same instance of _IfcVirtualElement_. Each instance of _IfcRelSpaceBoundary_ provides in addition the _ConnectionGeometry_ given within the local placement of each space.

!["IfcRelSpaceBoundary_virtual (35K)"](../../../../../../figures/ifcrelspaceboundary_virtual.png "Figure 5 &mdash; Space boundary of virtual element")

As shown in Figure 42, if the _IfcRelSpaceBoundary_ is used to express a physical boundary between two spaces, the attribute _PhysicalOrVirtualBoundary_ has to be set to PHYSICAL. The attribute _RelatedBuildingElement_ has to be given and points to the element providing the space boundary. The attribute _ConnectionGeometry_ may be inserted, in this case it describes the physical space boundary geometically, or it may be omited, in that case it describes a physical space boundary logically.

!["IfcRelSpaceBoundary_physical (35K)"](../../../../../../figures/ifcrelspaceboundary_physical.png "Figure 6 &mdash; Space boundary of physical element")

The _IfcRelSpaceBoundary_ may have geometry attached. If geometry is not attached, the relationship between space and building element is handled only on a logical level. If geometry is attached, it is given within the local coordinate systems of the space.

> NOTE&nbsp; The attributes _CurveOnRelatingElement_ at _IfcConnectionCurveGeometry_ or _SurfaceOnRelatingElement_ at _IfcConnectionSurfaceGeometry_ provide the geometry within the local coordinate system of the _IfcSpace_, whereas the attributes _CurveOnRelatedElement_ at _IfcConnectionCurveGeometry_ or _SurfaceOnRelatedElement_ at _IfcConnectionSurfaceGeometry_ provide the geometry within the local coordinate system of the subtype of _IfcElement_

> NOTE&nbsp; In most view definitions the connection geometry for the related _IfcElement_ is not provided.

The geometric representation (through the _ConnectionGeometry_ attribute) is defined using either 2D curve geometry or 3D surface geometry for space boundaries. In most view definitions the 3D connection surface geometry is required.

* 1^<small>st</small>^ level space boundary: 
    * only connection geometry for related space shall be provided
    * only surface connection geometry shall be provided
    * only the following surface representations are supported: 
        * _IfcSurfaceOfLinearExtrusion_
        * _IfcCurveBoundedPlane_
        * _IfcCurveBoundedSurface_
        * _IfcFaceBasedSurfaceModel_ 
* 2^<small>nd</small>^ level space boundary: 
    * only connection geometry for related space shall be provided
    * only surface connection geometry shall be provided
    * only the following surface representations are supported: 
        * _IfcCurveBoundedPlane_ with restrictions to have polygonal boundaries only
        * _IfcFaceBasedSurfaceModel_ 

**Surface connection geometry**

The following constraints apply to the surface connection geometry representation:

* planar boundaries: 
    * _IfcSurfaceOfLinearExtrusion_ defined by a _SweptCurve_ being an _IfcArbitraryOpenProfileDef_ with straight segements, or
    * _IfcCurveBoundedPlane_ 
* curved boundaries 
    * _IfcSurfaceOfLinearExtrusion_ defined by a _SweptCurve_ being an _IfcArbitraryOpenProfileDef_ with curves segements, or
    * _IfcCurveBoundedSurface_ with a _BasisSurface_ being a non planar surface, such as _IfcCylindricalSurface_, or
    * _IfcFaceBasedSurfaceModel_ if already faceted. 

**Curve connection geometry**

The following constraints apply to the 2D curve representation:

* Curve: _IfcPolyline_, _IfcTrimmedCurve_ or _IfcCompositeCurve_

> HISTORY&nbsp; New entity in IFC1.5, the entity has been modified in IFC2x.

{ .change-ifc2x}
> IFC2x CHANGE The data type of the attribute_RelatedBuildingElement_ has been changed from _IfcBuildingElement_ to its supertype _IfcElement_. The data type of the attribute _ConnectionGeometry_ has been changed from _IfcConnectionSurfaceGeometry_ to its supertype _IfcConnectionGeometry_.

{ .change-ifc2x4}
> IFC4 CHANGE The attribute _RelatedBuildingElement_ has been made mandatory. For virtual boundaries the reference to _IfcVirtualElement_ is now mandatory.
