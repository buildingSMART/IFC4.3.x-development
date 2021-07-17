# IfcCompoundPlaneAngleMeasure

_IfcCompoundPlaneAngleMeasure_ is a compound measure of plane angle in degrees, minutes, seconds, and optionally millionth-seconds of arc.

> NOTE&nbsp; _IfcCompoundPlaneAngleMeasure_ is used where angles need to be described to an accuracy as fine as one millionth of a degree and expressed as parts of an arc. It may be used for angular measurement by surveyors or for other angular measurements where precision is required. Another usage is exact or approximate global positioning against a geographic coordinate systems using longitude and latitude.

> NOTE&nbsp; While the unit of measurement of the type _IfcPlaneAngleMeasure_ depends on unit assignment (radian or degree or other derived units; globally at the _IfcPoject_ or locally at an _IfcMeasureWithUnit_), the units of _IfcCompoundPlaneAngleMeasure_ are always degrees, minutes, seconds, and millionth-seconds irrespective of unit assignments.

> HISTORY&nbsp; New type in IFC1.5.1.

Type: LIST [3:4] OF INTEGER

{ .use-head}
Value restrictions

* The first integer measure is the number of degrees and is generally not range-restricted. However, when _IfcCompoundPlaneAngleMeasure_ is used to express geographic coordinates, only latitudes of [-90, 90] and longitudes of [-180, 180] are used in practice.
* The second integer measure is the number of minutes and shall be in the range (-60, 60).
* The third integer measure is the number of seconds and shall be in the range (-60, 60).
* The optional fourth integer measure is the number of millionth-seconds and shall be in the range (-1 000 000, 1 000 000).

{ .use-head}
Signedness

All measure components have the same sign (positive or negative). It is therefore trivial to convert between floating point representation (decimal degrees) and compound representation regardless whether the angle is greater or smaller than zero. Example:

> 
> ```
> 
LOCAL  
> &nbsp;&nbsp;a : IfcPlaneAngleMeasure := -50.975864; &nbsp;(\* decimal degrees, -50&deg; 58' 33" 110400 \*)  
> &nbsp;&nbsp;b : IfcPlaneAngleMeasure;  
> &nbsp;&nbsp;c : IfcCompoundPlaneAngleMeasure;  
> &nbsp;&nbsp;s : IfcText;  
> END_LOCAL;  
>   
> (\* convert from float to compound \*)  
> &nbsp;&nbsp;c[1] := &nbsp;&nbsp;&nbsp;a; &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-- -50  
> &nbsp;&nbsp;c[2] := &nbsp;&nbsp;(a - c[1]) \* 60; &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-- -58  
> &nbsp;&nbsp;c[3] := &nbsp;((a - c[1]) \* 60 - c[2]) \* 60; &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-- -33  
> &nbsp;&nbsp;c[4] := (((a - c[1]) \* 60 - c[2]) \* 60 - c[3]) \* 1.e6; &nbsp;-- -110400  
>   
> (\* convert from compound to float \*)  
> &nbsp;&nbsp;b := c[1] + c[2]/60. + c[3]/3600. + c[4]/3600.e6; &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-- -50.975864  
> 
> ```


{ .use-head}
Use in string representations

When a compound plane angle measure is formatted for display or printout, the signs of the fractional components will usually be discarded because, to a human reader, the sign of the first component alone already indicates the sense of the angle:

> 
> ```
> 
(\* convert from compound to human-readable string \*)  
> &nbsp;&nbsp;s := FORMAT(c[1], '+##') &nbsp;&nbsp;&nbsp;&nbsp;+ "000000B0"  
> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;+ FORMAT(ABS(c[2]), '##') + ''''  
> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;+ FORMAT(ABS(c[3]), '##') + '"'  
> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;+ FORMAT(ABS(c[4]), '##'); &nbsp;-- -50&deg; 58' 33" 110400

> ```


Another often encountered display format of latitudes and longitudes is to omit the signs and print N, S, E, W indicators instead, for example, 
```
50&deg;58'33"S
```
. When stored as _IfcCompoundPlaneAngleMeasure_ however, a compound plane angle measure is always signed, with same sign of all components.

## Formal Propositions

### MinutesInRange
The second measure (minutes) shall be between -60 exclusive and 60 exclusive.

### SecondsInRange
The third measure (seconds) shall be between -60 exclusive and 60 exclusive.

### MicrosecondsInRange
The forth measure (millionth-seconds), if asserted, shall be between -1e6 exclusive and 1e6 exclusive.

### ConsistentSign
All non-zero measure components shall have the same sign (positive or negative).
