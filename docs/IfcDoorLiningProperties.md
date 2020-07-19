IfcDoorLiningProperties
=======================
The door lining is the frame which enables the door leaf to be fixed in
position. The door lining is used to hang the door leaf. The parameters of the
door lining define the geometrically relevant parameter of the lining.  
  
> NOTE  The _IfcDoorLiningProperties_ shall only be applied by the receiving
> application to parametrically define the 3D shape of a door, if the
> attribute _IfcDoorType_.ParameterTakesPrecedence is set TRUE.  
  
The _IfcDoorLiningProperties_ are included in the list of properties of
_IfcDoorType_.HasPropertySets. More information about the door lining can be
included in the same list of the _IfcDoorTyype_ using another _IfcPropertySet_
for dynamic extensions.  
  
The _IfcDoorLiningProperties_ does not hold its own geometric representation.
However it defines parameters which can be used to create the shape of the
door type (which is inserted by the _IfcDoor_ into the spatial context of the
project) as shown in Figure 1. The parameters of the _IfcDoorLiningProperties_
define a standard door lining, including (if given) a threshold and a transom.
The outer boundary of the lining is determined by the ''Profile'' shape
representation assigned to the _IfcDoor_, which inserts the _IfcDoorType_.  
  
  
  
  
  
  
  
  
| ![lining 1](figures/ifcdoorliningproperties-fig01.png)  
| The lining is applied to the left, right and upper side of the opening
reveal. The parameters are:  

  

  * _LiningDepth_ , if omited, equal to wall thickness - this only takes effect if a value for _LiningThickness_ is given. If both parameters are not given, then there is no lining.
  

  * _LiningThickness_
  

  * _LiningToPanelOffsetX_
  

  * _LiningToPanelOffsetY_
  

  

> NOTE  The parameters _LiningToPanelOffsetX_ and _LiningToPanelOffsetY_ are
> added in IFC4.

  
  
  
---|---  
  
  
![lining 2](figures/ifcdoorliningproperties-fig02.png)  
| The lining can only cover part of the opening reveal.  

  

  * _LiningOffset_ : given if lining edge has an offset to the x axis of the local placement.
  

  

> NOTE  In addition to the\S\ _LiningOffset_ , the local placement of the
> _IfcDoor_ can already have an  
>  offset to the wall edge and thereby shift the lining along the y axis. The
> actual position of the lining is calculated from the  
>  origin of the local placement along the positive y axis with the distance
> given by _LiningOffset_.

  
  
  
  
  
![lining 3](figures/ifcdoorliningproperties-fig03.png)  
| The lining may include a casing, which covers part of the wall faces around
the opening. The  
casing covers the left, right and upper side of the lining on both sides of
the wall. The parameters are:  

  

  * _CasingDepth_
  

  * _CasingThickness_
  

  
  
  
  
  
![lining 4](figures/ifcdoorliningproperties-fig04.png)  
| The lining may include a threshold, which covers the bottom side of the
opening. The parameters are:  

  

  * _ThresholdDepth_ -- if omited, equal to wall thickness - this only takes effect if a value for _ThresholdThickness_ is  
given. If both parameters are not given, then there is no threshold.

  

  * _ThresholdThickness_
  

  * _ThresholdOffset_ (not shown in figure): given, if the threshold edge has an offset to the x axis of the local placement.
  

  
  
  
  
  
![lining 5](figures/ifcdoorliningproperties-fig05.png)  
| The lining may have a transom which separates the door panel from a window
panel. The transom, if given, is defined by:  

  

  * _TransomOffset_ : a parallel edge to the x axis of the local placement
  

  * _TransomThickness_
  

  

The depth of the transom is identical to the depth of the lining and not given
as separate parameter.

  
  
  
  
  
  
  
  
  

Figure 1 -- Door lining properties

  
  
  
  
  
> NOTE  _LiningDepth_ describes the length of the lining along the reveal of
> the door opening. It can be given by an absolute value if the door lining
> has a specific depth depending on the door style. However often it is equal
> to the wall thickness. If the same door style is used (like the same type of
> single swing door), but inserted into different walls with different
> thicknesses, it would be necessary to create a special door style for each
> wall thickness. Therefore several CAD systems allow to set the value to
> "automatically aligned" to wall thickness. This should be exchanged by
> leaving the optional attribute LiningDepth unassigned. The same agreement
> applies to _ThresholdDepth_.  
  
> HISTORY  New entity in IFC2.0. Has been renamed from _IfcDoorLining_ in
> IFC2x.  
  
{ .change-ifc2x4}  
> IFC4 CHANGE  The following attributes have been added
> _LiningToPanelOffsetX_, _LiningToPanelOffsetY_. The attribute
> _ShapeAspectStyle_ is deprecated and shall no longer be used. Supertype
> changed to new _IfcPreDefinedPropertySet_.  
[ _bSI
Documentation_](https://standards.buildingsmart.org/IFC/DEV/IFC4_2/FINAL/HTML/schema/ifcarchitecturedomain/lexical/ifcdoorliningproperties.htm)


