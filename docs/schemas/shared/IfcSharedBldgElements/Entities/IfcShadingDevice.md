# IfcShadingDevice

Shading devices are purpose built devices to protect from the sunlight, from natural light, or screening them from view. Shading devices can form part of the facade or can be mounted inside the building, they can be fixed or operable.

> NOTE  Also other building elements such as protruding slabs or balconies can act as shading devices. Those elements however have another primary purpose and are defined as _IfcSlab_ or by other subtypes of _IfcBuildingElement_.

> HISTORY  New entity in IFC4

## Attributes

### PredefinedType
Predefined generic type for a shading device that is specified in an enumeration. There may be a property set given specifically for the predefined types.
> NOTE  The _PredefinedType_ shall only be used, if no _IfcShadingDeviceType_ is assigned, providing its own _IfcShadingDeviceType.PredefinedType_.

## Formal Propositions

### CorrectPredefinedType
Either the _PredefinedType_ attribute is unset (e.g. because an _IfcShadingDeviceType_ is associated), or the inherited attribute _ObjectType_ shall be provided, if the _PredefinedType_ is set to USERDEFINED.

### CorrectTypeAssigned
Either there is no shading device type object associated, i.e. the _IsTypedBy_ inverse relationship is not provided, or the associated type object has to be of type _IfcShadingDeviceType_.

## Concepts

### Material Single


### Object Typing


### Property Sets for Objects


### Spatial Containment

The IfcShadingDevice, as any subtype of IfcBuildingElement,
may participate alternatively in one of the two different containment relationships:


* the Spatial Containment (defined here), or
* the Element Composition.

