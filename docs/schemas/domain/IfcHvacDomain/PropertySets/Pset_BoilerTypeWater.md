# Pset_BoilerTypeWater

Water boiler type common attributes.
<!-- end of short definition -->

## Comments

### HeatOutput

For water boilers, it is a function of inlet versus outlet temperature. For steam boilers, it is a function of inlet temperature versus steam pressure. Note: as two variables are used, DefiningValues and DefinedValues are null, and values are stored in IfcTable in the following order: InletTemperature(IfcThermodynamicTemperatureMeasure), OutletTemperature(IfcThermodynamicTemperatureMeasure), HeatOutput(IfcEnergyMeasure). The IfcTable is related to IfcPropertyTableValue using IfcMetric and IfcResourceConstraintRelationship.

### NominalEfficiency

The nominal efficiency of the boiler as defined by the manufacturer. For water boilers, a function of inlet versus outlet temperature. Note: as two variables are used, DefiningValues and DefinedValues are null, and values are stored in IfcTable in the following order: InletTemperature(IfcThermodynamicTemperatureMeasure), OutletTemperature(IfcThermodynamicTemperatureMeasure), NominalEfficiency(IfcNormalisedRatioMeasure). The IfcTable is related to IfcPropertyTableValue using IfcMetric and IfcResourceConstraintRelationship.

