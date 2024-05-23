A surface feature is a modification at (onto, or into) of the surface of an element. Parts of the surface of the entire surface may be affected. The volume and mass of the element may be increased, remain unchanged, or be decreased by the surface feature, depending on manufacturing technology. However, any increase or decrease of volume is small compared to the total volume of the element.

<!-- end of short definition -->


The part–whole relationship is established by an aggregation relationship object, expressing the decomposition of an element type into one or more additive elements (element parts) and zero or more feature elements.

> HISTORY New entity in IFC4.

****Containment Use Definition****:

Surface features shall have no spatial containment relationship to the spatial structure since they are dependent on element types without spatial containment relationships or on an element occurrence with own spatial containment relationship.

* The _SELF\IfcElement.ContainedInStructure_ relationship shall be NIL.

****Geometry use definition****:

The geometric representation of _IfcSurfaceFeature_ is given by the _IfcProductDefinitionShape_, allowing multiple geometric representation.

**Local Placement**

The local placement for _IfcSurfaceFeature_ is defined in its supertype _IfcProduct_. It is defined by the _IfcLocalPlacement_, which defines the local coordinate system that is referenced by all geometric representations.

* In case of features which are part of an element type, absolute placement into the type object's implied coordinate system shall be used.
* In case of features which are voiding an element occurrence, the _PlacementRelTo_ relationship of _IfcLocalPlacement_ shall point to the local placement of the respective element.

**Shape representation**

Different shape representations may be used, depending on the nature of the feature and information requirements:

* Symbolic representation, such as the two-dimensional bounding box of a tag.
* A geometric set representing the geometric items of a mark.
* Surface representations of treated parts of the lement surface by means of _IfcShellBasedSurfaceModel_. The faces within the surface model may be included into a B-Rep model within a representation map of the parent element type.

Higher-level parameters (geometric and non-geometric) may be provided by property sets based on local agreements.

## Attributes

### PredefinedType
Indicates the kind of surface feature.

### AdheresToElement
Reference to the _IfcRelAdheresToElement_ relationship that uses this _IfcSurfaceFeature_ to adhere or treat the surface of the _IfcRelAdheresToElement_.RelatingElement.

## Formal Propositions

### HasObjectType
The attribute ObjectType shall be given if the predefined type is set to USERDEFINED.

## Concepts

### Body Geometry



#### IfcShellBasedSurfaceModel_SurfaceModel

Surface representations of treated parts of the lement surface by means of IfcShellBasedSurfaceModel. The faces within the surface model may be included into a B-Rep model within a representation map of the parent element type.

### Product Local Placement

The local placement for _IfcSurfaceFeature_ is defined in its supertype IfcProduct. It is defined by the IfcLocalPlacement, which defines the local coordinate system that is referenced by all geometric representations.

* In case of features which are part of an element type, absolute placement into the type object's implied coordinate system shall be used.
* In case of features which are voiding an element occurrence, the PlacementRelTo relationship of IfcLocalPlacement shall point to the local placement of the respective element.

### Property Sets for Objects



