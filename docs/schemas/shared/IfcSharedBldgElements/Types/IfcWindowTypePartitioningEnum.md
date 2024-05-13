# IfcWindowTypePartitioningEnum

This enumeration defines the basic configuration of the window type in terms of the number of window panels and the subdivision of the total window. The window configurations are given for windows with one, two or three panels (including fixed panels).<!-- end of definition -->

Windows which are subdivided into more than three panels have to be defined by the geometry only. The type of such windows is USERDEFINED.

> HISTORY  New Enumeration in IFC4. The new _IfcWindowTypePartitioningEnum_ replaces the use of _IfcWindowStyleOperationEnum_ that is deprecated from IFC4 onwards.

Note:

1. The way how each panel operates is defined at the _IfcWindowPanelProperties.OperationType_.
2. The reference from the window panel to the location of that panel in the window style configuration is handled by the _IfcWindowPanelProperties.PanelPosition_.
3. The figures/ are shown as elevations in the XZ plane of the local placement of the window, looking into the direction of the positive Y axis.
4. These figures/ are only shown as illustrations

## Items

### SINGLE_PANEL
Window with one panel.

![](../../../../figures/ifcwindowtypepartitioningenum-fig01.gif)

### DOUBLE_PANEL_VERTICAL
Window with two panels. The configuration of the panels is vertically.

![](../../../../figures/ifcwindowtypepartitioningenum-fig02.gif)

### DOUBLE_PANEL_HORIZONTAL
Window with two panels. The configuration of the panels is horizontally.

![](../../../../figures/ifcwindowtypepartitioningenum-fig03.gif)

### TRIPLE_PANEL_VERTICAL
Window with three panels. The configuration of the panels is vertically.

![](../../../../figures/ifcwindowtypepartitioningenum-fig04.gif)

### TRIPLE_PANEL_BOTTOM
Window with three panels. The configuration of two panels is vertically and the
third one is horizontally at the bottom.

![](../../../../figures/ifcwindowtypepartitioningenum-fig06.gif)

### TRIPLE_PANEL_TOP
Window with three panels. The configuration of two panels is vertically and the
third one is horizontally at the top.

![](../../../../figures/ifcwindowtypepartitioningenum-fig07.gif)

### TRIPLE_PANEL_LEFT
Window with three panels. The configuration of two panels is horizontally and the
third one is vertically at the left hand side.

![](../../../../figures/ifcwindowtypepartitioningenum-fig08.gif)

### TRIPLE_PANEL_RIGHT
Window with three panels. The configuration of two panels is horizontally and the
third one is vertically at the right hand side.

![](../../../../figures/ifcwindowtypepartitioningenum-fig09.gif)

### TRIPLE_PANEL_HORIZONTAL
Window with three panels. The configuration of the panels is horizontally.

![](../../../../figures/ifcwindowtypepartitioningenum-fig05.gif)

### USERDEFINED
User defined operation type.

### NOTDEFINED

