An identifier is an alphanumeric string which allows an individual thing to be identified. It may not provide natural-language meaning.

Type: STRING of up to 255 characters

> NOTE&nbsp; Type adapted from **identifier** defined in ISO 10303-41.

> HISTORY&nbsp; New type in IFC2x.

{ .change-ifc2x4}
> IFC 2x4 CHANGE&nbsp; Previously recommended size restriction of 255 characters is now mandatory.

{ .use-head}
Value restrictions

As a merely machine-readable string for identification purposes, an identifier is usually machine-generated and locale-independent (in contrast to human-readable labels, _IfcLabel_).

> NOTE&nbsp; The set of characters that may appear in STRINGs exchanged in the exchange structure as defined in ISO 10303.21 is provided in ISO 10646. The encoding of characters in case of file-based exchange is defined in ISO 10303-21 and ISO 10303-28. Among else, these specifications define the encoding of 8-bit characters from ISO 8859-1...-16 and of 2-byte and 4-byte Unicode characters from ISO 10646.

> NOTE&nbsp; While _IfcIdentifier_ is restricted to 255 characters, the size in exchange files after encoding may be considerably larger than 255 octets, depending on the particular encoding and on the contents of the identifier.