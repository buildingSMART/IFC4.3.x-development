# IfcResourceTime

_IfcResourceTime_ captures the time-related information about a construction resource.

> HISTORY  New entity in IFC4.

## Attributes

### ScheduleWork
Indicates the total work (e.g. person-hours) allocated to the task on behalf of the resource. 
Note: this is not necessarily the same as the task duration (IfcTaskTime.ScheduleDuration); it may vary according to the resource usage ratio and other resources assigned to the task.

### ScheduleUsage
Indicates the amount of the resource used concurrently. For example, 100% means 1 worker, 300% means 3 workers, 50% means half of 1 worker's time for scenarios where multitasking is feasible. If not provided, then the usage ratio is considered to be 100%.

### ScheduleStart
Indicates the time when the resource is scheduled to start working.

### ScheduleFinish
Indicates the time when the resource is scheduled to finish working.

### ScheduleContour
Indicates how a resource should be leveled over time by adjusting the resource usage according to a specified curve.  Standard values include: 'Flat', 'BackLoaded', 'FrontLoaded', 'DoublePeak', 'EarlyPeak', 'LatePeak', 'Bell', and 'Turtle'.  Custom values may specify a custom name or formula.

### LevelingDelay
Indicates a delay in the ScheduleStart caused by leveling.

### IsOverAllocated
Indicates that the resource is scheduled in excess of its capacity.

### StatusTime
Indicates the date and time for which status values are applicable; particularly completion, actual, and remaining values.  If values are time-phased (the referencing IfcConstructionResource has associated time series values for attributes), then the status values may be determined from such time-phased data as of the StatusTime.

### ActualWork
Indicates the actual work performed by the resource as of the StatusTime.

### ActualUsage
Indicates the actual amount of the resource used concurrently.

### ActualStart
Indicates the time when the resource actually started working.

### ActualFinish
Indicates the time when the resource actually finished working.

### RemainingWork
Indicates the work remaining to be completed by the resource.

### RemainingUsage


### Completion
Indicates the percent completion of this resource.  If the resource is assigned to a task, then indicates completion of the task on behalf of the resource; if the resource is partitioned into sub-allocations, then indicates overall completion of sub-allocations.
