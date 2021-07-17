IfcCartesianTransformationOperator2DnonUniform
==============================================

A Cartesian transformation operator 2d non uniform defines a geometric transformation in two-dimensional space composed of translation, rotation, mirroring and non uniform scaling. Non uniform scaling is given by two different scaling factors:

* _SELF\IfcCartesianTransformationOperator.Scale_: the x axis scale factor
* _Scale2_: the y axis scale factor

If the _Scale_ factor (at supertype _IfcCartesianTransformationOperator_) is omitted, it defaults to 1.0. If the _Scale2_ factor is omitted, it defaults to the value of _Scale_ (the x axis scale factor).

> NOTE&nbsp; The scale factor (_Scl_) defined at the supertype _IfcCartesianTransformationOperator_ is used to express the calculated _Scale_ factor (normally x axis scale factor).

> HISTORY&nbsp; New entity in IFC2x.
