This enumeration defines the different ways how path based elements (such as layered _IfcWall_ elements) can connect, as shown in Figure 1.

<!-- end of short definition -->


> HISTORY New type in IFC2.0

The enumerated items shall be used in the following combinations:

Connection shape | RelatingConnectionType | RelatedConnectionType | Illustration
--- | --- | --- | ---
L-Shape | AtStart | AtStart | ![L-shape](../../../../figures/ifcconnectiontypeenum-fig03.gif)
L-Shape | AtEnd | AtStart | ![L-shape](../../../../figures/ifcconnectiontypeenum-fig01.gif)
T-Shape | AtPath | AtStart | ![T-shape](../../../../figures/ifcconnectiontypeenum-fig02.gif)

Table 1 — Connection types

## Items

### ATPATH
Connection along the path of the connected element.

### ATSTART
Connection at the start of the connected element.

### ATEND
Connection at the end of the connected element.

### NOTDEFINED

