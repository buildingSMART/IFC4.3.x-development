IfcGeometricModelResource
=========================

The schema _IfcGeometricModelResource_ defines the resources used for geometric model representations. The primary application of this resource is for representation of the shape or geometric form of a product model.

The following is within the scope of the geometric model representation in the current version of the geometric model resource:

* data describing the precise geometric form of three-dimensional solid objects;
* constructive solid geometry (CSG) models;
* definition of half-spaces;
* creation of solid models by sweeping operations;
* manifold boundary representation (brep) models;
* surface models;
* tessellated models;
* geometric sets.



> NOTE  Many definitions of this schema are adapted from definitions defined within [ISO 10303-42](../content/bibliography.htm#iso-10303-42). The _IfcGeometricModelResource_ refers to the clause 6, "Geometric Model" of [ISO 10303-42](../content/bibliography.htm#iso-10303-42). The definitions of geometric and topological representation, when quoted from [ISO 10303-42](../content/bibliography.htm#iso-10303-42), are explicitly excluded from the copyright of this specification.

> REFERENCE  Definition according to ISO 10303-42

The constructive solid geometry models are represented by their component primitives and the sequence of Boolean operations (union, intersection, or difference) used in their construction. The entity which communicates the logical sequence of Boolean operations is the boolean result (_IfcBooleanResult_) which identifies an operator and two operands. Since the operands can themselves be Boolean results thus enabling nested operations. Swept solids and half-space solids are permissible Boolean operands. The swept solids are the solid of revolution and the solid of linear extrusion. The swept solids are obtained by extruding or sweeping a planar face which may contain holes. The half space solid is essentially defined as a semi-infinite solid on one side of a surface; it may be limited by a box domain.

> REFERENCE  Definition according to ISO 10303-42

Brep models are represented by the set of shells defining the exterior or interior boundaries. The faceted brep is restricted to represent breps in which all faces are planar and every loop is a poly loop. For such a solid this entity provides a more efficient form of representation. The shell based surface model, the face based surface model and the geometric set entities do not enforce the integrity checks of the manifold solid brep and can be used for the communication of incomplete models (including two-dimensional models).
