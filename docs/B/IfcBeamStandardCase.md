IfcBeamStandardCase
===================
The standard beam, _IfcBeamStandardCase_, defines a beam with certain
constraints for the provision of material usage, parameters and with certain
constraints for the geometric representation. The _IfcBeamStandardCase_
handles all cases of beams, that:  
  
* have a reference to the _IfcMaterialProfileSetUsage_ defining the material profile association of the beam with the cardinal point of its insertion relative to the local placement.  
* are consistent in using the correct cardinal point offset of the profile as compared to the ''Axis'' and ''Body'' shape representation  
* are based on a sweep of a planar profile, or set of profiles, as defined by the _IfcMaterialProfileSet_  
* have an ''Axis'' shape representation with constraints provided below in the geometry use definition  
* have a ''Body'' shape representation with constraints provided below in the geometry use definition   
* are extruded perpendicular to the profile definition plane  
* have a start profile, or set of profiles, that is swept  
* the sweeping operation can be linear extrusion, circular rotation, or a sweep along a directrix  
* the start profile, or set of profiles can be swept unchanged, or might be changed uniformly by a taper definition   
*   
>> NOTE  View definitions and implementer agreements may further constrain the
applicable geometry types, e.g. by excluding tapering from an
_IfcBeamStandardCase_ implementation.  
  
> HISTORY  New entity in IFC4.  
  
**_Geometric Representations_**  
  
The geometric representation of _IfcBeamStandardCase_ is defined using the
following multiple shape representations for its definition:  
  
* **Axis**: A three dimensional open curve (subtype of _IfcBoundedCurve_) defining the axis for the standard beam. The cardinal point is determined by the beam axis.  
* **Body**: A Swept Solid Representation or a CSG clipping representation defining the 3D shape of the standard beam.  
  
> NOTE  It is invalid to exchange a ''SurfaceModel'', ''Brep'', or
> ''MappedRepresentation'' representation for the ''Body'' shape
> representation of an _IfcBeamStandardCase_.  
[ _bSI
Documentation_](https://standards.buildingsmart.org/IFC/DEV/IFC4_2/FINAL/HTML/schema/ifcsharedbldgelements/lexical/ifcbeamstandardcase.htm)


Formal Propositions
-------------------
| Rule                       | Description   |
|----------------------------|---------------|
| HasMaterialProfileSetUsage |               |

