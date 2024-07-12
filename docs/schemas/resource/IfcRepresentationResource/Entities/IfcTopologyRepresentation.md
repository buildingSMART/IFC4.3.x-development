# IfcTopologyRepresentation

_IfcTopologyRepresentation_ represents the concept of a particular topological representation of a product or a product component within a representation context. This representation context does not need to be (but may be) a geometric representation context. Several representation types for shape representation are included as predefined types:

<!-- end of short definition -->

|Type|Description|
|--- |--- |
|Vertex|topological vertex representation (with or without assigned geometry)|
|Edge|topological edge representation (with or without assigned geometry)|
|Path|topological path representation (with or without assigned geometry)|
|Face|topological face representation (with or without assigned geometry)|
|Shell|topological shell representation (with or without assigned geometry)|
|Undefined|no constraints imposed|

The representation type is given as a string value at the inherited attribute '_RepresentationType_'.

> HISTORY New entity in IFC2x2.

## Formal Propositions

### WR21
Only topological representation items should be used.

### WR22
A representation type should be given to the topology representation.

### WR23
Checks the proper use of Items according to the RepresentationType.
