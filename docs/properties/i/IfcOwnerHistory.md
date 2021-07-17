IfcOwnerHistory
===============

_IfcOwnerHistory_ defines all history and identification related information. In order to provide fast access it is directly attached to all independent objects, relationships and properties.

_IfcOwnerHistory_ is used to identify the creating and owning application and user for the associated object, as well as capture the last modifying application and user.

> HISTORY&nbsp; New entity in IFC1.0.

{ .change-ifc2x4}
> IFC4 CHANGE&nbsp; ChangeAction is now optional and a related WHERE rule enforces conditions when it is asserted.

{ .spec-head}
Informal Propositions:

1. If LastModifiedDate is defined but ChangeAction is not asserted, then the state of ChangeAction is assumed to be UNDEFINED.
2. If both LastModifiedDate and ChangeAction are asserted, then the state of ChangeAction applies to the value asserted in LastModifiedDate.
