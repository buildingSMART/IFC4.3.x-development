IfcActionRequest
================
A request is the act or instance of asking for something, such as a request
for information, bid submission, or performance of work.  
  
Requests may take many forms depending on the need including fault reports for
maintenance, requests for small works, and purchase requests (where these are
to be made through a help desk or buying function).  
  
> HISTORY  New entity in IFC2x2.  
  
{ .change-ifc2x4}  
> IFC4 CHANGE  Atribute _RequestID_ renamed to _Identification_ and promoted
> to supertype _IfcControl_, attributes _PredefinedType_, _Status_, and
> _LongDescription_ added.  
[ _bSI
Documentation_](https://standards.buildingsmart.org/IFC/DEV/IFC4_2/FINAL/HTML/schema/ifcsharedmgmtelements/lexical/ifcactionrequest.htm)


Attribute definitions
---------------------
| Attribute       | Description                                                                                                                                                                                                                                                                                                                                                                                                                 |
|-----------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| PredefinedType  |                                                                                                                                                                                                                                                                                                                                                                                                                             |
| Status          | The status currently assigned to the request. Possible values include: \X\0DHold: wait to see if further requests are received before deciding on action \X\0DNoAction: no action is required on this request \X\0DSchedule: plan action to take place as part of maintenance or other task planning/scheduling \X\0DUrgent: take action immediately \X\0D{ .change-ifc2x4}\X\0D> IFC4 CHANGE The attribute has been added. |
| LongDescription | Detailed description of the permit.\X\0D\X\0D{ .change-ifc2x4}\X\0D> IFC4 CHANGE The attribute has been added.                                                                                                                                                                                                                                                                                                              |

