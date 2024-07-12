# IfcGeographicElement

An _IfcGeographicElement_ is a generalization of all elements within a geographical landscape. It includes occurrences of typical geographical elements, often referred to as features, such as trees or terrain. Common type information behind several occurrences of _IfcGeographicElement_ is provided by the _IfcGeographicElementType_.
<!-- end of short definition -->

> HISTORY New entity in IFC4.

## Attributes

### PredefinedType


## Formal Propositions

### CorrectPredefinedType
Either the _IfcGeographicElement_ attribute is unset (e.g. because an _IfcGeographicElementType_ is associated), or the inherited attribute _ObjectType_ shall be provided, if the _PredefinedType_ is set to USERDEFINED.

### CorrectTypeAssigned
Either there is no geographic element type object associated, i.e. the _IsTypedBy_ inverse relationship is not provided, or the associated type object has to be of type _IfcGeographicElementType_.

## Concepts

### Classification Association

An IfcGeographicElement might be further qualified by referencing a feature catalog as a particular classification. The feature classification is assigned using the inverse relationship HasAssociations pointing to IfcClassificationReference. The attributes should have the following meaning:

* Catalog : _IfcClassification.Name_
* Identity: _IfcClassificationReference.Identification_
* ElementName: _IfcClassificationReference.Name_

### Object Typing



### Property Sets for Objects



### Spatial Containment



#### IfcSite

Assignment to a site within a building project context

#### IfcSpatialZone

Assignment to any spatial structure

