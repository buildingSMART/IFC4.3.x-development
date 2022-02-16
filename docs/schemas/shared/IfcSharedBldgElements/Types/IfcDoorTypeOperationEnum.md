# IfcDoorTypeOperationEnum

This enumeration defines the basic ways to describe how an _IfcDoor_ or _IfcDoorType_ operate, as shown in Figure 1. It combines the partitioning of the access barrier into single or multiple panels and the operation types of those panels.

In the most common case of swinging doors the _IfcDoorTypeOperationEnum_ defined the hinge side (left hung or right hung) and the opening direction (opening to the left, opening to the right). Whether the door opens inwards or outwards is determined by the local coordinate system of the _IfcDoor_  

> NOTE&nbsp; There are different definitions in various countries on what a left opening or left hung or left swing door is (same for right). Therefore the IFC definition terms may derive from the local standard and may need to be mapped appropriately.  

> HISTORY&nbsp; New Enumeration in IFC4.  

{ .change-ifc2x4}  
> IFC4 CHANGE The new _IfcDoorTypeOperationEnum_ replaces the use of _IfcDoorStyleOperationEnum_ that is deprecated from IFC4 onwards.

<table><tr><td>

<table class="gridtable">
<tbody>
<tr>
<th valign="top" width="20%"><i>Enumerator</i></th>
<th valign="top" width="40%"><i>Description</i></th>
<th valign="top" width="20%"><i>Figures</i></th>
<th> </th>
</tr>
<tr>
<td valign="top" width="20%">
SINGLE_SWING_LEFT
</td>
<td valign="top" width="40%">Door with one panel that opens (swings) to the left. The hinges are on the left side as viewed
in the direction of the positive y-axis.<br>
<blockquote class="note">NOTE&nbsp; Direction of swing (whether in or out) is determined at the <em>IfcDoor</em> or <em>IfcDoorStandardCase</em>.<br>
<br></blockquote>
</td>
<td valign="top" width="20%"><img src="../../../../figures/ifcdoortypeenum-fig01.gif" alt="single swing left " border="0"></td>
<td><img src="../../../../figures/ifcdoortypeenum-fig01b.gif" alt="single swing left " border="0"></td>
</tr>
<tr>
<td valign="top" width="20%">
SINGLE_SWING_RIGHT
</td>
<td valign="top" width="40%">Door with one panel that opens
(swings) to the right. The hinges are on the right side as viewed
in the direction of the positive y-axis.<br>
<blockquote class="note">NOTE&nbsp; Direction of swing (whether in or out) is determined at the <em>IfcDoor</em> or <em>IfcDoorStandardCase</em>.<br>
<br></blockquote>
</td>
<td valign="top" width="20%"><img src="../../../../figures/ifcdoortypeenum-fig02.gif" alt="single swing right" border="0"></td>
<td><img src="../../../../figures/ifcdoortypeenum-fig02b.gif" alt="single swing right" border="0"></td>
</tr>
<tr>
<td valign="top" width="20%">
DOUBLE_DOOR_<br>
SINGLE_SWING
</td>
<td valign="top" width="40%">Door with two panels, one opens
(swings) to the left the other opens (swings) to the right.<br>
<blockquote class="note">NOTE&nbsp; Direction of swing (whether in or out) is determined at the <em>IfcDoor</em> or <em>IfcDoorStandardCase</em>.<br>
<br></blockquote>
</td>
<td valign="top" width="20%"><img src="../../../../figures/ifcdoortypeenum-fig03.gif" alt="double swing" border="0"></td>
<td><img src="../../../../figures/ifcdoortypeenum-fig03b.gif" alt="double swing" border="0"></td>
</tr>
<tr>
<td valign="top" width="20%">
DOUBLE_SWING_LEFT
</td>
<td valign="top" width="40%">Door with one panel that swings in
both directions and to the left in the main traffic direction.
Also called double acting door.<br>
<blockquote class="note">NOTE&nbsp; Direction of swing (whether in or out) is determined at the <em>IfcDoor</em> or <em>IfcDoorStandardCase</em>.<br>
<br></blockquote>
</td>
<td valign="top" width="20%"><img src="../../../../figures/ifcdoortypeenum-fig04.gif" alt="double swing left" border="0"></td>
<td><img src="../../../../figures/ifcdoortypeenum-fig04b.gif" alt="double swing left" border="0"></td>
</tr>
<tr>
<td valign="top" width="20%">
DOUBLE_SWING_RIGHT
</td>
<td valign="top" width="40%">Door with one panel that swings in
both directions and to the right in the main traffic direction.
Also called double acting door.<br>
<blockquote class="note">NOTE&nbsp; Direction of swing (whether in or out) is determined at the <em>IfcDoor</em> or <em>IfcDoorStandardCase</em>.<br>
<br></blockquote>
</td>
<td valign="top" width="20%"><img src="../../../../figures/ifcdoortypeenum-fig05.gif" alt="double swing right" border="0"></td>
<td><img src="../../../../figures/ifcdoortypeenum-fig05b.gif" alt="double swing right" border="0"></td>
</tr>
<tr>
<td valign="top" width="20%">
DOUBLE_DOOR_<br>
DOUBLE_SWING
</td>
<td valign="top" width="40%">Door with two panels, one swings in
both directions and to the right in the main traffic direction the
other swings also in both directions and to the left in the main
traffic direction.<br>
<blockquote class="note">NOTE&nbsp; Direction of swing (whether in or out) is determined at the <em>IfcDoor</em> or <em>IfcDoorStandardCase</em>.<br>
<br></blockquote>
</td>
<td valign="top" width="20%"><img src="../../../../figures/ifcdoortypeenum-fig06.gif" alt="double double swing" border="0"></td>
<td><img src="../../../../figures/ifcdoortypeenum-fig06b.gif" alt="double double swing" border="0"></td>
</tr>
<tr>
<td valign="top" width="20%">
DOUBLE_DOOR_
SINGLE_SWING_<br>
OPPOSITE_LEFT
</td>
<td valign="top" width="40%">Door with two panels that both open
to the left, one panel swings in one direction and the other
panel swings in the opposite direction.<br>
<blockquote class="note">NOTE&nbsp; Direction of swing (whether in or out) is determined at the <em>IfcDoor</em> or <em>IfcDoorStandardCase</em>.<br>
<br></blockquote>
</td>
<td valign="top" width="20%"><img src="../../../../figures/ifcdoortypeenum-fig07.gif" alt="opposite left" border="0"> </td>
<td> </td>
</tr>
<tr>
<td valign="top" width="20%">DOUBLE_DOOR_<br>
SINGLE_SWING_<br>
OPPOSITE_RIGHT</td>
<td valign="top" width="40%">Door with two panels that both open
to the right, one panel swings in one direction and the other
panel swings in the opposite direction.<br>
<blockquote class="note">NOTE&nbsp; Direction of swing (whether in or out) is determined at the <em>IfcDoor</em> or <em>IfcDoorStandardCase</em>.<br>
<br></blockquote>
</td>
<td valign="top" width="20%"><img src="../../../../figures/ifcdoortypeenum-fig08.gif" alt="opposite right" border="0"> </td>
<td> </td>
</tr>
<tr>
<td valign="top" width="20%">
SLIDING_TO_LEFT
</td>
<td valign="top" width="40%">Door with one panel that is sliding
to the left.</td>
<td valign="top" width="20%"><img src="../../../../figures/ifcdoortypeenum-fig09.gif" alt="sliding to left" border="0"></td>
<td><img src="../../../../figures/ifcdoortypeenum-fig09b.gif" alt="sliding to left" border="0"></td>
</tr>
<tr>
<td valign="top" width="20%">
SLIDING_TO_RIGHT
</td>
<td valign="top" width="40%">Door with one panel that is sliding
to the right.</td>
<td valign="top" width="20%"><img src="../../../../figures/ifcdoortypeenum-fig10.gif" alt="sliding to right" border="0"></td>
<td><img src="../../../../figures/ifcdoortypeenum-fig10b.gif" alt="sliding to right" border="0"></td>
</tr>
<tr>
<td valign="top" width="20%">
DOUBLE_DOOR_SLIDING
</td>
<td valign="top" width="40%">Door with two panels, one is sliding
to the left the other is sliding to the right.</td>
<td valign="top" width="20%"><img src="../../../../figures/ifcdoortypeenum-fig11.gif" alt="double sliding" border="0"></td>
<td><img src="../../../../figures/ifcdoortypeenum-fig11b.gif" alt="double sliding" border="0"></td>
</tr>
<tr>
<td valign="top" width="20%">
FOLDING_TO_LEFT
</td>
<td valign="top" width="40%">Door with one panel that is folding
to the left.</td>
<td valign="top" width="20%"><img src="../../../../figures/ifcdoortypeenum-fig12.gif" alt="folding to left" border="0"></td>
<td><img src="../../../../figures/ifcdoortypeenum-fig12b.gif" alt="folding to left" border="0"></td>
</tr>
<tr>
<td valign="top" width="20%">FOLDING_TO_RIGHT</td>
<td valign="top" width="40%">Door with one panel that is folding
to the right.</td>
<td valign="top" width="20%"><img src="../../../../figures/ifcdoortypeenum-fig13.gif" alt="folding to right" border="0"></td>
<td><img src="../../../../figures/ifcdoortypeenum-fig13b.gif" alt="folding to right" border="0"></td>
</tr>
<tr>
<td valign="top" width="20%">
DOUBLE_DOOR_FOLDING
</td>
<td valign="top" width="40%">Door with two panels, one is folding
to the left the other is folding to the right.</td>
<td valign="top" width="20%"><img src="../../../../figures/ifcdoortypeenum-fig14.gif" alt="double folding" border="0"></td>
<td><img src="../../../../figures/ifcdoortypeenum-fig14b.gif" alt="double folding" border="0"></td>
</tr>
<tr>
<td valign="top" width="20%">
REVOLVING
</td>
<td valign="top" width="40%">An entrance door consisting of four
leaves set in a form of a cross and revolving around a central
vertical axis (the four panels are described by a single
<a href="../../ifcsharedbldgelements/lexical/ifcdoor.htm">IfcDoor</a> panel property).</td>
<td valign="top" width="20%"><img src="../../../../figures/ifcdoortypeenum-fig15.gif" alt="revolving" border="0"> </td>
<td> </td>
</tr>
<tr>
<td valign="top" width="20%">
ROLLINGUP
</td>
<td valign="top" width="40%">Door that opens by rolling up.<br>
<blockquote class="note">NOTE&nbsp; Whether it rolls up to the inside or
outside is determined at the <em>IfcDoor</em>.</blockquote>
</td>
<td valign="top" width="20%"><img src="../../../../figures/ifcdoortypeenum-fig16.gif" alt="rolling" border="0"></td>
<td><img src="../../../../figures/ifcdoortypeenum-fig16b.gif" alt="rolling" border="0"></td>
</tr>
<tr>
<td valign="top" width="20%">SWING_FIXED_LEFT</td>
<td valign="top" width="40%">Door with one panel that opens
(swings) to the left and one fixed panel. The hinges of the
swinging panel are on the left side as viewed in the direction of
the positive y-axis.<br>
<blockquote class="note">NOTE&nbsp; Direction of swing (whether in or out) is determined at the <em>IfcDoor</em> or <em>IfcDoorStandardCase</em>.<br>
<br></blockquote>
</td>
<td valign="top" width="20%"><img src="../../../../figures/ifcdoortypeenum-fig18.gif" alt="swinging left and fixed" border="0"></td>
<td><img src="../../../../figures/ifcdoortypeenum-fig18b.gif" alt="swinging left and fixed" border="0"></td>
</tr>
<tr>
<td valign="top" width="20%">SWING_FIXED_RIGHT</td>
<td valign="top" width="40%">Door with one panel that opens
(swings) to the right and one fixed panel. The hinges of the
swinging panel are on the right side as viewed in the direction
of the positive y-axis.<br>
<blockquote class="note">NOTE&nbsp; Direction of swing (whether in or out) is determined at the <em>IfcDoor</em> or <em>IfcDoorStandardCase</em>.<br>
<br></blockquote>
</td>
<td valign="top" width="20%"><img src="../../../../figures/ifcdoortypeenum-fig19.gif" alt="swinging right and fixed" border="0"></td>
<td><img src="../../../../figures/ifcdoortypeenum-fig19b.gif" alt="swinging right and fixed" border="0"></td>
</tr>
<tr>
<td valign="top" width="20%">USERDEFINED</td>
<td valign="top" width="40%">User defined operation type</td>
<td valign="top" width="20%"> </td>
<td> </td>
</tr>
<tr>
<td valign="top" width="20%">NOTDEFINED</td>
<td valign="top" width="40%">A door with a not defined operation
type is considered as a door with a lining, but no panels. It is
thereby always open.</td>
<td valign="top" width="20%"><img src="../../../../figures/ifcdoortypeenum-fig17.gif" alt="not defined"><br></td>
<td> </td>
</tr>
</tbody>
</table>

</td></tr>
<tr><td><p class="figure">Figure 1 &mdash; Door operations</p></td></tr>
</table>

NOTE

1. Figures are shown in the ground view.
2. Figures (symbolic representation) depend on the national building code.
3. These figures/ are only shown as illustrations, the actual representation in the ground view might differ.
4. Open to the outside is declared as open into the direction of the positive y-axis, determined by the _ObjectPlacement_ at _IfcDoor_
5. The location of the panel relative to the wall thickness is defined by the _ObjectPlacement_ at _IfcDoor_, and the _IfcDoorLiningProperties.LiningOffset_ parameter.

## Items

### SINGLE_SWING_LEFT
Door with one panel that opens (swings) to the left. The hinges are on the left side as viewed in the direction of the positive y-axis.

### SINGLE_SWING_RIGHT
Door with one panel that opens (swings) to the right. The hinges are on the right side as viewed in the direction of the positive y-axis.

### DOUBLE_PANEL_SINGLE_SWING
Door with two panels, one opens (swings) to the left the other opens (swings) to the right.

### DOUBLE_PANEL_SINGLE_SWING_OPPOSITE_LEFT
Door with two panels that both open to the left, one panel swings in one direction and the other panel swings in the opposite direction.

### DOUBLE_PANEL_SINGLE_SWING_OPPOSITE_RIGHT
Door with two panels that both open to the right, one panel swings in one direction and the other panel swings in the opposite direction.

### DOUBLE_SWING_LEFT
Door with one panel that swings in both directions and to the left in the main traffic direction. Also called double acting door.

### DOUBLE_SWING_RIGHT
Door with one panel that swings in both directions and to the right in the main traffic direction. Also called double acting door.

### DOUBLE_PANEL_DOUBLE_SWING
Door with two panels, one swings in both directions and to the right in the main traffic direction the other swings also in both directions and to the left in the main traffic direction.

### SLIDING_TO_LEFT
Door with one panel that is sliding to the left.

### SLIDING_TO_RIGHT
Door with one panel that is sliding to the right.

### DOUBLE_PANEL_SLIDING
Door with two panels, one is sliding to the left the other is sliding to the right.

### FOLDING_TO_LEFT
Door with one panel that is folding to the left.

### FOLDING_TO_RIGHT
Door with one panel that is folding to the right.

### DOUBLE_PANEL_FOLDING
Door with two panels, one is folding to the left the other is folding to the right.

### REVOLVING_HORIZONTAL
An entrance door consisting of four leaves set in a form of a cross and revolving around a central vertical axis (the four panels are described by a single _IfcDoor_ panel property).

### ROLLINGUP
Door that opens by rolling up.

### SWING_FIXED_LEFT
Door with one panel that opens (swings) to the left and one fixed panel. The hinges of the swinging panel are on the left side as viewed in the direction of the positive y-axis.

### SWING_FIXED_RIGHT
Door with one panel that opens (swings) to the right and one fixed panel. The hinges of the swinging panel are on the right side as viewed in the direction
of the positive y-axis.

### DOUBLE_PANEL_LIFTING_VERTICAL


### LIFTING_HORIZONTAL


### LIFTING_VERTICAL_LEFT


### LIFTING_VERTICAL_RIGHT


### REVOLVING_VERTICAL


### USERDEFINED
User defined operation type.

### NOTDEFINED
A door with a not defined operation type is considered as a door with a lining, but no panels. It is thereby always open.
