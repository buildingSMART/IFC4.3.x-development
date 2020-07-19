IfcConstructionResource
=======================
_IfcConstructionResource_ is an abstract generalization of the different
resources used in construction projects, mainly labour, material, equipment
and product resources, plus subcontracted resources and aggregations such as a
crew resource.  
  
A resource represents "use of something" and does not necessarily correspond
to a single item such as a person or vehicle, but represents a pool of items
having limited availability such as general labor or an equipment fleet. A
resource can represent either a generic resource pool (not having any task
assignment) or a task-specific resource allocation (having an _IfcTask_
assignment).  
  
> HISTORY  New entity in IFC2x2.  
  
{ .change-ifc2x4}  
> IFC4 CHANGE  Modified in to promote _ResourceIdentifer_ and _ResourceGroup_
> (renamed to _LongDescription_) to supertype _IfcResource_ and add attributes
> as described.  
  
{ .use-head}  
Declaration use definition  
  
A root-level resource (specifically _IfcCrewResource_ or
_IfcSubContractResource_) is declared within the project by _IfcRelDeclares_
where _RelatingContext_ refers to the single _IfcProject_ and _RelatedObjects_
refers to one or more _IfcConstructionResource_, and other root-level objects
within the project.  
  
{ .use-head}  
Assignment use definition  
  
A resource may be assigned to an actor by _IfcRelAssignsToActor_ where
_RelatingActor_ refers to an _IfcActor_ and _RelatedObjects_ refers to one or
more _IfcConstructionResource_ or other objects. Such relationship indicates
the actor responsible for allocating the resource such as partitioning into
task-specific allocations, delegating to other actors, and/or scheduling over
time. Note that this assignment does not indicate the person or organization
performing the work; that is indicated by _IfcRelAssignsToResource_. The actor
responsible for the resource may or may not be the same as any actor(s)
performing work.  
  
A resource may be assigned to a control by _IfcRelAssignsToControl_ where
_RelatingProduct_ refers to an _IfcControl_ and _RelatedObjects_ refers to one
or more _IfcConstructionResource_ or other objects. Most commonly an
_IfcWorkCalendar_ is assigned indicating availability of the resource, where
such calendar is nested within a base calendar or an _IfcWorkPlan_ which in
turn is assigned to the _IfcProject_.  
  
A resource may be assigned to a group by _IfcRelAssignsToGroup_ where
_RelatingGroup_ refers to an _IfcGroup_ and _RelatedObjects_ refers to one or
more _IfcConstructionResource_ or other objects. Most commonly an _IfcAsset_
is assigned indicating the asset to be tracked, where such asset is nested
within an _IfcInventory_ which in turn is assigned to the _IfcProject_.  
  
A resource may be assigned to a product by _IfcRelAssignsToProduct_ where
_RelatingProduct_ refers to an _IfcProduct_ and _RelatedObjects_ refers to one
or more _IfcConstructionResource_ or other objects. Most commonly an
_IfcElement_ subtype is assigned indicating the product to be constructed,
where such product is connected to a spatial structure which in turn is
aggregated within the _IfcProject_.  
  
A resource may be assigned to a process by _IfcRelAssignsToProcess_ where
_RelatingProcess_ refers to an _IfcProcess_ and _RelatedObjects_ refers to one
or more _IfcConstructionResource_ or other objects. Most commonly an _IfcTask_
is assigned indicating the task to be performed by the resource, where such
task is nested within a summary task which in turn is assigned to the
_IfcProject_.  
  
A resource may have assignments of other objects using
_IfcRelAssignsToResource_ where _RelatingResource_ refers to the
_IfcConstructionResource_ and _RelatedObjects_ refers to one or more objects
such as _IfcActor_ or _IfcProduct_ subtypes. This relationship indicates
specific objects assigned to fulfill resource usage.  
  
Figure 1 illustrates resource assignment.  
  
!["Assignment Use Definition"](../figures/ifcconstructionresource-
assignment.png "Figure 1 -- Construction resource assignment use")  
  
{ .use-head}  
Baseline use definition  
  
A resource may have any number of baselines defined using the relationship
_IfcRelDefinesByObject_ where _RelatingObject_ is the "current" resource and
_RelatedObjects_ consists of multiple "baseline" resources, each representing
a copy of the resource as it existed at an earlier point in time as shown in
Figure 185. Each baseline _IfcConstructionResource_ is identified by its
nested _IfcRelAssignsToControl_ relationship to an _IfcWorkSchedule_ having
_PredefinedType=BASELINE_, _IfcWorkSchedule.CreationDate_ indicating the date
of the baseline, and _IfcWorkSchedule.Name_ indicating the name of the
baseline.  
  
!["Baseline Use Definition"](../figures/ifcconstructionresource-baseline.png
"Figure 2 -- Construction resource baseline use")  
[ _bSI
Documentation_](https://standards.buildingsmart.org/IFC/DEV/IFC4_2/FINAL/HTML/schema/ifcconstructionmgmtdomain/lexical/ifcconstructionresource.htm)


