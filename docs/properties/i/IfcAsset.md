IfcAsset
========

An asset is a uniquely identifiable grouping of elements acting as a single entity that has a financial value or that can be operated on as a single unit.

An asset is generally the level of granularity at which maintenance operations are undertaken. An asset is a group that can contain one or more elements. Whilst the financial value of a component or element can be defined, financial value is also defined for accounting purposes at the level of the asset.  
  
There are a number of actors that can be associated with an asset, each actor having a role. Actors within the scope of the project are indicated using the [IfcRelAssignsToActor](../../ifckernel/lexical/ifcrelassignstoactor.htm) relationship in which case roles should be defined through the [IfcActorRole](../../ifcactorresource/lexical/ifcactorrole.htm) class; otherwise principal actors are identified as attributes of the class. In the existence of both, direct attributes take precedence.  
  
There are a number of costs that can be associated with an asset, each cost having a role. These are specified through the _OriginalValue_, _CurrentValue_, _TotalReplacementCost_ and _DepreciatedValue_ attributes.

> HISTORY&nbsp; New entity in IFC2x.

{ .change-ifc2x4}
> IFC4 CHANGE&nbsp; All attributes made optional and date values changed to use _IfcDate_.
