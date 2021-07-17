Product Linear Placement
========================

A Product Linear Placement takes into account the ISO 19148 Linear referencing. Each product placed with Product Linear Placement has an absolute placement on the _IfcLinearPositioningElement_._Representation_ which is typically instantiated as an IfcAlignment with its appropriate axis geometry. Therefore, similarly to how _IfcSpatialElement_._ObjectPlacement_ sets the context for all contained elements, the IfcLinearPositioningElement sets the context for all elements positioned on it. Consequently, each product placement that uses Product Linear Placement references an _IfcLocalPlacement_ which is the placement of an _IfcLinearPositioningElement_ through _IfcLinearPlacement_._PlacementRelTo_.
