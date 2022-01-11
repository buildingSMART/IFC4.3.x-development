Reference View
==============

{#purpose .num}
### Purpose of the Reference View
With the publication of the IFC4 release, that has been accepted as ISO 16739 by the International Standardization Organization, several enhancements and improvements over the previous IFC releases are now available for improved open BIM interoperability using the IFC protocol.

The main purpose of this document is to define a standardized subset of the IFC4 schema, a Model View Definition MVD, that is particularly suitable for all BIM workflows that are based on reference models, where the exchange is mainly one-directional. Here requested modifications of the BIM data, mainly of the shape representation, are handled by a change request to the original author, and changes are not executed upon the imported IFC data with the intent to be sent back to the original source.

Examples of this reference workflow are:

* Coordination planning (combining different discipline specific IFC models for visual checking)
* Clash detection (finding clashes between different discipline specific IFC models)
* Background reference (loading an IFC model, usually from a different discipline) as a linked model
* Quantity take-off (determine the quantities of the various model elements with the IFC model)
* Construction sequencing (taking the IFC model and associating it to a construction schedule)
* Visual presentation (for presenting the IFC model to a broad audience)

Common characteristics of the workflow using reference models are:

* The source of the BIM information remains with the originator
* The full parametric behaviour, and thereby the intellectual engineering property, remains with the originator
* The ownership of the model, and responsibility for its correctness, remains with the originator
* The original model is published as IFC4 Reference View model reflecting the as-is status
* The receiver of the IFC4 Reference View model has access to the full model content
* The receiver of the IFC4 Reference View is not supposed to modify the model
* The receiver of the IFC4 Reference View can analyse and extract the information of the model
* If the receiver suggests or demands a change, it has to be communicated as a change request to the originator
* The buildingSMART standard BCF (BIM Collaboration Format) is developed to efficiently support these change requests.

The Level of Detail of the shape representation and the Level of Information for the property content of the actual reference models depends on the source model. The buildingSMART standard IDM (Information Delivery Manual) can be used to determine the minimum content for a particular workflow support. The IFC4 Reference View allows rich content to be published.

{#objective .num}
### Objective
The main objective of the IFC Reference View is the widest possible proliferation of IFC BIM data across a big range of software application types supporting different communication and collaboration workflows.

The IFC Reference View is characterized by the ability to publish BIM data following that subset of IFC definitions that enables semantically rish content of building data, and to some degree also other built environment data, to be exchanges with a streamlined geometric representation that is optimized for analysis and display, but excludes dimension-driven geometric parameters. The geometric representation is therefore suitable for all workflow scenarios, where the imported IFC model is displayed, analysed, compared, clashed, but not parametricly modified for futher work processes.

Semantic building data models being exchanged using the IFC4 Reference View would typically include:

* physical elements with explicit geometry, properties, quantities, material, and classification
* types of elements with associated physical elements to group common definitions (geometry, properties, material, and classification)
* spatial elements (spaces, zones) with explicit geometry, properties, quantities, and classification
* spatial structure elements (site, building, story), but also spatial zones for non-vertical construction
* element breakdown structure between physical elements (assemblies, sub-assemblies, parts)
* spatial breakdown structure between spatial elements (spatial decomposition of building, story or zones)
* spatial containment structure between spatial elements and physical elements (elements in spatial zone)
* logical system structure and assignment (physical elements assigned to systems and sub systems)
* topological structure of system networks (element to port, and port to port, relationship)
* common context of the building model, providing units, coordinate system and GIS positions
* general object identification using globally unique identifier

Additional capabilities for enriching the semantic information exposed by the IFC4 Reference View can be defined as an Add-on Model View Definition. Forseeable examples are capturing 4D models with the addition of the work schedule related entities, or 5D models with the addition of construction resource related entities.

{#workflow-support .num}
### Workflow support
The overall goal of the IFC Reference View is to provide workflows where building information models are to be consumed by the widest array of software applications that do not require modifying geometry. Such applications enable viewing, estimating, building, operating, and other downstream analysis.

> EXAMPLE One target scenario is an architect providing building design information to a contractor or facility manager. It is expected that the resulting geometry would reflect sufficient realism for viewing in software (dimensions, normals, colors, textures), but not of rendering quality for artistic presentations (lighting, shader effects, curve interpolation, rasterizing).

To support the widest array of consuming applications, the resulting schema should be as limited as possible for representing geometry in the interest of minimizing resources required of application developers. Such schema should also be as compact as possible to enable downstream use on mobile devices with limited network bandwidth. It is proposed that the resulting geometry is limited to triangles with normal vectors, colour and texture coordinates and simple sweeped solids with applied colour and texture.

{#compatibility-concerns .num}
### Compatibility concerns
As the IFC4 Reference View is new (there is no corresponding concept in the IFC2x3 Coordination View), there is no constraint for compatibility, and the resulting schema will leverage new triangulation definitions in IFC4 to support more efficient data transfer.

The second Model View Definition that is proposed in parallel to the IFC4 Reference View, the IFC4 Design Transfer View, is an extension of this model view. In other words, the IFC4 Reference View is a true subset of the IFC4 Design Transfer View.

Complying software interfaces, that implements import of the IFC4 Design Transfer View, shall also be able to correctly import IFC4 Reference View data sets. But not vice versa, a complying software interface, that implements import of the IFC4 Reference View will not be capable to import IFC4 Design Transfer View data sets. It is however required that a compliant software interface for importing IFC4 Reference View displays an agreed error messange showing the IFC version, and the IFC Model View Definition of the imported IFC file, that does not match "IFC4 Reference View" with an explanation, that a non-compatible IFC file has been received.

> NOTE The correct error message and the link to further information on the buildingSMART website explaining the purpose of the different IFC Model View Deinitions need to be agreed upon.

{#general-scope-definition .num}
### General scope definition
The general scope defines the main functionalities of the IFC4 Reference View as an overview. It includes a complete listing of the model elements and model element types that are included in the IFC4 Reference View Model View Definition.

> NOTE&nbsp; The Model elements are refered to as "Root Concepts" within the Model View Definition specification, being the indiviudual root elements, that contain the attributes, geometric shapes, dynamic property sets and other semantic information that are combined and expressed as "Concepts". The common definition of a "Concept", that is applicable to many "Root Concepts" is called a "Concept Template".

The detailed scope of the IFC4 Reference View is determined by the concept templates that are included. A detailed description of each concept template is provided by Chapter 4 "Fundamental concepts and assumptions".

{#model-elements .num}
### Model elements
The main components of the IFC4 Reference View are the semantic model elements that carry a predefined meaning. The complete breakdown of all model elements declared in IFC4 are also known as the IFC4 built-in classification following an element by function classification.

In addition to each of the model elements shown here in the subsequent tables, each Model element maybe further specialized by its "_PredefinedType_", or even a user defined type.

> EXAMPLE An _IfcFireSuppressionTerminal_ is a specific model element, that may be further specialized using its _PredefinedType_ enumeration being: a sprinkler, a hose reel, a fire hydrant, or a breeching inlet. If a proper predefined type is not yet included in the specification, a user defined type can be assigned as well.

**Architectural model elements**

{ .gridtable even}
shell and core | finishing | furnishing
-------------- | --------- | ----------
_IfcBeam_ | _IfcCovering_ | _IfcFurniture_
_IfcColumn_ | _IfcRailing_ | _IfcSystemFurnitureElement_
_IfcChimney_\* | _IfcShadingDevice_ | -
_IfcRamp_+ | _IfcCurtainWall_ | -
_IfcStair_++ | _IfcDoor_ | -
_IfcRoof_ | _IfcWindow_ | -
_IfcSlab_ | - | -
_IfcWall_ | - | -


{ .note}
> LEGEND&nbsp; \* new in IFC4, + includes _IfcRampFlight_, ++ includes _IfcStairFlight_

**Structural model elements**

{ .gridtable even}
Foundation &amp; Frame | Reinforcement | Fastener, etc.
---------------------- | ------------- | --------------
_IfcFooting_ | _IfcReinforcingBar_ | _IfcFastener_
_IfcPile_ | _IfcReinforcingMesh_ | _IfcMechanicalFastener_
_IfcMember_ | _IfcTendonAnchor_ | _IfcBuildingElementPart_
_IfcPlate_ | _IfcTendon_ | _IfcDiscreteAccessory_


> NOTE Architectural elements, like _IfcWall_, _IfcSlab_, _IfcBeam_, etc, are also used in structural models, and vice versa

**Building service model elements**

The model element specialization structure within the building service domain within the IFC standard is organized accoring to its function within a distribution system, and not primarily according to the main building service discipline, within it is mainly used.

The internal specialization structure for building service elements at its highest level is also independed of the fluid used within the distribution system:

* flow segments 
* flow fittings 
* flow terminals 
* flow moving devices 
* flow storage devices 
* flow controller 
* energy conversion device 
* distribution control elements 

The following tables intents to assign the model elements to the various disciplines within the building service system domain.

{ .gridtable even}
general MEP elements | used for gases and fluids | ports for connectivity
-------------------- | ------------------------- | ----------------------
_IfcEngine_\* | _IfcFlowMeter_\* | _IfcDistributionPort_
_IfcMedicalDevice_\* | _IfcFilter_\* | -
_IfcUnitaryEquipment_\* | - | -


{ .gridtable even}
Heating, Cooling | Plumbing | Common
---------------- | -------- | ------
_IfcBoiler_\* | _IfcFireSuppressionTerminal_\* | _IfcPipeSegment_\*
_IfcBurner_\* | _IfcInterceptor_\* | _IfcPipeFitting_\*
_IfcCoil_\* | _IfcSanitaryTerminal_\* | _IfcPump_\*
_IfcSpaceHeater_\* | _IfcStackTerminal_\* | _IfcValve_\*
_IfcTubeBundle_\* | _IfcTank_\* | -
- | _IfcWasteTerminal_\* | -


{ .gridtable even}
Ventilation | Air conditioning | Common
----------- | ---------------- | ------
_IfcAirTerminalBox_\* | _IfcAirToAirHeatRecovery_\* | _IfcDuctSegment_\*
_IfcDamper_\* | _IfcChiller_\* | _IfcDuctFitting_\*
_IfcDuctSilencer_\* | _IfcCondenser_\* | _IfcAirTerminal_\*
- | _IfcCooledBeam_\* | _IfcFan_\*
- | _IfcCoolingTower_\* | -
- | _IfcEvaporativeCooler_\* | -
- | _IfcEvaporator_\* | -
- | _IfcHeatExchanger_\* | -
- | _IfcHumidifier_\* | -
- | _IfcCompressor_\* | -


{ .gridtable even}
Electrical | cont. | Common
---------- | ----- | ------
_IfcElectricAppliance_\* | _IfcAudioVisualAppliance_\* | _IfcCableSegment_\*
_IfcElectricDistributionBoard_\* | _IfcCommunicationsAppliance_\* | _IfcCableFitting_\*
_IfcElectricGenerator_\* | _IfcJunctionBox_\* | _IfcCableCarrierSegment_\*
_IfcElectricMotor_\* | _IfcLamp_\* | _IfcCableCarrierFitting_\*
_IfcElectricFlowStorageDevice_\* | _IfcLightFixture_\* | -
_IfcElectricTimeControl_\* | _IfcSolarDevice_\* | -
_IfcMotorConnection_\* | _IfcSwitchingDevice_\* | -
_IfcProtectiveDevice_\* | _IfcTransformer_\* | -


{ .gridtable even}
Building automation | cont. | cont.
------------------- | ----- | -----
_IfcActuator_\* | _IfcFlowInstrument_\* | _IfcSensor_\*
_IfcAlarm_\* | _IfcProtectiveDeviceTrippingUnit_\* | -
_IfcController_\* | _IfcUnitaryControlElement_\* | -


{ .note}
> LEGEND&nbsp; \* new in IFC4, note all building service occurrence elements are new, the previous IFC2x3 release only included the generic occurrence elements: _IfcFlowSegment_, _IfcFlowFitting_, _IfcFlowTerminal_, _IfcFlowMovingDevice_, _IfcFlowStorageDevice_, _IfcFlowController_, _IfcEnergyConversionDevice_, and _IfcDistributionControlElement_. Those are still available as general purpose MEP Model elements, but its use is discouraged.

**Other model elements**

{ .gridtable even}
Other elements |
--------------
_IfcBuiltElementProxy_+ |
_IfcCivilElement_\*++ |
_IfcGeographicElement_\* |
_IfcDistributionChamberElement_ |
_IfcElementAssembly_ |
_IfcTransportElement_ |


{ .note}
> LEGEND&nbsp; \* new in IFC4, + also used as general element proxy ++ provided as stub for future infrastructure extensions

**Spatial elements, spatial structure and grouping elements**

{ .gridtable even}
Spatial structure | other grouping structure | others
----------------- | ------------------------ | ------
_IfcSpace_ | _IfcZone_ | _IfcGrid_
_IfcBuildingStorey_ | _IfcSystem_ | -
_IfcBuilding_ | _IfcBuildingSystem_\* | -
_IfcSite_ | _IfcDistributionSystem_\* | -
_IfcSpatialZone_\*+ | _IfcDistributionCircuit_\* | -
- | _IfcGroup_ | -


{ .note}
> LEGEND&nbsp; \* new in IFC4, + provided as a stub for non vertical constructions

{#odel-element-types .num}
### Model element types
Model element types are part of the IFC4 Reference View. They enable to describe and share common model element information that are shared by multiple occurrences of the same type. Sharable type information includes:

* Geometric shape representation; 
* Property information; 
* Material information. 

> EXAMPLE A particular air outlet as an article, with its shape, its material and its manufacturer information being described once as a type and then having several occurrences, each placed within the building, referencing the same type and hence its shape, material and properties.

Most of the Model elements introduced in the previous session have a corresponding Model element type, such as:

* _IfcWall_&nbsp;&mdash;&nbsp;_IfcWallType_;
* _IfcFastener_&nbsp;&mdash;&nbsp;_IfcFastenerType_;
* _IfcFan_&nbsp;&mdash;&nbsp;_IfcFanType_.

Only the following spatial structure elements _IfcSite_, _IfcBuilding_, _IfcBuildingStorey_, the grouping elements _IfcGroup_, _IfcZone_, _IfcSystem_ (and subtypes), and the _IfcDistributionPort_ and _IfcGrid_ do not have matching element types.

{#overview-on-major-concepts-used .num}
### Overview on major concepts used
{#object-attribute .num}
#### Object attribute
All model elements, listed in the previous section, are defined by several generic and direct object attributes, some specific model elements do carry additional direct attributes. The usage of the direct generic attributes is defined within the following concept templates (see also Chapter 4 "fundamental concepts and assumptions"):

* "_Software Identity_", it defines how to apply the Globally Unique Id and how to compress it during exchange; 
* "_User Identity_", it defins the meaning of _Name_, _Description_, _LongName_and _Tag_attributes; 
* "_Object Occurrence Predefined Type_", it defines how to use the _PredefinedType_and in case of user defined types, how to assign the user defined type information within the _ObjectType_attribute for occurrences of model elements; 
* "_Element Type Predefined Type_" it defines how to use the _PredefinedType_and in case of user defined types, how to assign the user defined type information within the _ElementType_attribute for types of model elements. 

{#project-context .num}
#### Project context
There is a single instance of _IfcProject_within each IFC data set. It sets the context for the exchange, including units, geometric context, global positioning and classification systems used within the data set. The usage of the project context is defined within the following concept templates (see also Chapter 4 "fundamental concepts and assumptions"):

* "_Project Units_", declaration of the units used within this data set, all geometric representations are forced to use the global units (e.g. for length measure and plane angle measure), property values may override global unit declarations; 
* "_Project Representation Context_", declaration of the 3D and 2D representation contexts, including precision factors; 
* "_Project Global Positioning_" (new in IFC4), positioning the project engineering coordinate system (right handed Cartesian coordinate system) within a global coordinate reference system; 
* "_Project Classification Information_", providing the name and version information about the classification systems used within the data set. 

{#object-definition .num}
#### Object definition
A main objective of the IFC4 Reference View is to enable rich information content for each model element. Model element occurrences can refer to their model element types for sharing common information. General properties are attached to model elements as property sets, either directly to the model element occurrence, or to its type. Individual model element occurrences can hold their quantities, if those are pre-calculated by the sender of the IFC data set. The usage of the object definition is defined within the following concept templates (see also Chapter 4 "fundamental concepts and assumptions"):

* "_Object Typing_", associates the Model element occurrences with the corresponding element type; 
* "_Property Sets_", assigns dynamically defined property sets, holding set of individual properties, to the model element occurrences of element type; 
* "_Quantity Sets_", assigns dynamically defined quantity sets, holding set of individual quantities, to the model element occurrences. 

{#object-typing .num}
##### Object typing
The contept template describes the mechnism of associating model element occurrences to the corresponding type and the way and restrictions of overriding type based properties by properties directly assigned to the model element occurrences.

{#property-sets .num}
##### Property sets
Property sets hold, as the name suggests, a set of properties grouped by a common theme. Each individual property has:

* a name 
* an optional description 
* a value, or number of values, of a given datatype 
* a unit or the information of being unitless 

The semantic meaning of each property is provided by its name. Properties, that are semantically declared within the scope of the IFC4 Reference View, are based on a property definition template that is published as an instrict part of the Model View Definition. Extensions to the property definitions can also be defined outside the property definition scope of the IFC4 Reference View, however the name prefix for property sets "Pset_" is restricted to properties defined within the original scope of IFC.

There are two ways to declare property templates:

* using the Property Set Definition PSD schema, an XML schema developed independent of the IFC specification, 
* using the newly introduced IFC4 property set template and property template 

> NOTE The PSD Schema has been used since many earlier versions of the IFC standard and has a broad legancy. The newer property set template definitions are now part of the IFC schema and can therefore be embedded within an IFC data set directly. Both schemas can be mapped without information loss.

{#quantity-sets .num}
##### Quantity sets
Quantity sets hold, as the name suggests, a set of quantities pre calculated for the model element occurrence. Each individual quantity has:

* a name 
* an optional description 
* a value of a given datatype corresponding to the quantity measure (length, area, volume, weight, time 
* a unit 
* a quantity formula, describing how the quantity value was calculated 

The semantic meaning of each qualtity is provided by its name. Quantities, that are semantically declared within the scope of the IFC4 Reference View, are based on a quantity definition template that is published as an instrict part of the Model View Definition. Extensions to the quantity definitions can also be defined outside the quantity definition scope of the IFC4 Reference View, however the name prefix for quantity sets "Qto_" is restricted to quantities defined within the original scope of IFC.

{#object-association .num}
#### Object association
In addition to the Property sets and the Quantity sets, also a classification reference to an external classification system can be assigned, and material as either single material, a material constituent sets or an material layer sets aor material profile sets combining material information with dimensions can be associated to one or many model elements.

> NOTE Material dimensions are layer thicknesses, or profile geometries for e.g. a column with an embedded steel profile and a concrete protection. Within the IFC4 Reference View, such material dimensions are used exclusively as alphanumeric information, and not as part of a dimension driven parametric shape representation.

The usage of the object association is defined within the following concept templates (see also Chapter 4 "fundamental concepts and assumptions"):

* "_Material Association_"; assigns a material (or material set - constituent, layer, profile) to one or several model elements (either to element occurrences, or as shared material information to element types). 
* "_Classification Association_"; assignes a classification reference to one or several model elements. 

{#product-shape .num}
#### Product shape
The first main objective of the IFC4 Reference View is to enable the exchange of highly accurate, not non-parametric, geometric representations of the model elements. Each model element is placed directly or indirectly within the project coordinate system, defining its own object coordinate system. The geometric representation items describing its shape are positioned within this object coordinate system.

In order to minimize the effort for receiving and interpreting the geometic representations by the receiving software systems, in terms of development effort, processing power and loading times, the complexity and variety of geometric models has been minimized for the IFC4 Reference View.

{#product-placement .num}
##### Product placement
Each model element defines its own object coordinate system. The placement is defined by the following concept template:

* "_Product Local Placement_", creating an object coordinate system for the shape representation of the model element, either absolutely to the project engineering coordinate system, or relatively to another object coordination system. 

{#product-geometric-representation .num}
##### Product geometric representation
In scope of geometric shape representations of the 3D body geometry of physical and spatial elements are the following concept templates:

* "_Body Tessellation Geometry_", using tessellated geometry in form of triangulated tessellations for describing the body shape of the model element; 
* "_Body SweptSolid Geometry_"; using extruded solid geometry or revolved solid geometry for describing the body shape of the model element; 
* "_Body AdvancedSweptSolid Geometry_"; using advanced swept solid geometry of circular cross sections for describing the body shape of the model element, only the swept disk solid is in scope; 

It is the default geometric representation of all model elements, allowing for a surface model representation with an indicator for closed shells (and therefore true volumes). The tessellated representation offers a very efficient way of exchanging 3D shape date, both for data set sizes and for processing time. Optionally the face normals can be exchanged as well.

Since curved shapes would lead to very densely triangulated areas, the following swept solid based representations are also in scope of the IFC4 Reference View, balancing simplicity and compactness of representation:

All other geometric models are out of scope of the IFC4 Reference View, in particular Boolean operations required for Constructive Solid Geometry CSG.

> NOTE The IFC2x3 Coordination View included CSG capabilities, the IFC4 Reference View therefore imposes a more restricted geometric representation of model elements. The IFC4 Design Transfer View should be used, if more complex geometric representations are required by the workflow. In particular, if a dimension-driven parametric representation, used by the IFC4 standard case elements, is needed.

The geometric shape representation can either be directly assigned to a model element, or to its type. In case of type-based geometry, a the following representation type is used at the model element using the following concept template:

* "_Mapped Geometry_", mapped representation defined at the corresponding element type. A mapped representation uses Cartesian transformation operations to place the type-based geometry within its object coordinate system. 

As an exception, the following elements, _IfcGrid_, _IfcSpace_, and _IfcSpatialZone_ may have an additional foot print 2D geometry (in case of _IfcGrid_this is the only geometric representation. It is described in the following concept template:

* "_FootPrint Geometry_", defining a 2D shape representation within the XY plane of the object coordinate system. 

{#geometric-presentation .num}
##### Geometric presentation
Visual appearance is an important factor for the communication process using BIM data. The objective is not to support photo-realistic rendering of reference models, but to use color, basic rendering, and texture information to add visually accessible meaning to the model elements.

In scope of presentation capabilities for the appearance of model element shapes are the following partial concept templates:

* "_Surface Style Shading_", applying a single coloring for each solid; 
* "_Surface Style Rendering_", applying a single rendering (color, transparency, reflection, etc.) for each solid; 
* "_Surface Style textures_", applying a single texture for each solid according to a texture mapping based on the solid type; 
* "_Suface Style Tessellation_", applying a color and/or texture for each face of a tessellated solid. 

The visually adaquate presentation of model elements is constraint by the shape representation

* for tessellated geometry: color per face, texture per face 
* for swept solid geometry: color and rendering information per solid, texture applied to solid using standard mapping 

{#object-composition .num}
#### Object Composition
The object composition functionality describes the product breakdown structure of model elements within an IFC data set, with separate breakdown structures for physical elements and spatial elements. Physical element structures describe parts and assemblies, spatial element structures describe vertical structures (for buildings) and horizontal structures (for other assets - as a stub in this release). A specific type of decomposition is the voiding - a subtraction of a void from a physical element. Another specific type is the nesting of ports within a distribution elements.

The usage of the object association is defined within the following concept templates (see also Chapter 4 "fundamental concepts and assumptions"):

* "_Element Decomposition_", creating a hierarchical product breakdown structure relationship between assemblies and parts; 
* "_Spatial Decomposition_", creating a hierarchical spatial decomposition relationship between spatial structure elements; 
* "_Element Voiding_", creating a voiding relationship between a physical element and penetrating voids - within the scope of the IFC4 Reference View this relationship is a logical relationship, the void is already part of the geometry of the physical element, 
* "_Port Nesting_", creating an 1:N relationship between the physical element and one or many ports defining inlets or outlets - used for distribution elements. 

{#object-assignment .num}
#### Object Assignment
The object assignment defines the assignment of objects, such as a link between model elements to groups, tasks or resources. Only the grouping assignment is in scope of the IFC4 Reference View and defined within the following concept template:

* "_Group Assignment_", Assignment of one or several model elements to a group. It includes the more specific assignments of _Grouping General_, _Grouping to System_, and _Grouping to Zones_. 

{#object-connectivity .num}
#### Object Connectivity
The object connectivity defines the interlinkage between model elements. Examples are the link between physical elements and the spatial structure, where they are located, of the connection betwee the two ports of two consecutive distribution elements.

The usage of the object association is defined within the following concept templates (see also Chapter 4 "fundamental concepts and assumptions"):

* "_Spatial Structure_", defines the containment of a physical element within a spatial container; 
* "_Port Connectivity_", defines the connection and the direction of flow between two ports of consecutive distribution elements; 
* "_Building Service Connectivity_", links a spatial or distribution system to a spatial structure (such as a building section); 
* "_Element Filling_", links a filling (usually a door or window) to an opening (usually in a wall or slab).
