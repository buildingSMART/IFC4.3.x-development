SetPoint
========

Indicates the setpoint and label.  For toggle switches, there are two positions, 0 for off and 1 for on.  For dimmer switches, the values may indicate the fully-off and full-on positions, where missing integer values in between are interpolated.   For selector switches, the range indicates the available positions.  
An IfcTable may be attached (using IfcMetric and IfcPropertyConstraintRelationship) containing columns of the specified header names and types:
'Position' (IfcInteger): The discrete setpoint level.
'Sink' (IfcLabel): The Name of the switched input port (IfcDistributionPort with FlowDirection=SINK).
'Source' (IfcLabel): The Name of the switched output port (IfcDistributionPort with FlowDirection=SOURCE).
'Ratio' (IfcNormalizedRatioMeasure): The ratio of power at the setpoint where 0.0 is off and 1.0 is fully on.
