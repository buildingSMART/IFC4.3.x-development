# IfcStructuralSurfaceReaction

This entity defines a reaction which occurs distributed over a surface. A surface reaction may be connected with a surface member or surface connection.

> HISTORY&nbsp; New entity in IFC4.

****Coordinate Systems****:

See definitions at _IfcStructuralActivity_.

****Topology Use Definitions****:

See definitions at _IfcStructuralActivity_.

{ .spec-head}
Informal Propositions:

<ol>
  <li>If the surface reaction is of the predefined type CONST, <em>SELF\IfcStructuralActivity.AppliedLoad</em> must not be of type <em>IfcStructuralLoadConfiguration</em>.</li>
  <li>If the surface reaction is of the predefined type BILINEAR, <em>SELF\IfcStructuralActivity.AppliedLoad</em> shall be of type <em>IfcStructuralLoadConfiguration</em> and shall contain three items with two-dimensional <em>IfcStructuralLoadConfiguration.Locations</em>, defining the location of the result samples in local coordinates of the surface reaction.
  <li>If the surface reaction is of the predefined type DISCRETE, <em>SELF\IfcStructuralActivity.AppliedLoad</em> shall be of type <em>IfcStructuralLoadConfiguration</em> and shall contain two or more items with two-dimensional locations.
  <li>If the surface reaction is of the predefined type ISOCONTOUR, <em>SELF\IfcStructuralActivity.AppliedLoad</em> shall be of type <em>IfcStructuralLoadConfiguration</em> and shall contain the same number of items as the set <em>SELF.IfcProduct.Representation.Representations[?].Items</em>.  Each item in the load configuration shall have a two-dimensional location, defining the location of the result samples in local coordinates of the surface reaction.  Each item in <em>SELF\IfcStructuralActivity.AppliedLoad</em> shall be located at exactly one of the isocontours.
  <blockquote class="note">NOTE&nbsp;  The set of representation items is unordered, hence result locations are required to correlate result values and isocontours.</blockquote>
  <blockquote class="note">NOTE&nbsp;  Isocontours are represented as <em>IfcPCurve</em>s which are defined in terms of surface parameters u,v, while result locations are given in local surface item coordinates x,y.  It is strongly recommended that the surface parameterization u,v is scaled 1:1 in order to avoid different scales of u,v versus x,y.  If u,v are scaled 1:1 and the <em>IfcPCurve</em>'s base surface is identical with the surface item's base surface, u,v and local x,y are identical.</blockquote>
  </li>
  <li>All items in <em>SELF\IfcStructuralActivity.AppliedLoad\IfcStructuralLoadConfiguration.Values</em> shall be of the same entity type.</li>
</ol>

## Attributes

### PredefinedType
Type of reaction according to its distribution of load values.

## Formal Propositions

### HasPredefinedType
The attribute ObjectType shall be given if the predefined type is set to USERDEFINED.

## Concepts

### Structural Activity


