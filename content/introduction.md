The Industry Foundation Classes (IFC) are an open international standard for Building Information Model (BIM)
data. The standard comprises:

 1. A schema (provided in various forms, see [scope](scope.htm))
 2. Documentation (provided in HTML, authored in Markdown)
 3. Property and Quantity Set definitions (standardized definitions for an extensibility mechanism realised in the schema - provided in XML)
 4. Exchange or serialization mechanisms of data files, see [scope](scope.htm)

The prevalent exchange format for IFC is the Step Physical File Format (ISO
10303-21:2002; Part 21). It is a clear-text encoding of the entity instances that
make up the exchange, in which attribute values are provided as a ordered
sequence of unnamed values. 

## Conventions

The IFC specification includes terms, concepts and data specification items that originate from use within disciplines, trades, and professions of the construction and facility management industry sector. Terms and concepts uses the plain English words, the data items within the data specification follow a naming convention. Translations can be found on [translations.buildingsmart.org](https://translations.buildingsmart.org).

* the data item names for types, entities, rules and functions start with the prefix "Ifc" and continue with the English words in CamelCase naming convention (no underscore, first letter in word in upper case);
* the attribute names within an entity follow the CamelCase naming convention with no prefix;
* the property set definitions that are part of this standard start with the prefix "Pset_" and continue with the English words in CamelCase naming convention;
* the quantity set definitions that are part of this standard start with the prefix "Qto_" and continue with the English words in CamelCase naming convention.

## Model View Definitions

buildingSMART International publishes official model view definitions (MVDs) as related specifications. The official MVD policy for IFC 4.3.0 currently holds 3 levels of implementation for IFC:
- Reference View
- Alignment Based Reference View
- Design Transfer view
These three MVDs can be seen as three levels of implementation for IFC 4.3.0. They are gradual levels adding more advanced features to the implementations.  The documentation is deposited at [standards.buildingsmart.org](https://standards.buildingsmart.org).

## Architecture
  
The data schema architecture of IFC defines four conceptual layers, each individual schema is assigned to exactly one conceptual layer. The figure below shows the schema architecture IFC 4.x layered architecture.

![Figure 1 — Data schema architecture with conceptual layers](https://raw.githubusercontent.com/buildingSMART/IFC4.3.x-development/b3911e98eaf9adc5287c41d2e55beda1688be5d6/content/IFC4_layered_architecture.png)

1. **Resource layer** — the lowest layer includes all individual schemas containing resource definitions, those definitions do not include an globally unique identifier and shall not be used independently of a definition declared at a higher layer;
2. **Core layer** — the next layer includes the kernel schema and the core extension schemas, containing the most general entity definitions, all entities defined at the core layer, or above carry a globally unique id and optionally owner and history information;
3. **Interoperability layer** — the next layer includes schemas containing entity definitions that are specific to a general product, process or resource specialization used across several disciplines, those definitions are typically utilized for inter-domain exchange and sharing of construction information;
4. **Domain layer** — the highest layer includes schemas containing entity definitions that are specializations of products, processes or resources specific to a certain discipline, those definitions are typically utilized for intra-domain exchange and sharing of information.

## Compatibility

Built assets have a long lifetime. Compatibility between IFC releases is a key concern in the development of the standard. 

*Backward compatibility* is the ability for a data file, written against a previous release of the standard, to be readable by an application supporting a later version.

*Forward compatibility* is the ability for a data file, written against a new release of the
standard, to still be readable by an application supporting a previous
version of the standard and for the reading application in this scenario not to lose functionality
provided by the earlier version of the standard.

The classes in the EXPRESS schema are typically reflected in program code and directly influence the structure (attribute counts, attribute types) of
Part 21 exchanges.

Conversely, Property and Quantity Sets are generally more supplementary data that don't
affect functioning of the software to the same extent. Property and Quantity
Sets are also explicitly provided to rapidly address specific use cases and
evolving software capabilities. Changes in Property and Quantity Sets do
not affect the structure (attribute counts, attribute types) of
Part 21 exchanges.

As such, compatibility of Property and Quantity Sets is not held to the same
standard as is the case for compatibility of the EXPRESS schema.

Except in rare cases, backward compatibility is a hard requirement in the
evolution of the IFC standard. Nevertheless, there is a varying degree of
severity in the types of changes that could occur. For example, renaming an
entity name, or inserting an attribute at the beginning of the attribute
sequence causes a near irrecoverable error in parsing a file written against
a previous release of the
standard. Whereas adding an enumeration item to an existing enumeration is
deemed fully backwards compatible.

> NOTE Forward compatibility is not explicitly considered in the development of this release, but seen as a desirable property where possible.

### Deprecation

As the standard evolves certain constructs become unfavourable, since they
have been superceeded by other constructs, because implementation in software proved inadequate or because
flaws were found in the definition that were impossible to correct in a
backwards compatible fashion.

In such cases the choice is often made to *deprecate* the construct, giving
implementers ample time to adapt their software.

> NOTE Complying interpreters shall still be able to import deprecated definitions.

> NOTE Complying interpreters shall consider to modify export using the proposed alternative definitions instead of the deprecated ones.

### List of known Part 21 incompatibilities with IFC4.0.2.1

For a full list of changes see the Change logs in Appendix F.

The following entities, types and functions have been deleted in this release:

* IfcBeamStandardCase
* IfcBuildingElement
* IfcBuildingElementType
* IfcColumnStandardCase
* IfcCorrectObjectAssignment
* IfcDoorStandardCase
* IfcDoorStyle
* IfcDoorStyleConstructionEnum
* IfcDoorStyleOperationEnum
* IfcMemberStandardCase
* IfcNullStyle
* IfcObjectTypeEnum
* IfcOpeningStandardCase
* IfcPlateStandardCase
* IfcPresentationStyleAssignment
* IfcPresentationStyleSelect
* IfcProxy
* IfcSlabElementedCase
* IfcSlabStandardCase
* IfcStyleAssignmentSelect
* IfcWallElementedCase
* IfcWindowStandardCase
* IfcWindowStyle
* IfcWindowStyleConstructionEnum
* IfcWindowStyleOperationEnum

The following entities, attributes and enumerators have been deprecated in this release:

* IfcBuildingSystem
* IfcCivilElement
* IfcCivilElementType
* IfcElectricDistributionBoard
* IfcElectricDistributionBoardType
* IfcFaceBasedSurfaceModel
* IfcPostalAddress
* IfcRelConnectsPortToElement
* IfcRelServicesBuildings
* IfcTelecomAddress
* IfcTrapeziumProfileDef
* IfcBuilding.BuildingAddress
* IfcBuilding.ElevationOfRefHeight
* IfcBuilding.ElevationOfTerrain
* IfcBuildingStorey.Elevation
* IfcOrganization.Addresses
* IfcPerson.Addresses
* IfcSite.LandTitleNumber
* IfcSite.SiteAddress
* IfcSurfaceStyleRendering.DiffuseTransmissionColour
* IfcSurfaceStyleRendering.ReflectionColour
* IfcSurfaceStyleRendering.TransmissionColour
* IfcSurfaceTexture.Parameter
* IfcTextureCoordinateGenerator.Parameter
* IfcCableCarrierFittingTypeEnum.CROSS
* IfcCableCarrierFittingTypeEnum.REDUCER
* IfcCableCarrierFittingTypeEnum.TEE
* IfcFireSuppressionTerminalTypeEnum.SPRINKLERDEFLECTOR
* IfcGeographicElementTypeEnum.SOIL_BORING_POINT

The following incompatibilities have been introduced in this release:

|  | Severity | Element | Incompatibility |
|---|---|---|---|
| 1 | Major | IfcGridPlacement | Result of PlacementRelTo attribute moving up to IfcObjectPlacement. |
| 2 | Minor | IfcCountMeasure | Definition changed from NUMBER to INTEGER. |
