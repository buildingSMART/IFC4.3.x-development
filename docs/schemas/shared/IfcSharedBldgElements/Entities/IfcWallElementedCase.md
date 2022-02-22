# IfcWallElementedCase

The _IfcWallElementedCase_ defines a wall with certain constraints for the provision of its components. The _IfcWallElementedCase_ handles all cases of walls, that are decomposed into parts:

* having components being assigned to the _IfcWallElementedCase_ using the _IfcRelAggregates_ relationship accessible by the inverse relationship _IsDecomposedBy_.

Parts within the decomposition are usually be of type:

* _IfcBuildingElementPart_ for wall layer, insolation layers and similar
* _IfcMember_ for studs, posts and similar elements,
* _IfcElementAssembly_ for other aggregates, or
* _IfcBuiltElementProxy_.

> EXAMPLE Elemented walls may extend the concepts of standard walls with the following features, as shown in Figure 1, including the _IfcRelConnectsWithRealizingElements_ relationship to define fasteners and accessories.

!["voiding"](../../../../figures/ifcwallelementedcase-partitioning.png "Figure 1 &mdash; Wall elemented case")

> HISTORY  New entity in IFC4.

## Formal Propositions

### HasDecomposition
A valid instance of _IfcWallElementedCase_ has to have parts in a decomposition hierarchy.

## Concepts

### Element Decomposition

An elemented wall is decomposed into parts for particular components such as framing and panels on each side. There must be an object corresponding to each type of part, however there may be single object instance indicating multiple placements (via mapping geometry) for each part, or multiple instances corresponding to each placement. For minimizing file size, it is recommended to use a single object with multiple placement unless there are specific connectivity relationships indicated (e.g. a junction box connected to a specific stud).




### Element Voiding

As shown in Figure 285, openings within the composite wall are directly assigned to IfcWallElementedCase using IfcRelVoidsElement pointing to IfcOpeningElement and apply to all aggregated parts. If individual parts have cutting and other voiding features, then the decomposed parts have a separate voiding relationship IfcRelVoidsElement pointing to IfcVoidingFeature.


![voiding](../../../../figures/ifcwallelementedcase_fig01.png)
Figure 285 — Wall elemented voiding



### Product Local Placement

The use of local placement is defined at the supertype
IfcWall. The local placement of the
IfcWallElementedCase defines the parent coordinate systems
for the parts within the decomposition. All parts shall be
positioned relative to the IfcWallElementedCase.



### Surface Geometry

The 'Surface Geometry' shape representation can be used to define a
 surfacic model of the building (e.g. for analytical purposes, or 
for reduced Level of Detail representation). It could suppress 
the geometric details of the parts in the
 decomposition.



> NOTE  It is invalid to exchange a 'Body' shape representation of an IfcWallElementedCase. The body geometry is defined by the parts within the decomposition.


