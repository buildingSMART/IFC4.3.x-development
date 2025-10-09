Resource definition data schemas
========================

The resource definition data schemas consist of supporting data structures as shown highlighted in blue. Entities and types defined in this layer can be referenced by all entities in the layers below.

Unlike entities in other layers, resource definition data structures cannot exist independently, but can only exist if referenced (directly or indirectly) by one or more entities deriving from IfcRoot. As resource definitions do not have a concept of identity (such as a GUID), multiple objects referencing the same instance of a resource entity does not imply a relationship. For example, two polylines (IfcPolyline) sharing the same instance for a point (IfcCartesianPoint), and two polylines using different instances for identical points (such as both having cordinates 0,0,0) are semantically equivalent. It is recommended (but not required) for applications to minimize file size by sharing identical resource definition instances where possible.

NOTE  The resource definition layer should not be confused with construction resource entities (IfcResource subtypes). While the terms are similar, they are unrelated concepts.
