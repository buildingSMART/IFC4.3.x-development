# IfcRegularTimeSeries

In a regular time series, the data arrives predictably at predefined intervals. In a regular time series there is no need to store multiple time stamps and the algorithms for analyzing the time series are therefore significantly simpler. Using the start time provided in the supertype, the time step is used to identify the frequency of the occurrences of the list of values.
<!-- end of short definition -->


> EXAMPLE A smoke detector samples the concentration of particulates in a space at a fixed rate (for example, every six seconds); a control system measures the outside air temperature every hour.

> HISTORY New entity in IFC2x2.

## Attributes

### TimeStep
A duration of time intervals between values.

### Values
The collection of time series values.
