# IfcSystem

A system is an organized combination of related parts within an AEC product, composed for a common purpose or function or to provide a service. A system is essentially a functionally related aggregation of products. The grouping relationship to one or several instances of _IfcProduct_ (the system members) is handled by _IfcRelAssignsToGroup_.
<!-- end of short definition -->


> NOTE The use of _IfcSystem_ often applies to the representation of building services related systems, such as the piping system, cold water system, etc. Members within such a system may or may not be connected using the connectivity related entities (through _IfcDistributionPort_).

> HISTORY New entity in IFC1.0

## Attributes

### ServicesBuildings
Reference to the spatial structure via the objectified relationship _IfcRelServicesBuildings_, which is serviced by the system.

### ServicesFacilities
Reference to the relationship _IfcRelReferencedInSpatialStructure_ that relates the system to a spatial element.

## Concepts

### Property Sets for Objects



### System Element Attributes



