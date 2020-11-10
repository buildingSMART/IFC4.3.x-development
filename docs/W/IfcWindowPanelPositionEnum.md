IfcWindowPanelPositionEnum
==========================
This enumeration defines the basic configuration of the window type in terms
of the location of window panels. The window configurations are given for
windows with one, two or three panels (including fixed panels) as shown in
Figure 1. It corresponds to the _OperationType_ of the _IfcWindowStyle_
definition, which references the _IfcWindowPanelProperties_.  
  
Windows which are subdivided into more than three panels have to be defined by
the geometry only. The type of such windows is given by an
_IfcWindowType.OperationType_ = USERDEFINED or NOTDEFINED (see
_IfcWindowStyleOperationEnum_ for details).  
  
  
  
\X\09  
\X\09 | _Enumerator from IfcWindowStyleOperationEnum_  
\X\09 | _Use of enumerators from IfcWindowPanelPositionEnum_  
\X\09 | _Figure_  
\X\09  
---|---|---  
  
\X\09  
\X\09 DoublePanelVertical  
\X\09 | first  
\X\09\X\09 IfcWindowPanelProperties with PanelPosition = LEFT  
second  
\X\09\X\09 IfcWindowPanelProperties with PanelPosition = RIGHT  
\X\09 | ![](../figures/ifcwindowpanelpositionenum-fig01.gif)  
\X\09  
  
\X\09  
\X\09 DoublePanelHorizontal  
\X\09 | first  
\X\09\X\09 IfcWindowPanelProperties with PanelPosition = TOP  
second  
\X\09\X\09 IfcWindowPanelProperties with PanelPosition = BOTTOM  
\X\09 | ![](../figures/ifcwindowpanelpositionenum-fig02.gif)  
\X\09  
  
\X\09  
\X\09 TriplePanelVertical  
\X\09 | first  
\X\09\X\09 IfcWindowPanelProperties with PanelPosition = LEFTsecond  
\X\09\X\09 IfcWindowPanelProperties with PanelPosition = MIDDLE  
third  
\X\09\X\09 IfcWindowPanelProperties with PanelPosition = RIGHT  
\X\09 | ![](../figures/ifcwindowpanelpositionenum-fig03.gif)  
\X\09  
  
\X\09  
\X\09 TriplePanelHorizontal  
\X\09 | first  
\X\09\X\09 IfcWindowPanelProperties with PanelPosition = TOP  
second  
\X\09\X\09 IfcWindowPanelProperties with PanelPosition = MIDDLE  
third  
\X\09\X\09 IfcWindowPanelProperties with PanelPosition = BOTTOM  
\X\09 | ![](../figures/ifcwindowpanelpositionenum-fig04.gif)  
\X\09  
  
\X\09  
\X\09 TriplePanelBottom  
\X\09 | first  
\X\09\X\09 IfcWindowPanelProperties with PanelPosition = LEFT  
second  
\X\09\X\09 IfcWindowPanelProperties with PanelPosition = RIGHT  
third  
\X\09\X\09 IfcWindowPanelProperties with PanelPosition = BOTTOM  
\X\09 | ![](../figures/ifcwindowpanelpositionenum-fig05.gif)  
\X\09  
  
\X\09  
\X\09 TriplePanelTop  
\X\09 | first  
\X\09\X\09 IfcWindowPanelProperties with PanelPosition = TOP  
second  
\X\09\X\09 IfcWindowPanelProperties with PanelPosition = LEFT  
third  
\X\09\X\09 IfcWindowPanelProperties with PanelPosition = RIGHT  
\X\09 | ![](../figures/ifcwindowpanelpositionenum-fig06.gif)  
\X\09  
  
\X\09  
\X\09 TriplePanelLeft  
\X\09 | first  
\X\09\X\09 IfcWindowPanelProperties with PanelPosition = LEFT  
second  
\X\09\X\09 IfcWindowPanelProperties with PanelPosition = TOP  
third  
\X\09\X\09 IfcWindowPanelProperties with PanelPosition = BOTTOM  
\X\09 | ![](../figures/ifcwindowpanelpositionenum-fig07.gif)  
\X\09  
  
\X\09  
\X\09 TriplePanelRight  
\X\09 | first  
\X\09\X\09 IfcWindowPanelProperties with PanelPosition = TOP  
second  
\X\09\X\09 IfcWindowPanelProperties with PanelPosition = BOTTOM  
third  
\X\09\X\09 IfcWindowPanelProperties with PanelPosition = RIGHT  
\X\09 | ![](../figures/ifcwindowpanelpositionenum-fig08.gif)  
\X\09  
  
  
  
  

Figure 1 -- Window panel positions  
  
  
  
  
> HISTORY  New enumeration in IFC2.0.  
  
NOTE  
  
1\. The figures are shown as elevations in the XZ plane of the local placement
of the window, looking into the direction of the positive Y axis.  
2\. These figures are only shown as illustrations.  
[ _bSI
Documentation_](https://standards.buildingsmart.org/IFC/DEV/IFC4_2/FINAL/HTML/schema/ifcarchitecturedomain/lexical/ifcwindowpanelpositionenum.htm)


