Design Transfer View
====================

{#purpose .num}
### Purpose of the Design Transfer View
The purpose of the Design Transfer View is to provide building information with support for editing of interconnected elements. Such applications enable inserting, deleting, moving, and modifying physical building elements and spaces. The target scenario is an architect providing building design information to an engineer for a particular discipline, where geometric modifications may need to be made.

To enable such editing, higher-level design parameters must be preserved for those elements that affect multiple disciplines, and applications must generate downstream geometry consistently according to such parameters. The scope of parameters is limited to those that impact interconnected elements: for example, increasing window dimensions impacts composition of walls; moving walls impacts geometry of connected walls, adjoining spaces, coverings, and embedded elements; adjusting pipes or ducts may require resizing openings.

Examples of this design transfer workflow are:

* Coordination planning and execution (combining different discipline specific IFC models for collaboration)
* Clash detection and resolution (finding clashes and resolutions between different discipline specific IFC models)
* Integrated reference (loading an IFC model, usually from a different discipline) as an integrated model
* Quantity take-off (determine the quantities of the various model elements with the IFC model)
* Construction sequencing (taking the IFC model and associating it to a construction schedule)
* Visual presentation (for presenting the IFC model to a broad audience)

Common characteristics of the workflow using design transfer models are:

* The source of the BIM information remains with the originator or may be shared
* The full parametric behaviour, and thereby the intellectual engineering property, remains with the originator or may be tranfered
* The ownership of the model, and responsibility for its correctness, remains with the originator or may be transfered
* The original model is published as IFC4 Design Transfer model reflecting the as-is status
* The receiver of the IFC4 Design Transfer View does not need to have access to the full model content
* The receiver of the IFC4 Design Transfer View may modify the model
* The receiver of the IFC4 Design Transfer View can analyse and extract the information of the model
* If the receiver suggests or demands a change, it may be made to the model directly

The Level of Detail of the shape representation and the Level of Information for the property content of the actual reference models depends on the source model. The buildingSMART standard IDM (Information Delivery Manual) can be used to determine the minimum content for a particular workflow support. The IFC4 Design Transfer View allows rich content to be published.

{#objective .num}
### Objective
The main objective of the IFC4 Design Transfer View is to enable collaboration on design elements impacting multiple disciplines.

{#workflow-support .num}
### Workflow support
The overall goal of the IFC4 Design Transfer View is to provide workflows where building information models may be edited by design software platforms. It is not intended to capture all design parameters, but rather a limited subset affecting major building elements, along with the design results for all components within a building.

{#compatibility-concerns .num}
### Compatibility concerns
The IFC4 Design Transfer View is intended to be compatible with the IFC2x3 Coordination View where possible. Exceptions to compatibility are made to support new features and remove obsolete data structures.

{#general-scope-definition .num}
### General scope definition
All geometry is supported in the Design Transfer View, including Constructive Solid Geometry (CSG) and new Non-Uniform Rational B-Spline (NURBS) geometry defined in IFC4 for precisely describing arbitrary curved surfaces.

The Design Transfer View derives from the Reference View, such that it is a superset of the Reference View. It is valid to include geometry defined within the Design Transfer View (e.g. CSG) along with geometry defined within the Reference View (e.g. tessellation). Reference View geometry may also be omitted, as it is defined as optional.

The IFC data model provides constructs for implicit and explicit parametric modeling. Explicit parametric behavior may be represented with the IFC constraint model (_IfcRelAssociatesConstraint_) to indicate product configuration tables and geometric formulas, which is out of scope for this model view. Implicit parametric behavior is based on defined rules for common elements defined by an axis path or footprint area, and may be modelled by _standard-case_ and _elemented-case_ entities.

_Standard-case_ entities are defined by material configuration at type definitions (either _IfcMaterialLayerSet_, _IfcMaterialProfileSet_, or _IfcMaterialConstituentSet_, which are applied to an axis path or footprint area. Material profiles define cross sections of materials that are swept along a curve. Material layers define thicknesses of materials that fill a bounded area. _Standard-case_ entities include the following:

{ .gridtable}
Entity | Material | Representation
------ | -------- | --------------
_IfcSlabStandardCase_ | _IfcMaterialLayerSetUsage_ | 'Footprint'
_IfcPlateStandardCase_ | _IfcMaterialLayerSetUsage_ | 'Footprint'
_IfcWallStandardCase_ | _IfcMaterialLayerSetUsage_ | 'Axis'
_IfcColumnStandardCase_ | _IfcMaterialProfileSetUsage_ | 'Axis'
_IfcBeamStandardCase_ | _IfcMaterialProfileSetUsage_ | 'Axis'
_IfcMemberStandardCase_ | _IfcMaterialProfileSetUsage_ | 'Axis'
_IfcDoorStandardCase_ | _IfcMaterialConstituentSet_ | 'Profile'
_IfcWindowStandardCase_ | _IfcMaterialConstituentSet_ | 'Profile'
_IfcOpeningStandardCase_ | _IfcMaterialConstituentSet_ | 'Profile'


_Elemented-case_ entities are defined by compositions of elements, where each composed element is defined by material configuration at type definitions. _Elemented-case_ entities include the following:

{ .gridtable}
Entity | Components
------ | ----------
_IfcSlabElementedCase_ | _IfcPlateStandardCase_ (subfloor)<br/>_IfcElementAssembly_ (joists)<br/>_IfcBuildingElementPart_ (ceiling drywall)
_IfcWallElementedCase_ | _IfcBuildingElementPart_ (panels on forward side)<br/>_IfcElementAssembly_ (studs, track, insulation)<br/>_IfcBuildingElementPart_ (panels on reverse side)
