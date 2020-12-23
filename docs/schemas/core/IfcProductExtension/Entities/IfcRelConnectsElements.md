# IfcRelConnectsElements

The _IfcRelConnectsElements_ objectified relationship provides the generalization of the connectivity between elements. It is a 1 to 1 relationship. The concept of two elements being physically or logically connected is described independently from the connecting elements. The connectivity may be related to the shape representation of the connected entities by providing a connection geometry.

* In this case the geometrical constraints of the connection are provided by the optional relationship to the _IfcConnectionGeometry_. The connection geometry is provided as a point, curve or surface within the local placement coordinate systems of the connecting elements. 
* If the connection geometry is omitted then the connection is provided as a logical connection. Under this circumstance, the connection point, curve or surface has to be recalculated by the receiving application. 

> HISTORY&nbsp; New entity in IFC1.0.

## Attributes

### ConnectionGeometry
The geometric shape representation of the connection geometry that is provided in the object coordinate system of the _RelatingElement_ (mandatory) and in the object coordinate system of the _RelatedElement_ (optionally).

### RelatingElement
Reference to a subtype of _IfcElement_ that is connected by the connection relationship in the role of _RelatingElement_.

### RelatedElement
Reference to a subtype of _IfcElement_ that is connected by the connection relationship in the role of _RelatedElement_.

## WhereRules

### NoSelfReference
The instance of the _RelatingElement_ shall not be the same instance as the _RelatedElement_.
