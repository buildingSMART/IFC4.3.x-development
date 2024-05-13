# IfcPresentationStyle

The _IfcPresentationStyle_ is an abstract generalization of style table for presentation information assigned to geometric representation items. It includes styles for curves, areas, surfaces, and text. Style information may include colour, hatching, rendering, and text fonts.<!-- end of definition -->

The different styles may include length measures (directly as a length measure with inferred unit, or indirectly as a ratio in relation to another length measure). They may apply to curve pattern, hatch line distances, text spacing and font sizes. The attribute _ModelOrDraughting_ determines whether those length measures are provided as model or draughting measures.

* Model measures, also called scale dependent measures, define the distance, size or other length measures as being always the same in model space and the distance size or other length measures on paper depend on the plotting scale.
* Draughting measures, also called scale independent measures, define the distance , size or other length measures as being always the same, when plotted on paper, independent of the plot scale.

Each subtype of  _IfcPresentationStyle_ is assigned to the _IfcGeometricRepresentationItem_'s through an intermediate _IfcStyledItem_.

> HISTORY  New entity in IFC2x3.

## Attributes

### Name
Name of the presentation style.
