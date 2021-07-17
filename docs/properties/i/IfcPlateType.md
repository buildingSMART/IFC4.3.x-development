IfcPlateType
============

The element type _IfcPlateType_ defines commonly shared information for occurrences of plates. The set of shared information may include:

* common properties within shared property sets
* common material information
* common material layer definitions
* common shape representations

> NOTE&nbsp; It is illegal to share shape representations as representation maps for occurrences of _IfcPlateStandardCase_.

It is used to define a plate specification (i.e. the specific product information, that is common to all occurrences of that product type). Plate types may be exchanged without being already assigned to occurrences.

> NOTE&nbsp; The product representations are defined as representation maps (at the level of the supertype _IfcTypeProduct_, which gets assigned by an element occurrence instance through the _IfcShapeRepresentation.Item[1]_ being an _IfcMappedItem_.

The occurrences of the _IfcPlateType_ within building models are represented by instances of _IfcPlateStandardCase_ if the _IfcPlateType_ has a single associated _IfcMaterialLayerSet_; otherwise they are represented by instances of _IfcPlate_.

> HISTORY&nbsp; New entity in IFC2x2.

{ .spec-head}
Informal Propositions:

1. The material assignment, if provided using the _IfcRelAssociatesMaterial_ relationship, shall not reference the _IfcMaterialLayerSetUsage_.
