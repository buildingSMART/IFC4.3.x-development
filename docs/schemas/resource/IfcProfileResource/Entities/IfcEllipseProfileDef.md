# IfcEllipseProfileDef

_IfcEllipseProfileDef_ defines an ellipse as the profile definition used by the swept surface geometry or the swept area solid. It is given by its semi axis attributes and placed within the 2D position coordinate system, established by the _Position_ attribute.

> HISTORY&nbsp; New entity in IFC2x

Figure 1 illustrates parameters for the ellipse profile definition. The parameterized profile defines its own position coordinate system. The underlying coordinate system is defined by the swept surface or swept area solid that uses the profile definition. It is the xy plane of either:

* _IfcSweptSurface.Position_
* _IfcSweptAreaSolid.Position_

Or in case of sectioned spines it is the xy plane of each list member of _IfcSectionedSpine.CrossSectionPositions_. By using offsets of the position location, the parameterized profile can be positioned centric (using x,y offsets = 0.), or at any position relative to the profile. Explicit coordinate offsets are used to define cardinal points (for example, upper-left bound). The location of the position coordinate system defines the center of the ellipse. The _SemiAxis1_ attribute defines the first radius of the ellipse in the direction of the X axis, the _SemiAxis2_ attribute defines the second radius of the ellipse in the direction of the Y axis.

> NOTE&nbsp; The semi axes of the ellipse are rectangular to each other by definition.

!["ellipse profile"](../../../../figures/ifcellipseprofiledef-layout1.gif "Figure 1 &mdash; Ellipse profile")

## Attributes

### SemiAxis1
The first radius of the ellipse. It is measured along the direction of Position.P[1].

### SemiAxis2
The second radius of the ellipse. It is measured along the direction of Position.P[2].
