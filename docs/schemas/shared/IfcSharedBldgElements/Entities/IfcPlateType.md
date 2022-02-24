# IfcPlateType

The element type _IfcPlateType_ defines commonly shared information for occurrences of plates. The set of shared information may include:

* common properties within shared property sets
* common material information
* common material layer definitions
* common shape representations

It is used to define a plate specification (i.e. the specific product information, that is common to all occurrences of that product type). Plate types may be exchanged without being already assigned to occurrences.

> NOTE  The product representations are defined as representation maps (at the level of the supertype _IfcTypeProduct_, which gets assigned by an element occurrence instance through the _IfcShapeRepresentation.Item[1]_ being an _IfcMappedItem_.

The occurrences of the _IfcPlateType_ within building models are represented by instances of _IfcPlate_.

> HISTORY  New entity in IFC2x2.

{ .spec-head}
Informal Propositions:

1. The material assignment, if provided using the _IfcRelAssociatesMaterial_ relationship, shall not reference the _IfcMaterialLayerSetUsage_.

## Attributes

### PredefinedType
Identifies the predefined types of a planar member element from which the type required may be set.

## Formal Propositions

### CorrectPredefinedType
The inherited attribute _ElementType_ shall be provided, if the _PredefinedType_ is set to USERDEFINED.

## Concepts

### Body Geometry


### Material Layer Set

The material of the IfcPlateType is defined by the
IfcMaterialLayerSet or as fall back by IfcMaterial
and attached by the
IfcRelAssociatesMaterial.RelatingMaterial. It is
accessible by the inverse HasAssociations relationship.

The shared material layer set definition is defined by assigning
an IfcMaterialLayerSet (see material use definition above).
The IfcMaterialLayer refers to one or several of
IfcMaterial that is the common for all plate occurrence, if
used. If an IfcMaterialProfileSet is used, all occurrences must have a corresponding IfcMaterialProfileSetUsage.

> NOTE  Since each individual instance of
> IfcPlate defines its own
> IfcMaterialLayerSetUsage including the offset from the
> reference plane, the same IfcPlateType can be used
> independently of the reference plane alignment of its
> occurrences.
