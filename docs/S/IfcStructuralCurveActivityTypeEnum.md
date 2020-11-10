IfcStructuralCurveActivityTypeEnum
==================================
This enumeration defines the distribution of load values in a curve action or
reaction.  
  
> HISTORY  New enumeration in IFC4  
[ _bSI
Documentation_](https://standards.buildingsmart.org/IFC/DEV/IFC4_2/FINAL/HTML/schema/ifcstructuralanalysisdomain/lexical/ifcstructuralcurveactivitytypeenum.htm)


Attribute definitions
---------------------
| Attribute   | Description                                                                                                                                                                                                                                                       |
|-------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| PARABOLA    | The load value is distributed as a half wave described by a symmetric quadratic parabola.                                                                                                                                                                         |
| SINUS       | The load value is distributed as a sinus half wave.                                                                                                                                                                                                               |
| CONST       |                                                                                                                                                                                                                                                                   |
| LINEAR      |                                                                                                                                                                                                                                                                   |
| DISCRETE    |                                                                                                                                                                                                                                                                   |
| EQUIDISTANT | The load consists of n consecutive sections of same length and is specified by n+1 load samples. The interpolation type over the segments is not defined by this distribution type but may be qualified in _IfcObject.ObjectType_ based on additional agreements. |
| POLYGONAL   |                                                                                                                                                                                                                                                                   |

