IfcColourRgbList
================
The _IfcColourRgbList_ defines an ordered collection of RGB colour values.
Each colour value is a fixed list of three colour components (red, green,
blue). The attribute _ColourList_ is a two-dimensional list, where:  
  
* first dimension is an unbounded list representing each colour value;  
* second dimension is a fixed list of four list members, where [1] is the red component, [2] the green component, and [3] the blue component.  
  
> NOTE  The _IfcColourRgbList_ is introduced to provide a compact
> representation of an indexable representation of colours for tessellated
> items.  
  
> HISTORY  New entity in IFC4.  
[ _bSI
Documentation_](https://standards.buildingsmart.org/IFC/DEV/IFC4_2/FINAL/HTML/schema/ifcpresentationappearanceresource/lexical/ifccolourrgblist.htm)


Attribute definitions
---------------------
| Attribute   | Description                                                                                                                                                                                                                                              |
|-------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ColourList  | List of colours defined by the red, green, blue components. All values are provided as a ratio of 0.0 ≤ _value_ ≤ 1.0. When using 8bit for each colour channel, a value of 0.0 equals 0, a value of 1.0 equals 255, and values between are interpolated. |

