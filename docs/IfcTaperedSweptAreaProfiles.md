IfcTaperedSweptAreaProfiles
===========================
This function checks whether the start and end profile in a tapered extrusion
are topologically similar, i.e. whether both have the same number of vertices
and edges.  
  
It returnes TRUE if:  
  
* The start profile is defined by a paramterized profile definition and   
* the end profile is either a derived profile, using the start profile as its parent profile, or  
* the end profile is besed on the same subtype of the paramterized profile definition as the start profile   
* The start profile is defined by an arbitrary bounded curve bounding a plane and   
* the end profile is a derived profile using the start profile as its parent profile   
  
> HISTORY\S\ New function in  
IFC2x Edition 4.  


