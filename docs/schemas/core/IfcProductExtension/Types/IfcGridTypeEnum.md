# IfcGridTypeEnum

This enumeration defines the different layout types of grids. Restriction on the correct use of _IfcGrid_ instantiations may be imposed depending on the value of the _PredefinedType_ being _IfcGridTypeEnum_.

> HISTORY&nbsp; New enumeration in IFC4.

> NOTE&nbsp; View definitions or implementer agreements may impose further restrictions on how to populate the grid axes. The first grid axis being part of u-axes may have to be parallel to the x-axis of the grid object placement.

## Items

### RECTANGULAR
An _IfcGrid_ with straight u-axes and straight v-axes being perpendicular to each other. All grid axes being part of u-axes can be described by one axis line and all other axes being 2D offsets from this axis line. The same applies to all grid axes being part of V-axes.

### RADIAL


### TRIANGULAR


### IRREGULAR


### USERDEFINED
Any other grid not conforming to any of the above restrictions.

### NOTDEFINED

