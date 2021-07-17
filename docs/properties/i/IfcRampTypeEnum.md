IfcRampTypeEnum
===============

This enumeration defines the basic configuration of the ramp type in terms of the number and shape of ramp flights, as shown in Figure 1. The type also distinguished turns by landings. In addition the subdivision of the straight and changing direction ramps is included. The ramp configurations are given for ramps without and with one and two landings.

Ramps which are subdivided into more than two landings, or ramps with non-regular shapes are to be defined with type being USERDEFINED or NOTDEFINED.

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
<td width="30%" valign="top" align="left">StraightRunRamp</td>
<td width="46%" valign="top" align="left">A ramp - which is a sloping floor, walk, or roadway - connecting two levels.
The straight ramp consists of one straight flight without turns or winders.</td>
<td width="23%" valign="top" align="left"><img src="../../../../../../figures/ifcramptypeenum-fig01.gif" width="171" height="39" border="0"></td>
</tr>
<tr valign="top">
<td width="30%" valign="top" align="left">TwoStraightRunRamp</td>
<td width="46%" valign="top" align="left">A straight ramp consisting of two straight flights without turns but with one
landing.</td>
<td width="23%" valign="top" align="left"><img src="../../../../../../figures/ifcramptypeenum-fig02.gif" width="171" height="39" border="0"></td>
</tr>
<tr valign="top">
<td width="30%" valign="top" align="left">QuarterTurnRamp</td>
<td width="46%" valign="top" align="left">A ramp making a 90&deg; turn, consisting of two straight flights connected by
a quarterspace landing. The direction of the turn is determined by the walking line.</td>
<td width="23%" valign="top" align="left"><img src="../../../../../../figures/ifcramptypeenum-fig03.gif" width="171" height="77" border="0"></td>
</tr>
<tr valign="top">
<td width="30%" valign="top" align="left">TwoQuarterTurnRamp</td>
<td width="46%" valign="top" align="left">A ramp making a 180&deg; turn, consisting of three straight flights connected
by two quarterspace landings. The direction of the turn is determined by the walking line.</td>
<td width="23%" valign="top" align="left"><img src="../../../../../../figures/ifcramptypeenum-fig04.gif" width="171" height="77" border="0"></td>
</tr>
<tr valign="top">
<td width="30%" valign="top" align="left">HalfTurnRamp</td>
<td width="46%" valign="top" align="left">A ramp making a 180&deg; turn, consisting of two straight flights connected
by a halfspace landing. The orientation of the turn is determined by the walking line.</td>
<td width="23%" valign="top" align="left"><img src="../../../../../../figures/ifcramptypeenum-fig05.gif" width="171" height="78" border="0"></td>
</tr>
<tr valign="top">
<td width="30%" valign="top" align="left">SpiralRamp</td>
<td width="46%" valign="top" align="left">A ramp constructed around a circular or elliptical well without newels and
landings.</td>
<td width="23%" valign="top" align="left"><img src="../../../../../../figures/ifcramptypeenum-fig06.gif" width="171" height="171" border="0"></td>
</tr>
<tr valign="top">
<td width="30%" valign="top" align="left">UserDefined</td>
<td width="46%" valign="top" align="left">Free form ramp (user defined operation type)</td>
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
<p class="figure">Figure 1 &mdash; Ramp types</p>
</td>
</tr>
</table>
