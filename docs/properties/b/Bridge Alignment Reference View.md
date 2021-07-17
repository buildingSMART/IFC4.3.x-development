Bridge Alignment Reference View
===============================

{#purpose .num}
### Purpose of the Reference View
The main purpose of this document is to define a standardized subset of the IFC4 schema, a Model View Definition MVD, that is particularly suitable for all BIM workflows in bridge projects that are based on reference models, where the exchange is mainly one-directional. Here requested modifications of the BIM data, mainly of the shape representation, are handled by a change request to the original author, and changes are not executed upon the imported IFC data with the intent to be sent back to the original source.

Compared to the Bridge Reference View the Bridge Alignment Reference View introduces the _IfcAlignment_ as a means of positioning and referencing linear infrastructure. Additionally, known locations represented by the _IfcReferent_ along a linear element can be defined and used as a reference for positioning.
