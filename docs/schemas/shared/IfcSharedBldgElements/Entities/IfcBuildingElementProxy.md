# IfcBuiltElementProxy

The _IfcBuiltElementProxy_ is a proxy definition that provides the same functionality as subtypes of _IfcBuildingElement_, but without having a predefined meaning of the special type of building element, it represents.

Proxies can also be used as spatial place holders or provisions, that are later replaced by special types of elements.

One use of the proxy object is a provision for voids, i.e. where a particular volume of space is requested by an engineering function that might later be accepted or rejected. If accepted it is transformed into a void within a building element, like a wall opening, or a slab opening. The provision for voids is exchanged as an _IfcBuiltElementProxy_ with the _PredefinedType_ = ProvisionForVoid. Such proxy shall have a swept solid geometry, where the profile of the swept solid lies on/near the surface of the referred building element and the extrusion depths is equal to or bigger then (in case of round or otherwise irregular element shape) the thickness of the building element. The appropriate property set should be attached.

In addition to the provision for voids, the building element proxy can also represent a provision for space, often the necessary space allocation for mechanical equipment that will be determined in a later design phase. The provision for space is exchanged as an _IfcBuiltElementProxy_ with the _PredefinedType_ = ProvisionForSpace.

Other usages of _IfcBuiltElementProxy_ include:

* The _IfcBuiltElementProxy_ can be used to exchange special types of building elements for which the current specification does not yet provide a semantic definition.
* The _IfcBuiltElementProxy_ can also be used to represent building elements for which the participating applications can not provide a semantic definition.

> HISTORY&nbsp; New entity in IFC2x.

## Attributes

### PredefinedType
Predefined generic type for a building element proxy that is specified in an enumeration. There may be a property set given specificly for the predefined types.
> NOTE&nbsp; The _PredefinedType_ shall only be used, if no _IfcBuiltElementProxyType_ is assigned, providing its own _IfcBuiltElementProxyType.PredefinedType_.

{ .change-ifc2x4}
> IFC4 CHANGE&nbsp; The attribute _CompositionType_ has been replaced by _PredefinedType_, being a superset of the enumerators.

## Formal Propositions

### HasObjectName
A Name attribute should be asserted for a building element proxy.

### CorrectPredefinedType
Either the _PredefinedType_ attribute is unset (e.g. because an _IfcBuiltElementProxyType_ is associated), or the inherited attribute _ObjectType_ shall be provided, if the _PredefinedType_ is set to USERDEFINED.

### CorrectTypeAssigned
Either there is no building element proxy type object associated, i.e. the _IsTypedBy_ inverse relationship is not provided, or the associated type object has to be of type _IfcBuiltElementProxyType_.

## Concepts

### Material Solid

The material of the IfcBuiltElementProxy is defined by
IfcMaterial and attached by the
IfcRelAssociatesMaterial.RelatingMaterial. It is
accessible by the inverse HasAssociations relationship.



> NOTE  It is illegal to assign an
> IfcMaterial to an IfcBuiltElementProxy with the
> PredefinedType = ProvisionForVoid.


Material information can also be given at the
IfcBuiltElementProxyType, defining the common attribute
data for all occurrences of the same type. It is then
accessible by the inverse IsTypedBy relationship pointing to
IfcBuiltElementProxyType.HasAssociations and via
IfcRelAssociatesMaterial.RelatingMaterial to
IfcMaterial. If both are given, then the material directly
assigned to IfcBuiltElementProxy overrides the material
assigned to IfcBuiltElementProxyType.



### Object Typing


> 
> NOTE  The IfcBuiltElementProxyType can be used to share common information among many occurrences of the same proxy without establishing a particular semantic meaning of the type.
> 


If no IfcBuiltElementProxyType is attached (i.e. if 
only occurrence information is available) the PredefinedType
should be provided. If set to .USERDEFINED. a user defined value has to be provided by the ObjectType attribute.



### Property Sets for Objects


### Spatial Containment

The IfcBuiltElementProxy, as any subtype of IfcBuildingElement, 
may participate alternatively in one of the two different containment relationships:


* the Spatial Containment (defined here), or
* the Element Composition.

