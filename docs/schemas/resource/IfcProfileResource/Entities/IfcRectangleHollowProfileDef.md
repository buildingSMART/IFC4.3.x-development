# IfcRectangleHollowProfileDef

_IfcRectangleHollowProfileDef_ defines a section profile that provides the defining parameters of a rectangular (or square) hollow section to be used by the swept surface geometry or the swept area solid. Its parameters and orientation relative to the position coordinate system are according to the following illustration. A square hollow section can be defined by equal values for h and b. The centre of the position coordinate system is in the profiles centre of the bounding box (for symmetric profiles identical with the centre of gravity). Normally, the longer sides are parallel to the y-axis, the shorter sides parallel to the x-axis.

> HISTORY&nbsp; New entity in IFC2x2.

{ .change-ifc2x4}
> IFC4 CHANGE&nbsp; Types of _InnerFilletRadius_ and _OuterFilletRadius_ relaxed to allow for zero values.

Figure 1 illustrates parameters of a rectangular or square hollow profile definition.

<table><tr><td>
<table style="text-align: left; width: 100%;" border="1" cellpadding="2" cellspacing="2">
  <tbody>
    <tr>
      <td style="vertical-align: top; text-align: left; width: 420px;">

<img src="../../../../../../figures/ifcrectanglehollowprofiledef.gif" alt="hollow rectange shape profile" border="0" height="300" width="400">

      </td>
      <td style="vertical-align: top; text-align: left;">

<p><u>Position</u><br>
The parameterized profile defines its own position coordinate system.
The underlying coordinate system is defined by the swept area solid
that uses the profile definition. It is the xy plane of:</p>
      <ul>
        <li style="font-style: italic;">IfcSweptAreaSolid.Position</li>
      </ul>
<p>by using offsets of the position location, the parameterized profile
can be positioned centric (using x,y offsets = 0.), or at any position
relative to the profile.</p>

      </td>
    </tr>
  </tbody>
</table>
</td></tr>
<tr><td><p class="figure">Figure 1 &mdash; Rectangle hollow profile</p></td></tr>
</table>

## Attributes

### WallThickness
Thickness of the material.

### InnerFilletRadius
Inner corner radius.

### OuterFilletRadius
Outer corner radius.

## Formal Propositions

### ValidWallThickness
The wall thickness shall be smaller than half of the X and Y dimension of the rectangle.

### ValidInnerRadius
The inner fillet radius (if given) shall be small enough to fit into the void.

### ValidOuterRadius
The outer fillet radius (if given) shall be small enough to fit into the bounding box.
