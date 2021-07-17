IFC2x3 to IFC4 4.0.0.0
======================

{ .std}
The IFC4 release combines a number of feature increases with major rework and improvement of the existing IFC specification. The overall goal is to enhance the consistency throughout the IFC schema, reduce the model footprint needed to populate an IFC dataset, and to apply the lessons learnt from current implementation and usage. IFC4 has been developed as the next basis for IFC enabled interoperability of Building Information Models as the standard for open BIM.

{ .std}
&nbsp;

{ .std}
**Core Definitions**

{ .std}
A new project library concept has been added that defines the register of all types (families or styles) of objects and their property templates that is associated to a project. The new concept of property set templates and property templates allow for the definition of property templates for the individual properties to be contained in the same project data set.

{ .std}
Product types can now be decomposed into parts and these declaring parts can be used to inform the parts of a decomposed occurrence, hence the concept of a deep copy of a type with decomposed part structure is supported.

{ .std}
The IFC object definition (occurrence and type objects) inheritance tree is now synchronized and the concept of providing a predefined type enumeration is consistently applied  with only a few noted exceptions. The IFC object definition inheritance tree represents the in-built IFC object catalog (or classification) and can be used to map external classifications to and from.  The IFC object definitions for building service components and systems has been greatly unified and if necessary extended. If provides now a neutral catalog for building service design, commissioning and operation and maintenance.

{ .std}
&nbsp;

{ .std}
**Building Elements**

{ .std}
Major subtypes of building element, slab, plate, beam, column, member, door and window, have been separated into a general definition and a specific specialization to represent the standard cases for a parametric exchange of its shape, material and underlying element type. For those elements there is now a separate standard case subtype available. For walls and slabs there is now in addition a subtype to handle the aggregated walls and slabs separately from the standard walls and slabs. It allows to add more control over the applicable aggregations. Element type definitions have been added for roof, stair and ramp. The chimney has been added as a new building element subtype.

{ .std}
The definition of material has been greatly enhanced to allow e.g. for wall layers to have vertical offsets, for beams, columns, and members to have a material definition of profiles and for supporting composite profile definitions (see Material below). The definitions of geometric representation items has been extended by new entities for tapered sweeps, by improved definitions for arbitrary sweeps and by an easier way to represent mirrored profiles (see Geometry below).

{ .std}
All longitudinal elements (beam, column, and member) can now carry an axis representation and a cardinal point to describe the position of the profile related to the axis. The shape representations have been extended to allow for advanced sweeps (along any directrix and with tapering). All planar elements (wall, slab, and plate) can now carry a surface representation.

{ .std}
The parametric definitions for doors and windows is extended and a standard case door and window is provided as well. The quantity use definitions of all building elements have been updated to reflect the new agreements on base quantities.

{ .std}
Provision for voids are supported by a special kind of proxy object and the interference relationship can be used to communicate the full or partial interference between elements.

{ .std}
Standardized base quantities are now added to the IFC specification for all relevant building and spatial elements. A separate, multi-lingual, xml-based base quantity configuration file is added for those elements covering name, unit and definition of the base quantities.

{ .std}
Standard property sets for capturing environmental impact indicators and values have been added to the specification for elements and element types.

{ .std}
&nbsp;

{ .std}
**Spatial Elements**

{ .std}
With the new entity for spatial zones, the zone can now have own location, shape and functional type as required e.g. in thermal or lighting zones. Both zones, with an without own shapes, can now be assigned to different levels of the project structure.

{ .std}
Space boundaries for curved building elements, such as arc walls, can now be defined by bounded cylindrical and bounded swept surfaces. A clear differentiation between 1st and 2nd level space boundaries has been made in the documentation.

{ .std}
External spaces to separate the external air, earth, water, with the definition of external space boundaries to identify the gross volume of stories or buildings.

{ .std}
A new entity for geographic elements placed in the context of a site has been added. Using the enhanced external reference mechanism (see Classification below) those geographic elements, as any other element, can be assigned to feature catalogs or any other external classification system.

{ .std}
&nbsp;

{ .std}
**Building Service Systems**

{ .std}
A specialization of System has been added to capture the concepts of a distribution system in a new element. The distribution systems have a predefined type for various heating, cooling, ventilation, plumbing, security and electrical systems. A new entity has been introduced for circuits.

{ .std}
The definition of distribution ports is greatly enhanced, with the possibility to assign ports to manufacturer types (before inserting into a project context). Ports are now defined using a nesting relationship to support ordering, more compact file size, and compatibility with IFC2x3 (both forward and backward). Clarifications have been made to the various property sets around the use of ports. Static property definitions have been reorganized into design and performance-based property sets.

{ .std}
For all building services schemas, occurrence entities have been added in parallel with type entities for overall consistency and to support usages where product type information might not be elaborated (early design, existing construction, parts within product types, etc.). The building service component structure has been greatly unified and extended.

{ .std}
&nbsp;

{ .std}
**Energy calculations**

{ .std}
The definition of space boundaries is updated to support energy calculations and advanced simulations. Thermal boundaries are added as a special subtype with direct reference to the opposite boundary and inner boundaries. External boundaries are now separated when facing outer air, earth, water, or neighboring buildings.

{ .std}
&nbsp;

{ .std}
**HVAC Elements**

{ .std}
The definitions of HVAC elements in regard to their system behavior (segment, fitting, flow terminal, energy conversion, etc.) are semantically improved. Examples include: a space heater has been changed to be a flow terminal (and to include also electric heaters), a gas burner can been generalized into a fuel independent burner class, etc.

{ .std}
A substantial number of documentation improvements have been made to both the semantic definitions and enumerators for many of the HVAC entity types. So have e.g.

{ .std}
tank type enumerators been redefined along functional definitions rather than construction definitions.  Diagrams have been added to illustrate port connectivity for air terminals and boilers.

{ .std}
Pipes and ducts now have specific entities to allow for parametric definitions.&nbsp; Segments can now carry an axis representation for sweeping a material profile set.

{ .std}
&nbsp;

{ .std}
**Electrical**

{ .std}
Improvements have been made to support for protective devices including separation of tripping and breaker units. More protective device types are supported with enhanced detail in property sets. In particular, curve interpolation has been added to property specification.

{ .std}
Cores and busbars have been added to cable segments. Electrical distribution board types have been added in place of electrical distribution points matching the customary type/occurrence pairings. Electric heaters have been moved to being types of space heater (rationalizing heaters by function rather than energy source). Types of electric appliances have been more clearly identified as temporarily connected loads (through a plug/socket outlet connection).

{ .std}
Audio visual and communication appliance types are now supported separately from electrical appliance type. These appliances respond to the improvements in identification of distribution systems.

{ .std}
&nbsp;

{ .std}
**Structural
modeling and detailing elements**

{ .std}
Due to the changes to Building Elements, cross section definition of columns, beams and similar elements has been enhanced.&nbsp; Section geometry and material information is now associated with building elements in the same fashion as with walls and slabs.&nbsp; Profile information is provided already at a higher level than the geometric representation.&nbsp; References to standards or libraries can now be added to profile definitions, and a number of details in profile definitions have been enhanced, e.g. by simpler mirroring of asymmetric profiles.

{ .std}
Structural elements for foundations can now be accompanied by type objects.&nbsp; Type objects are also available for element components like insulations now.&nbsp; New classes for manufacturing details such as cutouts have been added.&nbsp; The Core Definition changes for decomposed type objects enable effective models of detailed designs.

{ .std}
&nbsp;

{ .std}
**Structural
analysis elements**

{ .std}
The structural analysis domain model has been cleaned up and partially simplified.&nbsp; The use of topology representations and coordinate systems has been clarified.&nbsp; Profile and material association has been brought in line with Building Elements.&nbsp; More flexible models of curved surface members are now available due to Geometry changes.

{ .std}
Distributed loads are now modeled in a more straight-forward way.&nbsp; This change also made it possible to provide analysis results not only at point connections but also at curve or surface items.&nbsp; Required or provided reinforcement of surface members (slabs and walls) can now be included as well.&nbsp; Load cases and boundary conditions received minor enhancements.

{ .std}
&nbsp;

{ .std}
**Property Sets**

{ .std}
The first multi-lingual property set definitions are added for spatial and building elements (so far in French, German, Japanese, and Chinese). The multi-lingual capability is based on an XML configuration file for property set definitions and can be used to easily localize property sets in different markets.

{ .std}
&nbsp;

{ .std}
**Geometry**

{ .std}
Additional entities are added to the geometry resources. (1) The definition of manifold boundary representation has been enhanced to include advanced B-reps, based on NURBS. Therefore b-spline surfaces and b-spline curves are added. (2) The curve bounded surface based on bounding p-curves (curves defined in the parametric space of a surface) is added to allow any surface to be bound; it was restricted to only planar surfaces before. (3) Tapered solid of extrusion and tapered solid of revolution are now included to define simple taper, restricted to one section and to topological similarity of the start and end profile. (4) A fixed reference swept area solid is added to define an advance sweep along a directrix with a fixed orientation of the profile. The swept disk solid has been simplified by implicit start and end points on the directrix. (5) Elementary surfaces have been enhanced by incorporation or cylindrical surfaces. (6) Tessellated geometry is added to support triangle-based meshes with optional normals, texture coordinates, and color mappings using a compact format; rather than converting to B-rep, this enables a more compact and lossless representation of shapes imported from common geometry file formats.

{ .std}
&nbsp;

{ .std}
**Presentation**

{ .std}
The ability to assign graphic presentation information to geometric representation items and material definitions has been made more efficient by removing inefficient intermediate links. The use of texture maps has been corrected and improved and now based on X3D definitions.

{ .std}
&nbsp;

{ .std}
**Coordinate Systems**

{ .std}
The engineering, right-handed Cartesian coordinate system, that is still solely used to be the coordinate system of the IFC data set, can now include projection information to place it in any geographic coordinate system, including a map coordinate system. The constraint to not share local placement objects among multiple elements is relaxed.

{ .std}
&nbsp;

{ .std}
**Processes**

{ .std}
The concept of a process type and relevant subtypes has been introduced. Sequencing is applicable both to process type and to process occurrences. Definition of task times has been simplified, which now are directly attached to tasks and not to a relationship that assigns the task to a schedule. The documentation has been improved giving examples how to use work plans, work schedules and task hierarchies. It also explains the use of a summary task and the possibility to define a work task order for viewing purposes. It is furthermore possible to define work calendars with various recurrence patterns and assign them to work schedules, work tasks and resources. The new process definitions significantly reduce the model footprint when capturing 4D datasets.

{ .std}
&nbsp;

{ .std}
**Costs**

{ .std}
Definition of cost values has been simplified, which now are directly attached to cost items and not to a relationship.  The documentation has been improved giving examples how to use cost schedules, cost item hierarchies, and cost values.  It also explains how to link cost items to quantities from building elements, tasks, and resources. The new cost definitions significantly reduce the model footprint when capturing 5D datasets.

{ .std}
&nbsp;

{ .std}
**Construction
Resources**

{ .std}
The definitions for construction resources have been fully reworked, a notion of resource types (or templates) is added. The assignment of construction resources to schedules and costs is improved.

{ .std}
&nbsp;

{ .std}
**Constraints**

{ .std}
Constraints have been simplified and streamlined to support direct lists of metrics, where values may be defined using project default units. For aggregated constraints, more logical operators are now available. Constraints are now classified using the same external reference mechanism as other resource objects. Constraints now support references to attribute values, table mappings, and formulas.

{ .std}
&nbsp;

{ .std}
**Approvals**

{ .std}
Approvals can be assigned, in addition to properties, to other resource objects: documents, actors and materials. Also, documents (and other external references) can be associated with approvals.

{ .std}
&nbsp;

{ .std}
**Date and
Time**

{ .std}
The date and time definitions in IFC are now based on ISO 8601 string format (also identical with the equivalent XSD data types). It reduces the model footprint, particularly for ifcXML implementations.

{ .std}
&nbsp;

{ .std}
**Materials**

{ .std}
Definition and usage of material profile sets for linear elements are now supported, in addition to already existing material layer sets for elements such as walls and slabs. Both material layers and profiles can be given offsets with regard to their parent sets (for end/edge detail), and profile sets can be aligned according to specified cardinal points in their usage.

{ .std}
In general, materials now have the description and category supported and they can be classified using the same external reference mechanism as other resource objects; in material layers and profiles additionally their priority can be given (to apply in connection details).&nbsp; Also, composite materials can now be represented (constituents with their relative amounts), as well as arbitrary (unstructured) collections of different materials, as named and described sets. Extended material properties are defined for timber and wood-based materials (anisotropic).

{ .std}
&nbsp;

{ .std}
**Classification**

{ .std}
Classifications and library references now have the publication location supported as a web based (URI) reference whilst the classification edition is made optional. The label used for classification references can also now be split into facets with user defined separators. Library references additionally have a language attribute enabling the language used to be identified. Classifications and library references can now also be assigned to properties.

{ .std}
To support the use of dictionary content within the buildingSMART IFD library, a resource object relationship has been added that enables entities within the resource layer of the IFC technical architecture to have identifiers defined through use of external reference location and reference attributes.

{ .std}
&nbsp;

{ .std}
**General
Usage of Specification**

{ .std}
Great effort has been spent to better document the dependencies and usage between the various objects, relationships and properties/quantities, etc. A series of instantiation diagrams have been added to the entity descriptions.

{ .std}
&nbsp;

{ .std}
&nbsp;

{ .std}
_Disclaimer: The "What's New section of this IFC release is
provided as an overview of changes. It is intended to be an informative summary
and is not a complete listing of all changes made or a complete description of
individual changes. For a detailed summary of all changes made, see the change
log for this IFC release._
