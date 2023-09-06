# Pset_BoilerTypeSteam

Steam boiler type common attributes.


## Comments

### HeatOutput

For steam boilers, it is a function of inlet temperature versus steam pressure.  Note: as two variables are used, DefiningValues and DefinedValues are null, and values are stored in IfcTable in the following order: InletTemperature(IfcThermodynamicTemperatureMeasure) and OutletTemperature(IfcThermodynamicTemperatureMeasure) in DefiningValues, and HeatOutput(IfcEnergyMeasure) in DefinedValues. For example, DefiningValues(InletTemp, OutletTemp), DefinedValues(null, HeatOutput). The IfcTable is related to IfcPropertyTableValue using IfcMetric and IfcResourceConstraintRelationship.

