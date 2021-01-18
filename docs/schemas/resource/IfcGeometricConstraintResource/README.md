IfcGeometricConstraintResource
==============================

The schema _IfcGeometricConstraintResource_ defines the resources used to determine the placement of the shape representation of a product within the geometric representation context of a project. It also contains resource definitions to be assigned to product connectivity definitions to determine the connection geometry constraints between those products.

The primary application of this resource is to:

* determine the object placement used for the shape representation of the object
* determine the constraints applied to the connectivity between two shapes of objects

#### 8.7.1.1 Placement
The placement of an product's shape is given by the _IfcObjectPlacement_, used by the attribute _ObjectPlacement_ of _IfcProduct_. The object placement defines the local object coordinate system in which all shape representations of that product are defined. It is given either as

* absolute placement, 
    * the absolute placement is specified by using _IfcLocalPlacement_ and omitting the _PlacementRelTo_ attribute; 
* relative placement, 
    * the relative placement is specified by using _IfcLocalPlacement_ and pointing the _PlacementRelTo_ attribute to an _IfcObjectPlacement_ used in another _IfcProduct_ instance; 
* placement relative to a grid, 
    * the placement relative to a grid is specified by using _IfcGridPlacement_ pointing to one (or two) virtual intersections of _IfcGridAxis_. If two virtual intersections are references, than the second virtual intersections specifies the orientation of the object placement. Alternatively the direction can also be provided explicitly by ifcDirection. 

> NOTE&nbsp; When using relative placement the shape representation of each product is defined in the local object coordinate system provided by _ObjectPlacement_. That local object coordinate system is defined relative to the object coordinate system referred to by _PlacementRelTo_ which may be a relative placement as well. Finally the _ObjectPlacement_ not having an _PlacementRelTo_ attribute defined the transformation into the global coordinate system. The transformation of the current coordinate system into the parent coordinate systems have to be applied in that order.

#### 8.7.1.2 Connection geometry
The connection geometry defines the connectivity between the shapes of two products. The constraint can be defined by geometric representation items:

* point
* curve
* surface
* solid

or by topological representation items with associated geometry:

* vertex point
* edge curve
* face surface
* closed shell

As a special type of point connection includes the provision to express an eccentricity, i.e. a physical distance between the two points involved in the connection.
