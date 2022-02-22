# IfcMemberType

The element type _IfcMemberType_ defines commonly shared information for occurrences of members. Members are predominately linear building elements, often forming part of a structural system. The orientation of the member (being horizontal, vertical or sloped) is not relevant to its definition (in contrary to beam and column). The set of shared information may include:

* common properties within shared property sets
* common material information
* common profile definitions
* common shape representations

It is used to define a member specification, or member style (the specific product information that is common to all occurrences of that member type). Member types may be exchanged without being already assigned to occurrences.

Occurrences of the _IfcMemberType_ within building models are represented by instances of _IfcMemberStandardCase_ if the _IfcMemberType_ has a single associated _IfcMaterialProfileSet_; otherwise they are represented by instances of _IfcMember_. Occurrences of the _IfcMemberType_ within structural analysis models are represented by instances of _IfcStructuralCurveMember_, or its applicable subtypes.

> HISTORY  New entity in IFC2x2 Addendum 1.

## Attributes

### PredefinedType
Identifies the predefined types of a linear structural member element from which the type required may be set.

## Formal Propositions

### CorrectPredefinedType
The inherited attribute _ElementType_ shall be provided, if the _PredefinedType_ is set to USERDEFINED.

## Concepts

### Body Geometry

The IfcMemberType may define the shared geometric representation for all member occurrences. The RepresentationMaps attribute refers to a list of IfcRepresentationMap's, that allow for multiple geometric representations (e.g. with IfcShaperepresentation's having an RepresentationIdentifier 'Box', 'Axis', or 'Body'). It is only applicable if the IfcMemberType has only occurrences of type IfcMember (See geometric use definition of IfcMember for further information).



> 
> NOTE  If the IfcMemberType has an associated IfcMaterialProfileSet, then no shared geometric representation shall be provided.
> 



> 
> NOTE  The product shape representations are defined as RepresentationMaps (attribute of the supertype IfcTypeProduct), which get assigned by an element occurrence instance through the IfcShapeRepresentation.Item[n] being an IfcMappedItem. See IfcTypeProduct for further information.
> 



> 
> NOTE  The values of attributes RepresentationIdentifier and RepresentationType of IfcShapeRepresentation are restricted in the same way as those for IfcMember and IfcMemberStandardCase
> 



### Material Profile Set

The material of the IfcMemberType is defined by the
IfcMaterialProfileSet or as fall back by
IfcMaterial and attached by the
IfcRelAssociatesMaterial.RelatingMaterial. It is
accessible by the inverse HasAssociations
relationship.



> 
> NOTE  It is illegal to assign an IfcMaterial to an IfcMemberType, if there is at least one occurrences of IfcMemberStandardCase for this type.
> 


The shared profile definition is defined by assigning an
IfcMaterialProfileSet (see material use definition above).
The IfcMaterialProfile refers to the subtype of
IfcProfileDef that is the common profile for all member
occurrence, if used. It is only applicable if the
IfcMemberType has only occurrences of type
IfcMemberStandardCase (see definition of
IfcMemberStandardCase for further information).



> 
> NOTE  The attribute ProfileName of the
> IfcProfileDef subtype, referenced in
> IfcMaterialProfile should contain a standardized profile
> name according to local standards. However, an additional
> geometric representation of the profile is necessary (e.g. as
> IfcExtrudedAreaSolid). An importing application is allowed
> to check for the existence of the profile name: in case of
> identifying it as a standardized name, the corresponding profile
> geometry and possibly other cross sectional properties can be
> read from a library. Otherwise the geometric representation and
> possible non geometric IfcProfileProperties have to be
> used.



