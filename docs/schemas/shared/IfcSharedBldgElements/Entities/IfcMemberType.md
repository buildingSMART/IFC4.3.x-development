# IfcMemberType

The element type _IfcMemberType_ defines commonly shared information for occurrences of members. Members are predominately linear building elements, often forming part of a structural system. The orientation of the member (being horizontal, vertical or sloped) is not relevant to its definition (in contrary to beam and column). The set of shared information may include:

* common properties within shared property sets
* common material information
* common profile definitions
* common shape representations

<!-- end of short definition -->

It is used to define a member specification, or member style (the specific product information that is common to all occurrences of that member type). Member types may be exchanged without being already assigned to occurrences.

Occurrences of the _IfcMemberType_ within building models are represented by instances of _IfcMember_. Occurrences of the _IfcMemberType_ within structural analysis models are represented by instances of _IfcStructuralCurveMember_, or its applicable subtypes.

> HISTORY New entity in IFC2x2 Addendum 1.

## Attributes

### PredefinedType
Identifies the predefined types of a linear structural member element from which the type required may be set.

## Formal Propositions

### CorrectPredefinedType
The inherited attribute _ElementType_ shall be provided, if the _PredefinedType_ is set to USERDEFINED.

## Concepts

### Material Profile Set
The material of the _IfcMemberType_ is defined by the
_IfcMaterialProfileSet_ or as fall back by
_IfcMaterial_ and attached by the
_IfcRelAssociatesMaterial.RelatingMaterial_. It is
accessible by the inverse _HasAssociations_
relationship.

The shared profile definition is defined by assigning an
_IfcMaterialProfileSet_ (see material use definition above).
The _IfcMaterialProfile_ refers to the subtype of
_IfcProfileDef_ that is the common profile for all member
occurrence, if used. If an _IfcMaterialProfileSet_ is used, all occurrences must have a corresponding _IfcMaterialProfileSetUsage_.

> NOTE  The attribute _ProfileName_ of the
> _IfcProfileDef_ subtype, referenced in
> _IfcMaterialProfile_ should contain a standardized profile
> name according to local standards. However, an additional
> geometric representation of the profile is necessary (e.g. as
> _IfcExtrudedAreaSolid_). An importing application is allowed
> to check for the existence of the profile name: in case of
> identifying it as a standardized name, the corresponding profile
> geometry and possibly other cross sectional properties can be
> read from a library. Otherwise the geometric representation and
> possible non geometric _IfcProfileProperties_ have to be
> used.

### Type Body Geometry

The _IfcMemberType_ may define the shared geometric representation for all member occurrences. The _RepresentationMaps_ attribute refers to a list of _IfcRepresentationMap_'s, that allow for multiple geometric representations (e.g. with _IfcShapeRepresentation_'s having an _RepresentationIdentifier_ 'Box', 'Axis', or 'Body'). It is only applicable if the _IfcMemberType_ has only occurrences of type _IfcMember_ (See geometric use definition of _IfcMember_ for further information).

> NOTE If the _IfcMemberType_ has an associated _IfcMaterialProfileSet_, then no shared geometric representation shall be provided.

> NOTE The product shape representations are defined as _RepresentationMaps_ (attribute of the supertype _IfcTypeProduct_), which get assigned by an element occurrence instance through the _IfcShapeRepresentation.Item[n]_ being an _IfcMappedItem_. See _IfcTypeProduct_ for further information.

> NOTE The values of attributes _RepresentationIdentifier_ and _RepresentationType_ of _IfcShapeRepresentation_ are restricted in the same way as those for _IfcMember_

