IfcLogicalOperatorEnum
======================

_IfcLogicalOperatorEnum_ is an enumeration that defines the logical operators that may be applied for the satisfaction of one or more operands (_IfcConstraint_) at a time.

Table 1 illustrates application of _IfcLogicalOperatorEnum_ in a case of three operands, A, B and C, for each operator.

<table><tr><td>

<table border="1" cellspacing="0" cellpadding="0">
<th align="left" colspan="9">LOGICALAND(A,B,C)</th>
<tr>
<td><b>A</b></td>
<td align="center">F</td>
<td align="center">F</td>
<td align="center">F</td>
<td align="center">T</td>
<td align="center">F</td>
<td align="center">T</td>
<td align="center">T</td>
<td align="center">T</td>
</tr>
<tr>
<td><b>B</b></td>
<td align="center">F</td>
<td align="center">F</td>
<td align="center">T</td>
<td align="center">F</td>
<td align="center">T</td>
<td align="center">F</td>
<td align="center">T</td>
<td align="center">T</td>
</tr><tr>
<td><b>C</b></td>
<td align="center">F</td>
<td align="center">T</td>
<td align="center">F</td>
<td align="center">F</td>
<td align="center">T</td>
<td align="center">T</td>
<td align="center">F</td>
<td align="center">T</td>
</tr>
<tr>
<td><b>RESULT</b></td>
<td align="center">F</td>
<td align="center">F</td>
<td align="center">F</td>
<td align="center">F</td>
<td align="center">F</td>
<td align="center">F</td>
<td align="center">F</td>
<td align="center">T</td>
</tr>
<th align="left" colspan="9">LOGICALOR(A,B,C)</th>
<tr>
<td><b>A</b></td>
<td align="center">F</td>
<td align="center">F</td>
<td align="center">F</td>
<td align="center">T</td>
<td align="center">F</td>
<td align="center">T</td>
<td align="center">T</td>
<td align="center">T</td>
</tr>
<tr>
<td><b>B</b></td>
<td align="center">F</td>
<td align="center">F</td>
<td align="center">T</td>
<td align="center">F</td>
<td align="center">T</td>
<td align="center">F</td>
<td align="center">T</td>
<td align="center">T</td>
</tr><tr>
<td><b>C</b></td>
<td align="center">F</td>
<td align="center">T</td>
<td align="center">F</td>
<td align="center">F</td>
<td align="center">T</td>
<td align="center">T</td>
<td align="center">F</td>
<td align="center">T</td>
</tr>
<tr>
<td><b>RESULT</b></td>
<td align="center">F</td>
<td align="center">T</td>
<td align="center">T</td>
<td align="center">T</td>
<td align="center">T</td>
<td align="center">T</td>
<td align="center">T</td>
<td align="center">T</td>
</tr>
<th align="left" colspan="9">LOGICALXOR(A,B,C)</th>
<tr>
<td><b>A</b></td>
<td align="center">F</td>
<td align="center">F</td>
<td align="center">F</td>
<td align="center">T</td>
<td align="center">F</td>
<td align="center">T</td>
<td align="center">T</td>
<td align="center">T</td>
</tr>
<tr>
<td><b>B</b></td>
<td align="center">F</td>
<td align="center">F</td>
<td align="center">T</td>
<td align="center">F</td>
<td align="center">T</td>
<td align="center">F</td>
<td align="center">T</td>
<td align="center">T</td>
</tr><tr>
<td><b>C</b></td>
<td align="center">F</td>
<td align="center">T</td>
<td align="center">F</td>
<td align="center">F</td>
<td align="center">T</td>
<td align="center">T</td>
<td align="center">F</td>
<td align="center">T</td>
</tr>
<tr>
<td><b>RESULT</b></td>
<td align="center">F</td>
<td align="center">T</td>
<td align="center">T</td>
<td align="center">T</td>
<td align="center">F</td>
<td align="center">F</td>
<td align="center">F</td>
<td align="center">F</td>
</tr>
<th align="left" colspan="9">LOGICALNOTAND(A,B,C)</th>
<tr>
<td><b>A</b></td>
<td align="center">F</td>
<td align="center">F</td>
<td align="center">F</td>
<td align="center">T</td>
<td align="center">F</td>
<td align="center">T</td>
<td align="center">T</td>
<td align="center">T</td>
</tr>
<tr>
<td><b>B</b></td>
<td align="center">F</td>
<td align="center">F</td>
<td align="center">T</td>
<td align="center">F</td>
<td align="center">T</td>
<td align="center">F</td>
<td align="center">T</td>
<td align="center">T</td>
</tr><tr>
<td><b>C</b></td>
<td align="center">F</td>
<td align="center">T</td>
<td align="center">F</td>
<td align="center">F</td>
<td align="center">T</td>
<td align="center">T</td>
<td align="center">F</td>
<td align="center">T</td>
</tr>
<tr>
<td><b>RESULT</b></td>
<td align="center">T</td>
<td align="center">T</td>
<td align="center">T</td>
<td align="center">T</td>
<td align="center">T</td>
<td align="center">T</td>
<td align="center">T</td>
<td align="center">F</td>
</tr>
<th align="left" colspan="9">LOGICALNOTOR(A,B,C)</th>
<tr>
<td><b>A</b></td>
<td align="center">F</td>
<td align="center">F</td>
<td align="center">F</td>
<td align="center">T</td>
<td align="center">F</td>
<td align="center">T</td>
<td align="center">T</td>
<td align="center">T</td>
</tr>
<tr>
<td><b>B</b></td>
<td align="center">F</td>
<td align="center">F</td>
<td align="center">T</td>
<td align="center">F</td>
<td align="center">T</td>
<td align="center">F</td>
<td align="center">T</td>
<td align="center">T</td>
</tr><tr>
<td><b>C</b></td>
<td align="center">F</td>
<td align="center">T</td>
<td align="center">F</td>
<td align="center">F</td>
<td align="center">T</td>
<td align="center">T</td>
<td align="center">F</td>
<td align="center">T</td>
</tr>
<tr>
<td><b>RESULT</b></td>
<td align="center">T</td>
<td align="center">F</td>
<td align="center">F</td>
<td align="center">F</td>
<td align="center">F</td>
<td align="center">F</td>
<td align="center">F</td>
<td align="center">F</td>
</tr>
</table>

</td></tr>
<tr><td><p class="table">Table 1 &mdash; Logical operators</p></td></tr>
</table>

> HISTORY&nbsp; New enumeration in IFC2.0.

{ .change-ifc2x4}
> IFC4 CHANGE&nbsp; Extended to include LOGICALXOR, LOGICALNOTAND and LOGICALNOTOR.
