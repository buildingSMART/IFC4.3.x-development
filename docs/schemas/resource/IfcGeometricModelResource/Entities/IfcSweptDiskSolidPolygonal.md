# IfcSweptDiskSolidPolygonal

The _IfcSweptDiskSolidPolygonal_ is a _IfcSweptDiskSolid_ where the _Directrix_ is restricted to be provided by an poly line only. An optional _FilletRadius_ attribute can be asserted, it is then applied as a fillet to all transitions between the segments of the poly line.

> NOTE  The geometric item _IfcIndexedPolyCurve_ provides a more compact representation compared with _IfcPolyline_. Therefore it is the preferred curve representation for the _Directrix_. The _IfcIndexedPolyCurve_ shall not have _Segments_ defined, resticting it to a poly line only.

> HISTORY  New entity in IFC4.

## Informal Propositions

1. The _FilletRadius_, if provided, has to be smaller than or equal to the length of the start and end segment of the _IfcPolyline_, and smaller than or equal to one half of the length of the shortest inner segment.

## Attributes

### FilletRadius
The fillet that is equally applied to all transitions between the segments of the _IfcPolyline_, providing the geometric representation for _the Directrix_. If omitted, no fillet is applied to the segments.

## Formal Propositions

### CorrectRadii
If a _FilletRadius is given_, it has to be greater or equal to the _Radius_ of the disk.

### DirectrixIsPolyline
The _Directrix_ shall be of type _IfcIndexedPolyCurve_ with no _Segments_, or of type _IfcPolyline_.
