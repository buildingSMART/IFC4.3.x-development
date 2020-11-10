IfcRecurrencePattern
====================
_IfcRecurrencePattern_ defines repetitive time periods on the basis of regular
recurrences such as each Monday in a week, or every third Tuesday in a month.
The population of the remaining attributes such as _DayComponent_, _Position_,
and _Interval_ depend on the specified recurrence type.  
  
_IfcRecurrencePattern_ supports various recurrence patterns that are
differentiated by a type definition (_IfcRecurrencePattern.RecurrenceType_),
which is required to provide the meaning of the given values. It can be
further constrained by applicable times through specified _IfcTimePeriod_
instances, thus enabling time periods such as between 7:00 and 12:00 and
between 13:00 and 17:00 for each of the applicable days, weeks or months.  
  
> HISTORY  New entity in IFC4.  
[ _bSI
Documentation_](https://standards.buildingsmart.org/IFC/DEV/IFC4_2/FINAL/HTML/schema/ifcdatetimeresource/lexical/ifcrecurrencepattern.htm)


Attribute definitions
---------------------
| Attribute        | Description                                                                                                                                                                                                                                                                     |
|------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| TimePeriods      |                                                                                                                                                                                                                                                                                 |
| RecurrenceType   | Defines the recurrence type that gives meaning to the used\X\0D attributes and decides about possible attribute\X\0D combinations, i.e. what attributes are needed to fully\X\0D describe the pattern type.                                                                     |
| DayComponent     | The position of the specified day in a month.                                                                                                                                                                                                                                   |
| WeekdayComponent | The weekday name of the specified day in a week.                                                                                                                                                                                                                                |
| MonthComponent   | The position of the specified month in a year.                                                                                                                                                                                                                                  |
| Position         | The position of the specified component, e.g. the 3rd\X\0D (position=3) Tuesday (weekday component) in a month. A\X\0D negative position value is used to define the last position \X\0D of the component (-1), the next to last position (-2) etc.                             |
| Interval         | An interval can be given according to the pattern type. An\X\0D interval value of 2 can for instance every two days, weeks,\X\0D months, years. An empty interval value is regarded as 1. The\X\0D used interval values should be in a reasonable range, e.g.\X\0D not 0 or <0. |
| Occurrences      | Defines the number of occurrences of this pattern, e.g. a weekly \X\0D event might be defined to occur 5 times before it stops.                                                                                                                                                 |

