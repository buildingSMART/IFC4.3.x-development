# IfcExternalReferenceRelationship

_IfcExternalReferenceRelationship_ is a relationship entity that enables objects from the _IfcResourceObjectSelect_ to have the ability to be tagged by external references.

> NOTE  This relationship is used to assign classification, library or document information to entities that do not inherit from _IfcRoot_. It has a similar functionality as the subtypes of _IfcRelAssociates_.

> HISTORY  New entity in IFC4.

## Attributes

### RelatingReference
An external reference that can be used to tag an object within the range of _IfcResourceObjectSelect_.

> NOTE  External references can be a library reference (for example a dictionary or a catalogue reference), a classification reference, or a documentation reference.
>

### RelatedResourceObjects
Objects within the list of _IfcResourceObjectSelect_ that can be tagged by an external reference to a dictionary, library, catalogue, classification or documentation.
