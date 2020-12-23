# IfcOpeningElement

The opening element stands for opening, recess or chase, all reflecting voids. It represents a void within any element that has physical manifestation. Openings can be inserted into walls, slabs, beams, columns, or other elements.

The IFC specification provides two entities for opening elements:

* _IfcOpeningStandardCase_ is used for all openings that have a constant profile along a linear extrusion. They are placed relative to the voided elements and the extrusion direction is perpendicular to the plane of the element (horizontally for walls, vertically for slabs). Only a single extrusion body is allowed. It cuts through the whole thickness of the voided element, i.e. it reflects a true opening.
* _IfcOpeningElement_ is used for all other occurrences of openings and in particular also for niches or recesses.

> NOTE&nbsp; View definitions or implementer agreements may restrict the types of elements which can be voided by an _IfcOpeningElement_ or _IfcOpeningStandardCase_

There are two different types of opening elements:

* an opening, where the thickness of the opening is greater or equal to the thickness of the element;
* a recess or niche, where the thickness of the recess is smaller than the thickness of the element.

The attribute _PredefinedType_ should be used to capture the differences,

* the attribute is set to OPENING for an opening or
* the attribute is set to RECESS for a recess or niche.
* If the value for _PredefinedType_ is omitted, or the value is set to NOTDEFINED, no specific information of whether it is an opening or recess shall be assumed.

An _IfcOpeningElement_ has to be inserted into an _IfcElement_ by using the _IfcRelVoidsElement_ relationship. It may be filled by an _IfcDoor_, _IfcWindow_, or another filling element by using the relationship _IfcRelFillsElements_. Depending on the type of the _IfcShapeRepresentation_ of the _IfcOpeningElement_ the voiding relationship implies:

*  if the _IfcShapeRepresentation_.<emRepresentationIdentifier = 'Body', then the Body shape represntation of the opening has to be subtracted from the body shape representation of the voided element - implicit Boolean difference operation.
*  if the _IfcShapeRepresentation_.<emRepresentationIdentifier = 'Reference', then the Reference shape representation of the opening is not subtracted, it is provided in addition to the hole in the Body shape representation of the voided element.

The _IfcOpeningElement_ shall not participate in the containment relationship, i.e. it is not linked directly to the spatial structure of the project. It has a mandatory _VoidsElements_ inverse relationship pointing to the _IfcElement_ that is contained in the spatial structure.

* The inverse relationship _ContainedInStructure_ shall be NIL.

> NOTE&nbsp; See _IfcRelVoidsElement_ for a diagram on how to apply spatial containment and the voiding relationship.

> HISTORY&nbsp; New entity in IFC1.0

{ .change-ifc2x}
> IFC2x CHANGE&nbsp; The intermediate ABSTRACT supertypes _IfcFeatureElement_ and _IfcFeatureSubtraction_ have been added.

{ .change-ifc2x4}
> IFC4 CHANGE&nbsp; The attribute _PredefinedType_ has been added at the end of attribute list. It should be used instead of the inherited attribute _ObjectType_ from now on.

## Attributes

### PredefinedType
Predefined generic type for an opening that is specified in an enumeration. There may be a property set given specificly for the predefined types.
{ .change-ifc2x4}
> IFC4 CHANGE The attribute has been added at the end of the entity definition.

### HasFillings
Reference to the Filling Relationship that is used to assign Elements as Fillings for this Opening Element. The Opening Element can be filled with zero-to-many Elements.
