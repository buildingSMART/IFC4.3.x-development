# IfcAlignmentCantSegment

An _IfcAlignmentCantSegment_ is an individual segment along _IfcAlignmentCant_.
The cant alignment is defined by ordered segments that connect end-to-start. The points defined in a cant alignment segment are defined in a plane with x = distance along horizontal alignment and y = height relative to projected points in vertical alignment. 
The following cant segment types are defined:
* line segment - _IfcAlignmentCantSegmentTypeEnum_ .LINE.
* transition curve segment - _IfcAlignmentCantSegmentTypeEnum_ .NONLINEAR.


For each cant segment, the following information is provided:
* the start point, defined by distance along the horizontal alignment
* the length (as horizontal length along the distance along (not the curve segment length))
* the start cant, given by the values of left cant and right cant, measured relatively to vertical alignment
* the end cant, given by the values of left cant and right cant, measured from vertical alignment
* the information of tangential continuity that can be used to check continuity of segments (e.g. invalid sudden change of cant or missing cant information if end point and starting point differ over a threshold).

## Attributes

### StartDistAlong
Distance along the horizontal alignment, measured along the IfcAlignment2DHorizontal given in the length unit of the global IfcUnitAssignment.

### HorizontalLength
Length measured as distance along the horizontal alignment of the segment.

### StartCantLeft
Length measured for the left cant at the beginning of the segment.

### EndCantLeft
Length measured for the left cant at the end of the segment.

### StartCantRight
Length measured for the right cant at the beginning of the segment.

### EndCantRight
Length measured for the right cant at the end of the segment.

### SmoothingLength


### PredefinedType

