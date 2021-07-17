IfcSphere
=========

The _IfcSphere_ is a Construction Solid Geometry (CSG) 3D primitive. It is a solid where all points at the surface have the same distance from the center point. The inherited _Position_ attribute defines the _IfcAxisPlacement3D_ and provides:

* _SELF\IfcCsgPrimitive3D.Position_: The location and orientation of the axis system for the primitive.&nbsp;
* _SELF\IfcCsgPrimitive3D.Position.Location_: The center of the sphere.
* _SELF\IfcCsgPrimitive3D.Position.Position[3]:_ The z axis points at its positve direction towards the north pole, and by its negative directions towards the south pole.

&nbsp;

<table summary="illustration">
<tr>
<td><img src="../../../../../../figures/ifcsphere-layout1.png" border="0" height="300" width="400" alt="sphere"></td>
<td><blockquote class="example">EXAMPLE&nbsp; Figure 1 illustrates geometric parameters of the sphere. The sphere is positioned within its own placement
coordiante system relative to the object coordinate system. The origin is the center of the sphere.</blockquote>
</td></tr>
<tr>
<td>
<p class="figure">Figure 1 &mdash; Sphere geometry</p>
</td>
</tr>
</table>

{ .extDef}
> NOTE&nbsp; Definition according to ISO/CD 10303-42:1992  
> A sphere is a CSG primitive with a spherical shape defined by a centre and a radius.

> NOTE&nbsp; Entity adapted from **sphere** defined in ISO 10303-42.

> HISTORY&nbsp; New entity in IFC2x3.

{ .use-head}
Texture Use Definition

Textures are aligned facing upright with origin at the back (+Y direction) revolving counter-clockwise. Textures are stretched or repeated to the extent of the circumference at the equator according to RepeatS and RepeatT.

Figure 2 illustrates default texture mapping with a clamped texture (RepeatS=False and RepeatT=False). The image on the left shows the texture where the S axis points to the right and the T axis points up. The image on the right shows the texture applied to the geometry where the X axis points back to the right, the Y axis points back to the left, and the Z axis points up.

{ .gridtable}
<table summary="texture" class="gridtable">
<tr>
<td><img src="../../../../../../figures/ifcsphere-texture.png" alt="texture"></td>
</tr>
<tr>
<td>
<table summary="texture" width="512" class="gridtable">
<tr valign="top">
<th>Side</th>
<th>Normal</th>
<th>Origin&nbsp;X</th>
<th>Origin&nbsp;Y</th>
<th>Origin&nbsp;Z</th>
<th>S&nbsp;Axis</th>
<th>T&nbsp;Axis</th>
</tr>
<tr valign="top">
<td>Side</td>
<td>+Y</td>
<td>0</td>
<td>+Radius</td>
<td>0</td>
<td>(-X, then curving counter-clockwise)</td>
<td>(+Z, then curving towards top)</td>
</tr>
</table>
</td>
</tr>
<tr>
<td>
<p class="figure">Figure 2 &mdash; Sphere textures</p>
</td>
</tr>
</table>
