IfcTimePeriod
=============
_IfcTimePeriod_ defines a time period given by a start and end time. Both time
definitions consider the time zone and allow for the daylight savings offset.  
  
A time period is defined by a start and an end time, which is defined by
_IfcTime_. The given time period should be within reasonable values (for
example, the start time must be before the end time). It is furthermore
expected that both time definitions use the same time zone and, if given, the
same daylight saving offset.  
  
> HISTORY  New entity in IFC4.  
[ _bSI
Documentation_](https://standards.buildingsmart.org/IFC/DEV/IFC4_2/FINAL/HTML/schema/ifcdatetimeresource/lexical/ifctimeperiod.htm)


Attribute definitions
---------------------
| Attribute   | Description                    |
|-------------|--------------------------------|
| StartTime   | Start time of the time period. |
| EndTime     | End time of the time period.   |

