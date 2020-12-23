# IfcActionRequest

A request is the act or instance of asking for something, such as a request for information, bid submission, or performance of work.

Requests may take many forms depending on the need including fault reports for maintenance, requests for small works, and purchase requests (where these are to be made through a help desk or buying function).

> HISTORY&nbsp; New entity in IFC2x2.

{ .change-ifc2x4}
> IFC4 CHANGE&nbsp; Atribute _RequestID_ renamed to _Identification_ and promoted to supertype _IfcControl_, attributes _PredefinedType_, _Status_, and _LongDescription_ added.

## Attributes

### PredefinedType
Identifies the predefined type of sources through which a request can be made.

{ .change-ifc2x4}
> IFC4 CHANGE The attribute has been added.

### Status
The status currently assigned to the request.  Possible values include:  
Hold: wait to see if further requests are received before deciding on action  
NoAction: no action is required on this request  
Schedule: plan action to take place as part of maintenance or other task planning/scheduling  
Urgent: take action immediately  
{ .change-ifc2x4}
> IFC4 CHANGE The attribute has been added.

### LongDescription
Detailed description of the permit.

{ .change-ifc2x4}
> IFC4 CHANGE The attribute has been added.
