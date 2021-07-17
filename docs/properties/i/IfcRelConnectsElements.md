IfcRelConnectsElements
======================

The _IfcRelConnectsElements_ objectified relationship provides the generalization of the connectivity between elements. It is a 1 to 1 relationship. The concept of two elements being physically or logically connected is described independently from the connecting elements. The connectivity may be related to the shape representation of the connected entities by providing a connection geometry.

* In this case the geometrical constraints of the connection are provided by the optional relationship to the _IfcConnectionGeometry_. The connection geometry is provided as a point, curve or surface within the local placement coordinate systems of the connecting elements. 
* If the connection geometry is omitted then the connection is provided as a logical connection. Under this circumstance, the connection point, curve or surface has to be recalculated by the receiving application. 

> HISTORY&nbsp; New entity in IFC1.0.
