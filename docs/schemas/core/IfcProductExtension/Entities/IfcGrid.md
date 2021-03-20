# IfcGrid

_IfcGrid_ ia a planar design grid defined in 3D space used as an aid in locating structural and design elements. The position of the grid (_ObjectPlacement_) is defined by a 3D coordinate system (and thereby the design grid can be used in plan, section or in any position relative to the world coordinate system). The position can be relative to the object placement of other products or grids. The XY plane of the 3D coordinate system is used to place the grid axes, which are 2D curves (for example, line, circle, arc, polyline).

The inherited attributes _Name_ and _Description_ can be used to define a descriptive name of the grid and to indicate the grid's purpose. A grid is defined by (normally) two, or (in case of a triangular grid) three lists of grid axes. The following figures shows some examples.

A grid may support a rectangular layout as shown in Figure 1, a radial layout as shown in Figure 2, or a triangular layout as shown in Figure 3.

> NOTE&nbsp; The _PredefinedType_ denotes the type of grid that is represented by _IfcGrid_. The instantiation of _IfcGridAxis_'s has to agree to the _PredefinedType_, if provided.

> NOTE&nbsp; The grid axes, defined within the design grid, are those elements to which project objects will be placed relatively using the _IfcGridPlacement_.

<table cellpadding="2" cellspacing="2">
      <tbody>
        <tr>
          <td width="320">
            <img src="../../../../figures/ifcdesigngrid-type1.gif" alt="1" border="0" height="211" width="306">
          </td>
          <td width="320">
            <img src="../../../../figures/ifcdesigngrid-type2.gif" alt="2" border="0" height="211" width="306">
          </td>
          <td width="320">
            <img src="../../../../figures/ifcdesigngrid-type3.gif" alt="3" border="0" height="211" width="306">
          </td>
        </tr>
        <tr>
          <td width="320">
            <p class="figure">Figure 1 &mdash; Grid rectangular layout</p>
          </td>
          <td width="320">
            <p class="figure">Figure 2 &mdash; Grid radial layout</p>
          </td>
          <td width="320">
            <p class="figure">Figure 3 &mdash; Grid triangular layout</p>
          </td>
        </tr>
      </tbody>
    </table>

> HISTORY&nbsp; New entity in IFC1.0.

{ .change-ifc2x4}
> IFC4 CHANGE&nbsp; The attribute _PredefinedType_ has been added at the end of the attribute list.

&nbsp;

{ .spec-head}
Informal Propositions:

<table summary="IP">
      <tr>
        <td width="640">
          <ol>
            <li>Grid axes, which are referenced in different lists
            of axes (UAxes, VAxes, WAxes) shall not be parallel.
            </li>
            <li>Grid axes should be defined such as there are no
            two grid axes which intersect twice (see Figure 189).
            </li>
          </ol>
          <blockquote class="note">
            NOTE&nbsp; Left side: ambiguous intersections A1 and
            A2, a grid containing such grid axes is not a valid
            design grid;&nbsp; Right side: the conflict can be
            resolved by splitting one grid axis in a way, such as
            no ambiguous intersections exist.
          </blockquote>
        </td>
        <td align="right" valign="top" width="320">
          <img src="../../../../figures/ifcdesigngrid-ip2.gif" alt="IP2" border="0" height="97" width="306">
          <p class="figure">Figure 4 &mdash; Grid intersections</p>
        </td>
      </tr>
    </table>

## Attributes

### UAxes
List of grid axes defining the first row of grid lines.

### VAxes
List of grid axes defining the second row of grid lines.

### WAxes
List of grid axes defining the third row of grid lines. It may be given in the case of a triangular grid.

### PredefinedType
Predefined types to define the particular type of the grid. 
{ .change-ifc4}
> IFC4 Change&nbsp; New attribute.
