IfcWindowStandardCase
=====================

The standard window, _IfcWindowStandardCase_, defines a window with certain constraints for the provision of operation types, opening directions, frame and lining parameters, construction types and with certain constraints for the geometric representation. The _IfcWindowStandardCase_ handles all cases of windows, that:

* are inserted into an opening, represented by _IfcOpeningElement_, using the _IfcRelFillsElement_ relationship
* have a local placement relative to this opening, and with the y-axis of the placement pointing into the opening direction
* have a profile geometry, represented by _IfcShapeRepresentation.RepresentationIdentifier_="Profile" as a closed curve to which the window parameter apply. The profile represents a rectangle within the xz plane of the local placement
* have a reference to an _IfcWindowType_ to define the opening direction and the operation type (swinging, sliding, folding, etc.) of the window. The attribute _OperationType_ shall be provided and not being UNDEFINED, and the attribute _ParameterTakesPrecedence_ shall be "TRUE".
* have a single _IfcWindowLiningProperties_ and a set of _IfcWindowPanelProperties_ instances included in the set of _HasPropertySets_ at _IfcWindowType_

> HISTORY&nbsp; New entity in IFC4.

The geometric representation of _IfcWindowStandardCase_ is defined using the following multiple shape representations for its definition:

* **Profile**: a three-dimensional closed curve within a particular shape representation. The profile is used to apply the parameter of the parametric window representation. The profile around the edges of the opening is used to apply the window lining and window panel shape parameter.
* **Body**: A SweptSolid, SurfaceModel, or Brep Representation or a CSG additionally defining the 3D shape of the standard window in addition to the parametric representation by applying the _IfcWindowLiningProperties_ and an the _IfcWindowPanelProperties_ to the Profile representation.
