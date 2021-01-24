# IfcZShapeProfileDef

_IfcZShapeProfileDef_ defines a section profile that provides the defining parameters of a Z-shape section to be used by the swept area solid. Its parameters and orientation relative to the position coordinate system are according to the following illustration. The centre of the position coordinate system is in the profile's centre of the bounding box.

> HISTORY&nbsp; New entity in IFC2x2.

{ .change-ifc2x4}
> IFC4 CHANGE&nbsp; Type of _FilletRadius_ and _EdgeRadius_ relaxed to allow for zero radius.

Figure 1 illustrates parameters of the Z-shape profile definition.

<table><tr><td>
<table border="1" cellpadding="2" cellspacing="2" width="100%">
  <tbody>
    <tr>
      <td width="420">
<img src="../../../../../../figures/ifczshapeprofiledef.gif" alt="Z-shape profile" border="0" height="300" width="400">

      </td>
      <td valign="top">

<p><u>Position</u><br>
The parameterized profile defines its own position coordinate system.
The underlying coordinate system is defined by the swept area solid
that uses the profile definition. It is the xy plane of:</p>
      <ul>
        <li style="font-style: italic;">IfcSweptAreaSolid.Position</li>
      </ul>
<p>By using offsets of the position location, the parameterized profile
can be positioned centric (using x,y offsets = 0.), or at any position
relative to the profile.</p>

      </td>
    </tr>
  </tbody>
</table>
</td></tr>
<tr><td><p class="figure">Figure 1 &mdash; Z-shape profile</p></td></tr>
</table>

## Attributes

### Depth
Web length, see illustration above (= h).

### FlangeWidth
Flange length, see illustration above (= b).

### WebThickness
Constant wall thickness of web, see illustration above (= ts).

### FlangeThickness
Constant wall thickness of flange, see illustration above (= tg).

### FilletRadius
Fillet radius according the above illustration (= r1).

### EdgeRadius
Edge radius according the above illustration (= r2).

## Formal Propositions

### ValidFlangeThickness
The flange thickness shall be smaller than half of the depth.
