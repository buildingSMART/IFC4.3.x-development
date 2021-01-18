IfcStructuralAnalysisDomain
===========================

The _IfcStructuralAnalysisDomain_ describes the structural analysis model in order to tightly integrate the structural engineering domain. It reuses the existing building element and spatial structure element definition and associates the structural assumptions to it. The focus is to ensure that structural engineering information is captured and made visible to other related domains.

The following features are in scope:

* Defining planar and/or spatial structural analysis models which can be used by structural analysis applications.
* Included are, basically: 
    *  Straight or curved structural curve elements, planar or curved structural surface elements.
    *  Point, curve, and surface connections and supports.
    *  Specification of loadings including point, curve, surface loads, temperature loads, their assignment to load groups, load cases and load combinations.
    *  Specification of different structural analysis models in order to describe different aspects or parts of the building. Furthermore, dependencies between these models can be stored in the model for further use.
    *  Analysis results defined by forces and displacements.
Currently not in scope are:

* Dynamic analysis 
*  Description of prestressed loads 
*  Finite element topology 
*  Detailed results in finite element meshes as well as stresses and strains in the structural elements. 

> HISTORY&nbsp; New schema in IFC2x2.
