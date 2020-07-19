IfcRelAggregates
================
The aggregation relationship _IfcRelAggregates_ is a special type of the
general composition/decomposition (or whole/part) relationship
_IfcRelDecomposes_. The aggregation relationship can be applied to all
subtypes of _IfcObjectDefinition_.  
  
In cases of aggregation of physical elements into a physical aggregate the
shape representation of the whole (within the same representation identifier)
can be taken from the sum of the shape representations of the parts.  
  
> EXAMPLE  A roof is the aggregation of the roof elements, such as roof slabs,
> rafters, purlins, etc. Within the same representation identifier (such as
> the body geometric representation), the shape representation of the roof is
> given by the shape representation of its parts.  
  
Decompositions imply a dependency, implying that the whole depends on the
definition of the parts and the parts depend on the existence of the whole.
The behaviour that is implied from the dependency relationship has to be
established inside the applications.  
  
> HISTORY  New entity in IFC2x.  
  
{ .change-ifc2x4}  
> IFC4 CHANGE The attributes _RelatingObject_ and _RelatedObjects_ are demoted
> from the supertype _IfcRelDecomposes_.  
[ _bSI
Documentation_](https://standards.buildingsmart.org/IFC/DEV/IFC4_2/FINAL/HTML/schema/ifckernel/lexical/ifcrelaggregates.htm)


