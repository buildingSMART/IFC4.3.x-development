IfcConstructionMgmtDomain
=========================

The _IfcConstructionMgmtDomain_ schema defines resource concepts in the construction management domain. Together with the _IfcProcessExtension_ and _IfcSharedMgmtElement_ schemas it provides a set of models that can be used to exchange information between construction management applications.

The _IfcConstructionMgmtDomain_ schema extends resources and resource types as applicable to construction. The objective of the _IfcConstructionMgmtDomain_ schema is to capture information that supports specific business processes and resource requirements that are wholly within the domain of interest of the Construction Manager. The aim is to provide support for information exchange and sharing within computer aided management applications.

The following are within the scope of this schema:

* resources used in the construction process including material, labour, equipment, product, crew, and sub-contract resources;
* identification of products that result from processes performed that are used as resources in future processes.
* resource productivity calculation to determine work, usage, and ultimately durations of tasks.
* resource time information to support allocations and levelling.
* resource cost information to support earned value calculations.
* resource quantities to support derived costs within cost schedules.
* time-phased data to indicate scheduled and actual work, usage, and costs at particular periods in time.
* resource type definitions describing shared productivity and cost rates that may be applied to resource occurrences.

A resource is the use of any physical or virtual entity of limited availability. A resource may be fulfilled by tangible objects such as particular people or equipment, however a resource does not represent such objects, but a particular use of such objects such as labour. Construction resources extend the concept of resources to include the quantities, costs, schedule, and other impacts from use in construction processes.

Construction management activities may take place either on a complete product (the whole), on a part of the product or on a set of products acting as a single product entity (complex). The product composition structure enabling parts, whole, and complexes to be identified is achieved using aggregation or nesting subtype of the _IfcRelDecomposes_ relationship class.
