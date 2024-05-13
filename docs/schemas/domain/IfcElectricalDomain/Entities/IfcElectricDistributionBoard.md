# IfcElectricDistributionBoard

A distribution board is a flow controller in which instances of electrical devices are brought together at a single place for a particular purpose.<!-- end of definition -->

A distribution provides a housing for connected electrical distribution elements so that they can be viewed, operated or acted upon from a single place. Each connected item may have its own geometric representation and location.

> HISTORY  New entity in IFC4

> IFC4.3.0.0 DEPRECATION Use IfcDistributionBoard instead.

## Attributes

### PredefinedType


## Formal Propositions

### CorrectPredefinedType
Either the _PredefinedType_ attribute is unset (e.g. because an _IfcElectricDistributionBoardType_ is associated), or the inherited attribute _ObjectType_ shall be provided, if the _PredefinedType_ is set to USERDEFINED.

### CorrectTypeAssigned
Either there is no electric distribution board type object associated, i.e. the _IsTypedBy_ inverse relationship is not provided, or the associated type object has to be of type _IfcElectricDistributionBoardType_.

## Concepts

### Material Set



#### Casing

Material from which the casing is constructed.

### Object Typing



### Port Nesting



#### SINK_Line_CONSUMERUNIT_ELECTRICAL

Incoming power, such as a cable connecting from the electrical utility or another distribution board.

#### SINK_Ground_CONSUMERUNIT_EARTHING

Grounding connection, such as a cable connecting to a cable fitting connected to a cold water pipe segment coming from the ground.

#### SOURCE_Circuit1_CONSUMERUNIT_ELECTRICAL

A downstream circuit, typically connected to a circuit breaker protective device.

#### SOURCE_Circuit2_CONSUMERUNIT_ELECTRICAL

A downstream circuit, typically connected to a circuit breaker protective device.

#### SOURCE_Circuit3_CONSUMERUNIT_ELECTRICAL

A downstream circuit, typically connected to a circuit breaker protective device.

#### SOURCE_Circuit4_CONSUMERUNIT_ELECTRICAL

A downstream circuit, typically connected to a circuit breaker protective device.

#### SOURCE_Circuit5_CONSUMERUNIT_ELECTRICAL

A downstream circuit, typically connected to a circuit breaker protective device.

#### SOURCE_Circuit6_CONSUMERUNIT_ELECTRICAL

A downstream circuit, typically connected to a circuit breaker protective device.

#### SOURCE_Circuit7_CONSUMERUNIT_ELECTRICAL

A downstream circuit, typically connected to a circuit breaker protective device.

#### SOURCE_Circuit8_CONSUMERUNIT_ELECTRICAL

A downstream circuit, typically connected to a circuit breaker protective device.

### Property Sets for Objects



### Quantity Sets



