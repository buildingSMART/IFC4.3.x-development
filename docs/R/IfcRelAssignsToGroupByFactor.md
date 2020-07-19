IfcRelAssignsToGroupByFactor
============================
The objectified relationship _IfcRelAssignsToGroupByFactor_ is a
specialization of the general grouping mechanism. It allows to add a factor to
define the ratio that applies to the assignment of object definitions
(individual object occurrences as subtypes of _IfcObject_ and object types as
subtypes of _IfcTypeObject_) to a group (subtypes of _IfcGroup_).  
  
The ratio can be used to define a percentage assignment. For example, a
_Factor_ of 0.8 would indicate that the object is assigned by 80% to the
group, or a _Factor_ of 2.5 would indicate the object is assigned with a
weight factor of 2.5 to the group.  
  
> NOTE  Examples of factored groups include the assignment of load cases in a
> load combination in structural analysis, or the assignment of spaces by
> percentage to different rental zones.  
  
The same object or object type may be included with the same or different
_Factor_ values to many groups. Grouping relationships are not hierarchical.  
  
> HISTORY  New entity in IFC4.  
[ _bSI
Documentation_](https://standards.buildingsmart.org/IFC/DEV/IFC4_2/FINAL/HTML/schema/ifckernel/lexical/ifcrelassignstogroupbyfactor.htm)


