# IfcRailwayPartTypeEnum

The _IfcRailwayPartTypeEnum_ defines the range of different types of railway part that can be specified.

The spatial structure of a railway is sub-divided into several elements for lateral, vertical and longitudinal decomposition:

* TRACKSTRUCTURE is for the track part of the railway (vertical decomposition).
* SUPERSTRUCTURE is for the upper part of the railway (vertical decomposition).
* LINESIDESTRUCTURE is for the lateral part of the railway (lateral decomposition).

!["Railway vertical and lateral spatial decomposition "](../../../../figures/IfcRailwayPartTypeEnum-global.png "Figure 1 &mdash; Railway decomposition")
The subpart of the railway is generally either a _IfcFacilityPartCommonTypeEnum_ BELOWGROUND (non constructed ground) or SUBSTRUCTURE (constructed ground).

TRACKSTRUCTURE could have longitudinal decomposition based on track specificities:

* PLAINTRACKSUPESTRUCTURE for the plain line tracks (_IfcElementAssemblyTypeEnum_ TRACKPANEL).
* DILATATIONSUPERSTRUCTURE for the area of dilatation panels (_IfcElementAssemblyTypeEnum_ DILATATIONPANEL).
* TURNOUTSUPERSTRUCTURE for the area of turnouts (_IfcElementAssemblyTypeEnum_ TURNOUTPANEL).
* TRACKSTRUCTUREPART for generic longitudinal decomposition if needed.

!["Railway vertical and lateral spatial decomposition "](../../../../figures/IfcRailwayPartTypeEnum-track.png "Figure 2 &mdash; Track longitudinal decomposition")

More generic longitudinal subdivision is provided for LINESIDESTRUCTURE with LINESIDESTRUCTUREPART value if needed.
