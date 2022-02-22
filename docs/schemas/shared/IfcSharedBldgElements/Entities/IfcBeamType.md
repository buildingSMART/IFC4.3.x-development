# IfcBeamType

The element type _IfcBeamType_ defines commonly shared information for occurrences of beams. The set of shared information may include:

* common properties within shared property sets
* common material information
* common profile definitions
* common shape representations

It is used to define a beam specification, or beam style (the specific product information that is common to all occurrences of that beam type). Beam types may be exchanged without being already assigned to occurrences.

Occurrences of the _IfcBeamType_ within building models are represented by instances of _IfcBeamStandardCase_ if the _IfcBeamType_ has a single associated _IfcMaterialProfileSet_; otherwise they are represented by instances of _IfcBeam_. Occurrences of the _IfcBeamType_ within structural analysis models are represented by instances of _IfcStructuralCurveMember_, or its applicable subtypes.

> HISTORY  New entity in IFC2x2.

## Attributes

### PredefinedType
Identifies the predefined types of a beam element from which the type required may be set.

## Formal Propositions

### CorrectPredefinedType
The inherited attribute _ElementType_ shall be provided, if the _PredefinedType_ is set to USERDEFINED.

## Concepts

### Body Geometry

The IfcBeamType may define the shared geometric representation for all beam occurrences. The RepresentationMaps attribute refers to a list of IfcRepresentationMap's, that allow for multiple geometric representations (e.g. with IfcShaperepresentation's having an RepresentationIdentifier 'Box', 'Axis', or 'Body'). It is only applicable if the IfcBeamType has only occurrences of type IfcBeam (See geometric use definition of IfcBeam for further information).



>
> NOTE  If the IfcBeamType has an associated IfcMaterialProfileSet, then no shared geometric representation shall be provided.
>



>
> NOTE  The product shape representations are defined as RepresentationMaps (attribute of the supertype IfcTypeProduct), which get assigned by an element occurrence instance through the IfcShapeRepresentation.Item[n] being an IfcMappedItem. See IfcTypeProduct for further information.



>
> NOTE  The values of attributes RepresentationIdentifier and RepresentationType of IfcShapeRepresentation are restricted in the same way as those for IfcBeam and IfcBeamStandardCase
>



### Material Profile Set

The material of the IfcBeamType is defined by the IfcMaterialProfileSet or as fall back by IfcMaterial and attached by the IfcRelAssociatesMaterial.RelatingMaterial. It is accessible by the inverse HasAssociations relationship.



>
> NOTE  It is illegal to assign an IfcMaterial to an IfcBeamType, if there is at least one occurrence of IfcBeamStandardCase for this type.
>


The shared profile definition is defined by assigning an IfcMaterialProfileSet (see material use definition above). The IfcMaterialProfile refers to the subtype of IfcProfileDef that is the common profile for all beam occurrence, if used. It is only applicable if the IfcBeamType has only occurrences of type IfcBeamStandardCase (see definition of IfcBeamStandardCase for further information).



>
> NOTE  The attribute ProfileName of the IfcProfileDef subtype, referenced in IfcMaterialProfile should contain a standardized profile name according to local standards. However, an additional geometric representation of the profile is necessary (such as IfcExtrudedAreaSolid). An importing application is allowed to check for the existence of the profile name: in case of identifying it as a standardized name, the corresponding profile geometry and possibly other cross sectional properties can be read from a library. Otherwise the geometric representation and possible non geometric IfcProfileProperties have to be used.
>


