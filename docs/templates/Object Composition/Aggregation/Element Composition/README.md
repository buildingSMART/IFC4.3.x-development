Element Composition
===================

Provision of an aggregation structure where the element is part of another element representing the composite. The part then provides, if such concepts are in scope of the Model View Definition, exclusively the following:

* _Body Geometry_ &mdash; The partial body shape representation and its placement;
* _Material_ &mdash; The material information for the part.

The part may also provide, in addition to the aggregate, more specifically the following:

* _Property Sets_ &mdash; The parts may have individual property sets assigned, solely or in addition to the composite;
* _Quantity Sets_ &mdash; The parts may have individual quantity sets assigned, solely or in addition to the composite.

The part should not be contained in the spatial hierarchy, i.e. the concept _Spatial Containment_ shall not be used at the level of parts. The part is contained in the spatial structure by the spatial containment of its composite.

> EXAMPLE&nbsp; An _IfcBeam_ may be aggregated into an element assembly using the objectified relationship _IfcRelAggregates_, referring to it by its inverse attribute SELF\IfcObjectDefinition.Decomposes. Any subtype of _IfcElement_ can be an element assembly, with _IfcElementAssembly_ as a special focus subtype. In this case it should not be additionally contained in the spatial hierarchy, i.e. _SELF\IfcElement.ContainedInStructure_ should be NIL.

```
concept {
    IfcElement_0:Decomposes -> IfcRelAggregates:RelatedObjects
    IfcRelAggregates:RelatingObject -> IfcElement_1
    IfcElement_1:Name -> IfcLabel
    IfcElement_0:Decomposes[binding="Decomposes"]
    IfcRelAggregates:RelatingObject[binding="RelatingObject"]
    IfcElement_1:Name[binding="ElementName"]
}
```
