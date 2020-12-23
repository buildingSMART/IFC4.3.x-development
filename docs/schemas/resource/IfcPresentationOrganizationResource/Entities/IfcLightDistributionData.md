# IfcLightDistributionData

_IfcLightDistributionData_ defines the luminous intensity of a light source given at a particular main plane angle. It is based on some standardized light distribution curves; the _MainPlaneAngle_ is either the

* A angle; if the _IfcLightDistributionCurveEnum_ is set to TYPE_A
* B angle; if the _IfcLightDistributionCurveEnum_ is set to TYPE_B
* C angle; if the _IfcLightDistributionCurveEnum_ is set to TYPE_C

For each _MainPlaneAngle_ (considered as being the row of a table) a list of _SecondaryPlaneAngle'_s are given (considered to be the columns of a table). They are either the:

* &#945; angle; if the _IfcLightDistributionCurveEnum_ is set to TYPE_A
* &#946; angle; if the _IfcLightDistributionCurveEnum_ is set to TYPE_B
* &#947; angle; if the _IfcLightDistributionCurveEnum_ is set to TYPE_C

For each pair of _MainPlaneAngle_ and _SecondaryPlaneAngle_ the _LuminousIntensity_ is provided (the unit is given by the _IfcUnitAssignment_ referring to the LuminousIntensityDistributionUnit, normally cd/klm).

> HISTORY&nbsp; New entity in IFC2x2.

## Attributes

### MainPlaneAngle
The main plane angle (A, B or C angles, according to the light distribution curve chosen).

### SecondaryPlaneAngle
The list of secondary plane angles (the &#945;, &#946; or &#947; angles) according to the light distribution curve chosen.

> NOTE&nbsp; The _SecondaryPlaneAngle_ and _LuminousIntensity_ lists are corresponding lists.

### LuminousIntensity
The luminous intensity distribution measure for this pair of main and secondary plane angles according to the light distribution curve chosen.
