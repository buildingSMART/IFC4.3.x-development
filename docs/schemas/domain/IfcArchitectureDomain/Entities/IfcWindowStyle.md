# IfcWindowStyle

The window style defines a particular style of windows, which may be included into the spatial context of the building model through instances of _IfcWindow_. A window style defines the overall parameter of the window style and refers to the particular parameter of the lining and one (or several) panels through _IfcWindowLiningProperties_ and _IfcWindowPanelProperties_.

The window entity (_IfcWindow_) defines a particular occurrence of a window inserted in the spatial context of a project. The actual parameter of the window and/or its shape is defined at the _IfcWindowStyle_, to which the _IfcWindow_ related by the inverse relationship _IsDefinedBy_ pointing to _IfcRelDefinesByType_. The _IfcWindowStyle_ also defines the particular attributes for the lining (_IfcWindowLiningProperties_) and panels (_IfcWindowPanelProperties_).

The _IfcWindowStyle_ defines the baseline geometry, or the representation map, for all occurrences of the window style, given by the IfcWindow, pointing to this style. The representation of the window style may be given by the agreed set of minimal parameters, defined for the window lining and the window panel(s), or it may be given by a geometric representation used by the _IfcRepresentationMap_. The attribute _ParameterTakesPrecedence_ decides, whether the set of parameters can be used to exactly represent the shape of the window style (TRUE), or whether the attached _IfcRepresentationMap_ holds the exact representation (FALSE).

The _IfcWindowStyleOperationTypeEnum_ defines the general layout of the window style. Depending on the enumerator, the appropriate instances of _IfcWindowLiningProperties_ and _IfcWindowPanelProperties_ are attached in the list of _HasPropertySets_. See geometry use definitions there.

> HISTORY  New entity in IFC2x.

{ .deprecated}
> IFC4 CHANGE  The entity has been deprecated and shall not be used. The new entity _IfcWindowType_ shall be used instead.

## Attributes

### ConstructionType
Type defining the basic construction and material type of the window.

### OperationType
Type defining the general layout and operation of the window style.

### ParameterTakesPrecedence
The Boolean value reflects, whether the parameter given in the attached lining and panel properties exactly define the geometry (TRUE), or whether the attached style shape take precedence (FALSE). In the last case the parameter have only informative value.

### Sizeable
The Boolean indicates, whether the attached ShapeStyle can be sized (using scale factor of transformation), or not (FALSE). If not, the ShapeStyle should be inserted by the IfcWindow (using IfcMappedItem) with the scale factor = 1.
