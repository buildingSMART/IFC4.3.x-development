# IfcBuildingElementProxy

The _IfcBuildingElementProxy_ is a proxy definition that provides the same functionality as subtypes of _IfcBuildingElement_, but without having a predefined meaning of the special type of building element, it represents.

Proxies can also be used as spatial place holders or provisions, that are later replaced by special types of elements.

One use of the proxy object is a provision for voids, i.e. where a particular volume of space is requested by an engineering function that might later be accepted or rejected. If accepted it is transformed into a void within a building element, like a wall opening, or a slab opening. The provision for voids is exchanged as an _IfcBuildingElementProxy_ with the _PredefinedType_ = ProvisionForVoid. Such proxy shall have a swept solid geometry, where the profile of the swept solid lies on/near the surface of the referred building element and the extrusion depths is equal to or bigger then (in case of round or otherwise irregular element shape) the thickness of the building element. The appropriate property set should be attached.

In addition to the provision for voids, the building element proxy can also represent a provision for space, often the necessary space allocation for mechanical equipment that will be determined in a later design phase. The provision for space is exchanged as an _IfcBuildingElementProxy_ with the _PredefinedType_ = ProvisionForSpace.

Other usages of _IfcBuildingElementProxy_ include:

* The _IfcBuildingElementProxy_ can be used to exchange special types of building elements for which the current specification does not yet provide a semantic definition.
* The _IfcBuildingElementProxy_ can also be used to represent building elements for which the participating applications can not provide a semantic definition.

> HISTORY&nbsp; New entity in IFC2x.

## Attributes

### PredefinedType
Predefined generic type for a building element proxy that is specified in an enumeration. There may be a property set given specificly for the predefined types.
> NOTE&nbsp; The _PredefinedType_ shall only be used, if no _IfcBuildingElementProxyType_ is assigned, providing its own _IfcBuildingElementProxyType.PredefinedType_.

{ .change-ifc2x4}
> IFC4 CHANGE&nbsp; The attribute _CompositionType_ has been replaced by _PredefinedType_, being a superset of the enumerators.

## WhereRules

### HasObjectName
A Name attribute should be asserted for a building element proxy.

### CorrectPredefinedType
Either the _PredefinedType_ attribute is unset (e.g. because an _IfcBuildingElementProxyType_ is associated), or the inherited attribute _ObjectType_ shall be provided, if the _PredefinedType_ is set to USERDEFINED.

### CorrectTypeAssigned
Either there is no building element proxy type object associated, i.e. the _IsTypedBy_ inverse relationship is not provided, or the associated type object has to be of type _IfcBuildingElementProxyType_.
