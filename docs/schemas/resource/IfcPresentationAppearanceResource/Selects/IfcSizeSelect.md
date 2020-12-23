The _IfcSizeSelect_ provides for the selection between different measure types used for provision of a length measure.

> NOTE&nbsp; global units are defined at the single _IfcProject_ instance, given by _UnitsInContext:IfcUnitAssignment_, the same units are used for the geometric representation items and for the style definitions.

{ .extDef}
> NOTE&nbsp; Definition according to ISO/CD 10303-46:1992  
> The size select is a selection of a specific positive length measure.

> NOTE&nbsp; Type adapted from **size_select** defined in ISO10303-46.

> HISTORY&nbsp; New select type in IFC2x2.

{ .change-ifc2x3}
> IFC2x3 CHANGE&nbsp; The SELECT item _IfcMeasureWithUnit_ has been removed from the _IfcSizeSelect_, the _IfcRatioMeasure_ and _IfcDescriptiveMeasure_ have been added.