IfcConversionBasedUnit
======================
An IfcConversionBasedUnit is used to define a unit that has a conversion rate
to a base unit. To identify some commonly used conversion based units, the
standard designations (case insensitive) for the _Name_ attribute are
indicated in Table 1.  
  
  
  
  
  
  
\X\09|  _ **Name**_ \X\09|  _ **Description**_  
---|---  
  
\X\09''inch''\X\09\X\09| Length measure equal to 25.4 mm  
  
\X\09''foot''\X\09\X\09| Length measure equal to 304.8 mm  
  
\X\09''yard''\X\09\X\09| Length measure equal to 914 mm  
  
\X\09''mile''\X\09\X\09| Length measure equal to 1609 m  
  
\X\09''square inch''\X\09| Area measure equal to 0.0006452 square meters  
  
\X\09''square foot''\X\09| Area measure equal to 0.09290 square meters  
  
\X\09''square yard''\X\09| Area measure equal to 0.83612736 square meters  
  
\X\09''acre''\X\09\X\09| Area measure equal to 4046.86 square meters  
  
\X\09''square mile''\X\09| Area measure equal to 2 588 881 square meters  
  
\X\09''cubic inch''\X\09| Volume measure equal to 0.00001639 cubic meters  
  
\X\09''cubic foot''\X\09| Volume measure equal to 0.02832 cubic meters  
  
\X\09''cubic yard''\X\09| Volume measure equal to 0.7636 cubic meters  
  
\X\09''litre''\X\09\X\09| Volume measure equal to 0.001 cubic meters  
  
\X\09''fluid ounce UK''\X\09| Volume measure equal to 0.0000284130625 cubic
meters  
  
\X\09''fluid ounce US''\X\09| Volume measure equal to 0.00002957353 cubic
meters  
  
\X\09''pint UK''\X\09\X\09| Volume measure equal to 0.000568 cubic meters  
  
\X\09''pint US''\X\09\X\09| Volume measure equal to 0.000473 cubic meters  
  
\X\09''gallon UK''\X\09| Volume measure equal to 0.004546 cubic meters  
  
\X\09''gallon US''\X\09| Volume measure equal to 0.003785 cubic meters  
  
\X\09''degree''\X\09\X\09| Angle measure equal to π/180 rad  
  
\X\09''ounce''\X\09\X\09| Mass measure equal to 28.35 g  
  
\X\09''pound''\X\09\X\09| Mass measure equal to 0.454 kg  
  
\X\09''ton UK''\X\09\X\09| Mass measure equal to 1016.0469088 kg, also known
as long ton, gross ton, shipper''s ton  
  
\X\09''ton US''\X\09\X\09| Mass measure equal to 907.18474 kg, also known as
short ton, net ton  
  
\X\09''lbf''\X\09\X\09| Force measure equal to 4.4482216153 N, pound-force  
  
\X\09''kip''\X\09\X\09| Force measure equal to 4448.2216153 N, kilopound-force  
  
\X\09''psi''\X\09\X\09| Pressure measure equal to 6894.7572932 Pa, pound-force
per square inch  
  
\X\09''ksi''\X\09\X\09| Pressure measure equal to 6894757.2932 Pa, kilopound-
force per square inch  
  
\X\09''minute''\X\09\X\09| Time measure equal to 60 s  
  
\X\09''hour''\X\09\X\09| Time measure equal to 3600 s  
  
\X\09''day''\X\09\X\09| Time measure equal to 86400 s  
  
\X\09''btu''\X\09\X\09| Energy measure equal to 1055.056 J, British Thermal
Unit  
  
  
  
  

Table 1 -- Standard unit names  
  
  
  
  
> EXAMPLE  An inch is a converted unit. It is from the Imperial system, its
> name is "inch" and it can be related to the SI unit, millimetre, through a
> measure with unit whose value is 25.4 millimetre. A foot is also a converted
> unit. It is from the Imperial system, its name is "foot" and it can be
> related to an _IfcSIUnit_, millimetre, either directly or through the unit
> called "inch". Note that several US customary units differ from Imperial
> units (nonmetric English units) of the same name.  
  
{ .extDef}  
> NOTE  Definition according to ISO/CD 10303-41:1992  
> A conversion based unit is a unit that is defined based on a measure with
> unit.  
  
> NOTE  Entity adapted from **conversion_based_unit** defined in ISO 10303-41.  
  
> HISTORY  New entity in IFC1.5.1.  
  
{ .change-ifc2x3}  
> IFC2x3 CHANGE  Standard names of typical units added.  
  
{ .change-ifc2x4}  
> IFC4 CHANGE  Further names added: square inch, square foot, square mile,
> square yard, cubic inch, cubic foot, cubic yard, fluid ounce UK/US, ton
> UK/US, degree.  
[ _bSI
Documentation_](https://standards.buildingsmart.org/IFC/DEV/IFC4_2/FINAL/HTML/schema/ifcmeasureresource/lexical/ifcconversionbasedunit.htm)


Attribute definitions
---------------------
| Attribute            | Description                                                                     |
|----------------------|---------------------------------------------------------------------------------|
| HasExternalReference |                                                                                 |
| ConversionFactor     |                                                                                 |
| Name                 | The word, or group of words, by which the conversion based unit is referred to. |

