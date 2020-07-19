IfcRelAssignsToActor
====================
The objectified relationship _IfcRelAssignsToActor_ handles the assignment of
objects (subtypes of _IfcObject_) to an actor (subtypes of _IfcActor_).  
  
The _IfcRelAssignsToActor_ objectified relationship defines a relationship
between an _IfcActor_ and one or many objects. A particular role of the actor
played in that relationship can be associated. If specified, it takes priority
over the role that may be directly assigned to the person or organization.  
  
> EXAMPLE  An occupant (as an actor) may rent a flat (as a collection of
> spaces or a zone). This would be an application of this generic
> relationship.  
  
Reference to the objects (or single object) on which the actor acts upon in a
certain role (if given) is specified in the inherited _RelatedObjects_
attribute.  
  
> HISTORY  New entity in IFC2.0. Has been renamed from IfcRelActsUpon in
> IFC2x.  
[ _bSI
Documentation_](https://standards.buildingsmart.org/IFC/DEV/IFC4_2/FINAL/HTML/schema/ifckernel/lexical/ifcrelassignstoactor.htm)


