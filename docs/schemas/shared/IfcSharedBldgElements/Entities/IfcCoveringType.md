# IfcCoveringType

The element type _IfcCoveringType_ defines commonly shared information for occurrences of coverings. The set of shared information may include:

* common properties within shared property sets
* common material (layer set) information
* common shape representations
<!-- end of short definition -->

It is used to define an covering specification or covering style (i.e. the specific product information, that is common to all occurrences of that product type). Covering types may be exchanged without being already assigned to occurrences.

The occurrences of the _IfcCoveringType_ are represented by instances of _IfcCovering_

> HISTORY New entity in IFC2x2.

**Informal Propositions**

1. The material assignment, if provided using the _IfcRelAssociatesMaterial_ relationship, shall not reference _IfcMaterialLayerSetUsage_ or _IfcMaterialProfileSetUsage_. Use _IfcMaterialLayerSet_ and _IfcMaterialProfileSet_ instead.

## Attributes

### PredefinedType
Predefined types to define the particular type of the covering. There may be property set definitions available for each predefined type.

## Formal Propositions

### CorrectPredefinedType
The inherited attribute _ElementType_ shall be provided, if the _PredefinedType_ is set to USERDEFINED.

## Concepts

### Material Layer Set

The material of the _IfcCoveringType_ is defined by _IfcMaterialLayerSet_ for layer-based coverings or as fall back by IfcMaterial and attached by the _IfcRelAssociatesMaterial.RelatingMaterial_. It is accessible by the inverse _HasAssociations_ relationship.

### Material Profile Set

The material of the _IfcCoveringType_ is defined by _IfcMaterialProfileSet_ for profile-based coverings or as fall back by _IfcMaterial_ and attached by the _IfcRelAssociatesMaterial.RelatingMaterial_. It is accessible by the inverse _HasAssociations_ relationship.

### Type Body Geometry

The _IfcCoveringType_ may define the shared geometric representation for all covering occurrences. The _RepresentationMaps_ attribute refers to a list of _IfcRepresentationMap_'s, that allow for multiple geometric representations (e.g. with _IfcShapeRepresentation_'s having an _RepresentationIdentifier_ 'Box', 'Surface', or 'Body'). (See geometric use definition of _IfcCovering_ for further information).

> NOTE If the _IfcCoveringType_ has an associated IfcMaterialLayerSet, then no shared geometric representation shall be provided.

> NOTE The product shape representations are defined as _RepresentationMaps_ (attribute of the supertype _IfcTypeProduct_), which get assigned by an element occurrence instance through the _IfcShapeRepresentation.Item[n]_ being an _IfcMappedItem_. See _IfcTypeProduct_ for further information.

> NOTE The values of attributes _RepresentationIdentifier_ and _RepresentationType_ of _IfcShapeRepresentation_ are restricted in the same way as those for _IfcCoveringType_.

