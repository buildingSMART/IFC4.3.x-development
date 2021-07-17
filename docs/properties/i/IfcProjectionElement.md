IfcProjectionElement
====================

The projection element is a specialization of the general feature element to represent projections applied to building elements. It represents a solid attached to any element that has physical manifestation.

> EXAMPLE&nbsp; A wall projection such as a pilaster strip is handled by _IfcProjectionElement_

> NOTE&nbsp; View definitions or implementer agreements may restrict the types of elements to which _IfcProjectionElement_ can be applied.

An _IfcProjectionElement_ has to be linked to a element (all subtypes of _IfcElement_) by using the _IfcRelProjectsElement_ relationship. Its existence depends on the existence of the master element. The relationship implies a Boolean union operation between the volume of the projection element and the volume of the element.

The _IfcProjectionElement_ shall not participate in the containment relationship, i.e. it is not linked directly to the spatial structure of the project. It has a mandatory _ProjectsElements_ inverse relationship pointing to the _IfcElement_ that is contained in the spatial structure.

* The inverse relationship _ContainedInStructure_ shall be NIL.

> HISTORY&nbsp; New entity in IFC2x2.

{ .change-ifc2x4}
> IFC4 CHANGE&nbsp; The attribute _PredefinedType_ has been added at the end of attribute list.
