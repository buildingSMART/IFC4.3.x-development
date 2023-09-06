# Pset_DoorPanelProperties

Properties of the door panel.

> HISTORY New property set in IFC4.3.2.0 to replace the entity IfcDoorPanelProperties

## Comments

### PanelDepth
For a door, it is the depth of the door panel, measured perpendicular to the plane of the door leaf.

### PanelOperation
For a door, it is the way of operation of the panel. The _PanelOperation_ of the door panel shall correspond to the _OperationType_ of the _IfcDoorType_ by which it is referenced.

### PanelPosition
For a door, it is the position of the panel within the door. The _PanelPosition_ of the door panel shall correspond to the _OperationType_ of the _IfcDoorType_ by which it is referenced.

### PanelWidth
For a door, it is the width of the panel, given as ratio relative to the total clear opening width of the door. If omitted, it defaults to 1. A value shall be provided for all doors with _OperationType_'s at _IfcDoorType_ defining a door with more then one panel.