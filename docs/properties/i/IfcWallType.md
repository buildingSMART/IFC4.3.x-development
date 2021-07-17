IfcWallType
===========

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
