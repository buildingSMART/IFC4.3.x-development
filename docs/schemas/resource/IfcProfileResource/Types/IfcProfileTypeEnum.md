# IfcProfileTypeEnum

The enumeration defines whether the definition of a profile shape shall be geometrically resolved into a curve or into a surface.

> HISTORY  New type in IFC1.5.

## Items

### CURVE
The resulting geometric item is of type curve and closed (with the only exception of the curve created by the _IfcArbitraryOpenProfileDef_ which resolves into an open curve). The resulting geometry after applying a sweeping operation is a swept surface. This can be used to define shapes with thin sheets, such as ducts, where the thickness is not appropriate for geometric representation.

### AREA
The resulting geometric item is of type surface. The resulting geometry after applying a sweeping operation is a swept solid with defined volume.
