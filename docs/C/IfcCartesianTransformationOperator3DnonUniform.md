IfcCartesianTransformationOperator3DnonUniform
==============================================
A Cartesian transformation operator 3d non uniform defines a geometric
transformation in three-dimensional space composed of translation, rotation,
mirroring and non uniform scaling. Non uniform scaling is given by three
different scaling factors:  
  
* _SELF\\\IfcCartesianTransformationOperator.Scale_: the x axis scale factor  
* _Scale2_: the y axis scale factor  
* _Scale3_: the z axis scale factor  
  
If the _Scale_ factor (at supertype _IfcCartesianTransformationOperator_) is
omitted, it defaults to 1.0. If the _Scale2_ or the _Scale3_ factor is
omitted, it defaults to the value of _Scale_ (the x axis scale factor).  
  
> NOTE  The scale factor (_Scl_) defined at the supertype
> _IfcCartesianTransformationOperator_ is used to express the calculated
> _Scale_ factor (normally x axis scale factor).  
  
> HISTORY  New entity in IFC2x.  
[ _bSI
Documentation_](https://standards.buildingsmart.org/IFC/DEV/IFC4_2/FINAL/HTML/schema/ifcgeometryresource/lexical/ifccartesiantransformationoperator3dnonuniform.htm)


Attribute definitions
---------------------
| Attribute   | Description                                                                                                                                                                                     |
|-------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Scale2      | The scaling value specified for the transformation along the axis 2. This is normally the y scale factor.                                                                                       |
| Scale3      | The scaling value specified for the transformation along the axis 3. This is normally the z scale factor.                                                                                       |
| Scl2        | The derived scale S(2) of the transformation along the axis 2 (normally the y axis), equal to Scale2 if that exists, or equal to the derived Scl1 (normally the x axis scale factor) otherwise. |
| Scl3        | The derived scale S(3) of the transformation along the axis 3 (normally the z axis), equal to Scale3 if that exists, or equal to the derived Scl1 (normally the x axis scale factor) otherwise. |

