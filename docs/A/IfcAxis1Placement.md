IfcAxis1Placement
=================
The _IfcAxis1Placement_ provides location and direction of a single axis.  
  
  
  
![axis1 placement](../figures/ifcaxis1placement-layout1.gif)  
  
|

>  
>  Figure 1 illustrates the definition of the _IfcAxis1Placement_ within the
> parent three-dimensional coordinate system.  
>

  
  
  
---|---  
  
  

Figure 1 -- Axis1 placement

  
  
  
  
  
  
{ .extDef}  
> NOTE  Definition according to ISO/CD 10303-42:1992  
> The direction and location in three dimensional space of a single axis. An
> axis1_placement is defined in terms of a locating point (inherited from
> placement supertype) and an axis direction: this is either the direction of
> axis or defaults to (0.0,0.0,1.0). The actual direction for the axis
> placement is given by the derived attribute z.  
  
> NOTE  Entity adapted from **axis1_placement** defined in ISO10303-42.  
  
> HISTORY  New entity in IFC1.5  
[ _bSI
Documentation_](https://standards.buildingsmart.org/IFC/DEV/IFC4_2/FINAL/HTML/schema/ifcgeometryresource/lexical/ifcaxis1placement.htm)


Attribute definitions
---------------------
| Attribute   | Description                                                                                                                      |
|-------------|----------------------------------------------------------------------------------------------------------------------------------|
| Z           | The normalized direction of the local Z axis. It is either identical with the Axis value, if given, or it defaults to [0.,0.,1.] |

Formal Propositions
-------------------
| Rule         | Description   |
|--------------|---------------|
| AxisIs3D     |               |
| LocationIs3D |               |

Associations
------------
| Attribute   | Description   |
|-------------|---------------|
|             |               |
| Axis        |               |
|             |               |

