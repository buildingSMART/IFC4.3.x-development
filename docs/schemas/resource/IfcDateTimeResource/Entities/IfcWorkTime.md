# IfcWorkTime

_IfcWorkTime_ defines time periods that are used by _IfcWorkCalendar_ for either describing working times or non-working exception times. Besides start and finish dates, a set of time periods can be given by various types of recurrence patterns.
<!-- end of short definition -->

A work time should have a meaningful name that describes the time periods (for example, working week, holiday name). Non-recurring time periods should have a start date (_IfcWorkTime.Start_) and a finish date (_IfcWorkTime.Finish_). In that case it is assumed that the time period begins at 0:00 on the start date and ends at 24:00 on the finish date.

The start and finish date is optional if a recurrence pattern is given (_IfcWorkTime.RecurrencePattern_). They then restrict never-ending recurrence patterns.

> HISTORY New entity in IFC4.

## Attributes

### RecurrencePattern
Recurrence pattern that defines a time period, which, if given, is
  valid within the time period defined by
  _IfcWorkTime.Start_ and _IfcWorkTime.Finish_.

### Start
Start date of the work time (0:00), that might be further
  restricted by a recurrence pattern.

### Finish
End date of the work time (24:00), that might be further
  restricted by a recurrence pattern.
