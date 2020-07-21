IfcCostSchedule
===============
An _IfcCostSchedule_ brings together instances of _IfcCostItem_ either for the
purpose of identifying purely cost information as in an estimate for
constructions costs or for including cost information within another
presentation form such as a work order.  
  
> HISTORY  New entity in IFC2.0.  
  
{ .change-ifc2x4}  
> IFC4 CHANGE  Attribute _ID_ renamed to _Identification_ and promoted to
> supertype _IfcControl_, _PredefinedType_ made optional, attributes
> _PreparedBy_, _SubmittedBy_, _TargetUsers_ removed.  
[ _bSI
Documentation_](https://standards.buildingsmart.org/IFC/DEV/IFC4_2/FINAL/HTML/schema/ifcsharedmgmtelements/lexical/ifccostschedule.htm)


Attribute definitions
---------------------
| Attribute   | Description                                                                                                                                                                                      |
|-------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Status      | The current status of a cost schedule. Examples of status values that might be used for a cost schedule status include:\X\0D* PLANNED \X\0D* APPROVED \X\0D* AGREED \X\0D* ISSUED \X\0D* STARTED |
| SubmittedOn | The date and time on which the cost schedule was submitted.\X\0D{ .change-ifc2x4}\X\0D> IFC4 CHANGE Type changed from IfcDateTimeSelect.                                                         |
| UpdateDate  | The date and time that this cost schedule is updated; this allows tracking the schedule history.\X\0D{ .change-ifc2x4}\X\0D> IFC4 CHANGE Type changed from IfcDateTimeSelect.                    |

Associations
------------
| Attribute      | Description   |
|----------------|---------------|
| PredefinedType |               |

