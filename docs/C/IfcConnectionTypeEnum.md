IfcConnectionTypeEnum
=====================
This enumeration defines the different ways how path based elements (such as
_IfcWallStandardCase_) can connect, as shown in Figure 1.  
  
> HISTORY  New type in IFC2.0  
  
The enumerated items shall be used in the following combinations:  
  
  
  
  
  
  
| Connection type  
| Illustration  
  
---|---  
  
  
  
  
  

L-Shape Connection

  

  

  * RelatingConnectionType: AtStart
  

  * RelatedConnectionType: AtStart
  

  
  
| ![](../figures/IfcConnectionTypeEnum-Fig03.gif)  
  
  
  
  

L-Shape Connection

  

  

  * RelatingConnectionType: AtEnd
  

  * RelatedConnectionType: AtStart
  

  
  
| ![](../figures/IfcConnectionTypeEnum-Fig01.gif)  
  
  
  
  

T-Shape Connection

  

  

  * RelatingConnectionType: AtPath
  

  * RelatedConnectionType: AtStart
  

  
  
| ![](../figures/IfcConnectionTypeEnum-Fig02.gif)  
  
  
  
  
  
  
  
  

Figure 1 -- Connection types

  
  
  
  
  
[ _bSI
Documentation_](https://standards.buildingsmart.org/IFC/DEV/IFC4_2/FINAL/HTML/schema/ifcsharedbldgelements/lexical/ifcconnectiontypeenum.htm)


Attributes
----------
| Attribute   | Definition   |
|-------------|--------------|
| ATEND       |              |
| ATPATH      |              |
| ATSTART     |              |
| NOTDEFINED  |              |
