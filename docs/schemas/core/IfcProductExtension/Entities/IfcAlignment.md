# IfcAlignment

For the purposes of IFC the English term "alignment" defines three essentially separate but closely interconnected concepts.

1. defintion of a reference system for linear positioning
2. safeguarding and optimization of the movement of vehicles - kinematic perspective
3. geometric construction of roads, railway tracks or other linear infrastructure

**Reference system for linear positioning**

An alignment is used to define a reference system to position elements mainly for linear construction works, such as roads, rails, bridges, and others. The relative positioning along the alignment is defined by the linear referencing methodology.

> NOTE  See ISO 19148 Geographic information &ndash; Linear referencing for general definitions about linear referencing.

**Kinematic perspective**

In the kinematic perspective focus is on the safe and optimized movement of a vehicle under the constraints induced by changes in the direction of the horizontal and the vertical layout.

**Geometric perspective**

In the geometric perspective the focus is on the proper placement of horizontal and vertical segments to connect certain points along a proposed path. A huge body of knowledge has been developed over a long period of time, in many aspects predating the availability of modern computers and their software.



**State of the art in contemporary engineering**

1. Contemporary engineering usually establishes first a horizontal layout in a properly projected plane.

2. In a second step the vertical profile (i.e. sequence of segments with constant gradients  together with smoothing segments showing a variation in gradient) is added.

3. In the rail domain in most cases a cant layout is added to the horizontal layout to compensate a part of the unwanted lateral acceleration.

4. In a final step the proposed layout is checked against a defined set of rules, formulas and thresholds to guarantee the conformance against the regulation.

The sequence of steps might change from case to case and might be repeated one or more times to achieve the economic objectives and fulfill regulatory safety requirements.


Contemporary alignment design almost always implements a 2.5 dimension approach.

The resulting and documented geometry might be very precise or just good enough to meet safety thresholds. This depends on factors like priorities of the management, date of the design - existing alignments might have been designed more then 50 years ago - or software tools used. Working with legacy data in a high precision BIM model requires a good understanding of these factors.

**Distinction between business modeling and IFC core geometry**

According to IFC modeling principles alignment entities are organised in two large parts. The two parts work together, but they can also be used independently from each other

1. Business aspects of alignment
2. Representation with the IFC geometry resources

**Business aspects of alignment:** Here the focus is a on a schema structure as close to business terminology as possible. It is possible to have a very detailed segment structure with many domain specific properties attached. Examples for domain specific properties are design speed or cant deficiency.

**Representation with IFC geometry resources:** Here the focus is on using as much of the established IFC geometry entities as possible. A mapping between Business aspects and IFC geometry is proposed.

**IFC modelling**

In IFC a single alignment must have:

* a horizontal alignment defined in the x/y plane of the engineering coordinate system

A single alignment may have:

* an accompanying vertical alignment, defined along the horizontal alignment in the distance along / z coordinate space
* a relative alignment, defined as a span within another alignment and/or at constant or variable offsets
* a 3D alignment, either computed from the horizontal and vertical alignment, or extracted from geospatial data.

Alignments may be aggregated into referents (_IfcReferent_) or derivative alignments. Derivative alignments may be used to indicate dependent alignments, such as an alignment for a bridge that is relative to a parent alignment for a road, where the child _IfcAlignment_ may have its shape representation set to _IfcOffsetCurveByDistances_ that starts and ends at a span within the extent of the shape representation of the parent _IfcAlignment_.

Alignments may be assigned to groups using _IfcRelAssignsToGroup_, where _IfcGroup_ or subtypes may capture information common to multiple alignments.

Supported shape representations of <span class="self-ref">IfcAlignment</span> are:

* _IfcGradientCurve_ as a 3D horizontal and vertical alignment (represented by their alignment segments)
* _IfcCompositeCurve_ as a 2D horizontal alignment (represented by its horizontal alignment segments) without a vertical alignment
* _IfcOffsetCurveByDistances_ as a 2D or 3D curve defined relative to an _IfcAlignmentCurve_ or another _IfcOffsetCurveByDistances_
* _IfcSegmentedReferenceCurve_ as a 3D curve defined relative to an _IfcGradientCurve_ to incorporate the application of cant
* _IfcPolyline_ or _IfcIndexedPolyCurve_ as a 3D alignment by a 3D polyline representation (such as coming from a survey)
* _IfcPolyline_ or _IfcIndexedPolyCurve_ as a 2D horizontal alignment by a 2D polyline representation (such as in very early planning phases or as a map representation)

The _RepresentationIdentifier_ shall always be set to 'Axis' and the _RepresentationType_ shall be set to either 'Curve2D' or 'Curve3D' depending on if the referenced curve is 2- or 3-dimensional

> NOTE  Derivative specifications (Model View Definitions) may expand the above set to include additional supported curve types.

## Attributes

### PredefinedType

## Concepts

### Alignment Geometry Cant



### Alignment Geometry Gradient



### Alignment Layout



### Object Nesting



