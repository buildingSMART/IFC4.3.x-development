# IfcLShapeProfileDef

_IfcLShapeProfileDef_ defines a section profile that provides the defining parameters of an L-shaped section (equilateral L profiles are also covered by this entity) to be used by the swept area solid. Its parameters and orientation relative to the position coordinate system are according to the following illustration. The shorter leg has the same direction as the positive _Position.P[1]_-axis, the longer or equal leg the same as the positive _Position.P[2]_-axis. The centre of the position coordinate system is in the profiles centre of the bounding box.

> HISTORY&nbsp; New entity in IFC2x2.

{ .change-ifc2x3}
> IFC2x3 CHANGE&nbsp; All profile origins are now in the center of the bounding box.

{ .change-ifc2x4}
> IFC4 CHANGE&nbsp; Types of _FilletRadius_ and _EdgeRadius_ were relaxed to allow for zero values.  
> Trailing attributes _CentreOfGravityInX_ and _CentreOfGravityInY_ deleted, use respective properties in _IfcExtendedProfileProperties_ instead.  
> WHERE rule which required _Width_ <= _Depth_ removed.

Figure 1 illustrates parameters of equal-sided and non-equal sided L-shaped section definitions.

<table>
<tr><td>
<table border="1" cellpadding="2" cellspacing="2" width="100%">
  <tbody>
    <tr>
      <td align="left" valign="top" width="420">

<img alt="non equal sided L-shape" src="../../../../figures/ifclshapeprofiledef_layout1.gif" border="0" height="300" width="400">

      </td>
      <td align="left" valign="top">

<p><u>Position</u> <br>
The parameterized profile defines its own position coordinate system.
The underlying coordinate system is defined by the swept area solid
that uses the profile definition. It is the xy plane of:</p>
      <ul>
        <li><em>IfcSweptAreaSolid.Position</em></li>
      </ul>
<p>by using offsets of the position location, the parameterized profile
can be positioned centric (using x,y offsets = 0.), or at any position
relative to the profile.</p>

<p>In the illustrated example, the 'CentreOfGravityInX' and 'CentreOfGravityInY' properties in <em>IfcExtendedProfileProperties</em>, if provided, are both negative.</p>

      </td>
    </tr>
    <tr>
      <td>

<img alt="equal sided L-shape" src="../../../../figures/ifclshapeprofiledef_layout2.gif" border="0" height="300" width="400"><br>

<font size="-1">Note:
The black coordinate axes show the
underlying coordinate system of the swept surface or swept area solid</font>

      </td>
      <td align="left" valign="top">

<p><u>Position</u> <br>
The profile is inserted into the underlying
coordinate system of the swept area solid by using the <em>Position</em>
attribute. In this example (cardinal point of gravity) the
attribute values of <em>IfcAxis2Placement2D</em>
are:</p>

<blockquote>
<p><tt>Location = IfcCartesianPoint(<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;+|CentreOfGravityInX|,<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;+|CentreOfGravityInY|)<br>
RefDirection = NIL (defaults to 1.,0.)</tt></p>
</blockquote>

<p>In the illustrated example, the x and y value of <em>Position.Location</em>, i.e. the <u>measures</u> |CentreOfGravityInX| and |CentreOfGravityInY| are both positive.  On the other hand, the <u>properties</u> named 'CentreOfGravityInX' and 'CentreOfGravityInY' in <em>IfcExtendedProfileProperties</em>, if provided, must both be set to 0 now because the centre of gravity of the resulting profile definition is located in the coordinate origin.</p>

      </td>
    </tr>
  </tbody>
</table>
</td></tr>
<tr><td><p class="figure">Figure 1 &mdash; L-shape profile</p></td></tr>
</table>

## Attributes

### Depth
Leg length, see illustration above (= h). Same as the overall depth.

### Width
Leg length, see illustration above (= b). Same as the overall width. This attribute is formally optional for historic reasons only. Whenever the width is known, it shall be provided by value.

### Thickness
Constant wall thickness of profile, see illustration above (= ts).

### FilletRadius
Fillet radius according the above illustration (= r1).

### EdgeRadius
Edge radius according the above illustration (= r2).

### LegSlope
Slope of the inner face of each leg of the profile.

## Formal Propositions

### ValidThickness
The thickness shall be smaller than the depth and width.
