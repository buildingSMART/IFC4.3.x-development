# IfcShapeRepresentation

The _IfcShapeRepresentation_ represents the concept of a particular geometric representation of a product or a product component within a specific geometric representation context. The inherited attribute _RepresentationType_ is used to define the geometric model used for the shape representation (e.g. 'SweptSolid', or 'Brep'), the inherited attribute _RepresentationIdentifier_ is used to denote the kind of the representation captured by the _IfcShapeRepresentation_ (e.g. 'Axis', 'Body', etc.).

Several representation identifiers for shape representation are included as predefined values for _RepresentationIdentifier_. Table 1 indicates the defined list of values for _RepresentationIdentifier_.

<table>
<tr>
<td>
<table class="gridtable">
<tr>
<th>Identifier</th>
<th>&nbsp;</th>
</tr>
<tr>
<td align="left" valign="top" width="210"><b>CoG</b></td>
<td align="left" valign="top">Point to identify the center of gravity of an element. This value can be used for validation purposes.</td>
</tr>
<tr>
<td align="left" valign="top" width="210"><b>Box</b></td>
<td align="left" valign="top">Bounding box as simplified 3D box geometry of an element</td>
</tr>
<tr>
<td align="left" valign="top" width="210"><b>Annotation</b></td>
<td align="left" valign="top">3D annotations not representing elements</td>
</tr>
<tr>
<td align="left" valign="top" width="210"><b>Axis</b></td>
<td align="left" valign="top">2D or 3D Axis, or single line, representation of an element</td>
</tr>
<tr>
<td align="left" valign="top" width="210"><b>FootPrint</b></td>
<td align="left" valign="top">2D Foot print, or double line, representation of an element, projected to ground view</td>
</tr>
<tr>
<td align="left" valign="top" width="210"><b>Profile</b></td>
<td align="left" valign="top">3D line representation of a profile being planar, e.g. used for door and window outlines</td>
</tr>
<tr>
<td align="left" valign="top" width="210"><b>Surface</b></td>
<td align="left" valign="top">3D Surface representation, e.g. of an analytical surface, of an elementplane)</td>
</tr>
<tr>
<td align="left" valign="top" width="210"><b>Reference</b></td>
<td align="left" valign="top">3D representation that is not part of the Body representation. This is used, e.g., for opening geometries, if there are to be excluded from an implicit Boolean operation.</td>
</tr>
<tr>
<td align="left" valign="top" width="210"><b>Body</b></td>
<td align="left" valign="top">3D Body representation, e.g. as wireframe, surface, or solid model, of an element</td>
</tr>
<tr>
<td align="left" valign="top" width="210"><b>Body-FallBack</b></td>
<td align="left" valign="top">3D Body representation, e.g. as tessellation, or other surface, or boundary representation, added in addition to the solid model (potentially involving Boolean operations) of an element</td>
</tr>
<tr>
<td align="left" valign="top" width="210"><b>Clearance</b></td>
<td align="left" valign="top">3D clearance volume of the element. Such clearance region indicates space that should not intersect with the 'Body' representation of other elements, though may intersect with the 'Clearance' representation of other elements.</td>
</tr>
<tr>
<td align="left" valign="top" width="210"><b>Lighting</b></td>
<td align="left" valign="top">Representation of emitting light as a light source within a shape representation</td>
</tr>
</table>
</td>
</tr>
<tr>
<td>
<p class="table">Table 1 &mdash; Representation identifiers</p>
</td>
</tr>
</table>

Several representation types for shape representation are included as predefined values for _RepresentationType_. Table 2 indicates the defined list of values for _RepresentationType_.

<table>
<tr>
<td>
<table class="gridtable">
<tr>
<th colspan="2">Type</th>
<th>&nbsp;</th>
</tr>
<tr>
<td colspan="2" align="left" valign="top" width="20"><b>Point</b></td>
<td align="left" valign="top">2 or 3 dimensional point(s)</td>
</tr>
<tr>
<td colspan="2" align="left" valign="top" width="20"><b>PointCloud</b></td>
<td align="left" valign="top">3 dimensional points prepresented by a point list</td>
</tr>
<tr>
<td colspan="2" align="left" valign="top" width="20"><b>Curve</b></td>
<td align="left" valign="top">2 or 3 dimensional curve(s)</td>
</tr>
<tr>
<td colspan="2" align="left" valign="top" width="20"><b>Curve2D</b></td>
<td align="left" valign="top">2 dimensional curve(s)</td>
</tr>
<tr>
<td colspan="2" align="left" valign="top" width="20"><b>Curve3D</b></td>
<td align="left" valign="top">3 dimensional curve(s)</td>
</tr>
<tr>
<td colspan="2" align="left" valign="top" width="20"><b>Surface</b></td>
<td align="left" valign="top">2 or 3 dimensional surface(s)</td>
</tr>
<tr>
<td colspan="2" align="left" valign="top" width="20"><b>Surface2D</b></td>
<td align="left" valign="top">2 dimensional surface(s) (a region on ground view)</td>
</tr>
<tr>
<td colspan="2" align="left" valign="top" width="20"><b>Surface3D</b></td>
<td align="left" valign="top">3 dimensional surface(s)</td>
</tr>
<tr>
<td colspan="2" align="left" valign="top" width="20"><b>FillArea</b></td>
<td align="left" valign="top">2D region(s) represented as a filled area (hatching)</td>
</tr>
<tr>
<td colspan="2" align="left" valign="top" width="20"><b>Text</b></td>
<td align="left" valign="top">text defined as text literals</td>
</tr>
<tr>
<td colspan="2" align="left" valign="top" width="20">
<b>AdvancedSurface</b></td>
<td>3 dimensional b-spline surface(s)</td>
</tr>
<tr>
<td colspan="2" align="left" valign="top" width="20"><b>GeometricSet</b></td>
<td align="left" valign="top">points, curves, surfaces (2 or 3
dimensional)</td>
</tr>
<tr>
<td align="left" valign="top" width="20"></td>
<td align="left" valign="top" width="180"><b>GeometricCurveSet</b></td>
<td align="left" valign="top">points, curves (2 or 3 dimensional)</td>
</tr>
<tr>
<td align="left" valign="top" width="20"></td>
<td align="left" valign="top" width="180"><b>Annotation2D</b></td>
<td>points, curves (2 or 3 dimensional), hatches and text (2 dimensional)</td>
</tr>
<tr>
<td colspan="2" align="left" valign="top" width="20"><b>SurfaceModel</b></td>
<td align="left" valign="top">face based and shell based surface model(s), or tessellated surface model(s)</td>
</tr>
<tr>
<td align="left" valign="top" width="20"></td>
<td align="left" valign="top" width="180"><b>Tessellation</b></td>
<td align="left" valign="top">tessellated surface representation(s) only</td>
</tr>
<tr>
<td colspan="2" align="left" valign="top" width="20"><b>SolidModel</b></td>
<td align="left" valign="top">including swept solid, Boolean results and Brep bodies; more specific types are:</td>
</tr>
<tr>
<td align="left" valign="top" width="20"></td>
<td align="left" valign="top" width="180"><b>SweptSolid</b></td>
<td align="left" valign="top">swept area solids, by extrusion and revolution, excluding tapered sweeps</td>
</tr>
<tr>
<td align="left" valign="top" width="20"></td>
<td align="left" valign="top" width="180"><b>AdvancedSweptSolid</b></td>
<td align="left" valign="top">swept area solids created by sweeping a profile along a directrix, and tapered sweeps</td>
</tr>
<tr>
<td align="left" valign="top" width="20"></td>
<td align="left" valign="top" width="180"><b>Brep</b></td>
<td align="left" valign="top">faceted Brep's with and without voids</td>
</tr>
<tr>
<td align="left" valign="top" width="20"></td>
<td align="left" valign="top" width="180"><b>AdvancedBrep</b></td>
<td align="left" valign="top">Brep's based on advanced faces, with b-spline surface geometry, with and without voids</td>
</tr>
<tr>
<td align="left" valign="top" width="20"></td>
<td align="left" valign="top" width="180"><b>CSG</b></td>
<td align="left" valign="top">Boolean results of operations between solid models, half spaces and Boolean results</td>
</tr>
<tr>
<td align="left" valign="top" width="20"></td>
<td align="left" valign="top" width="180"><b>Clipping</b></td>
<td align="left" valign="top">Boolean differences between swept area solids, half spaces and Boolean results</td>
</tr>
<tr>
<td colspan="2" align="left" valign="top" width="20"><em><br>
additional types</em></td>
<td align="left" valign="top"><br>
some additional representation types are provided:</td>
</tr>
<tr>
<td align="left" valign="top" width="20"></td>
<td align="left" valign="top" width="180"><b>BoundingBox</b></td>
<td align="left" valign="top">simplistic 3D representation by a bounding box</td>
</tr>
<tr>
<td align="left" valign="top" width="20"></td>
<td align="left" valign="top" width="180"><b>SectionedSpine</b></td>
<td align="left" valign="top">cross section based representation of a spine curve and planar cross sections. It can represent a surface or a solid and the interpolations of the between the cross sections is not defined</td>
</tr>
<tr>
<td align="left" valign="top" width="20"></td>
<td align="left" valign="top" width="180"><b>LightSource</b></td>
<td align="left" valign="top">light source with (depending on type) position, orientation, light colour, intensity and attenuation</td>
</tr>
<tr>
<td align="left" valign="top" width="20"></td>
<td align="left" valign="top" width="180"><b>MappedRepresentation</b></td>
<td align="left" valign="top">representation based on mapped item(s), referring to a representation map. Note: it can be seen as an inserted block reference. The shape representation of the mapped item has a representation type declaring the type of its representation items.</td>
</tr>
</table>
</td>
</tr>
<tr>
<td>
<p class="table">Table 2 &mdash; Representation types</p>
</td>
</tr>
</table>

{ .extDef}
> NOTE&nbsp; The definition relates to **shape_representation** defined in ISO 10303-41.

> HISTORY&nbsp; New entity in IFC1.5.

{ .change-ifc2x4}
> IFC4 CHANGE&nbsp; The _RepresentationType_'s 'Point', 'PointCloud', 'Curve', 'Curve3D', 'Surface', 'Surface2D', 'Surface3D', 'FillArea', 'Text', 'Tessellation', 'AdvancedBrep', 'LightSource', and the _RepresentationIdentifier_ 'Body-FallBack', 'Profile', 'Clearance', 'Lighting' have been added.

## Formal Propositions

### CorrectContext
The context to which the IfcShapeRepresentation is assign, shall be of type IfcGeometricRepresentationContext.

### NoTopologicalItem
No topological representation item shall be directly used for shape representations, with the exception of IfcVertexPoint, IfcEdgeCurve, IfcFaceSurface.

### HasRepresentationType
A representation type should be provided for the shape representation.

### HasRepresentationIdentifier
A representation identifier should be provided for the shape representation.

### CorrectItemsForType
Checks the proper use of _Items_ according to the _RepresentationType_.
