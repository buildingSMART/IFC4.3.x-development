# IfcPropertyListValue

An _IfcPropertyListValue_ defines a property that has several (numeric or descriptive) values assigned, these values are given by an ordered list. It defines a property - list value combination for which the property _Name_, an optional _Description_, the optional _ListValues_ with measure type and optionally an _Unit_ is given. An _IfcPropertyListValue_ is a list of values. The order in which values appear is significant. All list members shall be of the same type.

The unit is handled by the _Unit_ attribute, see Table 1 for an example of a list property:

* If the _Unit_ attribute is not given, then the unit is already implied by the type of _IfcMeasureValue_ or _IfcDerivedMeasureValue_. The associated unit can be found at the _IfcUnitAssignment_ globally defined at the project level (_IfcProject.UnitsInContext_). 
* If the _Unit_ attribute is given, then the unit assigned by the _Unit_ attribute overrides the globally assigned unit. 

> NOTE&nbsp; An _IfcPropertyListValue_ may be exchanged with no values assigned yet. In this case the _ListValues_ are set to NIL.

&nbsp;

> <table>
 <tr>
  <td>
   <table class="gridtable">
    <tr valign="top">
     <th width="15%">Name</th></tr></table></td>
     <th width="30%">ListValues
     </th><th width="25%">Type<br><span style="font-size:smaller">(through <em>IfcValue</em>)</span>
     </th><th width="30%">Unit
    </th></tr>
    <tr>
     <td width="15%">ApplicableSizes</td>
     <td width="30%">1200</td>
     <td width="25%"><em>IfcPositiveLengthMeasure</em></td>
     <td width="30%">-</td>
    </tr>
    <tr>
     <td width="15%">-</td>
     <td width="30%">1600</td>
     <td width="25%"><em>IfcPositiveLengthMeasure</em></td>
     <td width="30%">-</td>
    </tr>
    <tr>
     <td width="15%">-</td>
     <td width="30%">2400</td>
     <td width="25%"><em>IfcPositiveLengthMeasure</em></td>
     <td width="30%">-</td>
    </tr>
   </table>

<tr>
  <td><p class="table">Table 1 &mdash; List property with values, measure types and units</p></td>
 </tr>

> HISTORY&nbsp; New entity in IFC2x2.

{ .change-ifc2x4}
> IFC4 CHANGE&nbsp; Attribute _ListValues_ has been made OPTIONAL with upward compatibility for file based exchange.

## Attributes

### ListValues
List of property values.
{ .change-ifc2x4}
> IFC4 CHANGE&nbsp; The attribute has been made optional with upward compatibility for file based exchange.

### Unit
Unit for the list values, if not given, the default value for the measure type (given by the TYPE of nominal value) is used as defined by the global unit assignment at IfcProject.

## WhereRules

### WR31
All values within the list of values shall be of the same measure type.
