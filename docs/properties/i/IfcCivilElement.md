IfcCivilElement
===============

An _IfcCivilElement_ is a generalization of all elements within a civil engineering works that cannot be represented as BuildingElements, DistributionElements or GeographicElements. Depending on the context of the construction project, included building work, such as buildings or factories, are represented as a collection of _IfcBuildingElement_'s, distribution systems, such as piping or drainage, are represented as a collection of _IfcDistributionElement_'s, and other geographic elements, such as trees, light posts, traffic signs etc. are represented as _IfcGeographicElement_'s.

> NOTE&nbsp; The _IfcCivilElement_ has been intruduced as a stub for future extensions of this specification to include an object model for civil engineering works.

Civil elements are typically horizontally organized using a spatial structure expressed by spatial zones, therefore _IfcCivilElement_ is spatially contained by default within an _IfcSpatialZone_.

> HISTORY &nbsp;New entity in IFC4.
