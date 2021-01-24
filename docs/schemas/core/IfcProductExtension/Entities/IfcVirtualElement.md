# IfcVirtualElement

A virtual element is a special element used to provide imaginary boundaries, such as between two adjacent, but not separated, spaces. Virtual elements are usually not displayed and does not have quantities and other measures. Therefore _IfcVirtualElement_ does not have material information and quantities attached.

> NOTE&nbsp; The main purpose of _IfcVirtualElement_ is the provision of a virtual space boundary. The _IfcVirtualElement_ may provide the 2D curve or 3D surface representation of the virtual space connection and is referenced by two instances of _IfcRelSpaceBoundary_, each pointing to one of the two adjacent _IfcSpaces_.

The _IfcVirtualElement_ is mainly used to define a virtual boundary between two spaces. Figure 1 describes how to use _IfcRelSpaceBoundary_ in conjunction with _IfcVirtualElement_ to define space boundaries.

!["space boundary"](../../../../../../figures/ifcvirtualelement_spaceboundaries.png "Figure 1 &mdash; Virtual element space boundaries")

> HISTORY&nbsp; New entity in IFC2x2 Addendum.

{ .change-ifc2x3}
> IFC2x2 CHANGE&nbsp; The entity _IfcVirtualElement_ has been added. Upward compatibility for file based exchange is guaranteed.
