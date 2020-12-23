# IfcBlock

The _IfcBlock_ is a Construction Solid Geometry (CSG) 3D primitive. It is defined by a position and a positve distance along the three orthogonal axes. The inherited _Position_ attribute has the _IfcAxisPlacement3D_ type and provides:

* _SELF\IfcCsgPrimitive3D.Position_: The location and orientation of the axis system for the primitive.
* _SELF\IfcCsgPrimitive3D.Position.Location_: The block has one vertex at location and the edges are aligned with the placement axes in the positive sense.

The _XLength_, _YLength_, and _ZLength_ attributes define the size of the IfcBlock along the three axes.

<table cellpadding="2" cellspacing="2" summary="block geometry">
<tr>
<td><img alt="block" src="../../../../../../figures/ifcblock-layout1.png" border="0" height="300" width="400"></td>
<td style="vertical-align:bottom;">
<p class="small">Figure 1 illustrates geometric parameters of a block where the block positioned within its own placement
coordinate system. The values for <em>XLength</em>, <em>YLength</em>, and <em>ZLength</em> are applied to the positive
direction of the X, Y, and Z axis.</p>
</td>
</tr>
<tr>
<td>
<p class="figure">Figure 1 &mdash; Block geometry</p>
</td>
<td>&nbsp;</td>
</tr>
</table>

{ .extDef}
> NOTE&nbsp; Definition according to ISO/CD 10303-42:1992  
> A block is a solid rectangular parallelepiped, defined with a location and placement coordinate system. The block is specified by the positive lengths x, y, and z along the axes of the placement coordinate system, and has one vertex at the origin of the placement coordinate system.

> NOTE&nbsp; Entity adapted from **block** defined in ISO 10303-42.

> HISTORY&nbsp; New entity in IFC2x3.

{ .use-head}
Texture definition

On each side face, textures are aligned facing upright. On the top and bottom faces, textures are aligned facing front-to-back. Textures are stretched or repeated to the extent of each face according to _RepeatS_ and _RepeatT_.

Figure 2 illustrates default texture mapping with a clamped texture (RepeatS=False and RepeatT=False). The image on the left shows the texture where the S axis points to the right and the T axis points up. The image on the right shows the texture applied to the geometry where the X axis points back to the right, the Y axis points back to the left, and the Z axis points up.

&nbsp;

{ .gridtable}
<table summary="block texture" class="gridtable">
<tr>
<td><img src="../../../../../../figures/ifcblock-texture.png" alt="texture"></td>
</tr>
<tr>
<td>
<table summary="texture" width="512" class="gridtable">
<tr>
<th>Side</th>
<th>Normal</th>
<th>Origin X</th>
<th>Origin Y</th>
<th>Origin Z</th>
<th>S Axis</th>
<th>T Axis</th>
</tr>
<tr>
<td>Left</td>
<td>-X</td>
<td>0</td>
<td>+YLength</td>
<td>0</td>
<td>-Y</td>
<td>+Z</td>
</tr>
<tr>
<td>Right</td>
<td>+X</td>
<td>+XLength</td>
<td>0</td>
<td>0</td>
<td>+Y</td>
<td>+Z</td>
</tr>
<tr>
<td>Front</td>
<td>-Y</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>+X</td>
<td>+Z</td>
</tr>
<tr>
<td>Back</td>
<td>+Y</td>
<td>+XLength</td>
<td>+YLength</td>
<td>0</td>
<td>-X</td>
<td>+Z</td>
</tr>
<tr>
<td>Bottom</td>
<td>-Z</td>
<td>0</td>
<td>+YLength</td>
<td>0</td>
<td>+X</td>
<td>-Y</td>
</tr>
<tr>
<td>Top</td>
<td>+Z</td>
<td>0</td>
<td>0</td>
<td>+ZLength</td>
<td>+X</td>
<td>+Y</td>
</tr>
</table>
</td>
</tr>
<tr>
<td>
<p class="figure">Figure 2 &mdash; Block textures</p>
</td>
</tr>
</table>

## Attributes

### XLength
The size of the block along the placement X axis. It is provided by the inherited axis placement through _SELF\IfcCsgPrimitive3D.Position.P[1]_.

### YLength
The size of the block along the placement Y axis. It is provided by the inherited axis placement through _SELF\IfcCsgPrimitive3D.Position.P[2]_.

### ZLength
The size of the block along the placement Z axis. It is provided by the inherited axis placement through _SELF\IfcCsgPrimitive3D.Position.P[3]_.
