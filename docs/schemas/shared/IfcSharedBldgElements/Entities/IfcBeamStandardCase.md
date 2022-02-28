# IfcBeamStandardCase

The standard beam, _IfcBeamStandardCase_, defines a beam with certain constraints for the provision of material usage, parameters and with certain constraints for the geometric representation. The _IfcBeamStandardCase_ handles all cases of beams, that:

* have a reference to the _IfcMaterialProfileSetUsage_ defining the material profile association of the beam with the cardinal point of its insertion relative to the local placement.
* are consistent in using the correct cardinal point offset of the profile as compared to the 'Axis' and 'Body' shape representation
* are based on a sweep of a planar profile, or set of profiles, as defined by the _IfcMaterialProfileSet_
* have an 'Axis' shape representation with constraints provided below in the geometry use definition
* have a 'Body' shape representation with constraints provided below in the geometry use definition
    * are extruded perpendicular to the profile definition plane
    * have a start profile, or set of profiles, that is swept
    * the sweeping operation can be linear extrusion, circular rotation, or a sweep along a directrix
    * the start profile, or set of profiles can be swept unchanged, or might be changed uniformly by a taper definition
*
>> NOTE  View definitions and implementer agreements may further constrain the applicable geometry types, e.g. by excluding tapering from an _IfcBeamStandardCase_ implementation.

> HISTORY  New entity in IFC4.

**_Geometric Representations_**

The geometric representation of _IfcBeamStandardCase_ is defined using the following multiple shape representations for its definition:

* **Axis**: A three dimensional open curve (subtype of _IfcBoundedCurve_) defining the axis for the standard beam. The cardinal point is determined by the beam axis.
* **Body**: A Swept Solid Representation or a CSG clipping representation defining the 3D shape of the standard beam.

> NOTE  It is invalid to exchange a 'SurfaceModel', 'Brep', or 'MappedRepresentation' representation for the 'Body' shape representation of an _IfcBeamStandardCase_.

## Formal Propositions

### HasMaterialProfileSetUsage
A valid instance of _IfcBeamStandardCase_ relies on the provision of an _IfcMaterialProfileSetUsage_.

## Concepts

### Axis 3D Geometry

The following additional constraints apply to the 'Axis' representation, if the 'Body' shape representation has the RepresentationType : 'SweptSolid':

* Axis 
    * IfcPolyline having two Points, or IfcTrimmedCurve with BasisCurve of Type IfcLine for 'SweptSolid' provided as IfcExtrudedAreaSolid. The axis curve lies on the z axis of the object coordinate system.
    * IfcTrimmedCurve with BasisCurve of Type IfcCircle for 'SweptSolid' provided as IfcRevolvedAreaSolid. The axis curve lies on the x/z plane of the object coordinate system, the tangent at the start is along the positive z-axis. 

&nbsp;

<table border="0" cellpadding="2" cellspacing="2" summary="Axis">

<tr><td align="left" valign="top" width="350">
<img src="../../../../figures/ifcbeamstandardcase_axis-01.png" alt="Axis" height="300" width="400" border="1"></td>
<td><blockquote class="example">EXAMPLE&nbsp; As shown in Figure 76, the axis shall be defined along the z axis of the object coordinate system. The axis representation can be used to represent the system length of a beam that may extent the body length of the beam.</blockquote>

</td>
</tr>

<tr><td><p class="figure">Figure 1 &mdash; Beam axis representation</p></td><td>&nbsp;</td></tr>

</table>

<table>

<tr><td align="left" valign="top" width="350">
<img src="../../../../figures/ifcbeamstandardcase_axis-02.png" alt="Axis" height="300" width="400" border="1"></td>
<td><blockquote class="example">EXAMPLE&nbsp; As shown in Figure 77, the axis representation shall be used to represent the cardinal point as the offset between the 'Axis' and the extrusion path of the beam. The extrusion path is provided as <em>IfcExtrudedAreaSolid.ExtrudedDirection</em> and should be parallel to the 'Axis' and the z axis. It has to be guaranteed that the value provided by
<em>IfcMaterialProfileSetUsage.CardinalPoint</em> is consistent to the <em>IfcExtrudedAreaSolid.Position</em>.</blockquote>

</td>
</tr>

<tr><td><p class="figure">Figure 2 &mdash; Beam axis cardinal point</p></td><td>&nbsp;</td></tr>

</table>

### Body AdvancedSweptSolid Geometry

The following additional constraints apply to the 'AdvancedSweptSolid' representation type:

* **Solid**: IfcSurfaceCurveSweptAreaSolid, IfcFixedReferenceSweptAreaSolid, IfcExtrudedAreaSolidTapered, IfcRevolvedAreaSolidTapered shall be supported. 
>> NOTE&nbsp; View definitions and implementer agreement can further constrain the allowed swept solid types. 
* **Solid Position** : see 'SweptSolid' geometric representation
* **Profile**: see 'SweptSolid' geometric representation
* **Profile Position** : see 'SweptSolid' geometric representation
* **Extrusion**:&nbsp;not applicable

### Body Clipping Geometry

The following constraints apply to the 'Clipping' representation:

* **Solid** : see 'SweptSolid' geometric representation
* **Solid Position** : see 'SweptSolid' geometric representation
* **Profile** : see 'SweptSolid' geometric representation
* **Profile Position** : see 'SweptSolid' geometric representation
* **Extrusion** : see 'SweptSolid' geometric representation
* **Orientation** : see 'SweptSolid' geometric representation
* **Boolean result**: The IfcBooleanClippingResult shall be supported, allowing for Boolean differences between the swept solid (here IfcExtrudedAreaSolid) and one or several IfcHalfSpaceSolid (or its subtypes).

Figure 1 illustrates a 'Clipping' geometric representation with use of IfcBooleanClippingResult between an IfcExtrudedAreaSolid and an IfcHalfSpaceSolid to create a clipped body, with cardinal point applied as **4** (mid-depth left)

!["clipped beam"](../../../../figures/ifcbeamstandardcase_clipping-01.png "Figure 1 &mdash; Beam body clipping")

### Body SweptSolid Geometry

The following additional constraints apply to the 'SweptSolid' representation:

* **Solid**: IfcExtrudedAreaSolid, IfcRevolvedAreaSolid shall be supported
* **Solid Position** : The _IfcSweptAreaSolid.Position_ shall exclusively been used to correspond to the cardinal point. The x/y offset of the Position represents the cardinal point offset of the profile against the axis. No rotation shall be allowed.
* **Profile**: All subtypes of IfcParameterizedProfileDef
* **Profile Position** : For all single profiles, the _IfcParameterizedProfileDef.Position_ shall be NIL, or having Location = 0.,0. and RefDirection = 1.,0.
* **Extrusion**:&nbsp;Perpendicular to the profile direction. The _IfcExtrudedAreaSolid.ExtrudedDirection_ shall be [0.,0.,1.].
* **Orientation**: The y-axis of the profile, as determined by _IfcSweptAreaSolid.Position.P[2]_ shall point upwards. It indicates the "role" of the beam, a role=0&deg; means y-axis of profile pointing upwards.

Figure 1 illustrates a standard geometric representation with cardinal point applied as **1** (bottom left).

The following interpretation of dimension parameter applies for rectangular beams with linear extrusions:

* _IfcRectangleProfileDef.YDim_ interpreted as beam height
* _IfcRectangleProfileDef.XDim_ interpreted as beam width

The following interpretation of dimension parameter applies for circular beams:

* _IfcCircleProfileDef.Radius_ interpreted as beam radius.

!["standard beam"](../../../../figures/ifcbeamstandardcase_sweptsolid-01.png "Figure 1 &mdash; Beam body extrusion")

### Material Profile Set Usage

The IfcBeamStandardCase defines in addition that the IfcBeamType should have a unique IfcMaterialProfileSet, that is referenced by the IfcMaterialProfileSetUsage that is assigned to all occurrences of this IfcBeamType.

<table>

 <tr>
  <td><img src="../../../../figures/ifcbeamstandardcase-01.png" height="500" width="500" alt="Material profile set and usage"></td>
  <td><blockquote class="example">EXAMPLE&nbsp; Figure 1 illustrates assignment of <em>IfcMaterialProfileSetUsage</em> and <em>IfcMaterialProfileSet</em> to the <em>IfcBeamStandardCase</em> as the beam occurrence and to the <em>IfcBeamType</em>. The same <em>IfcMaterialProfileSet</em> shall be shared by many occurrences of <em>IfcMaterialProfileSetUsage</em>. This relationship shall be consistent to the relationship between the <em>IfcBeamType</em> and the <em>IfcBeamStandardCase</em>.</blockquote>

 </td>
 </tr>
 
<tr>
  <td><p class="figure">Figure 1 &mdash; Beam profile usage</p></td>
  <td>&nbsp;</td>
 </tr>

</table>

<table>

 <tr>
  <td><img src="../../../../figures/ifcbeamstandardcase_cardinalpoint.png" height="250" width="500" alt="Cardinal point usage"></td>
  <td>

    <blockquote class="example">EXAMPLE&nbsp; Figure 2 illustrates alignment of cardinal points.</blockquote>
    
<blockquote class="note">NOTE&nbsp; It has to be guaranteed that the use of <em>IfcCardinalPointEnum</em> is consistent to the placement of the extrusion body provided by <em>IfcExtrudedAreaSolid.Position</em></blockquote>
    
<blockquote class="note">NOTE&nbsp; The cardinal points <b>8</b> (top centre) and <b>6</b> (mid-depth right) are assigned according to the definition at <em>IfcCardinalPointReference</em></blockquote> </td>
 </tr>
 
<tr>
  <td><p class="figure">Figure 2 &mdash; Beam cardinal points</p></td>
  <td>&nbsp;</td>
 </tr>

</table>

<table>
 
<tr>
  <td><img src="../../../../figures/ifcbeamstandardcase-02.png" height="550" width="500" alt="Material profile set and usage"></td>
  <td>
<blockquote class="example">EXAMPLE&nbsp; Figure 3 illustrates assignment of a composite profile by using <em>IfcCompositeProfile</em> for geometric representation and several <em>IfcMaterialProfile</em>'s within the <em>IfcMaterialProfileSet</em>.</blockquote>

 </td>
 </tr>

 <tr>
  <td><p class="figure">Figure 3 &mdash; Beam composite profiles</p></td>
 </tr>

</table>

### Product Local Placement

The following restriction is imposed:

* The local placement shall provide the location and directions for the standard beam, the x/y plane is the plane for the start profile, and the z-axis is the extrusion axis for the beam body (in case of rotation, the tangent direction).

