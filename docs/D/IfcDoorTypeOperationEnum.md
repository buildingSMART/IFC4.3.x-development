IfcDoorTypeOperationEnum
========================
This enumeration defines the basic ways to describe how an IfcDoor or
IfcDoorType operate, as shown in Figure 1. It combines the partitioning of the
access barrier into single or multiple REMOVE{door} panels and the operation
types of those panels.  
In the most common case of swinging doors the _IfcDoorTypeOperationEnum_
defined the hinge side (left hung or right hung) and the opening direction
(opening to the left, opening to the right). Whether the door opens inwards or
outwards is determined by the local coordinate system of the _IfcDoor_REMOVE{,
or _IfcDoorStandardCase_.}  
> NOTE There are different definitions in various countries on what a left
> opening or left hung or left swing door is (same for right). Therefore the
> IFC definition terms may derive from the local standard and may need to be
> mapped appropriately.  
> HISTORY New Enumeration in IFC4.  
{ .change-ifc2x4}  
> IFC4 CHANGE The new _IfcDoorTypeOperationEnum_ replaces the use of
> _IfcDoorStyleOperationEnum_ that is deprecated from IFC4 onwards.  
[ _bSI
Documentation_](https://standards.buildingsmart.org/IFC/DEV/IFC4_2/FINAL/HTML/schema/ifcsharedbldgelements/lexical/ifcdoortypeoperationenum.htm)


Attribute definitions
---------------------
| Attribute                                | Description                                                                                                                                                                                                                                                 |
|------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| SINGLE_SWING_LEFT                        | Door with one panel that opens (swings) to the left. The hinges are on the left side as viewed in the direction of the positive y-axis.NOTE Direction of swing (whether in or out) is determined at the IfcDoor                                             |
| SINGLE_SWING_RIGHT                       | Door with one panel that opens (swings) to the right. The hinges are on the right side as viewed in the direction of the positive y-axis.NOTE Direction of swing (whether in or out) is determined at the IfcDoor                                           |
| DOUBLE_PANEL_SINGLE_SWING                | Door with two panels, one opens (swings) to the left the other opens (swings) to the right.NOTE Direction of swing (whether in or out) is determined at the IfcDoor                                                                                         |
| DOUBLE_SWING_LEFT                        | Door with one panel that swings in both directions and to the left in the main traffic direction. Also called double acting door.                                                                                                                           |
| DOUBLE_SWING_RIGHT                       | Door with one panel that swings in both directions and to the right in the main traffic direction. Also called double acting door.                                                                                                                          |
| DOUBLE_PANEL_DOUBLE_SWING                | Door with two panels, one swings in both directions and to the right in the main traffic direction the other swings also in both directions and to the left in the main traffic direction.                                                                  |
| DOUBLE_PANEL_SINGLE_SWING_OPPOSITE_LEFT  | Door with two panels that both open to the left, one panel swings in one direction and the other panel swings in the opposite direction.NOTE Direction of swing (whether in or out) is determined at the IfcDoor                                            |
| DOUBLE_PANEL_SINGLE_SWING_OPPOSITE_RIGHT | Door with two panels that both open to the right, one panel swings in one direction and the other panel swings in the opposite direction.NOTE Direction of swing (whether in or out) is determined at the IfcDoor                                           |
| SLIDING_TO_LEFT                          | Door with one panel that is sliding to the left.                                                                                                                                                                                                            |
| SLIDING_TO_RIGHT                         | Door with one panel that is sliding to the right.                                                                                                                                                                                                           |
| DOUBLE_PANEL_SLIDING                     | Door with two panels, one is sliding to the left the other is sliding to the right.                                                                                                                                                                         |
| FOLDING_TO_LEFT                          | Door with one segmented panel that is folding to the left.                                                                                                                                                                                                  |
| FOLDING_TO_RIGHT                         | Door with one segmented panel that is folding to the right.                                                                                                                                                                                                 |
| DOUBLE_PANEL_FOLDING                     | Door with two segmented panels, one is folding to the left the other is folding to the right.                                                                                                                                                               |
| REVOLVING_VERTICAL                       | An entrance door consisting of a number of leaves revolving around a central vertical axis (the panels are described by a single IfcDoor panel property).                                                                                                   |
| REVOLVING_HORIZONTAL                     | An entrance door consisting of a number of leaves or posts revolving around a central horizontal axis (the panels are described by a single IfcDoor panel property).                                                                                        |
| ROLLINGUP                                | Door that opens by rolling up.NOTE Whether it rolls up to the inside or outside is determined at the IfcDoor.                                                                                                                                               |
| SWING_FIXED_LEFT                         | Door with one panel that opens (swings) to the left and one fixed panel. The hinges of the swinging panel are on the left side as viewed in the direction of the positive y-axis.NOTE Direction of swing (whether in or out) is determined at the IfcDoor   |
| SWING_FIXED_RIGHT                        | Door with one panel that opens (swings) to the right and one fixed panel. The hinges of the swinging panel are on the right side as viewed in the direction of the positive y-axis.NOTE Direction of swing (whether in or out) is determined at the IfcDoor |
| LIFTING_VERTICAL_LEFT                    | Access opening with one panel that lifts vertically, directly upward or rotates about a pivot located on the left side in the direction of the positive y-axis.                                                                                             |
| LIFTING_VERTICAL_RIGHT                   | Access opening with one panel that lifts vertically, directly upward or rotates about a pivot located on the right side in the direction of the positive y-axis.                                                                                            |
| DOUBLE_PANEL_LIFTING_VERTICAL            | Access opening with two panels that lifts vertically, directly upward or rotates about a pivot located on the left and the right side in the direction of the positive y-axis.                                                                              |
| LIFTING_HORIZONTAL                       | Access opening with one panel that lifts by rotating along a horizontal access.NOTE location of horizontal access (e.g. Top or bottom of opening) is determined at the IfcDoor.                                                                             |
| USERDEFINED                              |                                                                                                                                                                                                                                                             |
| NOTDEFINED                               |                                                                                                                                                                                                                                                             |

