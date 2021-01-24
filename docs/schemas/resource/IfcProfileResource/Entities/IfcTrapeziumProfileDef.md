# IfcTrapeziumProfileDef

_IfcTrapeziumProfileDef_ defines a trapezium as the profile definition used by the swept surface geometry or the swept area solid. It is given by its Top X and Bottom X extent and its Y extent as well as by the offset of the Top X extend, and placed within the 2D position coordinate system, established by the _Position_ attribute. It is placed centric within the position coordinate system, that is, in the center of the bounding box.

> HISTORY&nbsp; New entity in IFC1.5. The use definition has changed in IFC2x.

Figure 1 illustrates parameters of the trapezium profile definition.

<table><tr><td>
<table frame="border" width="100%">
  <tbody>
    <tr>
      <td width="420"><img src="../../../../../../figures/ifctrapeziumprofiledef-layout1.gif" alt="trapezium profile" border="0" height="300" width="400"></td>
      <td align="left" valign="top" width="100%"><u>Position</u>
      <br>
The parameterized profile defines its own position coordinate system.
The underlying
coordinate system is defined by the swept surface or swept area solid
that uses the profile definition. It is the xy plane of either:
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
The <em>IfcTrapeziumProfileDef</em>
is defined within the position
coordinate system, where the <em>BottomDim</em>
defines the length
measure for the bottom line (half along the positive x-axis) and the <em>YDim</em>
defines the length measure for the parallel distance of bottom and top
line (half along the positive y-axis). The top line starts with a
distance of <em>TopXOffset</em>
from [-BottomLine/2,YDim] (which can be
negative, zero, or positive) and has a length of <em>TopXDim</em>
along
the positive x-axis.</p>
      </td>
    </tr>
  </tbody>
</table>
</td></tr>
<tr><td><p class="figure">Figure 1 &mdash; Trapezium profile</p></td></tr>
</table>

## Attributes

### BottomXDim
The extent of the bottom line measured along the implicit x-axis.

### TopXDim
The extent of the top line measured along the implicit x-axis.

### YDim
The extent of the distance between the parallel bottom and top lines measured along the implicit y-axis.

### TopXOffset
Offset from the beginning of the top line to the bottom line, measured along the implicit x-axis.
