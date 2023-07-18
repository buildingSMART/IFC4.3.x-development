CoefficientOfPerformanceCurve
=============================

Chiller coefficient of performance (COP) is function of condensing temperature and evaporating temperature, data is in table form, COP= f (TempCon, TempEvp), COP = a2+b2\*Tei+c2\*Tei\^2+d2\*Tci+e2\*Tci\^2+f2\*Tei\*Tci.
This table uses multiple input variables; to represent, both DefiningValues and DefinedValues lists are null and IfcTable is attached using IfcResourceConstraintRelationship and IfcMetric.  Columns are specified in the following order:
1.IfcPositiveRatioMeasure:CoefficientOfPerformance
2.IfcThermodynamicTemperatureMeasure:CondensingTemperature
3.IfcThermodynamicTemperatureMeasure:EvaporatingTemperature
