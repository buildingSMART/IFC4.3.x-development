# IfcDateTime

The _IfcDateTime_ identifies a particular point in time, expressed by hours, minutes and optional seconds elapsed within a calendar day, expressed by year, calendar month and day in month. It is expressed by a string value following a particular lexical representation.<!-- end of definition -->

This lexical representation for _IfcDateTime_ is YYYY-MM-DDThh:mm:ss where "YYYY" represent the year, "MM" the month and "DD" the day, preceded by an optional leading "-" sign to indicate a negative year number. If the sign is omitted, "+" is assumed. The letter "T" is the date/time separator and "hh", "mm", "ss" represent hour, minute and second respectively. Additional digits can be used to increase the precision of fractional seconds if desired i.e the format ss.ss... with any number of digits after the decimal point is supported. The fractional seconds part is optional; other parts of the lexical form are not optional. To accommodate year values greater than 9999 additional digits can be added to the left of this representation. Leading zeros are required if the year value would otherwise have fewer than four digits; otherwise they are forbidden. The year 0000 is prohibited.

> NOTE  See extended format representation of **dateTime** as defined in ISO 8601. The restrictions defined in XML Schema Part 2 apply.

> HISTORY  New type in IFC4.
