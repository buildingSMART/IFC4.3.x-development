# IfcCoveringType

The element type _IfcCoveringType_ defines commonly shared information for occurrences of coverings. The set of shared information may include:

* common properties within shared property sets
* common material (layer set) information
* common shape representations

It is used to define an covering specification or covering style (i.e. the specific product information, that is common to all occurrences of that product type). Covering types may be exchanged without being already assigned to occurrences.

The occurrences of the _IfcCoveringType_ are represented by instances of _IfcCovering_

> HISTORY&nbsp; New entity in IFC2x2.

{ .spec-head}
Informal Propositions:

1. The material assignment, if provided using the _IfcRelAssociatesMaterial_ relationship, shall not reference _IfcMaterialLayerSetUsage_ or _IfcMaterialProfileSetUsage_.

## Attributes

### PredefinedType
Predefined types to define the particular type of the covering. There may be property set definitions available for each predefined type.

## Formal Propositions

### CorrectPredefinedType
The inherited attribute _ElementType_ shall be provided, if the _PredefinedType_ is set to USERDEFINED.

## Concepts

### Body Geometry

The IfcCoveringType may define the shared geometric
representation for all covering occurrences. The
RepresentationMaps attribute refers to a list of
IfcRepresentationMap's, that allow for multiple geometric
representations (e.g. with IfcShaperepresentation's having
an RepresentationIdentifier 'Box', 'Surface', or 'Body').
(See geometric use definition of IfcCovering for further
information).



> 
> NOTE  If the IfcCoveringType has an associated IfcMaterialLayerSet, then no shared geometric representation shall be provided.
> 



> 
> NOTE  The product shape representations are defined as RepresentationMaps (attribute of the supertype IfcTypeProduct), which get assigned by an element occurrence instance through the IfcShapeRepresentation.Item[n] being an IfcMappedItem. See IfcTypeProduct for further information.
> 



> 
> NOTE  The values of attributes RepresentationIdentifier and RepresentationType of IfcShapeRepresentation are restricted in the same way as those for IfcCoveringType.
> 



### Material Layer Set

The material of the IfcCoveringType is defined by 
IfcMaterialLayerSet for layer-based coverings or as fall back by IfcMaterial
and attached by the
IfcRelAssociatesMaterial.RelatingMaterial. It is
accessible by the inverse HasAssociations
relationship.



### Material Profile Set

The material of the IfcCoveringType is defined by 
IfcMaterialProfileSet for profile-based coverings or as fall back by IfcMaterial
and attached by the
IfcRelAssociatesMaterial.RelatingMaterial. It is
accessible by the inverse HasAssociations
relationship.



