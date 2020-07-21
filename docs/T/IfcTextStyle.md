IfcTextStyle
============
The _IfcTextStyle_ is a presentation style for annotations that place a text
in model space. The _IfcTextStyle_ provides the text style for presentation
information assigned to _IfcTextLiteral_''s. The style is defined by color,
text font characteristics, and text box characteristics.  
  
An _IfcTextStyle_ is instantiated with:  
  
* _TextCharacterAppearance_: _IfcTextStyleForDefinedFont_  
* _TextStyle_: _IfcTextStyleTextModel_  
* _TextFontStyle_: _IfcTextStyleFontModel_  
  
An _IfcTextStyle_ is assigned to _IfcTextLiteral_ through the _IfcStyledItem_
entity.  
  
> NOTE  Entity adopted from font properties (font-family, font-style, font-
> variant, font-weight, font-size), Color and background properties (color,
> background-color) and text properties (word-spacing, letter-spacing, text-
> decoration, text-transform, text-align, text-indent, line-height) defined in
> [CSS-1](../../../bibliography.htm#CSS1).  
  
> HISTORY  New entity in IFC2x2.  
  
{ .change-ifc2x3}  
> IFC2x3 CHANGE  The _IfcTextStyle_ has been changed by adding _TextFontStyle_
> and different data types for _TextStyle_ and _IfcTextCharacterAppearance_.  
  
{ .change-ifc2x4}  
> IFC4 CHANGE  The _IfcTextStyle_ has been simplified by removing old vector
> based text style definitions.  
[ _bSI
Documentation_](https://standards.buildingsmart.org/IFC/DEV/IFC4_2/FINAL/HTML/schema/ifcpresentationappearanceresource/lexical/ifctextstyle.htm)


Attribute definitions
---------------------
| Attribute         | Description                                                                                                                                                                                                                                              |
|-------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| TextFontStyle     | The style applied to the text font for its visual appearance. It defines the font family, font style, weight and size.\X\0D \X\0D{ .change-ifc2x2}\X\0D> IFC2x2 Add2 CHANGE The attribute _TextFontStyle_ is a new attribute attached to _IfcTextStyle_. |
| ModelOrDraughting | Indication whether the length measures provided for the presentation style are model based, or draughting based.\X\0D{ .change-ifc2x4}\X\0D> IFC4 CHANGE  New attribute.                                                                                 |

Associations
------------
| Attribute               | Description   |
|-------------------------|---------------|
| TextCharacterAppearance |               |
| TextStyle               |               |

