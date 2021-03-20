# IfcAxis2Placement2D

The _IfcAxis2Placement2D_ provides location and orientation to place items in a two-dimensional space. The attribute _RefDirection_ defines the x axis, the y axis is derived. If the attribute _RefDirection_ is not given, the placement defaults to P[1] (x-axis) as [1.,0.] and P[2] (y-axis) as [0.,1.].

<table>
      <tr>
        <td>
          <img src="../../../../figures/ifcaxis2placement2d-layout1.gif" alt="axis2 placement 2D" width="400" height="300" border="0">
        </td>
        <td style="vertical-align:bottom">
          <blockquote class="note">
            Figure 1 illustrates the definition of the
            <em>IfcAxis2Placement2D</em> within the two-dimensional
            coordinate system.
          </blockquote>
        </td>
      </tr>
      <tr>
        <td>
          <p class="figure">Figure 1 &mdash; Axis2 placement 2D</p>
        </td>
        <td>
          &nbsp;
        </td>
      </tr>
    </table>

{ .extDef}
> NOTE&nbsp; Definition according to ISO/CD 10303-42:1992  
> The location and orientation in two dimensional space of two mutually perpendicular axes. An axis2_placement_2d is defined in terms of a point, (inherited from the placement supertype), and an axis. It can be used to locate and originate an object in two dimensional space and to define a placement coordinate system. The entity includes a point which forms the origin of the placement coordinate system. A direction vector is required to complete the definition of the placement coordinate system. The reference direction defines the placement X axis direction, the placement Y axis is derived from this.

> NOTE&nbsp; Entity adapted from **axis2_placement_2d** defined in ISO 10303-42.

> HISTORY&nbsp; New entity in IFC1.5.

## Attributes

### RefDirection
The direction used to determine the direction of the local X axis. If a value is omited that it defaults to [1.0, 0.0.].

### P
_P[1]_: The normalized direction of the placement X Axis. This is [1.0,0.0] if _RefDirection_ is omitted.  
_P[2]_: The normalized direction of the placement Y Axis. This is a derived attribute and is orthogonal to P[1]. If _RefDirection_ is omitted, it defaults to [0.0,1.0]

## Formal Propositions

### RefDirIs2D


### LocationIs2D


### LocationIsCP

