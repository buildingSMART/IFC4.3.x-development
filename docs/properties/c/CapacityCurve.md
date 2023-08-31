CapacityCurve
=============

Chiller cooling capacity is a function of condensing temperature and evaporating temperature, data is in table form, Capacity = f (TempCon, TempEvp), capacity = a1+b1\*Tei+c1\*Tei\^2+d1\*Tci+e1\*Tci\^2+f1\*Tei\*Tci.
This table uses multiple input variables; to represent, both DefiningValues and DefinedValues lists are null and IfcTable is attached using IfcResourceConstraintRelationship and IfcMetric.  Columns are specified in the following order:
1.IfcPowerMeasure:Capacity
2.IfcThermodynamicTemperatureMeasure:CondensingTemperature
3.IfcThermodynamicTemperatureMeasure:EvaporatingTemperature
