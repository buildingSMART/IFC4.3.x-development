IfcRecurrencePattern
====================

_IfcRecurrencePattern_ defines repetitive time periods on the basis of regular recurrences such as each Monday in a week, or every third Tuesday in a month. The population of the remaining attributes such as _DayComponent_, _Position_, and _Interval_ depend on the specified recurrence type.

_IfcRecurrencePattern_ supports various recurrence patterns that are differentiated by a type definition (_IfcRecurrencePattern.RecurrenceType_), which is required to provide the meaning of the given values. It can be further constrained by applicable times through specified _IfcTimePeriod_ instances, thus enabling time periods such as between 7:00 and 12:00 and between 13:00 and 17:00 for each of the applicable days, weeks or months.

> HISTORY&nbsp; New entity in IFC4.
