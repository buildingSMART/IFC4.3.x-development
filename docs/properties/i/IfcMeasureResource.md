IfcMeasureResource
==================

The _IfcMeasureResource_ schema specifies units and defined measure types that may be assigned to quantities.

> NOTE&nbsp; The fundamental unit types used in this schema are based on the SI system defined in ISO 1000+A1, 1992, 1998. Units in measurement systems other than SI may be derived using this schema. Many definitions declared in the _IfcMeasureResource_ schema is adapted from [ISO 10303-41](../../bibliography.htm#iso-10303-41){ .int-ref}

> NOTE&nbsp; In the definitions of the unit exponents the use of superscript font has been omitted. Therefore, m2 means square metre, m3 means cubic meter.

In different types of units there are five basic cases:

* Basic SI-units, which cover a number of fundamental units of mainly physical quantities defined by [ISO-1000](../../bibliography.htm#iso-1000){ .int-ref} such as meter or millimeter as unit for length measure or square meter as a unit for area measure. The unit may have a scaling prefix (for example: milli, kilo).
* Derived SI-units, which are defined as a derivation of the basic SI-units, for example, Newton (kg m / s2) as a unit of force. Both basic and derived SI-units are in the IFCs represented by IfcSIUnit.
* Conversion based units, which can be derived from SI-units by a scaling factor; e.g. inch which can be defined using SI-unit for length measure, i.e. an inch is 25.4 millimeters.
* Derived units, which can be defined as a derivation or combination of a number of basic units. In a derived unit each of the basic unit "component" has a dimensional exponent in defining the derived unit; e.g. kg / m2, where kilogram (kg) has dimensional exponent 1 and meter (m) has exponent -2.
* Context dependent units, which cannot be defined as conversion based unit using SI-units.

With regard to the usage of the measure defined types (for example, _IfcLengthMeasure_, _IfcTimeMeasure_) as attribute datatypes in this specification, there are three basic cases:

<ol>
<li>The datatype of an attribute of an entity type is a measure defined type as such without possibility on an instance level to define the unit of the measure value:
<blockquote><code>
ENTITY IfcBoundingBox<br>SUBTYPE OF(IfcGeometricRepresentationItem);<br>Corner : IfcCartesianPoint;<br>XDim : IfcPositiveLengthMeasure;<br>YDim : IfcPositiveLengthMeasure;<br>ZDim : IfcPositiveLengthMeasure;<br>END_ENTITY;<br></code></blockquote>
In this case, it is the global unit assignment for the corresponding unit for the measure type that defines the unit for all the usages of this defined measure type (except for cases 2 and 3 below).
</li>
<li>The datatype of an attribute is IfcMeasureWithUnit, which allows for definition of unit per instance of that entity type, independent and possibly overriding the global unit assignment:
<blockquote><code>
ENTITY IfcConversionBasedUnit<br>
 SUPERTYPE OF (ONEOF<br>
  (IfcConversionBasedUnitWithOffset))<br>
 SUBTYPE OF (IfcNamedUnit);<br>
  Name : IfcLabel;<br>
  ConversionFactor : IfcMeasureWithUnit;<br>
END_ENTITY;<br>
</code></blockquote>
In this case the relevant measure defined type (from the IfcMeasureWithUnit.ValueComponent : IfcValue select list) is not exactly defined by the schema, but implied by the context.
</li>
<li>The entity type has a separate "unit" attribute which allows for defining the unit for another attribute of the entity type for representing the actual value:
<blockquote><code>
ENTITY IfcPropertySingleValue<br>SUBTYPE OF (IfcSimpleProperty);<br>NominalValue : IfcValue;<br>Unit : OPTIONAL IfcUnit;<br>END_ENTITY;<br></code></blockquote></li></ol>
Although in the cases 2 and 3 different units could be used for different instances of the same entity type or for the same measure type in attributes of different entity types, it is recommended not to mix different units for same measure defined types, if it can be avoided. Below some examples of each of the above basic cases are given.

> NOTE&nbsp; In the example instantiations in the form of IFC data exchange files, mainly the measure and unit -relevant attributes are given the values; the other attributes are given no values (in the form of $-sign) independent of whether they should actually have values because of being nonoptional attributes.

Table 1 indicates measures, units, and corresponding data types.

> <small>
<table class="gridtable">
<tr><td><b>Measure</b></td><td><b>Type</b></td><td><b>Unit</b></td><td><b>Symbol</b></td><td><b>Derivation</b></td><td><b>IfcSiUnitEnum</b></td><td><b>IfcUnitEnum</b></td><td><b>IfcDerivedUnitEnum</b></td><td><b>Defined value types</b></td></tr>
 <tr><td>Absorbed dose, specific energy<br>impact, kerma, absorbed dose index</td><td>SI / Derived</td><td>gray</td><td>Gy</td><td>J / kg</td><td>GRAY</td><td>ABSORBEDDOSEUNIT</td><td></td><td>IfcAbsorbedDoseMeasure</td></tr>
 <tr><td>Acceleration</td><td>Derived</td><td></td><td></td><td>m / s2</td><td></td><td></td><td>ACCELERATIONUNIT</td><td>IfcAccelerationMeasure</td></tr>
 <tr><td>Acidity (pH)</td><td>Derived</td><td>pH</td><td>pH</td><td>mol / l</td><td></td><td></td><td>PHUNIT</td><td>IfcPHMeasure</td></tr>
 <tr><td>Activity (of radionuclide)</td><td>SI / Derived</td><td>becquerel</td><td>Bq</td><td>1 / s</td><td>BECQUEREL</td><td>RADIOACTIVITYUNIT</td><td></td><td>IfcRadioActivityMeasure</td></tr>
 <tr><td>Amount of substance</td><td>SI/Basic</td><td>mole</td><td>mol</td><td></td><td>MOLE</td><td>AMOUNTOFSUBSTANCEUNIT</td><td></td><td>IfcAmountOfSubstanceMeasure</td></tr>
 <tr><td>Angular velocity</td><td>Derived</td><td></td><td></td><td>rad / s</td><td></td><td></td><td>ANGULARVELOCITYUNIT</td><td>IfcAngularVelocityMeasure</td></tr>
 <tr><td>Area</td><td>SI/Derived</td><td>square metre</td><td>m2</td><td>m2</td><td>SQUARE_METRE</td><td>AREAUNIT</td><td></td><td>IfcAreaMeasure</td></tr>
 <tr><td>Area density</td><td>Derived</td><td></td><td></td><td>kg / m2</td><td></td><td></td><td>AREADENSITYUNIT</td><td>IfcAreaDensityMeasure</td></tr>
 <tr><td>-</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>IfcBoolean</td></tr>
 <tr><td>-</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>IfcComplexNumber</td></tr>
 <tr><td>Compound plane angle</td><td>Compound</td><td></td><td></td><td>degree, min, s</td><td></td><td></td><td>COMPOUNDPLANEANGLEUNIT</td><td>IfcCompoundPlaneAngleMeasure</td></tr>
 <tr><td>-</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>IfcContextDependentMeasure</td></tr>
 <tr><td>-</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>IfcCountMeasure</td></tr>
 <tr><td>-</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>IfcDescriptiveMeasure</td></tr>
 <tr><td>Capacitance</td><td>SI / Derived</td><td>farad</td><td>F</td><td>C / V</td><td>FARAD</td><td>ELECTRICCAPACITANCEUNIT</td><td></td><td>IfcElectricCapacitanceMeasure</td></tr>
 <tr><td>Celsius temperature</td><td>SI / Basic</td><td>degree Celsius</td><td>ºC</td><td>1 ºC = 1 K</td><td>DEGREE_CELSIUS</td><td>THERMODYNAMICTEMPERATUREUNIT</td><td></td><td>IfcThermodynamicTemperatureMeasure</td></tr>
 <tr><td>Curvatue</td><td>Derived</td><td></td><td></td><td>rad / m</td><td></td><td></td><td>CURVATUREUNIT</td><td>IfcCurvatureMeasure</td></tr> 
 <tr><td>-</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>IfcDate <br>(lexical representation according to ISO 8601)</td></tr>
 <tr><td>-</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>IfcDateTime <br>(lexical representation according to ISO 8601)</td></tr>
 <tr><td>Dose equivalent, dose equivalent<br> index</td><td>SI / Derived</td><td>sievert</td><td>Sv</td><td>J / kg</td><td>SIEVERT</td><td>DOSEEQUIVALENTUNIT</td><td></td><td>IfcDoseEquivalentMeasure</td></tr>
 <tr><td>-</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>IfcDuration <br> (lexical representation according to ISO 8601)</td></tr>
 <tr><td>Dynamic viscosity</td><td>Derived</td><td></td><td></td><td>Pa · s</td><td></td><td></td><td>DYNAMICVISCOSITYUNIT</td><td>IfcDynamicViscosityMeasure</td></tr>
 <tr><td>Electric charge, <br>quantity of electricity</td><td>SI / Derived</td><td>coulomb</td><td>C</td><td>A · s</td><td>COULOMB</td><td>ELECTRICCHARGEUNIT</td><td></td><td>IfcElectricChargeMeasure</td></tr>
 <tr><td>Electric conductance</td><td>SI / Derived</td><td>siemens</td><td>S</td><td>1 / W</td><td>SIEMENS</td><td>ELECTRICCONDUCTANCEUNIT</td><td></td><td>IfcElectricConductanceMeasure</td></tr>
 <tr><td>Electric current</td>	<td>SI / Basic</td><td>ampere</td><td>A</td><td></td><td>AMPERE</td><td>ELECTRICCURRENTUNIT</td><td></td><td>IfcElectricCurrentMeasure</td></tr>
 <tr><td>Electric potential, potential <br>difference, tension, electromotive force</td><td>SI / Derived</td><td>volt</td><td>V</td><td>W / A</td><td>VOLT</td><td>ELECTRICVOLTAGEUNIT</td><td></td><td>IfcElectricVoltageMeasure</td></tr>
 <tr><td>Electric resistance</td><td>SI / Derived</td><td>ohm</td><td>W</td><td>V / A</td><td>OHM</td><td>ELECTRICRESISTANCEUNIT</td><td></td><td>IfcElectricResistanceMeasure</td></tr>
 <tr><td>Energy, work, quantity of heat</td><td>SI / Derived</td><td>joule</td><td>J</td><td>N · m</td><td>JOULE</td><td>ENERGYUNIT</td><td></td><td>IfcEnergyMeasure</td></tr>
 <tr><td>Force</td><td>SI / Derived</td><td>newton</td><td>N</td><td>kg · m / s2</td><td>NEWTON</td><td>FORCEUNIT</td><td></td><td>IfcForceMeasure</td></tr>
 <tr><td>Frequency</td><td>SI / Derived</td><td>hertz</td><td>Hz</td><td>1 / s</td><td>HERTZ</td><td>FREQUENCYUNIT</td><td></td><td>IfcFrequencyMeasure</td></tr>
 <tr><td>Heat flux density</td><td>Derived</td><td></td><td></td><td>W / m2</td><td></td><td></td><td>HEATFLUXDENSITYUNIT</td><td>IfcHeatFluxDensityMeasure</td></tr>
 <tr><td>Heating value</td><td>Derived</td><td></td><td></td><td>J / kg</td><td></td><td></td><td>HEATINGVALUEUNIT</td><td>IfcHeatingValueMeasure</td></tr>
 <tr><td>-</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>IfcIdentifier</td></tr>
 <tr><td>Illuminance</td><td>SI / Derived</td><td>lux</td><td>lx</td><td>lm / m2</td><td>LUX</td><td>ILLUMINANCEUNIT</td><td></td><td>IfcIlluminanceMeasure</td></tr>
 <tr><td>Inductance</td><td>SI / Derived</td><td>henry</td><td>H</td><td>Wb / A</td><td>HENRY</td><td>INDUCTANCEUNIT</td><td></td><td>IfcInductanceMeasure</td></tr>
 <tr><td>-</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>IfcInteger</td></tr>
 <tr><td>(Integer) Count rate</td><td>Derived</td><td></td><td></td><td>1 / s</td><td></td><td></td><td>INTEGERCOUNTRATEUNIT</td><td>IfcIntegerCountRateMeasure</td></tr>
 <tr><td>Ion concentration</td><td>Derived</td><td></td><td></td><td>g / l</td><td></td><td></td><td>IONCONCENTRATIONUNIT</td><td>IfcIonConcentrationMeasure</td></tr>
 <tr><td>Isothermal moisture capacity</td><td>Derived</td><td></td><td></td><td>m3 / kg</td><td></td><td></td><td>ISOTHERMALMOISTURECAPACITYUNIT</td><td>IfcIsothermalMoistureCapacityMeasure</td></tr>
 <tr><td>Kinematic viscosity</td><td>Derived</td><td></td><td></td><td>m2 / s</td><td></td><td></td><td>KINEMATICVISCOSITYUNIT</td><td>IfcKinematicViscosityMeasure</td></tr>
 <tr><td>Length</td><td>SI / Basic</td><td>metre</td><td>m</td><td></td><td>METRE</td><td>LENGTHUNIT</td><td></td><td>IfcLengthMeasure</td></tr>
 <tr><td>-</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>IfcLabel</td></tr>
 <tr><td>Linear force</td><td>Derived</td><td></td><td></td><td>N / m</td><td></td><td></td><td>LINEARFORCEUNIT</td><td>IfcLinearForceMeasure</td></tr>
 <tr><td>Linear moment</td><td>Derived</td><td></td><td></td><td>N · m / m</td><td></td><td></td><td>LINEARMOMENTUNIT</td><td>IfcLinearMomentMeasure</td></tr>
 <tr><td>Linear stiffness</td><td>Derived</td><td></td><td></td><td>N / m</td><td></td><td></td><td>LINEARSTIFFNESSUNIT</td><td>IfcLinearStiffnessMeasure</td></tr>
 <tr><td>Linear velocity</td><td>Derived</td><td></td><td></td><td>m / s</td><td></td><td></td><td>LINEARVELOCITYUNIT</td><td>IfcLinearVelocityMeasure</td></tr>
 <tr><td>-</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>IfcLogical</td></tr>
 <tr><td>Luminous flux</td><td>SI / Derived</td><td>lumen</td><td>lm</td><td>cd · sr</td><td>LUMEN</td><td>LUMINOUSFLUXUNIT</td><td></td><td>IfcLuminousFluxMeasure</td></tr>
 <tr><td>Luminous intensity</td><td>SI / Basic</td><td>candela</td><td>cd</td><td></td><td>CANDELA</td><td>LUMINOUSINTENSITYUNIT</td><td></td><td>IfcLuminousIntensityMeasure</td></tr>
 <tr><td>Luminous intensity distribution</td><td>Derived</td><td></td><td></td><td>cd / lm</td><td></td><td></td><td>LUMINOUSINTENSITYDISTRIBUTIONUNIT</td><td>IfcLuminousIntensityDistributionMeasure</td></tr>
 <tr><td>Magnetic flux</td><td>SI / Derived</td><td>weber</td><td>Wb</td><td>V · s</td><td>WEBER</td><td>MAGNETICFLUXUNIT</td><td></td><td>IfcMagneticFluxMeasure</td></tr>
 <tr><td>Magnetic flux density</td><td>SI / Derived</td><td>tesla</td><td>T</td><td>Wb / m2</td><td>TESLA</td><td>MAGNETICFLUXDENSITYUNIT</td><td></td><td>IfcMagneticFluxDensityMeasure</td></tr>
 <tr><td>Mass</td><td>SI / Basic</td><td>gram</td><td>g (kg)</td><td></td><td>GRAM</td><td>MASSUNIT</td><td></td><td>IfcMassMeasure</td></tr>
 <tr><td>Mass density</td><td>Derived</td><td></td><td></td><td>kg / m3</td><td></td><td></td><td>MASSDENSITYUNIT</td><td>IfcMassDensityMeasure</td></tr>
 <tr><td>Mass flow rate</td><td>Derived</td><td></td><td></td><td>kg / s</td><td></td><td></td><td>MASSFLOWRATEUNIT</td><td>IfcMassFlowRateMeasure</td></tr>
 <tr><td>Mass per length</td><td>Derived</td><td></td><td></td><td>kg / m</td><td></td><td></td><td>MASSPERLENGTHUNIT</td><td>IfcMassPerLengthMeasure</td></tr>
 <tr><td>Modulus of elasticity</td><td>Derived</td><td></td><td></td><td>N / m2</td><td></td><td></td><td>MODULUSOFELASTICITYUNIT</td><td>IfcModulusOfElasticityMeasure</td></tr>
 <tr><td>Modulus of linear subgrade reaction</td><td>Derived</td><td></td><td></td><td>N / m2</td><td></td><td></td><td>MODULUSOFLINEARSUBGRADEREACTIONUNIT</td><td>IfcModulusOfLinearSubgradeReactionMeasure</td></tr>
 <tr><td>Modulus of rotational subgrade reaction</td><td>Derived</td><td></td><td></td><td>N · m / m · rad</td><td></td><td></td><td>MODULUSOFROTATIONALSUBGRADEREACTIONUNIT</td><td>IfcModulusOfRotationalSubgradeReactionMeasure</td></tr>
 <tr><td>Modulus of subgrade reaction</td><td>Derived</td><td></td><td></td><td>N / m3</td><td></td><td></td><td>MODULUSOFSUBGRADEREACTIONUNIT</td><td>IfcModulusOfSubgradeReactionMeasure</td></tr>
 <tr><td>Moisture diffusivity</td><td>Derived</td><td></td><td></td><td>m3 / s</td><td></td><td></td><td>MOISTUREDIFFUSIVITYUNIT</td><td>IfcMoistureDiffusivityMeasure</td></tr>
 <tr><td>Molecular weight</td><td>Derived</td><td></td><td></td><td>g / mol</td><td></td><td></td><td>MOLECULARWEIGHTUNIT</td><td>IfcMolecularWeightMeasure</td></tr>
 <tr><td>Moment of inertia</td><td>Derived</td><td></td><td></td><td>m4</td><td></td><td></td><td>MOMENTOFINERTIAUNIT</td><td>IfcMomentOfInertiaMeasure</td></tr> 
 <tr><td>-</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>IfcMonetaryMeasure</td></tr>
 <tr><td>(Non negative length)</td><td></td><td></td><td>m</td><td></td><td></td><td>LENGTHUNIT</td><td></td><td>IfcNonNegativeLengthMeasure</td></tr>
 <tr><td>-</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>IfcNormalisedRatioMeasure</td></tr>
 <tr><td>-</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>IfcNumericMeasure</td></tr>
 <tr><td>-</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>IfcParameterValue</td></tr>
 <tr><td>Planar force</td><td>Derived</td><td></td><td></td><td>N / m2</td><td></td><td></td><td>PLANARFORCEUNIT</td><td>IfcPlanarForceMeasure</td></tr>
 <tr><td>Plane angle</td><td>SI / Derived</td><td>radian</td><td>rad</td><td>m / m = 1</td><td>RADIAN</td><td>PLANEANGLEUNIT</td><td></td><td>IfcPlaneAngleMeasure</td></tr>
 <tr><td>(Positive length)</td><td></td><td></td><td>m</td><td></td><td></td><td>LENGTHUNIT</td><td></td><td>IfcPositiveLengthMeasure</td></tr>
 <tr><td>(Positive plane angle)</td><td></td><td></td><td>rad</td><td></td><td></td><td>PLANEANGLEUNIT</td><td></td><td>IfcPositivePlaneAngleMeasure</td></tr>
 <tr><td>-</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>IfcPositiveRatioMeasure</td></tr>
 <tr><td>Power</td><td>SI / Derived</td><td>watt</td><td>W</td><td>J / s</td><td>WATT</td><td>POWERUNIT</td><td></td><td>IfcPowerMeasure</td></tr>
 <tr><td>Pressure, stress</td><td>SI / Derived</td><td>pascal</td><td>Pa</td><td>N / m2</td><td>PASCAL</td><td>PRESSUREUNIT</td><td></td><td>IfcPressureMeasure</td></tr>
 <tr><td>-</td><td></td><td></td><td></td><td></td><td></td><td></td> <td></td><td>IfcRatioMeasure</td></tr>
 <tr><td>-</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td>	<td>IfcReal</td></tr>
 <tr><td>Rotational frequency</td><td>Derived</td><td></td><td></td><td>cycles / s</td><td></td><td></td><td>ROTATIONALFREQUENCYUNIT</td><td>IfcRotationalFrequencyMeasure</td></tr>
 <tr><td>Rotational mass</td><td>Derived</td><td></td><td></td><td>kg · m2</td><td></td><td></td><td>ROTATIONALMASSUNIT</td><td>IfcRotationalMassMeasure</td></tr>
 <tr><td>Rotational stiffness</td><td>Derived</td><td></td><td></td><td>N · m / rad</td><td></td><td></td><td>ROTATIONALSTIFFNESSUNIT</td><td>IfcRotationalStiffnessMeasure</td></tr>
 <tr><td>Sectional area integral</td><td>Derived</td><td></td><td></td><td>m5</td><td></td><td></td><td>SECTIONALAREAINTEGRALUNIT</td><td>IfcSectionalAreaIntegralMeasure</td></tr>
 <tr><td>Section modulus</td><td>Derived</td><td></td><td></td><td>m3</td><td></td><td></td><td>SECTIONMODULUSUNIT</td><td>IfcSectionModulusMeasure</td></tr>
 <tr><td>Shear modulus</td><td>Derived</td><td></td><td></td><td>N / m2</td><td></td><td></td><td>SHEARMODULUSUNIT</td><td>IfcShearModulusMeasure</td></tr>
 <tr><td>Solid angle</td><td>SI / Derived</td><td>steradin</td><td>sr</td><td>m2 / m2 = 1</td><td>STERADIAN</td><td>SOLIDANGLEUNIT</td><td></td><td>IfcSolidAngleMeasure</td></tr>
 <tr><td>Sound power</td><td></td><td>watt</td><td>W</td><td>W</td><td></td><td></td><td>SOUNDPOWERUNIT</td><td>IfcSoundPowerMeasure</td></tr>
 <tr><td>Sound power level</td><td></td><td>decibel</td><td>db</td><td>W / W</td><td></td><td></td><td>SOUNDPOWERLEVELUNIT</td><td>IfcSoundPowerLevelMeasure</td></tr>
 <tr><td>Sound pressure</td><td></td><td>pascal</td><td>Pa</td><td>Pa</td><td></td><td></td><td>SOUNDPRESSUREUNIT</td><td>IfcSoundPressureMeasure</td></tr>
 <tr><td>Sound pressure level</td><td></td><td>decibel</td><td>db</td><td>Pa / Pa</td><td></td><td></td><td>SOUNDPRESSURELEVELUNIT</td><td>IfcSoundPressureLevelMeasure</td></tr>
 <tr><td>Specific heat capacity</td><td>Derived</td><td></td><td></td><td>J / kg· K</td><td></td><td></td><td>SPECIFICHEATCAPACITYUNIT</td><td>IfcSpecificHeatCapacityMeasure</td></tr>
 <tr><td>Temperature gradient</td><td></td><td></td><td></td><td>K / m</td><td></td><td></td><td>TEMPERATUREGRADIENTUNIT</td><td>IfcTemperatureGradientMeasure</td></tr>
 <tr><td>Temperature change</td><td></td><td></td><td></td><td>K / s</td><td></td><td></td><td>TEMPERATURERATEOFCHANGEUNIT</td><td>IfcTemperatureRateOfChangeMeasure</td></tr>
 <tr><td>-</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>IfcText</td></tr>
 <tr><td>Thermal admittance</td><td>Derived</td><td></td><td></td><td>W / m2 · K</td><td></td><td></td><td>THERMALADMITTANCEUNIT</td><td>IfcThermalAdmittanceMeasure</td></tr>
 <tr><td>Thermal conductivity</td><td>Derived</td><td></td><td></td><td>W / m · K</td><td></td><td></td><td>THERMALCONDUCTIVITYUNIT</td><td>IfcThermalConductivityMeasure</td></tr>
 <tr><td>Thermal expansion coefficient</td><td></td><td></td><td></td><td>1 / K</td><td></td><td></td><td>THERMALEXPANSIONCOEFFICIENTUNIT</td><td>IfcThermalExpansionCoefficientMeasure</td></tr>
 <tr><td>Thermal resistance</td><td>Derived</td><td></td><td></td><td>m2 · K / W</td><td></td><td></td><td>THERMALRESISTANCEUNIT</td><td>IfcThermalResistanceMeasure</td></tr>
 <tr><td>Thermal transmittance</td><td>Derived</td><td></td><td></td><td>W / m2 · K</td><td></td><td></td><td>THERMALTRANSMITTANCEUNIT</td><td>IfcThermalTransmittanceMeasure</td></tr>
 <tr><td>Thermodynamic temperature</td><td>SI / Basic</td><td>kelvin</td><td>K</td><td></td><td>KELVIN</td><td>THERMODYNAMICTEMPERATUREUNIT</td><td></td><td>IfcThermodynamicTemperatureMeasure</td></tr>
 <tr><td>-</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>IfcTime <br>    (lexical representation according to ISO 8601)</td></tr>
 <tr><td>Time</td><td>SI / Basic</td><td>second</td><td>s</td><td></td><td>SECOND</td><td>TIMEUNIT</td><td></td><td>IfcTimeMeasure</td></tr>
 <tr><td>-</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>IfcTimeStamp</td></tr>
 <tr><td>Torque</td><td>Derived</td><td></td><td></td><td>N· m</td><td></td><td></td><td>TORQUEUNIT</td><td>IfcTorqueMeasure</td></tr>
 <tr><td>Vapor permeability</td><td>Derived</td><td></td><td></td><td>kg / s · m · Pa</td><td></td><td></td><td>VAPORPERMEABILITYUNIT</td><td>IfcVaporPermeabilityMeasure</td></tr>
 <tr><td>Volume</td><td>SI / Derived</td><td>cubic metre</td><td>m3</td><td>m3</td><td>CUBIC_METRE</td><td>VOLUMEUNIT</td><td></td><td>IfcVolumeMeasure</td></tr>
 <tr><td>Volumetric flow rate</td><td>Derived</td><td></td><td></td><td>m3 / s</td><td></td><td></td><td>VOLUMETRICFLOWRATEUNIT</td><td>IfcVolumetricFlowRateMeasure</td></tr>
 <tr><td>Warping constant</td><td></td><td></td><td></td><td>m6</td><td></td><td></td><td>WARPINGCONSTANTUNIT</td><td>IfcWarpingConstantMeasure</td></tr>
 <tr><td>Warping moment</td><td>Derived</td><td></td><td></td><td>N · m2</td><td></td><td></td><td>WARPINGMOMENTUNIT</td><td>IfcWarpingMomentMeasure</td></tr>
</table>
</small>

{ .table}


Table 1 &mdash; Measures and units
