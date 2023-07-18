# IfcCivilElement

An _IfcCivilElement_ is a generalization of all elements within a civil engineering works that cannot be represented as BuildingElements, DistributionElements or GeographicElements. Depending on the context of the construction project, included building work, such as buildings or factories, are represented as a collection of _IfcBuiltElement_'s, distribution systems, such as piping or drainage, are represented as a collection of _IfcDistributionElement_'s, and other geographic elements, such as trees, light posts, traffic signs etc. are represented as _IfcGeographicElement_'s.

> NOTE  The _IfcCivilElement_ has been introduced as a stub for future extensions of this specification to include an object model for civil engineering works.

Civil elements are typically horizontally organized using a spatial structure expressed by spatial zones, therefore _IfcCivilElement_ is spatially contained by default within an _IfcSpatialZone_.

> HISTORY  New entity in IFC4.

> IFC4.3.0.0 DEPRECATION This entity is deprecated. Usage of a generic element for civil engineering works is no longer desirable with specific types now provided as subtypes of IfcBuiltElement, IfcEarthworksElement, IfcFacility and IfcGeotechnicalElement.

## Concepts

### Object Typing



### Property Sets for Objects



### Spatial Containment



