# IfcDraughtingPreDefinedColour

The draughting pre defined colour is a pre defined colour for the purpose to identify a colour by name. Allowable names are:

* 'black',
* 'red',
* 'green',
* 'blue',
* 'yellow',
* 'magenta',
* 'cyan',
* 'white',
* 'by layer'

> NOTE&nbsp; The _IfcDraughtingPreDefinedColour_ is an entity that had been adopted from ISO 10303-202, Industrial automation systems and integration&mdash;Product data representation and exchange, Part 202: Application protocol: Associative draughting.

The following table states the RGB values associated with the names given by the _IfcDraughtingPreDefinedColour._

> <table>
<tbody>
<tr>
<td><b>Colour name</b></td>
<td align="center"><b>Red</b></td>
<td align="center"><b>Green</b></td>
<td align="center"><b>Blue</b></td>
</tr>
<tr>
<td>black</td>
<td align="center">0</td>
<td align="center">0</td>
<td align="center">0</td>
</tr>
<tr>
<td>red</td>
<td align="center">1.0</td>
<td align="center">0</td>
<td align="center">0</td>
</tr>
<tr>
<td>green</td>
<td align="center">0</td>
<td align="center">1.0</td>
<td align="center">0</td>
</tr>
<tr>
<td>blue</td>
<td align="center">0</td>
<td align="center">0</td>
<td align="center">1.0</td>
</tr>
<tr>
<td>yellow</td>
<td align="center">1.0</td>
<td align="center">1.0</td>
<td align="center">0</td>
</tr>
<tr>
<td>magenta</td>
<td align="center">1.0</td>
<td align="center">0</td>
<td align="center">1.0</td>
</tr>
<tr>
<td>cyan</td>
<td align="center">0</td>
<td align="center">1.0</td>
<td align="center">1.0</td>
</tr>
<tr>
<td>white</td>
<td align="center">1.0</td>
<td align="center">1.0</td>
<td align="center">1.0</td>
</tr>
<tr valign="top">
<td>by layer</td>
<td align="left" colspan="3">colour values obtained from<br>
<em>IfcPresentationLayerWithStyle</em>.</td>
<td></td>
<td></td>
</tr>
</tbody>
</table>

> NOTE&nbsp; Corresponding ISO 10303 name: draughting_pre_defined_colour. Please refer to ISO/IS 10303-202:1994 page 194 for the final definition of the formal standard.

> HISTORY&nbsp; New entity in IFC2x2.

{ .spec-head}
Informal Propositions:

1. The value 'by layer' shall only be inserted, if the geometric representation item using the colour definition has an association to _IfcPresentationLayerWithStyle_, and if that instance of _IfcPresentationLayerWithStyle_ has a valid colour definition for _IfcCurveStyle_, _IfcSymbolStyle_, or _IfcSurfaceStyle_ (depending on what is applicable).

## Formal Propositions

### PreDefinedColourNames
The inherited name for pre defined items shall only have the value of one of the following words.
