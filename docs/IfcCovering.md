IfcCovering
===========
A covering is an element which covers some part of another element and is
fully dependent on that other element. The _IfcCovering_ defines the
occurrence of a covering type, that (if given) is expressed by the
_IfcCoveringType_.  
  
{ .extDef}  
> NOTE  Definition according to ISO ISO 6707-1: final coverings and treatments
> of surfaces and their intersections.  
  
Coverings are elements with relationships to the covered element and the space
on the other side, they may contain openings, assigned by
_IfcRelVoidsElement_, material information, assigned by
_IfcRelAssociatesMaterial_, and others.  
  
> EXAMPLE  Coverings include wall claddings, floorings, suspended ceilings,
> moldings and skirting boards.  
  
> NOTE  A more basic information about claddings, floorings, and ceilings of a
> space can be attached to _IfcSpace_''s using the Pset_SpaceCommon
> properties. Then only a name can be provided and the covering quantities
> would be interpreted from the space quantities.  
  
Coverings can be assigned to  
  
* a space represented by _IfcSpace_   
* using the inverse relationship _CoversSpaces_ pointing to _IfcRelCoversSpaces_. The space is then accessible via _IfcRelCoversSpaces.RelatedSpace_. It defines to which space a covering is facing towards.   
* a space boundary represented by _IfcRelSpaceBoundary_   
* using the inverse relationship _ProvidesBoundaries_ pointing to _IfcRelSpaceBoundary._ The space is then accessible via _IfcRelSpaceBoundary.RelatingSpace_.   
* a building element represented by _IfcBuildingElement_   
* using the inverse relationship _Covers_ pointing to _IfcRelCoversBldgElements_. The building element is then accessible via _IfcRelCoversBldgElements.RelatingBuildingElement_.   
  
> NOTE  The mere containment relationship between an _IfcCovering_ and an
> _IfcSpace_ is created by using _IfcRelContainedInSpatialStructure_  
  
The following guideline shall apply:  
  
* (default) if the space has coverings that may not have their own shape representation and no defined relationships to the building elements they cover, then the _IfcCovering_ shall be assigned to _IfcSpace_ using the _IfcRelCoversSpaces_ relationship,  
* if the space has coverings that have an own shape representation and the space has defined space boundaries, then the covering, which relates to that space, shall be contained in the space using _IfcRelContainedInSpatialStructure_. It may be assigned to the space boundaries using the _IfcRelSpaceBoundary_.  
* if the covering does not relate to a space, then the covering should be assigned to the building element or a distribution element using the _IfcRelCoversBldgElements_ relationship.  
  
> HISTORY  New entity in IFC1.0.  
  
{ .change-ifc2x}  
> IFC2x CHANGE  The attribute _PredefinedType_ is now optional and should only
> be inserted when no type information, given by _IfcCoveringType_, is
> assigned to the _IfcCovering_ occurrence by _IfcRelDefinesByType_.  
[ _bSI
Documentation_](https://standards.buildingsmart.org/IFC/DEV/IFC4_2/FINAL/HTML/schema/ifcsharedbldgelements/lexical/ifccovering.htm)


