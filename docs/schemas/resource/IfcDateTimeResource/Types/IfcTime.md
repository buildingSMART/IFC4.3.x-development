The _IfcTime_ identifies a time within a day, expressed by hours, minutes and second. It is expressed by a string value following a particular lexical representation.

The lexical representation for _IfcTime_ is: hh:mm:ss where where hh represents hours, mm minutes and ss seconds. Additional digits can be used to increase the precision of fractional seconds if desired i.e the format ss.ss... A time zone indicator may be provided by a representation of the different to the Coordinated Universal Time. It is appended with a sign [+/-] followed by hh and optionally :mm.

> EXAMPLE&nbsp; 13:20:00-05:00 represents 1:20 pm for a time zone which is 5 hours behind Coordinated Universal Time (such as Eastern Standard Time)

> NOTE&nbsp; See extended format representation of **time** as defined in ISO&nbsp;8601. The restrictions defined in XML Schema Part 2 apply.

> HISTORY&nbsp; New type in IFC4.