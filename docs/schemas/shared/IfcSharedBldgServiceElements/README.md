IfcSharedBldgServiceElements
============================

The _IfcSharedBldgServiceElements_ schema in the interoperability layer defines basic concepts required for interoperability primarily between Building Service domain extensions, notably _IfcHvacDomain_, _IfcPlumbingFireProtectionDomain_, _IfcElectricalDomain_ and _IfcBuildingControlsDomain_. This schema includes concepts such as basic type and occurrence definitions for flow and distribution systems and property sets for common building service scenarios such as fluid-flow properties, electrical properties, and space thermal properties.

Figure 1 illustrates the concepts of type, occurrence and performance. Types are specializations of _IfcDistributionElementType_ while occurrences are specializations of _IfcDistributionElement_. A third theme, defined in the _IfcControlExtension_ schema, relates to the performance characteristics of an occurrence using instances of the _IfcPerformanceHistory_ entity.

A type can have zero or many occurrences. Each occurrence can have many performance history entities associated with it, allowing data that is specific to a certain phase of the lifecycle to be captured and maintained throughout the life of the dataset.

!["type, occurrence and performance history concepts"](../../../../figures/ifcdistributionport_conceptslide2.gif "Figure 1 &mdash; Building service lifecycle")

The _IfcSharedBldgServiceElements_ schema specializes building services concepts symmetrically for occurrences and types, with the _primary_ functional role of the entity determining its classification into the following generic concepts:

* **Distribution Chamber**: a formed volume used in a distribution system, such as a sump, trench or manhole.
* **Energy Conversion Device**: a building systems device that converts energy from one form into another such as a boiler (combusting gas to heat water), chiller (using a refrigeration cycle to cool a liquid), or a cooling coil (using the phase-change characteristics of a refrigerant to cool air).
* **Flow Controller**: a device that regulates flow within a distribution system, such as a valve in a piping system, modulating damper in an air distribution system, or electrical switch in an electrical distribution system.
* **Flow Fitting**: a device that is used to interconnect flow segments or other fittings within a distribution system, such as a tee in a ducted system that branches flow into two directions, or a junction box in an electrical distribution system.
* **Flow Moving Device**: a device that is used to produce a pressure differential in a distribution system, such as a pump, fan, or compressor.
* **Flow Segment**: a section of a distribution system, such as a duct, pipe, or conduit.
* **Flow Storage Device**: a device used for the temporary storage of a substance (solid, liquid, or gas) such as a tank, or the voltage potential induced by the induced electron flow (a battery).
* **Flow Terminal**: acts as a terminus or beginning element in a distribution system such as a ceiling register in a ducted air distribution system, a sink in a waste-water system, or a light fixture in an electrical lighting system.
* **Flow Treatment Device**: a device used to change the physical properties of the medium, such as an air, oil or water filter (used to remove particulates from the fluid), or a duct silencer (used to attenuate noise).

Refer to the domain schemas where types and occurrences are further elaborated using _PredefinedType_ enumerations for examples of the range of supported concepts within these broad classifications. If a new type is needed within this classification, extend using the ElementType attribute. However, if a completely new concept is required that does not fit within this classification, use instances of the generic _IfcDistributionElementType_ and _IfcDistributionElement_ entities for the type/occurrence objects as needed.

Occurrences in a distribution system are typically coupled together using instances of _IfcDistributionPort_. This is also where concepts such as mass-flow properties are applied based on performance characteristics. Refer to the _IfcDistributionPort_ documentation within this schema for further elaboration on coupling together components in a distribution system and tracking the flow characteristics across the port boundaries.

> HISTORY This schema has been significantly modified in IFC2x2. Refer to the change log and issues resolution database for details.
