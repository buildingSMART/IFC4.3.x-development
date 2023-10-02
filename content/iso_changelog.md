# Change log

This document is the second edition of ISO 16739-1. The following sections describe how compatibility issues with previous release are handled in general. A full list of all changes against the previous list are shown in Chapter F.1.

## Compatibility

The classes in the ISO 10303-11 EXPRESS schema distribution of this document are typically reflected in program code and directly influence the exchange structure (attribute counts, attribute types) using the ISO 10303-21 exchange format.

Conversely, property and quantity sets are generally more supplementary data that don't affect functioning of the software interfaces to the same extent. Property and quantity sets are also explicitly provided to rapidly address specific use cases and evolving software capabilities. Changes in property and quantity sets do not affect the structure (attribute counts, attribute types) of the ISO 10303-21 exchange formats.

As such, compatibility of property and quantity sets is not held to the same rigor as is the case for compatibility of the EXPRESS schema.

Except in rare cases, backward compatibility is a hard requirement in the evolution of this document. Nevertheless, there is a varying degree of severity in the types of changes that could occur. For example, renaming an entity name, or inserting an attribute at the beginning of the attribute sequence causes a near irrecoverable error in parsing a file written against a previous release of this document. Whereas adding an enumeration item to an existing enumeration is deemed fully backwards compatible.

> NOTE Forward compatibility is not explicitly considered in the development of this release, but seen as a desirable feature where possible.

### Deprecation

As this document evolves certain constructs become unfavourable, since they have been superseded by other constructs, because implementation in software proved inadequate or because flaws were found in the definition that were impossible to correct in a backwards compatible fashion.

In such cases the choice is often made to *deprecate* the construct, giving implementers ample time to adapt their software. Deprecation implies:

* Complying interpreters shall still be able to import deprecated definitions.
* Complying interpreters shall consider modifying the export using the proposed alternative definitions instead of the deprecated ones.

### List of known backward incompatibilities

The following backward incompatibilities occur in this document compared to its previous edition.

> NOTE For a full list of changes see the Change logs in Appendix F.1

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

The following backward incompatibilities have been introduced in this release:

|  | Severity | Element | Incompatibility |
|---|---|---|---|
| 1 | Major | IfcGridPlacement | Result of PlacementRelTo attribute moving up to IfcObjectPlacement. |
| 2 | Minor | IfcCountMeasure | Definition changed from NUMBER to INTEGER. |
