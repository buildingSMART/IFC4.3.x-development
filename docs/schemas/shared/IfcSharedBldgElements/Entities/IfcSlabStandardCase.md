# IfcSlabStandardCase

The standard slab, _IfcSlabStandardCase_, defines a slab with certain constraints for the provision of material usage, parameters and with certain constraints for the geometric representation. The _IfcSlabStandardCase_ handles all cases of slabs, that:

* have a reference to the _IfcMaterialLayerSetUsage_ defining the material layers of the slab with thicknesses
* are based on an extrusion of a planar surface as defined by the slab profile
* have a constant thickness along the extrusion direction
* are consistent in using the correct material layer set offset to the base planar surface in regard to the shape representation
* are extruded either perpendicular or slanted to the plane surface

The definitions of slab openings and niches are the same as given at the supertype _IfcSlab_. The same agreements to the special types of slabs, as defined in the _PredefinedType_ attribute apply as well.

> NOTE  If the _IfcSlabStandardCase_ is of type Landing and is used within an _IfcStair_ or _IfcRamp_, the special agreements to handle stair and ramp geometry will also affect the geometric representation of the _IfcSlabStandardCase_.

> HISTORY  New entity in IFC4.

## Formal Propositions

### HasMaterialLayerSetusage
A valid instance of _IfcSlabStandardCase_ relies on the provision of an _IfcMaterialLayerSetUsage_.

## Concepts

### Body Clipping Geometry

The following constraints apply to the 'Clipping' representation:

* **Solid**: see 'SweptSolid' shape representation,
* **Profile**: see 'SweptSolid' shape representation,
* **Extrusion**: see 'SweptSolid' shape representation,
* **Material**: see 'SweptSolid' shape representation,
* **Boolean result**: The IfcBooleanClippingResult shall be supported, allowing for Boolean differences between the swept solid (here IfcExtrudedAreaSolid) and one or several IfcHalfSpaceSolid.



<table>

 <tr>
  <td><img src="../../../../figures/ifcslab_advanced-layout1.gif" alt="advanced slab" border="0" height="274" width="399"></td>
  <td>

<blockquote class="example">EXAMPLE  Figure 1 illustrates a 'Clipping' geometric representation with definition of a roof slab using advanced geometric representation. The profile is extruded non-perpendicular and the slab body is clipped at the eave.</blockquote>

</td>
 </tr>

 <tr>
  <td><p class="figure">Figure 1 &mdash; Slab body clipping</p></td>
  <td> </td>
 </tr>

</table>

### Body SweptSolid Geometry

The following additional constraints apply to the swept solid representation:

* **Solid**: IfcExtrudedAreaSolid is required,
* **Profile**: _IfcArbitraryClosedProfileDef, IfcRectangleProfileDef, IfcCircleProfileDef, IfcEllipseProfileDef_ shall be supported.
* **Extrusion**: The profile can be extruded perpendicularly or non-perpendicularly to the plane of the swept profile.
* **Material**: The definition of the IfcMaterialLayerSetUsage, particularly of the OffsetFromReferenceLine and the _ForLayerSet.TotalThickness_, has to be consistent to the 'SweptSolid' representation.



<table>

<tr>
  <td><img src="../../../../figures/ifcslab_standard-layout1.gif" alt="standard slab" border="0" height="274" width="399"></td>
  <td>

<blockquote class="example">EXAMPLE  Figure 1 illustrates a 'SweptSolid' geometric representation. The following interpretation of dimension parameter applies for polygonal slabs (in ground floor view):
 <em>IfcArbitraryClosedProfileDef.OuterCurve</em>: closed bounded curve interpreted as area (or foot print) of the slab.</blockquote>

</td>
 </tr>

 <tr>
  <td><p class="figure">Figure 1 &mdash; Slab body extrusion</p></td>
  <td> </td>
 </tr>

</table>

### Material Layer Set Usage

Multi-layer slabs can be represented by refering to several IfcMaterialLayer's within the IfcMaterialLayerSet that is referenced from the IfcMaterialLayerSetUsage.

Material information can also be given at the IfcSlabType, defining the common attribute data for all occurrences of the same type. It is then accessible by the inverse IsDefinedBy relationship pointing to _IfcSlabType.HasAssociations_ and via _IfcRelAssociatesMaterial.RelatingMaterial_. The IfcSlabStandardCase defines in addition that the IfcSlabType should have a unique IfcMaterialLayerSet, that is referenced by the IfcMaterialLayerSetUsage assigned to all occurrences of this IfcSlabType.



<table>

 <tr>
  <td><img src="../../../../figures/ifcslab_materialusage-01.png" alt="Material layer set and usage" height="220" width="501"></td>

<td><blockquote class="example">EXAMPLE  Figure 1 illustrates assignment of <em>IfcMaterialLayerSetUsage</em> and <em>IfcMaterialLayerSet</em> to the <em>IfcSlabStandardCase</em> as the slab occurrence and to the <em>IfcSlabType</em>. The same <em>IfcMaterialLayerSet</em> shall be shared by many occurrences of <em>IfcMaterialLayerSetUsage</em>. This relationship shall be consistent to the relationship between the <em>IfcSlabType</em> and the <em>IfcSlabStandardCase</em>.</blockquote></td>
 </tr>

<tr><td><p class="figure">Figure 1 &mdash; Slab type definition</p></td>
  <td> </td>
 </tr>

</table>

Figure 2 illustrates slab material usage, where the following conventions shall be met:

* The reference coordinate system is the coordinate system established by the _IfcExtrudedAreaSolid.Position_.
* The reference plane is the plane defined by the extruded profile of _IfcExtrudedAreaSolid.SweptSolid_. The _IfcMaterialLayerSetUsage.OffsetFromReferenceLine_ is given as a distance from this plane.
* The _IfcMaterialLayerSetUsage.DirectionSense_ defines how the IfcMaterialLayer's are assigned to the reference plane. POSITIVE means in direction to the positive z-axis of the reference coordinate system.
* The _IfcMaterialLayerSetUsage.OffsetFromReferenceLine_ is the distance parallel to the reference plane and always perpendicular to the base (XY) plane of the reference coordinate system. This is independent of a potential non-perpendicular extrusion given by _IfcExtrudedAreaSolid.ExtrudedDirection_ &lt;&gt; 0.,0.,1. A positive value of _IfcMaterialLayerSetUsage.OffsetFromReferenceLine_ would then point into the positive z-axis of the reference coordinate system.
* The Thickness of each IfcMaterialLayer shall be the parallel distance (measured perpendicular to the base plane). The TotalThickness of the IfcMaterialLayerSet is the sum of all layer thicknesses and in case of a perpendicular extrusion identical with _IfcExtrudedAreaSolid.Depth_
* The _IfcMaterialLayerSetUsage.LayerSetDirection_ is always AXIS3.

<table summary="material use definition for standard slabs">

 <tr>
  <td align="left" valign="top" width="610">
<img src="../../../../figures/ifcmateriallayersetusage_slab-01.png" alt="slab material layer set" width="601" height="321" border="0">
</td></tr>
<tr><td align="left" valign="top" width="610">
<img src="../../../../figures/ifcmateriallayersetusage_roofslab-01.png" alt="roof slab material layer set" width="600" height="400" border="0"></td></tr>
<tr><td><p class="figure">Figure 2 &mdash; Slab material layers</p></td></tr>
</table>

### Product Local Placement

The following restriction is imposed:

* The local placement shall provide the location and directions for the standard slab, the x/y plane is the plane for the profile, and the z-axis is the extrusion axis for the slab body.

