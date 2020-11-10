IfcTextLiteralWithExtent
========================
The text literal with extent is a text literal with the additional explicit
information of the planar extent. An alignment attribute defines how the text
box is aligned to the placement and how it may expand if additional lines of
text need to be added.  
  
Figure 1 shows the use of planar extent and box alignment to position the text
string  
  
!["IfcTextLiteralWithExtent_Fig1.png 8,1
KB"](../figures/ifctextliteralwithextent_fig1.png "Figure 1 -- Text literal
with extent and alignment")  
  
The planar extent defines the box model within which the text is placed.
Padding maybe defined in the text style that offsets the text from the box to
its inside.  
  
> NOTE  Entity adapted from **text_literal_with_extent** defined in
> ISO10303-46  
  
> HISTORY  New entity in IFC2x2.  
  
{ .change-ifc2x3}  
> IFC2x3 CHANGE  The _IfcTextLiteralWithExtent_ has been changed by adding
> _BoxAlignment_.  
[ _bSI
Documentation_](https://standards.buildingsmart.org/IFC/DEV/IFC4_2/FINAL/HTML/schema/ifcpresentationdefinitionresource/lexical/ifctextliteralwithextent.htm)


Attribute definitions
---------------------
| Attribute    | Description                                                 |
|--------------|-------------------------------------------------------------|
| Extent       |                                                             |
| BoxAlignment | The alignment of the text literal relative to its position. |

