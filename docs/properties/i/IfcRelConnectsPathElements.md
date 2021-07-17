IfcRelConnectsPathElements
==========================

The _IfcRelConnectsPathElements_ relationship provides the connectivity information between two elements, which have path information.

The objectified relationship provides the additional information required to describe the connection between two path based elements that might have single or multiple layers of material. The connection type specifies where at the path based element a connection is given (at the start, in the middle or at the end).

The connection is described by a connection geometry, given within the object coordinate systems of the _RelatingElement_ and of the _RelatedElement_. In case of _IfcWallStandardCase_ as the _RelatingElement_ and _RelatedElement_ the connection geometry is provided by the subtype _IfcConnectionCurveGeometry_. Both curves indicate the so called "end cap", i.e. the curve that trims the wall outer edges (being parallel along the wall axis) at the end.

<table cellpadding="2" cellspacing="2">
 <tr valign="top">
  <td valign="top" align="left" width="410"><img src="../../../../../../figures/ifcrelconnectspathelements-fig1.png" alt="wall connection" width="400" height="300" border="0">
  </td>
  <td>Figure 1 shows the application of <em>IfcRelConnectsPathElements</em> with the <em>ConnectionGeometry</em> of type  <em>IfcConnectionCurveGeometry</em>. The example shows the connection relationship between two instances of <em>IfcWallStandardCase</em> using the
 <em>IfcRelConnectsPathElements</em> relationship. The <em>ConnectionCurveGeometry</em> defines the <em>CurveOnReleatingElement</em> and
 <em>CurveOnRelatedElement</em>, both are of type <em>IfcPolyline</em>.</td>
 </tr>
 <tr>
  <td>
   <p class="figure">Figure 1 &mdash; Path connection geometry</p>
  </td>
  <td>
  </td>
 </tr>
</table>

<table cellpadding="2" cellspacing="2">
 <tr valign="top">
  <td valign="top" align="left" width="410"><img src="../../../../../../figures/ifcrelconnectspathelements-fig3.png" alt="wall connection" width="400" height="260" border="0">
  </td>
  <td valign="top" align="left">&nbsp;<img src="../../../../../../figures/ifcrelconnectspathelements-fig2.png" alt="wall connection" width="320" height="200" border="0">
  </td>
 </tr>
 <tr valign="top">
  <td valign="top" align="left" width="410">
   <p class="figure">Figure 2 &mdash; Path connection T-Type</p>
  </td>
  <td valign="top" align="left" width="400">
   <p class="figure">Figure 3 &mdash; Path connection L-Type</p>
  </td>
 </tr>
 <tr valign="top">
  <td valign="top" align="left" width="410">
   <p>Figure 2 illustrates using the <em>IfcRelConnectsPathElements</em> for a "T" type connection between two instances of <em>IfcWallStandardCase</em>.</p>
  </td>
  <td valign="top" align="left" width="400">
   <p>Figure 3 illustrates using the <em>IfcRelConnectsPathElements</em> for a "L" type connection between two instances of <em>IfcWallStandardCase</em>.</p>
  </td>
 </tr> 
</table>

> NOTE&nbsp; The two wall axes connect in each case.

&nbsp;

> HISTORY&nbsp; New entity in IFC1.5.

{ .change-ifc2x4}
> IFC4 CHANGE&nbsp; The data type of _RelatingPriorities_ and _RelatedPriorities_ are restricted to a range o [0..100] to be a normalized ratio measure.
