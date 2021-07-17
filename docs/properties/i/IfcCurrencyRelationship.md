IfcCurrencyRelationship
=======================

_IfcCurrencyRelationship_ defines the rate of exchange that applies between two designated currencies at a particular time and as published by a particular source.

An _IfcCurrencyRelationship_ is used where there may be a need to reference an _IfcCostValue_ in one currency to an _IfcCostValue_ in another currency. It takes account of fact that currency exchange rates may vary by requiring the recording the date and time of the currency exchange rate used and the source that publishes the rate. There may be many sources and there are different strategies for currency conversion (spot rate, forward buying of currency at a fixed rate).

The source for the currency exchange is defined as an instance of _IfcLibraryInformation_ that includes a name and a URL.

> HISTORY&nbsp; New entity in IFC2x2.

{ .change-ifc2x4}
> IFC4 CHANGE&nbsp; Subtyped from _IfcResourceLevelRelationship_, attribute order changed.
