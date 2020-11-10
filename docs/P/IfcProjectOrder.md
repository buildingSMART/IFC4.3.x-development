IfcProjectOrder
===============
A project order is a directive to purchase products and/or perform work, such
as for construction or facilities management.  
  
Project orders are typically formal contracts between two organizations, where
cost and time information may be rigid or flexible according to contained
schedule types and constraints.  
  
> HISTORY  New entity in IFC2.0  
  
{ .change-ifc2x4}  
> IFC4 CHANGE  Attribute _ID_ renamed to _Identification_ and promoted to
> supertype _IfcControl_. Attribute ''LongDescription'' added.  
[ _bSI
Documentation_](https://standards.buildingsmart.org/IFC/DEV/IFC4_2/FINAL/HTML/schema/ifcsharedmgmtelements/lexical/ifcprojectorder.htm)


Attribute definitions
---------------------
| Attribute       | Description                                                                                                                                                                                                             |
|-----------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| PredefinedType  |                                                                                                                                                                                                                         |
| Status          | The current status of a project order.Examples of status values that might be used for a project order status include:\X\0D* PLANNED\X\0D* REQUESTED\X\0D* APPROVED\X\0D* ISSUED\X\0D* STARTED\X\0D* DELAYED\X\0D* DONE |
| LongDescription | A detailed description of the project order describing the work to be completed.                                                                                                                                        |

