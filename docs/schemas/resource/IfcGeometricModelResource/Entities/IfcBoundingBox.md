# IfcBoundingBox

The _IfcBoundingBox_ defines an orthogonal box oriented parallel to the axes of the object coordinate system in which it is defined. It is defined by a _Corner_ being a three-dimensional Cartesian point and three length measures defining the X, Y and Z parameters of the box in the direction of the positive axes.
<!-- end of short definition -->

> NOTE Any subtype of _IfcProduct_ having a product shape representation may have a bounding box representation. The 'Box' representation identifier defined at IfcShapeRepresentation utilizes the _IfcBoundingBox_ as the simplest 3D shape representation.

![bounding box](../../../../figures/ifcboundingbox-layout1.gif)

Figure 1 — Bounding box

As shown in Figure 1, the <em>IfcBoundingBox</em> is defined with its own location which can be used to place the <em>IfcBoundingBox</em> relative to the geometric coordinate system. The <em>IfcBoundingBox</em> is defined by the lower left corner (<em>Corner</em>) and the upper right corner (<em>XDim, YDim, ZDim</em> measured within the parent coordinate system).

> NOTE Corresponding STEP type **box_domain** defined in ISO 10303-42.

> HISTORY New entity in IFC1.0.

## Attributes

### Corner
Location of the bottom left corner (having the minimum values).

### XDim
Length attribute (measured along the edge parallel to the X Axis)

### YDim
Width attribute (measured along the edge parallel to the Y Axis)

### ZDim
Height attribute (measured along the edge parallel to the Z Axis).

### Dim
The space dimensionality of this class, it is always 3.
