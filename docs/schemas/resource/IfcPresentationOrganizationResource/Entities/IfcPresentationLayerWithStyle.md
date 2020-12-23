# IfcPresentationLayerWithStyle

An _IfcPresentationLayerAssignmentWithStyle_ extends the presentation layer assignment with capabilities to define visibility control, access control and common style information.

The visibility control allows to define a layer to be either 'on' or 'off', and/or 'frozen' or 'not frozen'. The access control allows to block graphical entities from manipulations by setting a layer to be either 'blocked' or 'not blocked'. Common style information can be given to the layer.

> NOTE&nbsp; Style information assigned to layers is often restricted to 'layer colour', 'curve font', and/or 'curve width'. These styles are assigned by using the _IfcCurveStyle_ within the _LayerStyles_.

> NOTE&nbsp; If a styled item is assigned to a layer using the _IfcPresentationLayerAssignmentWithStyle_, it inherits the style information from the layer. In this case, it should omit its own style information. If the styled item has style information assigned (such as by _IfcCurveStyle_, _IfcFillAreaStyle_, _IfcTextStyle_, _IfcSurfaceStyle_, _IfcSymbolStyle_), then it overrides the style provided by the _IfcPresentationLayerAssignmentWithStyle_.

> NOTE&nbsp; The _IfcPresentationLayerAssignmentWithStyle_ extends the presentation_layer_assignment entity as defined in ISO/IS 10303-46:1994, p. 36.

> HISTORY&nbsp; New entity in IFC2x2.

{ .change-ifc2x3}
> IFC2x3 CHANGE &nbsp;The attributes have been modified without upward compatibility.

## Attributes

### LayerOn
A logical setting, TRUE indicates that the layer is set to 'On', FALSE that the layer is set to 'Off', UNKNOWN that such information is not available.

### LayerFrozen
A logical setting, TRUE indicates that the layer is set to 'Frozen', FALSE that the layer is set to 'Not frozen', UNKNOWN that such information is not available.

### LayerBlocked
A logical setting, TRUE indicates that the layer is set to 'Blocked', FALSE that the layer is set to 'Not blocked', UNKNOWN that such information is not available.

### LayerStyles
Assignment of presentation styles to the layer to provide a default style for representation items.
> NOTE&nbsp; In most cases the assignment of styles to a layer is restricted to an _IfcCurveStyle_ representing the layer curve colour, layer curve thickness, and layer curve type.

{ .change-ifc2x4}
> IFC4 CHANGE&nbsp; The data type has been changed from _IfcPresentationStyleSelect_ (now deprecated) to _IfcPresentationStyle_.

## Formal Propositions

### ApplicableOnlyToItems
The _IfcPresentationLayerWithStyle_ shall only be used to assign subtypes of _IfcGeometricRepresentationItem_'s and to _IfcMappedItem_. There shall be no instance of subtypes of _IfcRepresentation_ in the set of _AssignedItem_'s.
{ .change-ifc2x4}
> IFC4 CHANGE&nbsp; New where rule.
