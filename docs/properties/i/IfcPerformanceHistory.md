IfcPerformanceHistory
=====================

_IfcPerformanceHistory_ is used to document the actual performance of an occurrence instance over time. It includes machine-measured data from building automation systems and human-specified data such as task and resource usage. The data may represent actual conditions, predictions, or simulations.

The realtime data tracked by performance history takes the form of property sets where all properties are based on time series. Unlike design-based data at occurrences and types, performance-driven data is time-sensitive and may change in realtime by some measurement device. Data may be captured at irregular intervals such as when values change beyond established thresholds, or at regular intervals of specified duration.

#### Declaration use definition
_IfcPerformanceHistory_ may be declared within a project using _IfcRelDeclares_ where _RelatingContext_ refers to the _IfcProject_ and _RelatedDefinitions_ includes the _IfcPerformanceHistory_. Default units (used for property sets) are indicated by the declaring project. Only top-level objects are declared; nested performance history objects (through _IfcRelNests_) do not participate in such relationship.

> HISTORY&nbsp; New entity in IFC2x2.
