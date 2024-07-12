# Pset_PavementCommon

Describes the common properties and nominal dimensions of pavement.
<!-- end of short definition -->


**Property use clarification**
The nominal thickness of the pavement remains constant with the value from NominalThickness, unless the property NominalThicknessEnd is provided. In which case NominalThickness is the value at the beginning of a transition (usually at the object placement location). e.g. a (road) transition segment where the pavement object's linear placement along an alignment denotes the beginning location and NominalThicknessEnd is the value at the end as indicated by the property NominalLength. In the case of local placements, it is user defined along which axis lengths and widths are measured.
