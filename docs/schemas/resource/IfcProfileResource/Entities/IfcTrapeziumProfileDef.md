# IfcTrapeziumProfileDef

_IfcTrapeziumProfileDef_ defines a trapezium as the profile definition used by the swept surface geometry or the swept area solid. It is given by its Top X and Bottom X extent and its Y extent as well as by the offset of the Top X extend, and placed within the 2D position coordinate system, established by the _Position_ attribute. It is placed centric within the position coordinate system, that is, in the center of the bounding box.<!-- end of definition -->

> HISTORY  New entity in IFC1.5. The use definition has changed in IFC2x.

> IFC4.3.0.0 DEPRECATION This entity is deprecated. Use IfcArbitraryClosedProfileDef instead to define the trapezium by means of an explicit outer boundary.

Figure 1 illustrates parameters of the trapezium profile definition.

![trapezium profile](../../../../figures/ifctrapeziumprofiledef-layout1.gif)

Figure 1 — Trapezium profile

<u>Position</u>

The parameterized profile defines its own position coordinate system.  The underlying coordinate system is defined by the swept surface or swept area solid that uses the profile definition. It is the xy plane of either:

 * IfcSweptSurface.Position
 * IfcSweptAreaSolid.Position

or in case of sectioned spines the xy plane of each list member of IfcSectionedSpine.CrossSectionPositions.

By using offsets of the position location, the parameterized profile
can be positioned centric (using x,y offsets = 0.), or at any position
relative to the profile. Explicit coordinate offsets are used to define
cardinal points (e.g. upper-left bound).

<u>Parameter</u>

The <em>IfcTrapeziumProfileDef</em> is defined within the position coordinate system, where the <em>BottomDim</em> defines the length measure for the bottom line (half along the positive x-axis) and the <em>YDim</em> defines the length measure for the parallel distance of bottom and top line (half along the positive y-axis). The top line starts with a distance of <em>TopXOffset</em> from -BottomLine/2,YDim (which can be negative, zero, or positive) and has a length of <em>TopXDim</em> along the positive x-axis.


## Attributes

### BottomXDim
The extent of the bottom line measured along the implicit x-axis.

### TopXDim
The extent of the top line measured along the implicit x-axis.

### YDim
The extent of the distance between the parallel bottom and top lines measured along the implicit y-axis.

### TopXOffset
Offset from the beginning of the top line to the bottom line, measured along the implicit x-axis.
