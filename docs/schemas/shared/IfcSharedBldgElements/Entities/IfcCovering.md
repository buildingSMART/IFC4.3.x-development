# IfcCovering

A covering is an element which covers some part of another element and is fully dependent on that other element. The _IfcCovering_ defines the occurrence of a covering type, that (if given) is expressed by the _IfcCoveringType_.
<!-- end of short definition -->

{ .extDef}
> NOTE Definition according to ISO ISO 6707-1: final coverings and treatments of surfaces and their intersections.

Coverings are elements with relationships to the covered element and the space on the other side, they may contain openings, assigned by _IfcRelVoidsElement_, material information, assigned by _IfcRelAssociatesMaterial_, and others.

> EXAMPLE Coverings include wall claddings, floorings, suspended ceilings, moldings and skirting boards.

> NOTE A more basic information about claddings, floorings, and ceilings of a space can be attached to _IfcSpace_'s using the _Pset_SpaceCommon_ properties. Then only a name can be provided and the covering quantities would be interpreted from the space quantities.

Coverings can be assigned to

* a space represented by _IfcSpace_
  * using the inverse relationship _CoversSpaces_ pointing to _IfcRelCoversSpaces_. The space is then accessible via _IfcRelCoversSpaces.RelatedSpace_. It defines to which space a covering is facing towards.
* a space boundary represented by _IfcRelSpaceBoundary_
  * using the inverse relationship _ProvidesBoundaries_ pointing to _IfcRelSpaceBoundary._ The space is then accessible via _IfcRelSpaceBoundary.RelatingSpace_.
* a built element represented by _IfcBuiltElement_
  * using the inverse relationship _Covers_ pointing to _IfcRelCoversBldgElements_. The building element is then accessible via _IfcRelCoversBldgElements.RelatingBuildingElement_.

> NOTE The mere containment relationship between an _IfcCovering_ and an _IfcSpace_ is created by using _IfcRelContainedInSpatialStructure_

The following guideline shall apply:

* (default) if the space has coverings that may not have their own shape representation and no defined relationships to the building elements they cover, then the _IfcCovering_ shall be assigned to _IfcSpace_ using the _IfcRelCoversSpaces_ relationship,
* if the space has coverings that have an own shape representation and the space has defined space boundaries, then the covering, which relates to that space, shall be contained in the space using _IfcRelContainedInSpatialStructure_. It may be assigned to the space boundaries using the _IfcRelSpaceBoundary_.
* if the covering does not relate to a space, then the covering should be assigned to the building element or a distribution element using the _IfcRelCoversBldgElements_ relationship.

> HISTORY New entity in IFC1.0.

{ .change-ifc2x}
> IFC2x CHANGE The attribute _PredefinedType_ is now optional and should only be inserted when no type information, given by _IfcCoveringType_, is assigned to the _IfcCovering_ occurrence by _IfcRelDefinesByType_.

## Attributes

### PredefinedType
Predefined types to define the particular type of the covering. There may be property set definitions available for each predefined type.
> NOTE The _PredefinedType_ shall only be used, if no _IfcCoveringType_ is assigned, providing its own _IfcCoveringType.PredefinedType_.

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

The following additional constraints apply to the 'SweptSolid'
representation of _IfcCovering_:


* for planar base surfaces - swept area representation
* for cylindrical base surfaces - swept area representation

![advanded solid covering](../../../../figures/ifccovering_advanced-1-layout1.gif)

Figure 227 — Covering body planar

> EXAMPLE  Figure 227 illustrates a body representation where the volume of
> _IfcCovering_ is given by an _IfcExtrudedAreaSolid_ for
> planar base surfaces (here given by the
> _IfcRelSpaceBoundary_). The extruded area (_IfcArbitraryClosedProfileDef_) shall
> be coplanar to the surface defined by the
> _IfcRelSpaceBoundary_.

![advanced solid covering](../../../../figures/ifccovering_advanced-2-layout1.gif)

Figure 228 — Covering body circular

> EXAMPLE  Figure 228 illustrates a body representation where the volume of
> the _IfcCovering_ is given by an _IfcExtrudedAreaSolid_
> for cylindrical base surfaces (here given by the
> _IfcRelSpaceBoundary_ - such as caused by a round wall).

> * The geometry representation of the _IfcCovering_ is given
> by the _IfcCompositeCurve_ (the _OuterCurve_ parameter of
> the _IfcArbitraryClosedProfileDef_ - in cases of faceted
> representation also a closed _IfcPolyline_). It is extruded
> along the plane of the base surface using the _Depth_
> parameter of the _IfcSurfaceOfLinearExtrusion_.

### Material Set

Coverings for surfaces (CEILING, FLOORING, CLADDING, CEILING, ROOFING) may have materials defined according to layers.

Coverings for edges (MOLDING, SKIRTINGBOARD) may have materials defined according to profiles.

#### Front

Optional front-facing material of layer-based coverings such as drywall paper.

#### Fill

The solid material of layer-based coverings such as drywall gypsum.

#### Back

Optional back-facing material of layer-based coverings such as drywall paper.

#### Trim

Profile of trim such as crown molding or base molding.

### Object Typing



### Property Sets for Objects



### Quantity Sets



### Spatial Containment

The _IfcCovering_ has a containment relationship within the hierarchical spatial structure.

* The _IfcCovering_ is placed within the project spatial hierarchy using the objectified relationship _IfcRelContainedInSpatialStructure_, referring to it by its inverse attribute _SELF\IfcElement.ContainedInStructure_. Subtypes of _IfcSpatialStructureElement_ are valid spatial containers, with _IfcSpace_ being the default container.

### Surface Geometry

The following additional constraints apply to the 'GeometricSet'
representation of _IfcCovering_:


* for planar base surfaces - bounded surface representation
* for cylindrical base surfaces - swept surface
representation


![standard planar covering](../../../../figures/ifccovering_standard-1-layout1.gif)

Figure 225 — Covering surface planar

> EXAMPLE  Figure 225 illustrates a planar surface representation where the
> area of _IfcCovering_ is given by an _IfcPolyLoop_ for
> planar base surfaces (here provided by the
> _IfcRelSpaceBoundary_). The implicit planar surface of the _IfcPolyLoop_ shall be
> identical with the planar surface defined by the
> _IfcRelSpaceBoundary_.




![standard cylindrical covering](../../../../figures/ifccovering_standard-2-layout1.gif)

Figure 226 — Covering surface cylindrical

> EXAMPLE  Figure 226 illustrates a cylindrical surface representation where
> the area of the _IfcCovering_ is given by an
> _IfcSurfaceOfLinearExtrusion_ for cylindrical base surfaces
> (here given by the _IfcRelSpaceBoundary_, such as caused by a
> round wall).

> * The geometry representation of the _IfcCovering_ is given
> by the _IfcTrimmedCurve_ (the _Curve_ parameter of the
> _IfcArbitraryOpenProfileDef_ - in cases of faceted
> representation also an _IfcPolyline_). It is extruded within
> the plane of the base surface using the _Depth_ parameter of
> the _IfcSurfaceOfLinearExtrusion_.
