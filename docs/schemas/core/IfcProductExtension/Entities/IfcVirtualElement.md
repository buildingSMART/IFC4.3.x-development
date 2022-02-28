# IfcVirtualElement

A virtual element is a special element used to provide imaginary boundaries, such as between two adjacent, but not separated, spaces. Virtual elements are usually not displayed and does not have quantities and other measures. Therefore _IfcVirtualElement_ does not have material information and quantities attached.

> NOTE  The main purpose of _IfcVirtualElement_ is the provision of a virtual space boundary. The _IfcVirtualElement_ may provide the 2D curve or 3D surface representation of the virtual space connection and is referenced by two instances of _IfcRelSpaceBoundary_, each pointing to one of the two adjacent _IfcSpaces_.

The _IfcVirtualElement_ is mainly used to define a virtual boundary between two spaces. Figure 1 describes how to use _IfcRelSpaceBoundary_ in conjunction with _IfcVirtualElement_ to define space boundaries.

![space boundary](../../../../figures/ifcvirtualelement_spaceboundaries.png "Figure 1 &mdash; Virtual element space boundaries")

> HISTORY  New entity in IFC2x2 Addendum.

{ .change-ifc2x3}
> IFC2x2 CHANGE  The entity _IfcVirtualElement_ has been added. Upward compatibility for file based exchange is guaranteed.

## Concepts

### FootPrint Geometry



### Surface Geometry

The 3D geometric representation of IfcVirtualElement is d efined using a surface geometry. The following constraints apply to the 3D surface representation:

<ul>
 
<li>'Surface3D': <em>IfcSurfaceOfLinearExtrusion</em>,
<em>IfcCurveBoundedPlane</em>, <em>IfcCurveBoundedSurface</em>,
<em>IfcRectangularTrimmedSurface</em></li>

 <li style="list-style-type: none;"><small>in case of an
<em>IfcSurfaceOfLinearExtrusion</em></small>

  <ul>
   
<li><small><u>Profile</u>:
<em>IfcArbitraryOpenProfileDef</em></small></li>
   
<li><small><u>Extrusion</u>: The extrusion direction shall be
vertically, i.e., along the positive Z Axis of the co-ordinate
system of the containing spatial structure element.</small></li>
  
</ul>

 </li>

 <li style="list-style-type: none;"><small>in case of an
<em>IfcCurveBoundedPlane</em>, <em>IfcCurveBoundedSurface</em>,
<em>IfcRectangularTrimmedSurface</em></small>
  
<ul>
   
<li><small><u>Extrusion</u>: The <em>BasisSurface</em> shall be a
surface that is upright, i.e. standing perpendicular to the xy
place of the co-ordinate system of the containing spatial
structure element.</small></li>

   </ul>

 </li>
 
<li>'GeometricSet': a list of 3D surfaces within the constraints
shown above.</li>

</ul>

