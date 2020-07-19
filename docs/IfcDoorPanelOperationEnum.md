IfcDoorPanelOperationEnum
=========================
This enumeration defines the basic ways how individual door panels operate as
shown in Figure 1.  
  
  
  
  
  
  
| Enumerator  
| Illustration  
  
---|---  
  
  
Swinging  
| ![](figures/ifcdoorpaneloperationenum-fig01.gif)  
  
  
  
DoubleActing  
| ![](figures/ifcdoorpaneloperationenum-fig02.gif)  
  
  
  
Sliding  
| ![](figures/ifcdoorpaneloperationenum-fig03.gif)  
  
  
  
Folding  
| ![](figures/ifcdoorpaneloperationenum-fig04.gif)  
  
  
  
Revolving  
| ![](figures/ifcdoorpaneloperationenum-fig05.gif)  
  
  
  
Rollingup  
| ![](figures/ifcdoorpaneloperationenum-fig06.gif)  
  
  
  
FixedPanel  
| ![](figures/ifcdoorpaneloperationenum-fig07.gif)  
  
  
  
  
UserDefined  
|  
  
  
  
NotDefined  
|  
  
  
  
  
  
  
  

Figure 1 -- Door operations

  
  
  
  
  
The opening direction of the door panels is given by the local placement of
the _IfcDoor_. The positive y-axis determines the direction as shown in Figure
2.  
  
!["panel direction"](figures/ifcdoorpaneloperationenum-fig10.gif "Figure 2 --
Door panel operations")  
  
> NOTE  Figures (symbolic representation) depend on the national building
> code. These figures are only shown as illustrations  
  
> HISTORY  New enumeration in IFC2.0.  
  
{ .change-ifc2x4}  
> IFC4 CHANGE  Enumerator FIXEDPANEL added.  
[ _bSI
Documentation_](https://standards.buildingsmart.org/IFC/DEV/IFC4_2/FINAL/HTML/schema/ifcarchitecturedomain/lexical/ifcdoorpaneloperationenum.htm)


Attributes
----------
| Attribute     | Definition   |
|---------------|--------------|
| DOUBLE_ACTING |              |
| FIXEDPANEL    |              |
| FOLDING       |              |
| NOTDEFINED    |              |
| REVOLVING     |              |
| ROLLINGUP     |              |
| SLIDING       |              |
| SWINGING      |              |
| USERDEFINED   |              |
