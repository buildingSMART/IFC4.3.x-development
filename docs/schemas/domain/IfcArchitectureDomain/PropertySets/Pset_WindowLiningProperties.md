# Pset_WindowLiningProperties

Properties of the window lining.

> HISTORY New property set in IFC4.3.2.0 to replace the entity IfcWindowLiningProperties

## Comments

### LiningDepth
For a window, it is the depth of the window lining, measured perpendicularly to window elevation plane.

### LiningOffset
For a window, it is the offset of the window lining, given as distance along the y axis of the local placement (perpendicular to the window plane).

### LiningThickness
For a window, it is the thickness of the window lining as explained in the figure below. If _LiningThickness_ value is 0. (zero) it denotes a window without a lining (all other lining parameters shall be set to NIL in this case). If the _LiningThickness_ is NIL it denotes that the value is not available.

### LiningToPanelOffsetX
For a window, it is the offset between the lining and the window panel. Should be smaller or equal to the _LiningThickness_.

### LiningToPanelOffsetY
For a window, it is the offset between the lining and the window panel. Should be smaller or equal to the _IfcWindowPanelProperties.PanelThickness_.

### MullionThickness
For a window, it is the thickness of the mullion (i.e., the vertical separator of window panels within a window), measured parallel to the window elevation plane. The mullion is part of the lining and the mullion depth is assumed to be identical to the lining depth. If the _MullionThickness_ is set to zero (and the _MullionOffset_ set to a positive length), then the window is divided horizontally without a physical divider.

### TransomThickness
For a window, it is the thickness of the transom (horizontal separator of window panels within a window), measured parallel to the window elevation plane. The transom is part of the lining and the transom depth is assumed to be identical to the lining depth. If the _TransomThickness_ is set to zero (and the _TransomOffset_ set to a positive length), then the window is divided vertically without a physical divider.