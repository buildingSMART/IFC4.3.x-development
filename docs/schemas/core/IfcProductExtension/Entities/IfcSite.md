# IfcSite

A site is a defined area of land, possibly covered with water, on which the project construction is to be completed. A site may be used to erect, retrofit or turn down building(s), or for other construction related developments.

> NOTE&nbsp; Term according to ISO6707-1 vocabulary "area of land or water where construction work or other development is undertaken".

A site may include a definition of the single geographic reference point for this site (global position using WGS84 with _Longitude_, _Latitude_ and _Elevation_). The precision is provided up to millionth of a second and it provides an absolute placement in relation to the real world as used in exchange with geospational information systems. If asserted, the _Longitude_, _Latitude_ and _Elevation_ establish the point in WGS84 where the point 0.,0.,0. of the _LocalPlacement_ of _IfcSite_ is situated.

The geometrical placement of the site, defined by the _IfcLocalPlacement_, shall be always relative to the spatial structure element, in which this site is included, or absolute, i.e. to the world coordinate system, as established by the geometric representation context of the project. The world coordinate system, established at the _IfcProject.RepresentationContexts_, may include a definition of the true north within the XY plane of the world coordinate system, if provided, it can be obtained at _IfcGeometricRepresentationContext.TrueNorth_.

A project may span over several connected or disconnected sites. Therefore site complex provides for a collection of sites included in a project. A site can also be decomposed in parts, where each part defines a site section. This is defined by the composition type attribute of the supertype _IfcSpatialStructureElements_ which is interpreted as follow:

* COMPLEX = site complex
* ELEMENT = site
* PARTIAL = site section

The _IfcSite_ is used to build the spatial structure of a building (that serves as the primary project breakdown and is required to be hierarchical).

Figure 1 shows the _IfcSite_ as part of the spatial structure. In addition to the logical spatial structure, also the placement hierarchy is shown. In this example the spatial structure hierarchy and the placement hierarchy are identical.

> NOTE&nbsp; Detailed requirements on mandatory element containment and placement structure relationships are given in view definitions and implementer agreements.

!["IfcSite as part of a spatial structure"](../../../../figures/ifcsite-spatialstructure.png "Figure 1 &mdash; Site composition")

Figure 2 describes the heights and elevations of the _IfcSite_. It is used to provide the geographic longitude, latitude, and height above sea level for the origin of the site. The origin of the site is the local placement.

The provision of longitude, latitude, height at the _IfcSite_ for georeferencing is provided for upward compatibility reasons. It requires a single instance of _IfcSite_ and WGS84 as coordinate reference system.

For exact georeferencing (or referencing to any other geographic coordinate system other than WSG84) the entities _IfcCoordinateReferenceSystem_ and _IfcMapConversion_ have to be used to define an exact mapping of the project engineering coordinate system to the geographic (or map) coordinate system.

* <small>reference height of site is provided by: <em>IfcSite.RefElevation</em>, it is given according to the height datum used at this location.</small>
* <small>the reference height of each building situated at the site is given againt the same height datum used at this location.</small>
* <small>the elevations of each storey belonging to each building are given as local height relative to the reference height of the building.</small>

<table border="0" cellpadding="2" cellspacing="2" summary="attribute use">
<tbody>
<tr valign="top">
<td align="left" valign="top"><img src="../../../../figures/ifcsite_heights.png" alt="building heights" border="0" height="400" width="500">&nbsp;</td>
</tr>
<tr>
<td>
<p class="figure">Figure 2 &mdash; Site elevations</p>
</td>
</tr>
</tbody>
</table>

> HISTORY &nbsp;New entity in IFC1.0.

## Attributes

### RefLatitude
World Latitude at reference point (most likely defined in legal description). Defined as integer values for degrees, minutes, seconds, and, optionally, millionths of seconds with respect to the world geodetic system WGS84.
> NOTE&nbsp; Latitudes are measured relative to the geodetic equator, north of the equator by positive values - from 0 till +90, south of the equator by negative values - from 0 till -90.

### RefLongitude
World Longitude at reference point (most likely defined in legal description). Defined as integer values for degrees, minutes, seconds, and, optionally, millionths of seconds with respect to the world geodetic system WGS84.
> NOTE&nbsp; Longitudes are measured relative to the geodetic zero meridian, nominally the same as the Greenwich prime meridian: longitudes west of the zero meridian have negative values - from 0 till -180, longitudes east of the zero meridian have positive values - from 0 till -180.

> EXAMPLE&nbsp; Chicago Harbor Light has according to WGS84 a longitude -87.35.40 (or 87.35.40W) and a latitude 41.53.30 (or 41.53.30N).

### RefElevation
Datum elevation relative to sea level.

### LandTitleNumber
The land title number (designation of the site within a regional system).

### SiteAddress
Address given to the site for postal purposes.
