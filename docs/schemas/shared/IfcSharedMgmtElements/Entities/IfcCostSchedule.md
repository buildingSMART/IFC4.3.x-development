# IfcCostSchedule

An _IfcCostSchedule_ brings together instances of _IfcCostItem_ either for the purpose of identifying purely cost information as in an estimate for constructions costs or for including cost information within another presentation form such as a work order.

> HISTORY&nbsp; New entity in IFC2.0.

{ .change-ifc2x4}
> IFC4 CHANGE&nbsp; Attribute _ID_ renamed to _Identification_ and promoted to supertype _IfcControl_, _PredefinedType_ made optional, attributes _PreparedBy_, _SubmittedBy_, _TargetUsers_ removed.

## Attributes

### PredefinedType
Predefined generic type for a cost schedule that is specified in an enumeration. There may be a property set given specifically for the predefined types.

{ .change-ifc2x4}
> IFC4 CHANGE The attribute has been made optional.

### Status
The current status of a cost schedule. Examples of status values that might be used for a cost schedule status include:
*  PLANNED 
*  APPROVED 
*  AGREED 
*  ISSUED 
*  STARTED

### SubmittedOn
The date and time on which the cost schedule was submitted.
{ .change-ifc2x4}
> IFC4 CHANGE Type changed from IfcDateTimeSelect.

### UpdateDate
The date and time that this cost schedule is updated; this allows tracking the schedule history.
{ .change-ifc2x4}
> IFC4 CHANGE Type changed from IfcDateTimeSelect.
