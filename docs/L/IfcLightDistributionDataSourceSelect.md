IfcLightDistributionDataSourceSelect
====================================
A goniometric light gets its intensity distribution function (how much light
goes in any one direction) from one of two sources: (i) an industry-standard
file, (ii) from distribution data passed directly via the
_IfcLightIntensityDistribution_.  
  
The light distribution provides the luminous intensity distribution according
to some standardized light distribution curves.  
  
SELECT  
  
  
\X\09\X\09  
\X\09\X\09 _Type_  
\X\09\X\09 | _Definition_  
\X\09\X\09  
---|---  
  
\X\09\X\09  
\X\09\X\09 _IfcExternalReference_  
\X\09\X\09 | Light distribution is represented by a standard photometric data
file such as Eulumdat, IES, CIBSE TM14.  
\X\09\X\09  
  
\X\09\X\09  
\X\09\X\09 _IfcLightIntensityDistribution_  
\X\09\X\09 | For representing a light distribution directly the  
\X\09\X\09\X\09 following values needs to be given in a table like structure
with column and  
\X\09\X\09\X\09 row headings. These headings should contain the angles (C/γ or
B/β )  
\X\09\X\09\X\09 and the table body contains the intensity values, (normally
normalized to  
\X\09\X\09\X\09 cd/Klm). The angles can be non- equidistant and the angle
steps can be almost  
\X\09\X\09\X\09 any value in the valid range, so a list of all available
angles in both  
\X\09\X\09\X\09 directions covers all cases.  
\X\09\X\09  
  
\X\09  
  
> HISTORY  New type in IFC2x2.  


