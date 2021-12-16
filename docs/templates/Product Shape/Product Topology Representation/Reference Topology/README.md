Reference Topology
==================

Structural activities may have a 'Reference' representation describing the distribution of a load.

```
concept {
    IfcProduct:Representation -> IfcProductDefinitionShape
    IfcProductDefinitionShape:Representations -> IfcTopologyRepresentation
    IfcTopologyRepresentation:ContextOfItems -> IfcGeometricRepresentationContext
    IfcTopologyRepresentation:ContextOfItems -> IfcRepresentationContext
    IfcTopologyRepresentation:RepresentationIdentifier -> IfcLabel_0
    IfcTopologyRepresentation:RepresentationType -> IfcLabel_1
    IfcTopologyRepresentation:Items -> IfcTopologicalRepresentationItem
    IfcTopologyRepresentation:Items[binding="Topology"]
}
```
