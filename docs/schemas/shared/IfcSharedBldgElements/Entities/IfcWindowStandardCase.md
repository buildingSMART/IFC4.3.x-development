# IfcWindowStandardCase

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

## Concepts

### Profile Geometry

The following additional constraints apply to the 'Profile'
representation type:


* Curve: being an IfcPolyline defining a
rectangle.
* Position: The curve shall lie in the xz plane of the
object placement coordinate (the y coordinate values of the
IfcCartesianPoint's shall be 0.).


As shown in Figure 299, the profile defines the outer boundary to which the window
lining parameters relate as:


* IfcWindowLiningProperties.LiningDepth starting at
distance defined by LiningOffset going into the positive y
direction.
* IfcWindowLiningProperties.LiningThickness offset into
the inner side of the rectangle.
* IfcWindowLiningProperties.LiningOffset distance along
the positive y direction to where the LiningDepth
applies.
* IfcWindowLiningProperties.FirstTransomOffset starting
at the bottom edge of the rectangle (along local x axis) into the
inner side of the rectangle, distance provided as percentage of
overall height. Distance to the centre line of the transom.
SecondTransomOffset defined accordingly.
* IfcWindowLiningProperties.FirstMullionOffset starting
at the left edge of the rectangle (along local z-axis) into the
inner side of the rectangle, distance provided as percentage of
overall width. Distance to the centre line of the mullion.
SecondMullionOffset defined accordingly.


![standard window](../../../../figuresifcwindowstandardcase-01.png)
Figure 299 — Window profile



