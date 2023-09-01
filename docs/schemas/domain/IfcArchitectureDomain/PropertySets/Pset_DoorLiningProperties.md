# Pset_DoorLiningProperties

Properties of the door lining.

> HISTORY New property set in IFC4.3.2.0 to replace the entity IfcDoorLiningProperties

## Comments

### CasingDepth

For a door, it is the dimension in the plane perpendicular to door leaf. If given it is applied equally to all four sides of the adjacent wall.

### CasingThickness
For a door, it is the dimension in plane of the door leaf. If given it is applied equally to all four sides of the adjacent wall.

### LiningDepth
For a door, it is the depth of the door lining, measured perpendicular to the plane of the door lining. If omitted (and with a given value to lining thickness) it indicates an adjustable depth (i.e. a depth that adjusts to the thickness of the wall into which the occurrence of this door style is inserted).

### LiningOffset
For a door, it is the offset (dimension in plane perpendicular to door leaf) of the door lining. The offset is given as distance to the x axis of the local placement.

### LiningThickness
For a door, it is the thickness of the door lining as explained in the figure above. If _LiningThickness_ value is 0. (zero) it denotes a door without a lining (all other lining parameters shall be set to NIL in this case). If the _LiningThickness_ is NIL it denotes that the value is not available.

### LiningToPanelOffsetX
For a door, it is the offset between the lining and the window panel.

### LiningToPanelOffsetY
For a door, it is the offset between the lining and the door panel.

### TransomThickness
For a door, it is the thickness (width in plane parallel to door leaf) of the transom (if provided - that is, if the _TransomOffset_ attribute is set), which divides the door leaf from a glazing (or window) above. If the _TransomThickness_ is set to zero (and the _TransomOffset_ set to a positive length), then the door is divided vertically into a leaf and transom window area without a physical frame.