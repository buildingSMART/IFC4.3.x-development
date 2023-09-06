Alignment Layouts
============================================

A single alignment may be described by one ore more of the following layouts:

* a horizontal layout (_IfcAlignmentHorizontal_), defined in the x/y plane of the engineering coordinate system.
* an accompanying vertical layout (_IfcAlignmentVertical_), defined along the horizontal layout in the distance along / z coordinate space.
* an accompanying cant layout (_IfcAlignmentCant_), defined as lateral inclination along the horizontal layout.

These 3 layouts may be used in different configurations. See **Alignment Layout - Horizontal, Vertical and Cant** and **Alignment Layout - Reusing Horizontal Layout** for details.

```
concept {
    IfcAlignment:IsNestedBy -> IfcRelNests_0:RelatingObject
    IfcRelNests_0:RelatedObjects -> IfcAlignmentHorizontal
    IfcRelNests_0:RelatedObjects -> IfcAlignmentVertical
    IfcRelNests_0:RelatedObjects -> IfcAlignmentCant
}
```