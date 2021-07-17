# IfcDate

The _IfcData_ identifies a particular calender day, expressed by year, calender month and day in month. It is expressed by a string value following a particular lexical representation.

The lexical representation for _IfcDate_ is the YYYY-MM-DD, where YYYY represents the calendar year, MM the ordinal number of the calendar month, and DD the ordinal number of the day within the calendar month. No left truncation is allowed. An optional following time zone qualifier is allowed. To accommodate year values outside the range from 0001 to 9999, additional digits can be added to the left of this representation and a preceding "-" sign is allowed.

> NOTE&nbsp; See extended format representation of **date** as defined in ISO&nbsp;8601. The restrictions defined in XML Schema Part 2 apply.

> HISTORY&nbsp; New type in IFC4.
