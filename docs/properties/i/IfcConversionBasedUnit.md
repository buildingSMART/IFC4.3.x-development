IfcConversionBasedUnit
======================

An IfcConversionBasedUnit is used to define a unit that has a conversion rate to a base unit. To identify some commonly used conversion based units, the standard designations (case insensitive) for the _Name_ attribute are indicated in Table 1.

&nbsp;

<table>
<tr><td>
<table class="gridtable">
	<tr><th><em><b>Name</b></em></th>	<th><em><b>Description</b></em></th></tr>
	<tr><td>'inch'</td>		<td>Length measure equal to 25.4 mm</td></tr>
	<tr><td>'foot'</td>		<td>Length measure equal to 304.8 mm</td></tr>
	<tr><td>'yard'</td>		<td>Length measure equal to 914 mm</td></tr>
	<tr><td>'mile'</td>		<td>Length measure equal to 1609 m</td></tr>
	<tr><td>'square inch'</td>	<td>Area measure equal to 0.0006452 square meters</td></tr>
	<tr><td>'square foot'</td>	<td>Area measure equal to 0.09290 square meters</td></tr>
	<tr><td>'square yard'</td>	<td>Area measure equal to 0.83612736 square meters</td></tr>
	<tr><td>'acre'</td>		<td>Area measure equal to 4046.86 square meters</td></tr>
	<tr><td>'square mile'</td>	<td>Area measure equal to 2 588 881 square meters</td></tr>
	<tr><td>'cubic inch'</td>	<td>Volume measure equal to 0.00001639 cubic meters</td></tr>
	<tr><td>'cubic foot'</td>	<td>Volume measure equal to 0.02832 cubic meters</td></tr>
	<tr><td>'cubic yard'</td>	<td>Volume measure equal to 0.7636 cubic meters</td></tr>
	<tr><td>'litre'</td>		<td>Volume measure equal to 0.001 cubic meters</td></tr>
	<tr><td>'fluid ounce UK'</td>	<td>Volume measure equal to 0.0000284130625 cubic meters</td></tr>
	<tr><td>'fluid ounce US'</td>	<td>Volume measure equal to 0.00002957353 cubic meters</td></tr>
	<tr><td>'pint UK'</td>		<td>Volume measure equal to 0.000568 cubic meters</td></tr>
	<tr><td>'pint US'</td>		<td>Volume measure equal to 0.000473 cubic meters</td></tr>
	<tr><td>'gallon UK'</td>	<td>Volume measure equal to 0.004546 cubic meters</td></tr>
	<tr><td>'gallon US'</td>	<td>Volume measure equal to 0.003785 cubic meters</td></tr>
	<tr><td>'degree'</td>		<td>Angle measure equal to &pi;/180 rad</td></tr>
	<tr><td>'ounce'</td>		<td>Mass measure equal to 28.35 g</td></tr>
	<tr><td>'pound'</td>		<td>Mass measure equal to 0.454 kg</td></tr>
	<tr><td>'ton UK'</td>		<td>Mass measure equal to 1016.0469088 kg, also known as long ton, gross ton, shipper's ton</td></tr>
	<tr><td>'ton US'</td>		<td>Mass measure equal to 907.18474 kg, also known as short ton, net ton</td></tr>
	<tr><td>'lbf'</td>		<td>Force measure equal to 4.4482216153 N, pound-force</td></tr>
	<tr><td>'kip'</td>		<td>Force measure equal to 4448.2216153 N, kilopound-force</td></tr>
	<tr><td>'psi'</td>		<td>Pressure measure equal to 6894.7572932 Pa, pound-force per square inch</td></tr>
	<tr><td>'ksi'</td>		<td>Pressure measure equal to 6894757.2932 Pa, kilopound-force per square inch</td></tr>
	<tr><td>'minute'</td>		<td>Time measure equal to 60 s</td></tr>
	<tr><td>'hour'</td>		<td>Time measure equal to 3600 s</td></tr>
	<tr><td>'day'</td>		<td>Time measure equal to 86400 s</td></tr>
	<tr><td>'btu'</td>		<td>Energy measure equal to 1055.056 J, British Thermal Unit</td></tr>
</table>
</td></tr>
<tr><td><p class="table">Table 1 &mdash; Standard unit names</p></td></tr>
</table>

> EXAMPLE&nbsp; An inch is a converted unit. It is from the Imperial system, its name is "inch" and it can be related to the SI unit, millimetre, through a measure with unit whose value is 25.4 millimetre. A foot is also a converted unit. It is from the Imperial system, its name is "foot" and it can be related to an _IfcSIUnit_, millimetre, either directly or through the unit called "inch". Note that several US customary units differ from Imperial units (nonmetric English units) of the same name.

{ .extDef}
> NOTE&nbsp; Definition according to ISO/CD 10303-41:1992  
> A conversion based unit is a unit that is defined based on a measure with unit.

> NOTE&nbsp; Entity adapted from **conversion_based_unit** defined in ISO 10303-41.

> HISTORY&nbsp; New entity in IFC1.5.1.

{ .change-ifc2x3}
> IFC2x3 CHANGE&nbsp; Standard names of typical units added.

{ .change-ifc2x4}
> IFC4 CHANGE&nbsp; Further names added: square inch, square foot, square mile, square yard, cubic inch, cubic foot, cubic yard, fluid ounce UK/US, ton UK/US, degree.
