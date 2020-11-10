IfcLagTime
==========
_IfcLagTime_ describes the time parameters that may exist within a sequence
relationship between two processes.  
  
An _IfcLagTime_ provides information about the time lag that exists between
the predecessor and successor process in a sequence. The assertion of the time
lag is optional for a sequence but for work schedules that specifically deal
with processes occurring at particular times, it should be asserted.  
  
A lag time has a duration type. This allows the identification of whether
elapsed time or work time is being measured (where work time is the estimate
of the time required to complete the process and elapsed time being the amount
of time actually allocated to the process)  
  
The form of measurement of the duration can be captured. Allowed values for
this are MEASURED, PREDICTED or SIMULATED. The selection of this value depends
on the use of the schedule. A NOTDEFINED value is also allowed.  
  
The value of the time lag may be selected as being either a percentage ratio
or an actual time measure. If selected as a ratio, the percentage should apply
to the duration of the predecessor process (relating process) such that e.g. a
value of 0.5 (50%) would indicate that the successor task should start when
the predecessor task is 50% complete (if a START-START sequence type is used)
or should wait for 50% of the duration of the predecessor process to have
elapsed after the finish of the predecessor process in case of a FINISH-START
sequence type.  
  
The time unit for the task duration may also be set and this may be set to any
allowed unit of time measure.  
  
> HISTORY  New entity in IFC4.  
[ _bSI
Documentation_](https://standards.buildingsmart.org/IFC/DEV/IFC4_2/FINAL/HTML/schema/ifcdatetimeresource/lexical/ifclagtime.htm)


Attribute definitions
---------------------
| Attribute    | Description                                                                                                |
|--------------|------------------------------------------------------------------------------------------------------------|
| LagValue     | Value of the time lag selected as being either a ratio or a\X\0D time measure.                             |
| DurationType | The allowed types of task duration that specify the lag time\X\0D measurement (work time or elapsed time). |

