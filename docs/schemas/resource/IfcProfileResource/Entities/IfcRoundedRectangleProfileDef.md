# IfcRoundedRectangleProfileDef

_IfcRoundedRectangleProfileDef_ defines a rectangle with equally rounded corners as the profile definition used by the swept surface geometry or the swept area solid. It is given by the X extent, the Y extent, and the radius for the rounded corners, and placed within the 2D position coordinate system, established by the _Position_ attribute. It is placed centric within the position coordinate system, that is, in the center of the bounding box.

> HISTORY&nbsp; New entity in IFC2x.

{ .change-ifc2x}
> IFC2x CHANGE&nbsp; The _IfcRoundedRectangleProfileDef_ is now subtyped from _IfcRectangleProfileDef_. The _XDim_ and _YDim_ attributes have been removed (now inherited from supertype).

Figure 1 illustrates parameters of the rounded rectangle profile definition.

<table><tr><td>
<table frame="border" width="100%">
  <tbody>
    <tr>
      <td width="420"><img src="../../../../figures/ifcroundedrectangleprofiledef-layout1.gif" alt="rounded rectangle profile" border="0" height="300" width="400"></td>
      <td align="left" valign="top" width="100%">
      <p><u>Position</u>
      <br>
The parameterized profile defines its own position coordinate system.
The underlying
coordinate system is defined by the swept surface or swept area solid
that uses the profile definition. It is the xy plane of either: </p>
      <ul>
        <li style="font-style: italic;">IfcSweptSurface.Position</li>
        <li style="font-style: italic;">IfcSweptAreaSolid.Position</li>
      </ul>
or in case of sectioned spines the xy plane of each list member of <span style="font-style: italic;">IfcSectionedSpine.CrossSectionPositions.</span>
      <br>
      <br>
By using offsets of the position location, the parameterized profile
can be positioned centric (using x,y offsets = 0.), or at any position
relative to the profile. Explicit coordinate offsets are used to define
cardinal points (e.g. upper-left bound).
      <p><u>Parameter</u>
      <br>
The <em>IfcRoundedRectangleProfileDef</em>
is defined within the
position coordinate system, where the <em>XDim</em>
defines the measure
for the length of the rectangle (half along the positive x-axis), the <em>YDim</em>
defines the length measure for the width of the rectangle (half along
the positive y-axis) and the <em>RoundingRadius</em>
defines the radius
of curvature in all four corners of the rectangle.</p>
      </td>
    </tr>
  </tbody>
</table>
</td></tr>
<tr><td><p class="figure">Figure 1 &mdash; Rounded rectangle profile</p></td></tr>
</table>

## Attributes

### RoundingRadius
Radius of the circular arcs by which all four corners of the rectangle are equally rounded.

## WhereRules

### ValidRadius
The value of the attribute RoundingRadius shall be lower or equal than either of both, half the value of the Xdim and the YDim attribute.
