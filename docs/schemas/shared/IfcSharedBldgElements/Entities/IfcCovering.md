# IfcCovering

A covering is an element which covers some part of another element and is fully dependent on that other element. The _IfcCovering_ defines the occurrence of a covering type, that (if given) is expressed by the _IfcCoveringType_.

{ .extDef}
> NOTE  Definition according to ISO ISO 6707-1: final coverings and treatments of surfaces and their intersections.

Coverings are elements with relationships to the covered element and the space on the other side, they may contain openings, assigned by _IfcRelVoidsElement_, material information, assigned by _IfcRelAssociatesMaterial_, and others.

> EXAMPLE  Coverings include wall claddings, floorings, suspended ceilings, moldings and skirting boards.

> NOTE  A more basic information about claddings, floorings, and ceilings of a space can be attached to _IfcSpace_'s using the Pset_SpaceCommon properties. Then only a name can be provided and the covering quantities would be interpreted from the space quantities.

Coverings can be assigned to

* a space represented by _IfcSpace_
    * using the inverse relationship _CoversSpaces_ pointing to _IfcRelCoversSpaces_. The space is then accessible via _IfcRelCoversSpaces.RelatedSpace_. It defines to which space a covering is facing towards.
* a space boundary represented by _IfcRelSpaceBoundary_
    * using the inverse relationship _ProvidesBoundaries_ pointing to _IfcRelSpaceBoundary._ The space is then accessible via _IfcRelSpaceBoundary.RelatingSpace_.
* a building element represented by _IfcBuildingElement_
    * using the inverse relationship _Covers_ pointing to _IfcRelCoversBldgElements_. The building element is then accessible via _IfcRelCoversBldgElements.RelatingBuildingElement_.

> NOTE  The mere containment relationship between an _IfcCovering_ and an _IfcSpace_ is created by using _IfcRelContainedInSpatialStructure_

The following guideline shall apply:

* (default) if the space has coverings that may not have their own shape representation and no defined relationships to the building elements they cover, then the _IfcCovering_ shall be assigned to _IfcSpace_ using the _IfcRelCoversSpaces_ relationship,
* if the space has coverings that have an own shape representation and the space has defined space boundaries, then the covering, which relates to that space, shall be contained in the space using _IfcRelContainedInSpatialStructure_. It may be assigned to the space boundaries using the _IfcRelSpaceBoundary_.
* if the covering does not relate to a space, then the covering should be assigned to the building element or a distribution element using the _IfcRelCoversBldgElements_ relationship.

> HISTORY  New entity in IFC1.0.

{ .change-ifc2x}
> IFC2x CHANGE  The attribute _PredefinedType_ is now optional and should only be inserted when no type information, given by _IfcCoveringType_, is assigned to the _IfcCovering_ occurrence by _IfcRelDefinesByType_.

## Attributes

### PredefinedType
Predefined types to define the particular type of the covering. There may be property set definitions available for each predefined type.
> NOTE  The _PredefinedType_ shall only be used, if no _IfcCoveringType_ is assigned, providing its own _IfcCoveringType.PredefinedType_.

### CoversSpaces
Reference to the objectified relationship that handles the relationship of the covering to the covered space.

### CoversElements
Reference to the objectified relationship that handles the relationship of the covering to the covered element.
{ .change-ifc2x4}
> IFC4 CHANGE Renamed into _CoversElements_ for consistency.

## Formal Propositions

### CorrectPredefinedType
Either the _PredefinedType_ attribute is unset (e.g. because an _IfcCoveringType_ is associated), or the inherited attribute _ObjectType_ shall be given, if the _PredefinedType_ is set to USERDEFINED.

### CorrectTypeAssigned
Either there is no covering type object associated, i.e. the _IsTypedBy_ inverse relationship is not provided, or the associated type object has to be of type _IfcCoveringType_.

## Concepts

### Body SweptSolid Geometry

The following additional constraints apply to the 'SweptSolid' representation of IfcCovering:

* for planar base surfaces - swept area representation
* for cylindrical base surfaces - swept area representation

&nbsp;

<table>
 
<tr>
  
<td><img src="../../../../figures/ifccovering_advanced-1-layout1.gif" alt="advanded solid covering" border="0" height="274" width="399"></td>

  <td><blockquote class="example">EXAMPLE&nbsp; Figure 1 illustrates a body representation where the volume of
<em>IfcCovering</em> is given by an <em>IfcExtrudedAreaSolid</em> for
planar base surfaces (here given by the
<em>IfcRelSpaceBoundary</em>). The extruded area (<em>IfcArbitraryClosedProfileDef</em>) shall 
be coplanar to the surface defined by the
<em>IfcRelSpaceBoundary</em>.
</blockquote></td>
 </tr>

 <tr>
  
<td>
<p class="figure">Figure 1 &mdash; Covering body planar</p>
</td>

  <td>&nbsp;</td>
 </tr>

</table>

<table>
 
<tr>
  
<td><img src="../../../../figures/ifccovering_advanced-2-layout1.gif" alt="advanced solid covering" border="0" height="274" width="399"></td>

  <td><blockquote class="example">EXAMPLE&nbsp; Figure 2 illustrates a body representation where the volume of
the <em>IfcCovering</em> is given by an <em>IfcExtrudedAreaSolid</em>
for cylindrical base surfaces (here given by the
<em>IfcRelSpaceBoundary</em> - such as caused by a round wall).</blockquote>
  <blockquote>
   
<ul>
<li class="small">The geometry representation of the <em>IfcCovering</em> is given
by the <em>IfcCompositeCurve</em> (the <em>OuterCurve</em> parameter of
the <em>IfcArbitraryClosedProfileDef</em> - in cases of faceted
representation also a closed <em>IfcPolyline</em>). It is extruded
along the plane of the base surface using the <em>Depth</em>
parameter of the <em>IfcSurfaceOfLinearExtrusion</em>.</li>
</ul></blockquote>
 </td>
 </tr>
 
<tr>
  
<td>
<p class="figure">Figure 2 &mdash; Covering body circular</p>
</td>

  <td>&nbsp;</td>
 </tr>

</table>

### Material Layer Set Usage

Coverings for surfaces (CEILING, FLOORING, CLADDING, CEILING, ROOFING) may have materials defined according to layers.

#### Front

Optional front-facing material of layer-based coverings such as drywall paper.

#### Fill

The solid material of layer-based coverings such as drywall gypsum.

#### Back

Optional back-facing material of layer-based coverings such as drywall paper.

### Material Profile Set Usage

Coverings for edges (MOLDING, SKIRTINGBOARD) may have materials defined according to profiles.

#### Trim

Profile of trim such as crown molding or base molding.

### Object Typing



### Property Sets for Objects



### Quantity Sets



### Spatial Containment

The IfcCovering has a containment relationship within the hierarchical spatial structure.

* The IfcCovering is places within the project spatial hierarchy using the objectified relationship IfcRelContainedInSpatialStructure, referring to it by its inverse attribute _SELF\IfcElement.ContainedInStructure_. Subtypes of IfcSpatialStructureElement are valid spatial containers, with IfcSpace being the default container.

### Surface Geometry

The following additional constraints apply to the 'GeometricSet' representation of IfcCovering:

* for planar base surfaces - bounded surface representation
* for cylindrical base surfaces - swept surface representation

&nbsp;

<table>

 <tr>

  <td><img src="../../../../figures/ifccovering_standard-1-layout1.gif" alt="standard planar covering" border="0" height="274" width="399"></td>

  <td><blockquote class="example">EXAMPLE&nbsp; Figure 1 illustrates a planar surface representation where the
area of <em>IfcCovering</em> is given by an <em>IfcPolyLoop</em> for
planar base surfaces (here provided by the
<em>IfcRelSpaceBoundary</em>). The implicit planar surface of the <em>IfcPolyLoop</em> shall be
identical with the planar surface defined by the
<em>IfcRelSpaceBoundary</em>.</blockquote></td>
 </tr>

 <tr>

  <td>
<p class="figure">Figure 1 &mdash; Covering surface planar</p>
</td>

 </tr>

</table>

<table>

 <tr>

  <td><img src="../../../../figures/ifccovering_standard-2-layout1.gif" alt="standard cylindrical covering" border="0" height="274" width="399"></td>
  <td><blockquote class="example">EXAMPLE&nbsp; Figure 2 illustrates a cylindrical surface representation where
the area of the <em>IfcCovering</em> is given by an
<em>IfcSurfaceOfLinearExtrusion</em> for cylindrical base surfaces
(here given by the <em>IfcRelSpaceBoundary</em>, such as caused by a
round wall).</blockquote>
  <blockquote>

   <ul>
    
<li class="small">The geometry representation of the <em>IfcCovering</em> is given
by the <em>IfcTrimmedCurved</em> (the Curve parameter of the
<em>IfcArbitraryOpenProfileDef</em> - in cases of faceted
representation also an <em>IfcPolyline</em>). It is extruded within
the plane of the base surface using the <em>Depth</em> parameter of
the <em>IfcSurfaceOfLinearExtrusion</em>.</li>
</ul></blockquote>
</td>
 
</tr>
 
<tr>

  <td>
<p class="figure">Figure 2 &mdash; Covering surface
cylindrical</p>
</td>
  <td>&nbsp;</td>

</tr>

</table>

