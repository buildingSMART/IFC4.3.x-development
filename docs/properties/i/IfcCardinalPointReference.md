IfcCardinalPointReference
=========================

An _IfcCardinalPointReference_ is an index reference to significant points of a section profile. This index is used to describe the spatial relationship between the section of a member and a reference axis of the same member.

> HISTORY  New Type in IFC4.

Indexes 1...9 refer to points at the bounding box of a profile. Indexes 10...19 refer to points defined by geometric centroid (usually centre of gravity) and shear centre, and their combinations with bounding box coordinates. In particular, the following index values are specified in this specification:

1. bottom left
2. bottom centre
3. bottom right
4. mid-depth left
5. mid-depth centre
6. mid-depth right
7. top left
8. top centre
9. top right
10. geometric centroid
11. bottom in line with the geometric centroid
12. left in line with the geometric centroid
13. right in line with the geometric centroid
14. top in line with the geometric centroid
15. shear centre
16. bottom in line with the shear centre
17. left in line with the shear centre
18. right in line with the shear centre
19. top in line with the shear centre
20. Lowest point inside of pipe or channel profile (centre of flat bottom)

Other index values are possible but outside the scope of this specification.

Figure 1 illustrates cardinal point values.

!["arbitrary profile with cardinal points"](../../../../../../figures/ifccardinalpointreference-01.png "Figure 1 &mdash; Cardinal point values")

Figure 2 illustrates an example extrusion shape with arbitrary profile (_IfcArbitraryClosedProfileDef_), aligned "mid-depth right" on the member axis. The line of sight follows the extrusion direction Z which points into the drawing plane of above illustration. Hence, "left" is in the positive X direction of the _IfcProfileDef_. "Top" is in the positive Y direction of the _IfcProfileDef_.

!["extrusion shape with arbitrary profile and alignment"](../../../../../../figures/ifccardinalpointreference-02.png "Figure 2 &mdash; Cardinal point extrusion")
