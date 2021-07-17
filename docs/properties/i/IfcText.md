IfcText
=======

An _IfcText_ is an alphanumeric string of characters which is intended to be read and understood by a human being. It is for information purposes only.

Type: STRING

> NOTE&nbsp; Type adapted from **text** defined in ISO 10303-41.

> HISTORY&nbsp; New type in IFC2x.

> NOTE&nbsp; The set of characters that may appear in STRINGs exchanged in the exchange structure as defined in ISO 10303.21 is provided in ISO 10646. The encoding of characters in case of file-based exchange is defined in ISO 10303-21 and ISO 10303-28. Among else, these specifications define the encoding of 8-bit characters from ISO 8859-1...-16 and of 2-byte and 4-byte Unicode characters from ISO 10646.

> Note that while _IfcText_ is not formally restricted in length, the size of a string in ISO 10303-21 conforming exchange files must not exceed 32767 octets after encoding and escaping.
