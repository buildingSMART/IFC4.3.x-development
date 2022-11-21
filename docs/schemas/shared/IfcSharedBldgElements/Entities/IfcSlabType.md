# IfcSlabType

The element type _IfcSlabType_ defines commonly shared information for occurrences of slabs. The set of shared information may include:

* common properties within shared property sets
* common material information
* common material layer definitions
* common shape representations

It is used to define a slab specification (i.e. the specific product information, that is common to all occurrences of that product type). Slab types may be exchanged without being already assigned to occurrences.

> NOTE  The product representations are defined as representation maps (at the level of the supertype _IfcTypeProduct_, which gets assigned by an element occurrence instance through the _IfcShapeRepresentation.Item[1]_ being an _IfcMappedItem_.

The occurrences of the _IfcSlabType_ within building models are represented by instances of _IfcSlab_.

> HISTORY  New entity in IFC2x2.

{ .spec-head}
Informal Propositions:

1. The material assignment, if provided using the _IfcRelAssociatesMaterial_ relationship, shall not reference the _IfcMaterialLayerSetUsage_. Use _IfcMaterialLayerSet_ instead.

## Attributes

### PredefinedType
Identifies the predefined types of a slab element from which the type required may be set.

## Formal Propositions

### CorrectPredefinedType
The inherited attribute _ElementType_ shall be provided, if the _PredefinedType_ is set to USERDEFINED.

## Concepts

### Material Layer Set

The material of the IfcSlabType is defined by the
IfcMaterialLayerSet or as fall back by IfcMaterial
and attached by the
IfcRelAssociatesMaterial.RelatingMaterial. It is
accessible by the inverse HasAssociations relationship.

The shared material layer set definition is defined by assigning
an IfcMaterialLayerSet (see material use definition above).
The IfcMaterialLayer refers to one or several of
IfcMaterial that is the common for all slab occurrence, if
used. If an IfcMaterialProfileSet is used, all occurrences must have a corresponding IfcMaterialProfileSetUsage.

> NOTE  Since each individual instance of
> IfcSlab defines its own
> IfcMaterialLayerSetUsage including the offset from the
> reference plane, the same IfcSlabType can be used
> independently of the reference plane alignment of its
> occurrences.

### Type Body Geometry



