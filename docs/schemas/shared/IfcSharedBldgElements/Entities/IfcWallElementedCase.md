# IfcWallElementedCase

The _IfcWallElementedCase_ defines a wall with certain constraints for the provision of its components. The _IfcWallElementedCase_ handles all cases of walls, that are decomposed into parts:

* having components being assigned to the _IfcWallElementedCase_ using the _IfcRelAggregates_ relationship accessible by the inverse relationship _IsDecomposedBy_.

Parts within the decomposition are usually be of type:

* _IfcBuildingElementPart_ for wall layer, insolation layers and similar
* _IfcMember_ for studs, posts and similar elements,
* _IfcElementAssembly_ for other aggregates, or
* _IfcBuildingElementProxy_.

> EXAMPLE&nbsp;Elemented walls may extend the concepts of standard walls with the following features, as shown in Figure 1, including the _IfcRelConnectsWithRealizingElements_ relationship to define fasteners and accessories.

!["voiding"](../../../../../../figures/ifcwallelementedcase-partitioning.png "Figure 1 &mdash; Wall elemented case")

> HISTORY&nbsp; New entity in IFC4.

## Formal Propositions

### HasDecomposition
A valid instance of _IfcWallElementedCase_ has to have parts in a decomposition hierarchy.
