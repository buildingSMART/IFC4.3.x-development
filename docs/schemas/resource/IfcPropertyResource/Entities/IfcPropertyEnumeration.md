# IfcPropertyEnumeration

_IfcPropertyEnumeration_ is a collection of simple or measure values that define a prescribed set of alternatives from which 'enumeration values' are selected. This enables inclusion of enumeration values in property sets. _IfcPropertyEnumeration_ provides a name for the enumeration as well as a list of unique (numeric or descriptive) values (that may have a measure type assigned). The entity defines the list of potential enumerators to be exchanged together (or separately) with properties of type _IfcPropertyEnumeratedValue_ that selects their actual property values from this enumeration.

The unit is handled by the _Unit_ attribute, see Table 1 for an example of a unitless property enumeration:

* If the _Unit_ attribute is not given, than the unit is already implied by the type of _IfcMeasureValue_ or _IfcDerivedMeasureValue_. The associated unit can be found at the _IfcUnitAssignment_ globally defined at the project level (_IfcProject.UnitsInContext_).
*  If the _Unit_ attribute is given, the unit assigned by the unit attribute overrides the globally assigned unit.

&nbsp;

<table>
 <tr>
  <td>
   <table class="gridtable">
    <tr>
      <th width="30%"><b>Name</b></th>
      <th width="30%"><b>EnumerationValues</b></th>
      <th width="25%"><b>Type</b> <span style="font-size:smaller">(through <em>IfcValue</em>)</span></th>
      <th width="15%"><b>Unit</b></th>
    </tr>
    <tr>
      <td>PEnum_DamperBladeAction</td>
      <td>Parallel</td>
      <td><em>IfcLabel</em></td>
      <td>-</td>
    </tr>
    <tr>
      <td>&nbsp;</td>
      <td>Opposed</td>
      <td><em>IfcLabel</em></td>
      <td>&nbsp;</td>
    </tr>
    <tr>
      <td>&nbsp;</td>
      <td>Other</td>
      <td><em>IfcLabel</em></td>
      <td>&nbsp;</td>
    </tr>
    <tr>
      <td>&nbsp;</td>
      <td>Unset</td>
      <td><em>IfcLabel</em></td>
      <td>&nbsp;</td>
    </tr>
   </table>
  </td>
 </tr>
 <tr>
  <td><p class="table">Table 1 &mdash; Property enumeration with values, measure types and units</p></td>
 </tr>
</table>

> HISTORY&nbsp; New entity in IFC2.0, capabilities enhanced in IFC2x.

{ .change-ifc2x}
> IFC2x CHANGE&nbsp; Entity has been renamed from IfcEnumeration

## Attributes

### Name
Name of this enumeration.

### EnumerationValues
List of values that form the enumeration.

### Unit
Unit for the enumerator values, if not given, the default value for the measure type (given by the TYPE of nominal value) is used as defined by the global unit assignment at IfcProject.

## Formal Propositions

### WR01
All values within the list of _EnumerationValues_ shall be of the same measure type.

## UniqueRules

### UR1

