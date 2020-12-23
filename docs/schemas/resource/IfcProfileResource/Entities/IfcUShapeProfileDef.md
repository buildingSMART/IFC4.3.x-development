# IfcUShapeProfileDef

_IfcUShapeProfileDef_ defines a section profile that provides the defining parameters of a U-shape (channel) section to be used by the swept area solid. Its parameters and orientation relative to the position coordinate system are according to the following illustration. The centre of the position coordinate system is in the profile's centre of the bounding box.

> HISTORY&nbsp; New entity in IFC2x2.

{ .change-ifc2x3}
> IFC2x3 CHANGE&nbsp; All profile origins are now in the center of the bounding box.

{ .change-ifc2x4}
> IFC4 CHANGE&nbsp; Type of _FilletRadius_ and _EdgeRadius_ relaxed to allow for zero radius. Trailing attribute _CentreOfGravityInX_ deleted, use respective property in _IfcExtendedProfileProperties_ instead.

Figure 1 illustrates parameters of the U-shape profile definition.

<table><tr><td>
<table border="1" cellpadding="2" cellspacing="2" width="100%">
  <tbody>
    <tr>
      <td valign="top" width="420">

<img src="../../../../../../figures/ifcushapeprofiledef.gif" alt="U-shape profile" border="0" height="300" width="400">

      </td>
      <td valign="top">

<p><u>Position</u> <br>
The parameterized profile defines its own position coordinate system.
The underlying coordinate system is defined by the swept area solid
that uses the profile definition. It is the xy plane of:</p>
      <ul>
        <li><em>IfcSweptAreaSolid.Position</em></li>
      </ul>
<p>By using offsets of the position location, the parameterized profile
can be positioned centric (using x,y offsets = 0.), or at any position
relative to the profile.</p>

      </td>
    </tr>
  </tbody>
</table>
</td></tr>
<tr><td><p class="figure">Figure 1 &mdash; U-shape profile</p></td></tr>
</table>

## Attributes

### Depth
Web lengths, see illustration above (= h).

### FlangeWidth
Flange lengths, see illustration above (= b).

### WebThickness
Constant wall thickness of web (= ts).

### FlangeThickness
Constant wall thickness of flange (= tg).

### FilletRadius
Fillet radius according the above illustration (= r1).

### EdgeRadius
Edge radius according the above illustration (= r2).

### FlangeSlope
Slope of flange of the profile.

## WhereRules

### ValidFlangeThickness
The flange thickness shall be smaller than half of the depth.

### ValidWebThickness
The web thickness shall be smaller than the flange width.
