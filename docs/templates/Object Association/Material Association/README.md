Material Association
====================

Any product or product type can have associated materials indicating the physical composition of an object.

> EXAMPLE&nbsp; An object can be comprised of a single material or a set of materials with a particular layout. Several examples include: > * a slab may have an associated layer of concrete; 
> * a beam may have an associated I-Shape profile of steel;
> * a door may have associated constituents for framing and glazing;
> * a port may have an associated profile and/or material flowing through it such as hot water.

Materials can have representations for surface styles indicating colors, textures, and light reflectance for 3D rendering. Materials can have representations for fill styles indicating colors, tiles, and hatch patterns for 2D rendering. Materials can have properties such as density, elasticity, thermal resistance, and others as defined in this specification. Materials can also be classified according to a referenced industry standard.

> EXAMPLE&nbsp; Material information can also be given at object type, defining the common material data for all occurrences of the same type. It is then accessible by the inverse _IsTypedBy_ relationship pointing via _HasAssociations_ and via _IfcRelAssociatesMaterial.RelatingMaterial_ to the material information. If both are given, then the material directly assigned to object occurrence overrides the material assigned to object type.

```
concept {
    IfcObjectDefinition:HasAssociations -> IfcRelAssociatesMaterial:RelatedObjects
}
```
