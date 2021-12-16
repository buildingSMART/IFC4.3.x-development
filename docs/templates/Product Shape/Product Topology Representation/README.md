Product Topology Representation
===============================

The topology of products may be represented in multiple ways for different purposes. Each representation has a well-known string identifier and a particular representation context. There may be multiple representation contexts to describe a topology for various uses.

```
concept {
    IfcProduct:Representation -> IfcProductDefinitionShape
    IfcProductDefinitionShape:Representations -> IfcTopologyRepresentation
    IfcTopologyRepresentation:ContextOfItems -> IfcRepresentationContext
    IfcTopologyRepresentation:RepresentationIdentifier -> IfcLabel_0
    IfcTopologyRepresentation:RepresentationType -> IfcLabel_1
}
```
