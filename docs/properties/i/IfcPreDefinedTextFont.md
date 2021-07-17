IfcPreDefinedTextFont
=====================

The pre defined text font determines those qualified names which can be used for fonts that are in scope of the current data exchange specification (in contrary to externally defined text fonts). There are two choices:

* _IfcDraughtingPreDefinedTextFont_ for definitions from ISO/IS 10303-46:1994 for (old) vector based and monospace text.   
* _IfcTextStyleFontModel_ for definitions from [Cascading Style Sheets, level 1](http://www.w3.org/TR/REC-CSS1){ target="_blank"}, W3C Recommendation 17 Dec 1996, revised 11 Jan 1999, CSS1, for all true type text. The use of the CSS1 definitions is the preferred way to represent text fonts.

> NOTE&nbsp; Corresponding ISO 10303 name: pre_defined_text_font. Please refer to ISO/IS 10303-46:1994, p. 138 for the final definition of the formal standard.

> HISTORY&nbsp; New entity in IFC2x2.

{ .change-ifc2x3}
> IFC2x3 CHANGE&nbsp; The _IfcTextStyleFontModel_ has been added as new subtype.
