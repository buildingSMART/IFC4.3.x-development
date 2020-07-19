IfcMaterialLayer
================
_IfcMaterialLayer_ is a single and identifiable part of an element which is
constructed of a number of layers (one or more). Each _IfcMaterialLayer_ has a
constant thickness and is located relative to the referencing
_IfcMaterialLayerSet_ along the material layer set base (MlsBase).  
  
Air gaps within a material layer set are represented as an _IfcMaterialLayer_
with the attribute _IsVentilated_ having the value TRUE or UNKNOWN. Such air
gaps shall be interpreted as voids (not having a material).  
  
> EXAMPLE  A cavity wall with brick masonry used with an air gap in between
> would be modeled using three _IfcMaterialLayer_''s: [1] Brick, [2] Air gap,
> [3] Brick. The inner layer "Brick" would have a _Name_ = "Brick", an
> individual _LayerThickness_, and potentially a _Category_ indicating it as
> "load bearing", and a _Priority_ that controls how this material layer
> interacts with other material layers in wall connections.  
  
The _IfcMaterialLayer_ may have a material layer name which may differ from
the _IfcMaterial_ name referenced.  
  
> EXAMPLE  The _IfcMaterialLayer_ name of an insulation layer can be
> "Insulation", whereas the _IfcMaterial_ name is "polystyrene insulating
> boards".  
  
> HISTORY  New entity in IFC1.5  
  
{ .change-ifc2x4}  
> IFC4 CHANGE  The attributes _Name_, _Description_, _Category_, _Priority_
> have been added at the end of attribute list. Data type of _LayerThickness_
> relaxed to _IfcNonNegativeLengthMeasure_.  
[ _bSI
Documentation_](https://standards.buildingsmart.org/IFC/DEV/IFC4_2/FINAL/HTML/schema/ifcmaterialresource/lexical/ifcmateriallayer.htm)


