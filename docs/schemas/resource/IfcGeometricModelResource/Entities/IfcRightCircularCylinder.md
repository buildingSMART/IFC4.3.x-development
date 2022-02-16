# IfcRightCircularCylinder

The _IfcRightCircularCylinder_ is a Construction Solid Geometry (CSG) 3D primitive. It is a solid with a circular base and top. The cylindrical surface between if formed by points at a fixed distance from the axis of the cylinder. The inherited _Position_ attribute defines the _IfcAxisPlacement3D_ and provides:

* _SELF\IfcCsgPrimitive3D.Position_: The location and orientation of the axis system for the primitive.
* _SELF\IfcCsgPrimitive3D.Position.Location_: The center of the circular area being the bottom face of the cylinder.
* _SELF\IfcCsgPrimitive3D.Position.Position[3]:_ The z axis provides the center axis and the height is measured from the origin along the positive direction of the z axis.

Figure 1 illustrates geometric parameters of the cylinder. The cylinder is positioned within its own placement coordinate system. The origin is the center of the bottom circular disk, that lies in the XY plane. The center of the top circular disk is on the positive z axis at [0, 0, _Height_].

!["cylinder"](../../../../figures/ifcrightcircularcylinder-layout1.png "Figure 1 &mdash; Right circular cylinder geometry")

{ .extDef}
> NOTE&nbsp; Definition according to ISO/CD 10303-42:1992  
> A right circular cylinder is a CSG primitive in the form of a solid cylinder of finite height. It is defined by an axis point at the centre of one planar circular face, an axis, a height, and a radius. The faces are perpendicular to the axis and are circular discs with the specified radius. The height is the distance from the first circular face centre in the positive direction of the axis to the second circular face centre.

> NOTE&nbsp; Entity adapted from **right_circular_cylinder** defined in ISO 10303-42.

> HISTORY&nbsp; New entity in IFC2x3.

{ .use-head}
Texture use definition

On the circular side, textures are aligned facing upright with origin at the back (+Y direction) revolving counter-clockwise. Textures are stretched or repeated to the extent of the circumference according to RepeatS. Textures are stretched or repeated to the extent of the _Height_ according to RepeatT.

On the top and bottom faces, textures are aligned facing front-to-back, with the center of the circle aligned to the center of the texture.

Figure 2 illustrates default texture mapping with a clamped texture (RepeatS=False and RepeatT=False). The image on the left shows the texture where the S axis points to the right and the T axis points up. The image on the right shows the texture applied to the geometry where the X axis points back to the right, the Y axis points back to the left, and the Z axis points up.

{ .gridtable}
<table summary="texture" class="gridtable">
<tr>
<td><img alt="texture" src="../../../../figures/ifcrightcircularcylinder-texture.png"></td>
</tr>
<tr>
<td>
<table summary="texture" width="512" class="gridtable">
<tr>
<th>Side</th>
<th>Normal</th>
<th>Origin&nbsp;X</th>
<th>Origin&nbsp;Y</th>
<th>Origin&nbsp;Z</th>
<th>S&nbsp;Axis</th>
<th>T&nbsp;Axis</th>
</tr>
<tr>
<td>Side</td>
<td>+Y</td>
<td>0</td>
<td>+Radius</td>
<td>0</td>
<td>-X</td>
<td>+Z</td>
</tr>
<tr>
<td>Bottom</td>
<td>-Z</td>
<td>-Radius</td>
<td>+Radius</td>
<td>0</td>
<td>+X</td>
<td>-Y</td>
</tr>
<tr>
<td>Top</td>
<td>+Z</td>
<td>-Radius</td>
<td>-Radius</td>
<td>+Height</td>
<td>+X</td>
<td>+Y</td>
</tr>
</table>
</td>
</tr>
<tr>
<td>
<p class="figure">Figure 2 &mdash; Right circular cylinder textures</p>
</td>
</tr>
</table>

## Attributes

### Height
The distance between the planar circular faces of the cylinder.

### Radius
The radius of the cylinder.
