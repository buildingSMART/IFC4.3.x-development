IfcEventTime
============
_IfcEventTime_ captures the time-related information about an event including
the different types of event dates (i.e. actual, scheduled, early, and late).  
  
All given values should be provided by the application, that is, the IFC
schema does not deal with dependencies between process time values. At this
stage there is also no consistency check through where rules that guarantee a
meaningful population of date values. Thus, an application is responsible to
provide reasonable values and, if an application receives event dates, has to
make consistency checks by their own.  
  
_IfcEventTime_ furthermore provides a generic mechanism to differentiate
between user given time values and time values derived from user given time
values and other constraints such as work calendars and assigned resources
(derived from the process graph). The data origin flag is provided as a single
attribute applying to all date time related attributes of _IfcEventTime_.  
  
> HISTORY  New entity in IFC4.  
[ _bSI
Documentation_](https://standards.buildingsmart.org/IFC/DEV/IFC4_2/FINAL/HTML/schema/ifcdatetimeresource/lexical/ifceventtime.htm)


