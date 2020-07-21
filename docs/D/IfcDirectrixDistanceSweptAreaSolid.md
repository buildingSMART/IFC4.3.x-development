IfcDirectrixDistanceSweptAreaSolid
==================================
An abstract entity defining common information about a type of swept area
solid which is the result of sweeping an area along a Directrix. The swept
area is provided by a subtype of IfcProfileDef. The profile is placed by an
implicit cartesian transformation operator at the start point of the sweep.
The profile normal is where the profile normal agrees to the tangent of the
directrix at this point. The rule of orientation of profile’s x-axis is
specialized by the subtypes of IfcDirextrixDistanceSweptAreaSolid.  
The start of the sweeping operation is at the StartDistance, provided by
IfcDistanceExpression. If no StartDistance is provided the start defaults to
the begin of the directrix. The end of the sweeping operation is at the
EndDistance, provided by IfcDistanceExpression. If no EndDistance is provided
the end defaults to the end of the directrix.  


Associations
------------
| Attribute     | Description   |
|---------------|---------------|
| Directrix     |               |
| EndDistance   |               |
| StartDistance |               |

