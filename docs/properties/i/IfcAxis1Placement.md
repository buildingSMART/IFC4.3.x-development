IfcAxis1Placement
=================

The _IfcAxis1Placement_ provides location and direction of a single axis.

<table>
 <tr>
  <td><img src="../../../../../../figures/ifcaxis1placement-layout1.gif" alt="axis1 placement" width="400" height="300" border="0">
  </td>
  <td style="vertical-align:bottom"><blockquote class="note">
   Figure 1 illustrates the definition of the <em>IfcAxis1Placement</em> within the parent three-dimensional coordinate system.
   </blockquote>
  </td>
 </tr>
 <tr>
  <td><p class="figure">Figure 1 &mdash; Axis1 placement</p>
  </td>
 </tr>
</table>

{ .extDef}
> NOTE&nbsp; Definition according to ISO/CD 10303-42:1992  
> The direction and location in three dimensional space of a single axis. An axis1_placement is defined in terms of a locating point (inherited from placement supertype) and an axis direction: this is either the direction of axis or defaults to (0.0,0.0,1.0). The actual direction for the axis placement is given by the derived attribute z.

> NOTE&nbsp; Entity adapted from **axis1_placement** defined in ISO10303-42.

> HISTORY&nbsp; New entity in IFC1.5
