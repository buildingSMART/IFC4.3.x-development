IfcResourceConstraintRelationship
=================================
An _IfcResourceConstraintRelationship_ is a relationship entity that enables a
constraint to be related to one or more resource level objects.  
  
An _IfcResourceConstraintRelationship_ allows for the specification of a
constraint to be applied to many entity types. An important case is to apply
constraints to properties. The constraints applied therefore enable a property
to carry values identifying requirements as well as those identifying the
fulfilment of those requirements.  
  
> HISTORY  New entity in IFC2x2.  
  
{ .change-ifc2x4}  
> IFC4 CHANGE  Renamed from IfcPropertyConstraintRelationship and extended to
> apply to all resource level entities. Subtyped from
> _IfcResourceLevelRelationship_.  
[ _bSI
Documentation_](https://standards.buildingsmart.org/IFC/DEV/IFC4_2/FINAL/HTML/schema/ifcconstraintresource/lexical/ifcresourceconstraintrelationship.htm)


Attribute definitions
---------------------
| Attribute              | Description                                            |
|------------------------|--------------------------------------------------------|
| RelatingConstraint     |                                                        |
| RelatedResourceObjects | The properties to which a constraint is to be related. |

