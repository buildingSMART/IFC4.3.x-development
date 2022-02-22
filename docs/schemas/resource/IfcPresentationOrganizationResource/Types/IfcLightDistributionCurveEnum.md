# IfcLightDistributionCurveEnum

There are three kinds of light distribution curves, see Figure 1.

> NOTE  The classification as type A, B, C is according to Standard CEN TC 169, prEN 13032-1, CIE 121:

> HISTORY  New enumeration in IFC2x2.

## Items

### TYPE_A
Type A is basically not used. For completeness the Type A Photometry equals the Type B rotated 90&deg; around the Z-Axis counter clockwise.

### TYPE_B
Type B is sometimes used for floodlights. The B-Plane System has a horizontal axis. B-Angles are valid from -180&deg; to +180&deg; with B 0&deg; at the bottom and B180&deg;/B-180&deg; at the top, &#946;-Angles are valid from -90&deg; to +90&deg;.

![B-Type](../../../../figures/ifclightdistributioncurveenum_b-plane.gif)

### TYPE_C
Type C is the recommended standard system. The C-Plane system equals a globe with a vertical axis. C-Angles are valid from 0&deg; to 360&deg;, &#947;-Angles are valid from 0&deg; (south pole) to 180&deg; (north pole).

![C-Type](../../../../figures/ifclightdistributioncurveenum_c-plane.gif)

### NOTDEFINED

