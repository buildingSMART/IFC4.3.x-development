IfcRoof
=======

A roof is the covering of the top part of a building, it protects the building against the effects of wheather.

{ .extDef}
> NOTE&nbsp; Definition according to ISO 6707-1: construction enclosing the building from above.

The _IfcRoof_ shall either be represented:

* as a roof assembly that aggregates all parts (slabs, rafters and purlins, or other included roofs, such as dormers) with own shape representaion, or
* as a single roof without decomposition including all shape representations directly at the roof entity.

> NOTE&nbsp; In case of an _IfcRoof_ being the assembly of all parts of the roof the aggregation is handled by the _IfcRelAggregates_ relationship, relating an _IfcRoof_ with the related roof elements, like slabs (represented by _IfcSlab_), rafters and purlins (represented by _IfcBeam_), or other included roofs, such as dormers (represented by _IfcRoof_).

> NOTE&nbsp; Model View Definitions and implementer agreements may restrict the _IfcRoof_ being an assembly to not have an independent shape representation, but to always require that the decomposed parts have a shape representation. In this case, at least the 'Body' geometric representations shall not be provided directly at _IfcRoof_ if it is an assembly. The 'Body' geometric representation of the _IfcRoof_ is then the sum of the 'Body' shape representation of the parts within the decomposition structure.

> HISTORY&nbsp; New entity in IFC2.0.

{ .change-ifc2x4}
> IFC4 CHANGE&nbsp; Attribute _ShapeType_ renamed to _PredefinedType_.
