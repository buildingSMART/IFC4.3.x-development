IfcElementComponent
===================
An element component is a representation for minor items included in, added to
or connecting to or between elements, which usually are not of interest from
the overall building structure viewpoint. However, these small parts may have
vital and load carrying functions within the construction. These items do not
provide any actual space boundaries. Typical examples of
[_IfcElementComponent_]($element://{5C7C3076-BCD7-4de1-8FFE-3EA6C177A25F})s
include different kinds of fasteners and various accessories.  
One or several instances of subtypes of
[_IfcElementComponent_]($element://{5C7C3076-BCD7-4de1-8FFE-3EA6C177A25F})
should always be accompanied by a defining instance of a respective subtype of
[_IfcElementComponentType_]($element://{D6848B26-0C64-4a58-ADD7-AA2243A08FF1}).
The type object holds shape and material information.  
HISTORY New entity in IFC2x2  
It is often desirable to model a number of same-shaped element components by
means of a single occurrence object, e.g. several bolts within a connection or
a row of reinforcement elements. In this IFC release, this is possible by
means of multiple mapped representation as documented below.  
To express the multiplicity of element components also on a higher semantic
level, a Qto_ElementComponentPatternQuantities should be provided via
[_IfcRelDefinesByProperties_]($element://{2FF400DC-2070-4b81-85BE-03894DE067A9})
and contain the number of pieces which are placed by a single
[_IfcElementComponent_]($element://{5C7C3076-BCD7-4de1-8FFE-3EA6C177A25F})
instance.  
  
 **Symbolic Representation**  
A symbolic representation is defined for a row of components or several rows
of components within a single instance of
[_IfcElementComponent_]($element://{5C7C3076-BCD7-4de1-8FFE-3EA6C177A25F}).
Such rows or arrays may contain possibly large numbers of individual pieces.
The product definition shape consists of an _IfcShapeRepresentation_ with the
attribute values  

  

  * RepresentationIdentifier: ''Row''
  

  * RepresentationType: ''GeometricCurveSet''
  

  
and one or several curves as geometric items. The curves represent where
reference points of the pieces are located. For example, such reference points
may be at the heads of mechanical fasteners or at the starting point of the
extrusion axis of reinforcement bars. In case of straight components (bolts,
nails, staples, straight reinforcement bars, or similar), the local placement
of the
[_IfcElementComponent_]($element://{5C7C3076-BCD7-4de1-8FFE-3EA6C177A25F})
shall be located and oriented such that the local z axis is parallel with the
axes of the components. A Qto_ElementComponentPatternQuantities should denote
the count of pieces in the row or array and their spacing.  
[ _bSI
Documentation_](https://standards.buildingsmart.org/IFC/DEV/IFC4_2/FINAL/HTML/schema/ifcsharedcomponentelements/lexical/ifcelementcomponent.htm)


