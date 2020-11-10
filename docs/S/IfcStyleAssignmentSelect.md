IfcStyleAssignmentSelect
========================
The style assignment select is a selection of two wasy of assigning
presentation styles to an _IfcStyledItem_.  
  
* by directly assigning presentation styles as subtypes of _IfcPresentationStyle_  
* by assigning presentation stypes via an intermediate collection entity _IfcPresentationStyleAssignment_  
  
> HISTORY  New select type in IFC4.  
  
{ .change-ifc2x4}  
> IFC4 CHANGE  The select type has been introduced to provide an upward
> compatible improvement for assigning styles to a styled items.  
  
{ .deprecated}  
> DEPRECATION  Using _IfcPresentationStyleAssignment_ is deprecated, use the
> direct assignment of a subtype of _IfcPresentationStyle_ instead.  


