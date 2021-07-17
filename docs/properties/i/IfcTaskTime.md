IfcTaskTime
===========

_IfcTaskTime_ captures the time-related information about a task including the different types (actual or scheduled) of starting and ending times.

All given values should be provided by the application; the IFC schema does not deal with dependencies between task time values. There is also no consistency check through where rules that guarantee a meaningful population of time values. Thus, an application is responsible to provide reasonable values and, if an application receives task times, has to make consistency checks by their own.

_IfcTaskTime_ furthermore provides a generic mechanism to differentiate between user given time values and time values derived from user given time values and other constraints such as work calendars and assigned resources.

> HISTORY&nbsp; New entity in IFC4, adapted from _IfcScheduleTimeControl_. Differently to _IfcScheduleTimeControl_ it is also possible to differentiate duration time measures between the two possible types; (1) work time and (2) elapsed time.
