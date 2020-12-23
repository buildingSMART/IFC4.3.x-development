# IfcRelAssociatesLibrary

The objectified relationship (_IfcRelAssociatesLibrary_) handles the assignment of a library item (items of the select _IfcLibrarySelect_) to subtypes of _IfcObjectDefinition_ or _IfcPropertyDefinition_.

The relationship is used to assign a library reference or a more detailed link to a library information to objects, property sets or types. A single library reference can be applied to multiple items.

The inherited attribute _RelatedObjects_ define the items to which the library association is applied. The attribute _RelatingLibrary_ is the reference to a library reference, applied to the item(s).

> HISTORY&nbsp; New entity in IFC2x.

## Attributes

### RelatingLibrary
Reference to a library, from which the definition of the property set is taken.
