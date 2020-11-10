IfcArbitraryClosedProfileDef
============================
The closed profile _IfcArbitraryClosedProfileDef_ defines an arbitrary two-
dimensional profile for the use within the swept surface geometry, the swept
area solid or a sectioned spine. It is given by an outer boundary from which
the surface or solid can be constructed.  
  
> HISTORY  New entity in IFC1.5. Entity has been renamed from
> _IfcArbitraryProfileDef_ in IFC2x.  
  
{ .spec-head}  
Informal Propositions:  
  
1\. The _OuterCurve_ has to be a closed curve.  
2\. The _OuterCurve_ shall not intersect.  
  
Figure 1 illustrates the arbitrary closed profile definition. The _OuterCurve_
is defined in the underlying coordinate system. The underlying coordinate
system is defined by the swept surface or swept area solid that uses the
profile definition. It is the xy plane of either:  
  
* IfcSweptSurface.Position  
* IfcSweptAreaSolid.Position  
  
or in case of sectioned spines the xy plane of each list member of
_IfcSectionedSpine.CrossSectionPositions_. The _OuterCurve_ attribute defines
a two dimensional closed bounded curve.  
  
!["arbitrary profile without boundaries"](../figures/ifcarbitraryprofiledef-
layout1.gif "Figure 1 -- Arbitrary closed profile")  
[ _bSI
Documentation_](https://standards.buildingsmart.org/IFC/DEV/IFC4_2/FINAL/HTML/schema/ifcprofileresource/lexical/ifcarbitraryclosedprofiledef.htm)


Attribute definitions
---------------------
| Attribute   | Description   |
|-------------|---------------|
| OuterCurve  |               |

