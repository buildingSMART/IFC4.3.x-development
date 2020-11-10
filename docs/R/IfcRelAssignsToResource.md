IfcRelAssignsToResource
=======================
The objectified relationship _IfcRelAssignsToResource_ handles the assignment
of objects (as subtypes of _IfcObject_), acting as a resource usage or
consumption, to a resource (as subtypes of _IfcResource_).  
  
> EXAMPLE  The assignment of a resource usage to a construction resource is an
> application of this generic relationship. It could be an actor, as person or
> organization assigned to a labor resource, or a raw product assigned to a
> construction product or material resource).  
  
> HISTORY  New entity in IFC2x.  
[ _bSI
Documentation_](https://standards.buildingsmart.org/IFC/DEV/IFC4_2/FINAL/HTML/schema/ifckernel/lexical/ifcrelassignstoresource.htm)


Attribute definitions
---------------------
| Attribute        | Description                                                                                                                                                               |
|------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| RelatingResource | Reference to the resource to which the objects are assigned to.\X\0D{ .change-ifc2x4}\X\0D> IFC4 CHANGE Datatype expanded to include _IfcResource_ and _IfcTypeResource_. |

