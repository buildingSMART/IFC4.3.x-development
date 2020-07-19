IfcTendon
=========
A tendon is a steel element such as a wire, cable, bar, rod, or strand used to
impart prestress to concrete when the element is tensioned.  
  
{ .extDef}  
> NOTE  Definition according to ISO 6707-1: steel bar(s) or groups of bars,
> strands or wires given a tensile stress that produces a compressive stress
> in prestressed concrete or masonry.  
  
{ .extDef}  
> NOTE  To be efficient, the cable follows the deck alignment and moves
> vertically up on the top of the piers and down in the middle of the span.
> Therefore the cable axis is defined relatively towards the deck alignment.
> The ShapeRepresentation should be ''AdvancedSweptSolid'' geometry based on
> SectionedSolidHorizontal description including DistanceExpression,
> CircleProfileDef and AlignmentCurve, leading to a polyline describing the
> cable directrix.  
  
{ .extDef}  
> NOTE  Regarding the Structural Analysis model, the cable has to be
> transformed into loads applied at each CartesianPoint defining the polyline.  
  
> HISTORY  New entity in IFC2x2.  
  
{ .change-ifc2x4}  
> IFC4 CHANGE  Attribute _PredefinedType_ made optional. _NominalDiameter_ and
> _CrossSectionArea_ made optional and deprecated; this information can now be
> provided by _IfcTendonType_. Description of _FrictionCoefficient_ corrected.  
[ _bSI
Documentation_](https://standards.buildingsmart.org/IFC/DEV/IFC4_2/FINAL/HTML/schema/ifcstructuralelementsdomain/lexical/ifctendon.htm)


