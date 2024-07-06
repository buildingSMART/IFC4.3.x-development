A switching device is a device designed to make or break the current in one or more electric circuits.

<!-- end of short definition -->



## Comments

### NumberOfGangs

Number of gangs/buttons on this switch.

### SetPoint

For toggle switches, there are two positions, 0 for off and 1 for on. For dimmer switches, the values may indicate the fully-off and full-on positions, where missing integer values in between are interpolated. For selector switches, the range indicates the available positions.
An IfcTable may be attached (using IfcMetric and IfcResourceConstraintRelationship) containing columns of the specified header names and types:
'Position' (IfcInteger): The discrete setpoint level.
'Sink' (IfcLabel): The Name of the switched input port (IfcDistributionPort with FlowDirection=SINK).
'Source' (IfcLabel): The Name of the switched output port (IfcDistributionPort with FlowDirection=SOURCE).
'Ratio' (IfcNormalisedRatioMeasure): The ratio of power at the setpoint where 0.0 is off and 1.0 is fully on.

