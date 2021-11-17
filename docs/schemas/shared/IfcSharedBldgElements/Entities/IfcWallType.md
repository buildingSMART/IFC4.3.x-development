# IfcWallType

The element type _IfcWallType_ defines commonly shared information for occurrences of walls. The set of shared information may include:

* common properties within shared property sets
* common material information
* common material layer definitions
* common shape representations

> NOTE&nbsp; It is illegal to share shape representations as representation maps for occurrences of _IfcWallStandardcase_.

It is used to define a wall specification (i.e. the specific product information, that is common to all occurrences of that product type). Wall types may be exchanged without being already assigned to occurrences.

> NOTE&nbsp; The product representations are defined as representation maps (at the level of the supertype _IfcTypeProduct_, which gets assigned by an element occurrence instance through the _IfcShapeRepresentation.Item[1]_ being an _IfcMappedItem_.

Occurrences of the _IfcWallType_ within building models are represented by instances of _IfcWallStandardCase_ if the _IfcWallType_ has a single associated _IfcMaterialLayerSet_; otherwise they are represented by instances of _IfcWall_, or _IfcWallElementedCase_. Occurrences of the _IfcWallType_ within structural analysis models are represented by instances of _IfcStructuralSurfaceMember_, or its applicable subtypes.

> HISTORY&nbsp; New entity in IFC2x2.

{ .spec-head}
Informal Propositions:

1. The material assignment, if provided using the _IfcRelAssociatesMaterial_ relationship, shall not reference the _IfcMaterialLayerSetUsage_.

## Attributes

### PredefinedType
Identifies the predefined types of a wall element from which the type required may be set.

## Formal Propositions

### CorrectPredefinedType
The inherited attribute _ElementType_ shall be provided, if the _PredefinedType_ is set to USERDEFINED.

## Concepts

### Body Geometry


### Material Layer Set

The material of the IfcWallType is defined by the
IfcMaterialLayerSet or as fall back by IfcMaterial
and attached by the
IfcRelAssociatesMaterial.RelatingMaterial. It is
accessible by the inverse HasAssociations
relationship.



> NOTE  It is illegal to assign an
> IfcMaterial to an IfcWallType, if there is at least
> one occurrences. of IfcWallStandardCase for this
> type.


The shared material layer set definition is defined by
assigning an IfcMaterialLayerSet (see material use
definition above). The IfcMaterialLayer refers to one or
several of IfcMaterialLayer that is the common for all
wall occurrence, if used. It is only applicable if the
IfcWallType has only occurrences of type
IfcWallStandardCase (see definition of
IfcWallStandardCase for further information).



> NOTE  Since each individual instance of
> IfcWallStandardCase defines its own
> IfcMaterialLayerSetUsage including the offset from the
> wall axis, the same IfcWallType can be used independently
> of the axis alignment of its occurrences.



