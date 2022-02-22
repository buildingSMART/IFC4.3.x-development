# IfcDoorStyleOperationEnum

This enumeration defines the basic ways to describe how doors operate.

> HISTORY&nbsp; New enumeration in IFC2x.

Note:

1. Figures are shown in the ground view.
2. Figures (symbolic representation) depend on the national building code.
3. These figures/ are only shown as illustrations, the actual representation in the ground view might differ. 
4. Open to the outside is declared as open into the direction of the positive y-axis, determined by the _ObjectPlacement_ at _IfcDoor_
5. The location of the panel relative to the wall thickness is defined by the&nbsp;_ObjectPlacement_ at _IfcDoor_, and the _IfcDoorLiningProperties.LiningOffset_ parameter.

## Items

### SINGLE_SWING_LEFT
Door with one panel that opens (swings) to the left. The hinges are on the left side as viewed in the direction of the positive y-axis.

> NOTE Direction of swing (whether in or out) is determined at the <em>IfcDoor</em>.

![single swing left ](../../../../figures/ifcdoorstyleoperationenum-fig01.gif)

### SINGLE_SWING_RIGHT
Door with one panel that swings in both directions and to the right in the main trafic direction. Also called double acting door.

> NOTE Direction of swing (whether in or out) is determined at the <em>IfcDoor</em>.

![single swing right](../../../../figures/ifcdoorstyleoperationenum-fig02.gif)

### DOUBLE_DOOR_SINGLE_SWING
Door with two panels, one swings in both directions and to the right in the main trafic direction the other swings also in both directions and to the left in the main trafic direction.

> NOTE Direction of swing (whether in or out) is determined at the <em>IfcDoor</em>.

![double swing](../../../../figures/ifcdoorstyleoperationenum-fig03.gif)

### DOUBLE_DOOR_SINGLE_SWING_OPPOSITE_LEFT
Door with two panels that both open to the left, one panel swings in one direction and the other panel swings in the opposite direction.

> NOTE Direction of swing (whether in or out) is determined at the <em>IfcDoor</em>.

![opposite left](../../../../figures/ifcdoorstyleoperationenum-fig06a.gif)

### DOUBLE_DOOR_SINGLE_SWING_OPPOSITE_RIGHT
Door with two panels that both open to the right, one panel swings in one direction and the other panel swings in the opposite direction.

> NOTE Direction of swing (whether in or out) is determined at the <em>IfcDoor</em>.

![opposite right](../../../../figures/ifcdoorstyleoperationenum-fig06b.gif)

### DOUBLE_SWING_LEFT

> NOTE Direction of swing (whether in or out) is determined at the <em>IfcDoor</em>.

![double swing left](../../../../figures/ifcdoorstyleoperationenum-fig04.gif)

### DOUBLE_SWING_RIGHT

> NOTE Direction of swing (whether in or out) is determined at the <em>IfcDoor</em>.

![double swing right](../../../../figures/ifcdoorstyleoperationenum-fig05.gif)

### DOUBLE_DOOR_DOUBLE_SWING

> NOTE Direction of swing (whether in or out) is determined at the <em>IfcDoor</em>.

![double double swing](../../../../figures/ifcdoorstyleoperationenum-fig06.gif)

### SLIDING_TO_LEFT
Door with one panel that is sliding to the left.

![sliding to left](../../../../figures/ifcdoorstyleoperationenum-fig07.gif)

### SLIDING_TO_RIGHT
Door with one panel that is sliding to the right.

![sliding to right](../../../../figures/ifcdoorstyleoperationenum-fig08.gif)

### DOUBLE_DOOR_SLIDING
Door with two panels, one is sliding to the left the other is sliding to the right.

![double sliding](../../../../figures/ifcdoorstyleoperationenum-fig09.gif)

### FOLDING_TO_LEFT
Door with one panel that is folding to the left.

![folding to left](../../../../figures/ifcdoorstyleoperationenum-fig10.gif)

### FOLDING_TO_RIGHT
Door with one panel that is folding to the right.

![folding to right](../../../../figures/ifcdoorstyleoperationenum-fig11.gif)

### DOUBLE_DOOR_FOLDING
Door with two panels, one is folding to the left the other is folding to the right.

![double folding](../../../../figures/ifcdoorstyleoperationenum-fig12.gif)

### REVOLVING
An entrance door consisting of four leaves set in a form of a cross and revolving around a central vertical axis (the four panels are described by a single _IfcDoor_ panel property).

![revolving](../../../../figures/ifcdoorstyleoperationenum-fig13.gif)

### ROLLINGUP
Door that opens by rolling up.

> NOTE Whether it rolls up to the inside or outside is determined at the <em>IfcDoor</em>.

![rolling](../../../../figures/ifcdoorstyleoperationenum-fig14.gif)

### USERDEFINED
User defined operation type

![not defined](../../../../figures/ifcdoorstyleoperationenum-fig15.gif)

### NOTDEFINED
A door with a
not defined operation type is
considered as a door with a lining, but no panels. It is thereby always
open.
