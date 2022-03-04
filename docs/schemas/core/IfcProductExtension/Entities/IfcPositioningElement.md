# IfcPositioningElement

New and abstract entity definition for positioning and annotating elements that are used to position other elements relatively.

> EXAMPLE  A grid is a positioning element to position building components mainly in vertical structures, an alignment is a linear positioning element to position geographic and civil elements mainly in infrastructure works.

> EXAMPLE  An alignment is a linear positioning element for using a linear referencing method to position other items. See ISO 19148 “Linear referencing” for general information about linear referencing methods and expressions.

## Attributes

### ContainedInStructure
Relationship to a spatial structure element, to which the positioning element is primarily associated.
{ .change-ifc2x}
> IFC2x CHANGE  The inverse relationship has been added to _IfcGrid_ with upward compatibility

{ .change-ifc4}
> IFC4 CHANGE  The inverse relationship has been promoted from _IfcGrid_ to this new supertype with upward compatibility

### Positions


## Formal Propositions

### HasPlacement
The placement for the grid has to be given.

## Concepts

### FootPrint Geometry

The 2D geometric representation of IfcGrid is defined using the 'GeometricCurveSet' geometry. The following attribute values should be inserted

*  _IfcShapeRepresentation.RepresentationIdentifier_ = 'FootPrint'.
*  _IfcShapeRepresentation.RepresentationType_ = 'GeometricCurveSet' .

The following constraints apply to the 2D representation:

* The IfcGeometricCurveSet shall be an (and the only) Item of the IfcShapeRepresentation. It should contain an IfcGeometricCurveSet containing subtypes of IfcCurve, each representing a grid axis. Applicable subtypes of IfcCurve are: IfcPolyline, IfcCircle, IfcTrimmedCurve (based on BaseCurve referencing IfcLine or IfcCircle), and IfcOffsetCurve2D.
* Each subtype of IfcCurve may have a curve style assigned, using IfcStyledItem referencing IfcCurveStyle.
* Optionally the grid axis labels may be added as IfcTextLiteral, and they may have text styles assigned, using IfcStyledItem referencing IfcTextStyle.


![design grid](../../../../figures/ifcdesigngrid-layout1.gif)

Figure 31 &mdash; Grid layout

As shown in Figure 31, the <em>IfcGrid</em> defines a placement coordinate system using the <em>ObjectPlacement</em>. The XY plane of the coordinate system is used to place the 2D grid axes.  The <em>Representation</em> of <em>IfcGrid</em> is defined using <em>IfcProductRepresentation</em>, referencing an <em>IfcShapeRepresentation</em>, that includes <em>IfcGeometricCurveSet</em> as <em>Items</em>. All grid axes are added as <em>IfcPolyline</em> to the <em>IfcGeometricCurveSet</em>.

![representation of a design grid](../../../../figures/ifcgrid-representation.png)

Figure 32 &mdash; Grid representation

As shown in Figure 32, the attributes <em>UAxes</em> and <em>VAxes</em> define lists of <em>IfcGridAxis</em> within the context of the grid. Each instance of <em>IfcGridAxis</em> refers to the same instance of <em>IfcCurve</em> (here the subtype <em>IfcPolyline</em>) that is contained within the <em>IfcGeometricCurveSet</em> that represents the <em>IfcGrid</em>.

### Product Local Placement

The local placement for IfcGrid is defined in its supertype IfcProduct. It is defined by the IfcLocalPlacement, which defines the local coordinate system that is referenced by all geometric representations.

* The PlacementRelTo relationship of IfcLocalPlacement shall point (if given) to the local placement of the same IfcSpatialStructureElement, which is used in the ContainedInStructure inverse attribute, or to a spatial structure element at a higher level, referenced by that.
* If the relative placement is not used, the absolute placement is defined within the world coordinate system.

