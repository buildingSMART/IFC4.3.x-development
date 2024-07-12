# IfcRelAdheresToElement

The _IfcRelAdheresToElement_ is an objectified relationship between an element and one to many surface feature elements that adhere to the surface of the element. The relationship is defined to be a 1 to many relationship. The _IfcRelAdheresToElement_ establishes an aggregation relationship between the main element and a sub ordinary surface feature.
<!-- end of short definition -->

> NOTE In contrary the _IfcRelAggregates_ relationship establishes an aggregation of equal parts to a whole.

The _IfcRelAdheresToElement_ implies a surface interface between the geometric bodies of the element and the surface feature . As with all decomposition relationships it determines:

* existence dependency - the _RelatedSurfaceFeature_ cannot exist without the _RelatingElement_
* hierarchical and non-cyclical relationship - the _IfcRelAdheresToElement_ can only alter a single _IfcElement_
* no spatial containment - the _IfcSurfaceFeature_ as related element never participates in the hierarchical spatial containment relationship _IfcRelContainedInSpatialStructure_

> HISTORY New entity in IFC4x3.

## Attributes

### RelatingElement
Element to which the _IfcSurfaceFeature_ is adhered to.

### RelatedSurfaceFeatures
The _IfcSurfaceFeature_(s) that adheres to the surface of the parent element.
