IfcStyledRepresentation
=======================

The _IfcStyledRepresentation_ represents the concept of a styled presentation being a representation of a product or a product component, like material. within a representation context. This representation context does not need to be (but may be) a geometric representation context.

> NOTE&nbsp; Current usage of _IfcStyledRepresentation_ is restricted to the assignment of presentation information to an material. The _IfcStyledRepresentation_ includes only presentation styles (_IfcCurveStyle_, _FillAreaStyle_, _IfcSurfaceStyle_) that define how a material should be presented within a particular (eventually view and scale dependent) representation context. All instances of _IfcStyledRepresentation_ are referenced by _IfcMaterialDefinitionRepresentation_, and assigned to _IfcMaterial_ by _IfcMaterialDefinitionRepresentation.RepresentedMaterial_.

A styled representation has to include one or several styled items with the associated style information (curve, symbol, text, fill area, or surface styles). It shall not contain the geometric representation items that are styled.

> HISTORY&nbsp; New entity in IFC2x2.
