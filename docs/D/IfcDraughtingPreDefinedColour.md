IfcDraughtingPreDefinedColour
=============================
The draughting pre defined colour is a pre defined colour for the purpose to
identify a colour by name. Allowable names are:  
  
* ''black'',  
* ''red'',  
* ''green'',  
* ''blue'',  
* ''yellow'',  
* ''magenta'',  
* ''cyan'',  
* ''white'',  
* ''by layer''  
  
> NOTE \S\ The _IfcDraughtingPreDefinedColour_ is an entity that had been
> adopted from ISO 10303-202, Industrial automation systems and integration--
> Product data representation and exchange, Part 202: Application protocol:
> Associative draughting.  
  
The following table states the RGB values associated with the names given by
the _IfcDraughtingPreDefinedColour._  
  
>  
  
  
**Colour name**  
|  **Red**  
|  **Green**  
|  **Blue**  
  
---|---|---|---  
  
  
black  
| 0  
| 0  
| 0  
  
  
  
red  
| 1.0  
| 0  
| 0  
  
  
  
green  
| 0  
| 1.0  
| 0  
  
  
  
blue  
| 0  
| 0  
| 1.0  
  
  
  
yellow  
| 1.0  
| 1.0  
| 0  
  
  
  
magenta  
| 1.0  
| 0  
| 1.0  
  
  
  
cyan  
| 0  
| 1.0  
| 1.0  
  
  
  
white  
| 1.0  
| 1.0  
| 1.0  
  
  
  
by layer  
| colour values obtained from  
  
 _IfcPresentationLayerWithStyle_.  
|  
|  
  
  
  
  
  
> NOTE \S\ Corresponding ISO 10303 name: draughting_pre_defined_colour. Please
> refer to ISO/IS 10303-202:1994 page 194 for the final definition of the
> formal standard.  
  
> HISTORY \S\ New entity in IFC2x2.  
  
{ .spec-head}  
Informal Propositions:  
  
1\. The value ''by layer'' shall only be inserted, if the geometric
representation item using the colour definition has an association to
_IfcPresentationLayerWithStyle_, and if that instance of
_IfcPresentationLayerWithStyle_ has a valid colour definition for
_IfcCurveStyle_, _IfcSymbolStyle_, or _IfcSurfaceStyle_ (depending on what is
applicable).  
[ _bSI
Documentation_](https://standards.buildingsmart.org/IFC/DEV/IFC4_2/FINAL/HTML/schema/ifcpresentationappearanceresource/lexical/ifcdraughtingpredefinedcolour.htm)


