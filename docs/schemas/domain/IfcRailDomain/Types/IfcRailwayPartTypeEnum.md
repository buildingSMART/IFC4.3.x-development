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

## Items

### TRACKSTRUCTURE


### TRACKSTRUCTUREPART
A track structure part refers to a segment of a track system. It usually has one of the following functions: plain-track, turnout-track, dilatation-track.

### LINESIDESTRUCTUREPART
A railway line side structure part is a longitudinal decomposition of railway lineside structure in more managable volume for engineering purposes.

### DILATATIONSUPERSTRUCTURE


### PLAINTRACKSUPESTRUCTURE
The plain-track superstructure is one specific type of the track structure. It does not contain any turnout panel or dilatation panel.

### LINESIDESTRUCTURE
A spatial structure element that contains the elements of the railway that are not in or over the tracks, hence line-side.

### SUPERSTRUCTURE
A spatial structure element that contains elements that are positioned over the tracks, such as catenaries.

### TURNOUTSUPERSTRUCTURE


### USERDEFINED


### NOTDEFINED

