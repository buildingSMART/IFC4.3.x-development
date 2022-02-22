IfcBuildingControlsDomain
=========================

The _IfcBuildingControlsDomain_ schema forms part of the Domain Layer of the IFC Model. It extends the ideas concerning building services outlined in the _IfcSharedBldgServicesElements_ schema. It defines concepts of building automation, control, instrumentation and alarm.

The _IfcBuildingControlsDomain_ schema supports ideas including types and occurrences of:

* actuator
* alarm
* controller
* sensor
* flow instrument
* unitary control element

Elements that perform the control action such as valves and dampers are principally types of distribution flow element and are located in the _IfcHvacDomain_ and _IfcElectricalDomain_ schemas.

Occurrences of control elements capture design information, while realtime device state is captured on _IfcPerformanceHistory_, for which control elements may be assigned. Various standard property sets are defined for performance history to capture direct control data.

Control elements are identified within control systems using _IfcRelAssociatesClassification_ to indicate URLs of gateways and addresses of devices and data points.

To support multiple lifecycle stages, realtime control data (_IfcPerformanceHistory_) and design data (_IfcDistributionElement_ subtypes) are separate such that each may be used independently without the existence of the other, however both may be related via _IfcRelAssignsToControl_. If device addressing is known at the time of design where classification is applied to occurrence entities, then upon connecting to a control system the control element occurrences can be assigned to realtime device data (_IfcPerformanceHistory_) automatically according to matching classification.

To connect control elements to physical flow elements measured or controlled, the _IfcRelFlowControlElements_ relationship is used. For example, such relationship may map an actuator to a damper, or a temperature sensor to an evaporator coil. Performance data for _IfcDistributionFlowElement_ entities may be derived by traversing such relationships.

The _IfcBuildingControlsDomain_ schema does not specify building automation protocols, but may be mapped to standard protocols or vendor implementations for commissioning and operations interoperability. Common applicable entities are described as follows:

* _IfcPerformanceHistory_: Captures realtime device data in the form of property sets.
* _IfcPropertySet_: Captures a set of realtime device data, either using predefined data structures or custom information.
* _IfcPropertySetTemplate_: Captures metadata about custom properties, such as names, descriptions, data types, units, and ranges.
* _IfcRelAssociatesClassification_: Associates addresses of devices and control points to uniquely identify within a control system.
* _IfcController_: Captures non-realtime occurrence information for hardware or software-based arbitrary analog and digital data.
* _IfcAlarm_: Captures non-realtime occurrence information for hardware or software-based alarm sources.
* _IfcEvent_: Captures alarm event handling information.
* _IfcProcedure_: Captures device procedures that may be run arbitrarily or in response to events.
* _IfcTask_: Captures device programs that may be scheduled at various times.

> HISTORY  New schema in IFC2x2.
