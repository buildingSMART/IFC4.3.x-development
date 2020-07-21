IfcAdvancedBrep
===============
An advanced B-rep is a boundary representation model in which all faces, edges
and vertices are explicitly represented. It is a solid with explicit topology
and elementary or free-form geometry. The faces of the B-rep are of type
_IfcAdvancedFace_. An advanced B-rep has to meet the same topological
constraints as the manifold solid B-rep.  
  
> NOTE  The advanced B-rep has been introduced in order to support the
> increasing number of applications that can define and exchange B-rep models
> based on NURBS or other b-spline surfaces.  
  
  
  
![advanced brep b-spline surface](../figures/ifcadvancedbrep_01.png)  
|  

Figure 1 illustrates use of _IfcAdvancedBrep_ for boundary representation
models with b-spline surfaces. The diagram shows the topological and geometric
representation items that are used for advanced B-reps, based on
_IfcAdvancedFace_.

  
  
  
---|---  
  
  
  

Figure 1 -- Advanced Brep, b-spline surface

  



  
  
|  
  
  
  
   ![advanced brep elementary surface](../figures/ifcadvancedbrep_02.png)  
|  

Figure 2 illustrates use of _IfcAdvancedBrep_ for boundary representation
models with elementary surfaces. The diagram shows the topological and
geometric representation items that are used for advanced B-reps, based on
_IfcAdvancedFace_. It shows the use of _IfcIntersectionCurve_ to provide the
geometric representation of the edge curve both as 3D curve and as u,v pcurve
in the parametric space of the adjacent surfaces.

  
  
  
  
  
  

Figure 2 -- Advanced Brep, elementary surface

  
  
|  
  
  
  
  
> NOTE  Entity adapted from **advanced_brep_shape_representation** defined in
> ISO 10303-514.  
  
> HISTORY  New entity in IFC4  
  
{ .spec-head}  
Informal Propositions:  
  
1\. each face is a face surface;  
2\. each face surface has its geometry defined by an elementary surface, swept
surface or a b-spline surface;  
3\. the edges used to define the boundaries of the face shall all reference an
edge curve  
4\. each curve used to define the geometry of the faces and face bounds shall
be either a conic, or a line or a polyline or a b-spline curve  
5\. the edges used to define the face boundaries shall all be trimmed by
vertices of type vertex point  
6\. no loop used to define a face bound shall be of the oriented subtype  
[ _bSI
Documentation_](https://standards.buildingsmart.org/IFC/DEV/IFC4_2/FINAL/HTML/schema/ifcgeometricmodelresource/lexical/ifcadvancedbrep.htm)


Formal Propositions
-------------------
| Rule             | Description   |
|------------------|---------------|
| HasAdvancedFaces |               |

