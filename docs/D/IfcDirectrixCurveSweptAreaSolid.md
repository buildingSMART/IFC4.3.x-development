IfcDirectrixCurveSweptAreaSolid
===============================
An abstract entity defining common information about a type of swept area
solid which is the result of sweeping an area along a Directrix. The swept
area is provided by a subtype of IfcProfileDef. The profile is placed by an
implicit cartesian transformation operator at the start point of the sweep,
where the profile normal agrees to the tangent of the directrix at this point.
The direction of profile’s x-axis is specialized by the subtypes of
IfcDirextrixCurveSweptAreaSolid.  
The start of the sweeping operation is at the StartParam, the parameter value
is provided based on the curve parameterization. If no StartParam is provided
the start defaults to the begin of the directrix. The end of the sweeping
operation is at the EndParam, the parameter value is provided based on the
curve parameterization. If no EndParam is provided the end defaults to the end
of the directrix.  


