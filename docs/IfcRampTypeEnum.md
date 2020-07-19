IfcRampTypeEnum
===============
This enumeration defines the basic configuration of the ramp type in terms of
the number and shape of ramp flights, as shown in Figure 1. The type also
distinguished turns by landings. In addition the subdivision of the straight
and changing direction ramps is included. The ramp configurations are given
for ramps without and with one and two landings.  
  
Ramps which are subdivided into more than two landings, or ramps with non-
regular shapes are to be defined with type being USERDEFINED or NOTDEFINED.  
  
> HISTORY  New enumeration in IFC2.0.  
  
  
  
  
  
  
|  _Enumerator_  
|  _Description_  
|  _Figure_  
  
---|---|---  
  
  
StraightRunRamp  
| A ramp - which is a sloping floor, walk, or roadway - connecting two levels.  
The straight ramp consists of one straight flight without turns or winders.  
| ![](figures/ifcramptypeenum-fig01.gif)  
  
  
  
TwoStraightRunRamp  
| A straight ramp consisting of two straight flights without turns but with
one  
landing.  
| ![](figures/ifcramptypeenum-fig02.gif)  
  
  
  
QuarterTurnRamp  
| A ramp making a 90° turn, consisting of two straight flights connected by  
a quarterspace landing. The direction of the turn is determined by the walking
line.  
| ![](figures/ifcramptypeenum-fig03.gif)  
  
  
  
TwoQuarterTurnRamp  
| A ramp making a 180° turn, consisting of three straight flights connected  
by two quarterspace landings. The direction of the turn is determined by the
walking line.  
| ![](figures/ifcramptypeenum-fig04.gif)  
  
  
  
HalfTurnRamp  
| A ramp making a 180° turn, consisting of two straight flights connected  
by a halfspace landing. The orientation of the turn is determined by the
walking line.  
| ![](figures/ifcramptypeenum-fig05.gif)  
  
  
  
SpiralRamp  
| A ramp constructed around a circular or elliptical well without newels and  
landings.  
| ![](figures/ifcramptypeenum-fig06.gif)  
  
  
  
UserDefined  
| Free form ramp (user defined operation type)  
|  
  
  
  
NotDefined  
|  
|  
  
  
  
  
  
  
  
  

Figure 1 -- Ramp types

  
  
  
  
  
[ _bSI
Documentation_](https://standards.buildingsmart.org/IFC/DEV/IFC4_2/FINAL/HTML/schema/ifcsharedbldgelements/lexical/ifcramptypeenum.htm)


