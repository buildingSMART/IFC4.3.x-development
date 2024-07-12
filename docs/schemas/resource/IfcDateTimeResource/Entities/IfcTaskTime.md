# IfcTaskTime

_IfcTaskTime_ captures the time-related information about a task including the different types (actual or scheduled) of starting and ending times.
<!-- end of short definition -->


All given values should be provided by the application; the IFC schema does not deal with dependencies between task time values. There is also no consistency check through where rules that guarantee a meaningful population of time values. Thus, an application is responsible to provide reasonable values and, if an application receives task times, has to make consistency checks by their own.

_IfcTaskTime_ furthermore provides a generic mechanism to differentiate between user given time values and time values derived from user given time values and other constraints such as work calendars and assigned resources.

> HISTORY New entity in IFC4, adapted from _IfcScheduleTimeControl_. Differently to _IfcScheduleTimeControl_ it is also possible to differentiate duration time measures between the two possible types; (1) work time and (2) elapsed time.

## Attributes

### DurationType
Enables to specify the type of duration values for _ScheduleDuration_, _ActualDuration_ and _RemainingTime_. The duration type is either work time or elapsed time.

### ScheduleDuration
The amount of time which is scheduled for completion of a task. The value might be measured or somehow calculated, which is defined by
_ScheduleDataOrigin_. The value is either given as elapsed time or work time, which is defined by _DurationType_.

> NOTE Scheduled Duration may be calculated as the time from scheduled start date to scheduled finish date.

### ScheduleStart
The date on which a task is scheduled to be started. The value might be measured or somehow calculated, which is defined by
_ScheduleDataOrigin_.
> NOTE The scheduled start date must be greater than or equal to the earliest start date.

### ScheduleFinish
The date on which a task is scheduled to be finished. The value might be measured or somehow calculated, which is defined by _ScheduleDataOrigin_.
> NOTE The scheduled finish date must be greater than or equal to the earliest finish date.

### EarlyStart
The earliest date on which a task can be started. It is a calculated value.

### EarlyFinish
The earliest date on which a task can be finished. It is a calculated value.

### LateStart
The latest date on which a task can be started. It is a calculated value.

### LateFinish
The latest date on which a task can be finished. It is a calculated value.

### FreeFloat
The amount of time during which the start or finish of a task may be varied without any effect on the overall programme of work. It is a calculated elapsed time value.

### TotalFloat
The difference between the duration available to carry out a task and the scheduled duration of the task. It is a calculated elapsed time value.
> NOTE Total Float time may be calculated as being the difference between the scheduled duration of a task and the available duration from earliest start to latest finish. Float time may be either positive, zero or negative. Where it is zero or negative, the task becomes critical.

### IsCritical
A flag which identifies whether a scheduled task is a critical item within the programme.
> NOTE A task becomes critical when the float time becomes zero or negative.

### StatusTime
The date or time at which the status of the tasks within the schedule is analyzed.

### ActualDuration
The actual duration of the task. It is a measured value. The value is either given as elapsed time or work time, which is defined by _DurationType_.

### ActualStart
The date on which a task is actually started. It is a measured value.
> NOTE The scheduled start date must be greater than or equal to the earliest start date. No constraint is applied to the actual start date with respect to the scheduled start date since a task may be started earlier than had originally been scheduled if circumstances allow.

### ActualFinish
The date on which a task is actually finished.

### RemainingTime
The amount of time remaining to complete a task. It is a predicted value. The value is either given as elapsed time or work time, which is defined by _DurationType_.
> NOTE The time remaining in which to complete a task may be determined both for tasks which have not yet started and those which have. Remaining time for a task not yet started has the same value as the scheduled duration. For a task already started, remaining time is calculated as the difference between the scheduled finish and the point of analysis.

### Completion
The extent of completion expressed as a ratio or percentage. It is a measured value.
