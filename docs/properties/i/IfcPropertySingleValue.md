IfcPropertySingleValue
======================

The property with a single value _IfcPropertySingleValue_ defines a property object which has a single (numeric or descriptive) value assigned. It defines a property - single value combination for which the property _Name_, an optional _Description_, and an optional _NominalValue_ with measure type is provided. In addition, the default unit as specified within the project unit context can be overriden by assigning an _Unit_.

The unit is handled by the _Unit_ attribute, see Table 1 for an example of various single value properties:

* If the _Unit_ attribute is not given, then the unit is already implied by the type of _IfcMeasureValue_ or _IfcDerivedMeasureValue_. The associated unit can be found at the _IfcUnitAssignment_ globally defined at the project level (_IfcProject.UnitsInContext_).
* If the _Unit_ attribute is given, then the unit assigned by the _Unit_ attribute overrides the globally assigned unit.

&nbsp;

<table>
 <tr>
  <td>
   <table class="gridtable">
    <tr>
      <th width="30%"><b>Name</b></th>
      <th width="30%"><b>NominalValue</b></th>
      <th width="25%"><b>Type</b> <span style="font-size:smaller">(through <em>IfcValue</em>)</span></th>
      <th width="15%"><b>Unit</b></th>
    </tr>
    <tr>
      <td>Description</td>
      <td>Manufacturer "A" door</td>
      <td><em>IfcLabel</em></td>
      <td>-</td>
    </tr>
    <tr>
      <td>PanelThickness</td>
      <td>0.12</td>
      <td><em>IfcPositiveLengthMeasure</em></td>
      <td>-</td>
    </tr>
    <tr>
      <td>ThermalTransmittance</td>
      <td>2.6</td>
      <td><em>IfcThermalTransmittanceMeasure</em></td>
      <td>W/(m<sup>2</sup>K)</td>
    </tr>
   </table>
  </td>
 </tr>
 <tr>
  <td><p class="table">Table 1 &mdash; Single value properties with values, measure types and units</p></td>
 </tr>
</table>

> HISTORY&nbsp; New entity in IFC1.0.

{ .change-ifc2x}
> IFC2x CHANGE&nbsp; Entity has been renamed from IfcSimpleProperty.

{ .change-ifc2x3}
> IFC2x3 CHANGE&nbsp; Attribute _NominalValue_ has been made OPTIONAL with upward compatibility for file based exchange.
