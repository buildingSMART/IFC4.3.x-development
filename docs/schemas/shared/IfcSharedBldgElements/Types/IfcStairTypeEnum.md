This enumeration defines the basic configuration of the stair type in terms of the number of stair flights and the number of landings, as illustrated in Figure 1. The type also distinguished turns by windings or by landings. In addition the subdivision of the straight and changing direction stairs is included. The stair configurations are given for stairs without and with one, two or three landings.

Stairs which are subdivided into more than three landings, or stairs with non-regular shapes are to be defined with type being USERDEFINED or NOTDEFINED.

> HISTORY&nbsp; New enumeration in IFC2.0.

<table>
<tr>
<td>
<table class="gridtable">
<tr valign="top">
<th width="30%" valign="top" align="left"><i>Enumerator</i></th>
<th width="46%" valign="top" align="left"><i>Description</i></th>
<th width="23%" valign="top" align="left"><i>Figure</i></th>
</tr>
<tr valign="top">
<td width="30%" valign="top" align="left">StraightRunStair</td>
<td width="46%" valign="top" align="left"><br>
A stair extending from one level to another without turns or winders. The stair consists of one straight flight.</td>
<td width="23%" valign="top" align="left"><img src="../../../../../../figures/ifcstairtypeenum-fig01.gif" width="173" height="39" border="0"></td>
</tr>
<tr valign="top">
<td width="30%" valign="top" align="left">TwoStraightRunStair</td>
<td width="46%" valign="top" align="left"><br>
A straight stair consisting of two straight flights without turns but with one landing.</td>
<td width="23%" valign="top" align="left"><img src="../../../../../../figures/ifcstairtypeenum-fig06.gif" width="173" height="39" border="0"></td>
</tr>
<tr valign="top">
<td width="30%" valign="top" align="left">QuarterWindingStair</td>
<td width="46%" valign="top" align="left"><br>
A stair consisting of one flight with a quarter winder, which is making a 90&deg; turn. The direction of the turn is
determined by the walking line.</td>
<td width="23%" valign="top" align="left"><img src="../../../../../../figures/ifcstairtypeenum-fig02.gif" width="171" height="60" border="0"></td>
</tr>
<tr valign="top">
<td width="30%" valign="top" align="left">QuarterTurnStair</td>
<td width="46%" valign="top" align="left"><br>
A stair making a 90&deg; turn, consisting of two straight flights connected by a quarterspace landing. The direction of
the turn is determined by the walking line.</td>
<td width="23%" valign="top" align="left"><img src="../../../../../../figures/ifcstairtypeenum-fig07.gif" width="171" height="79" border="0"></td>
</tr>
<tr valign="top">
<td width="30%" valign="top" align="left">HalfWindingStair</td>
<td width="46%" valign="top" align="left"><br>
A stair consisting of one flight with one half winder, which makes a 180&deg; turn. The orientation of the turn is
determined by the walking line.</td>
<td width="23%" valign="top" align="left"><img src="../../../../../../figures/ifcstairtypeenum-fig04.gif" width="77" height="107" border="0"></td>
</tr>
<tr valign="top">
<td width="30%" valign="top" align="left">HalfTurnStair</td>
<td width="46%" valign="top" align="left">A stair making a 180&deg; turn, consisting of two straight flights connected
by a halfspace landing. The orientation of the turn is determined by the walking line.</td>
<td width="23%" valign="top" align="left"><img src="../../../../../../figures/ifcstairtypeenum-fig08.gif" width="77" height="107" border="0"></td>
</tr>
<tr valign="top">
<td width="30%" valign="top" align="left">TwoQuarterWindingStair</td>
<td width="46%" valign="top" align="left">A stair consisting of one flight with two quarter winders, which make a
90&deg; turn. The stair makes a 180&deg; turn. The direction of the turns is determined by the walking line.</td>
<td width="23%" valign="top" align="left"><img src="../../../../../../figures/ifcstairtypeenum-fig03.gif" width="171" height="60" border="0"></td>
</tr>
<tr valign="top">
<td width="30%" valign="top" align="left">TwoQuarterTurnStair</td>
<td width="46%" valign="top" align="left">A stair making a 180&deg; turn, consisting of three straight flights
connected by two quarterspace landings. The direction of the turns is determined by the walking line.</td>
<td width="23%" valign="top" align="left"><img src="../../../../../../figures/ifcstairtypeenum-fig10.gif" width="171" height="79" border="0"></td>
</tr>
<tr valign="top">
<td width="30%" valign="top" align="left">ThreeQuarterWindingStair</td>
<td width="46%" valign="top" align="left">A stair consisting of one flight with three quarter winders, which make a
90&deg; turn. The stair makes a 270&deg; turn. The direction of the turns is determined by the walking line.</td>
<td width="23%" valign="top" align="left"><img src="../../../../../../figures/ifcstairtypeenum-fig03a.gif" width="171" height="96" border="0"></td>
</tr>
<tr valign="top">
<td width="30%" valign="top" align="left">ThreeQuarterTurnStair</td>
<td width="46%" valign="top" align="left">A stair making a 270&deg; turn, consisting of four straight flights connected
by three quarterspace landings. The direction of the turns is determined by the walking line.</td>
<td width="23%" valign="top" align="left"><img src="../../../../../../figures/ifcstairtypeenum-fig10a.gif" width="171" height="115" border="0"></td>
</tr>
<tr valign="top">
<td width="30%" valign="top" align="left">SpiralStair</td>
<td width="46%" valign="top" align="left"><br>
A stair constructed with winders around a circular newel often without landings. Depending on outer boundary it can be
either a circular, elliptical or rectangular spiral stair. The orientation of the winding stairs is determined by the
walking line.</td>
<td width="23%" valign="top" align="left"><img src="../../../../../../figures/ifcstairtypeenum-fig05.gif" width="77" height="77" border="0"></td>
</tr>
<tr valign="top">
<td width="30%" valign="top" align="left">DoubleReturnStair</td>
<td width="46%" valign="top" align="left"><br>
A stair having one straight flight to a wide quarterspace landing, and two side flights from that landing into opposite
directions. The stair is making a 90&deg; turn. The direction of traffic is determined by the walking line.</td>
<td width="23%" valign="top" align="left"><img src="../../../../../../figures/ifcstairtypeenum-fig09.gif" width="171" height="79" border="0"></td>
</tr>
<tr valign="top">
<td width="30%" valign="top" align="left">CurvedRunStair</td>
<td width="46%" valign="top" align="left">A stair extending from one level to another without turns or winders. The
stair is consisting of one curved flight.</td>
<td width="23%" valign="top" align="left"><img src="../../../../../../figures/ifcstairtypeenum-fig11.gif" width="171" height="46" border="0"></td>
</tr>
<tr valign="top">
<td width="30%" valign="top" align="left">TwoCurvedRunStair</td>
<td width="46%" valign="top" align="left">A curved stair consisting of two curved flights without turns but with one
landing.</td>
<td width="23%" valign="top" align="left"><img src="../../../../../../figures/ifcstairtypeenum-fig12.gif" width="171" height="46" border="0"></td>
</tr>
<tr valign="top">
<td width="30%" valign="top" align="left">UserDefined</td>
<td width="46%" valign="top" align="left">Free form stair (user defined operation type)</td>
<td width="23%" valign="top" align="left">&nbsp;</td>
</tr>
<tr valign="top">
<td width="30%" valign="top" align="left">NotDefined</td>
<td width="46%" valign="top" align="left">&nbsp;</td>
<td width="23%" valign="top" align="left">&nbsp;</td>
</tr>
</table>
</td>
</tr>
<tr>
<td>
<p class="figure">Figure 1 &mdash; Stair types</p>
</td>
</tr>
</table>