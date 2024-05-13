# IfcRelFlowControlElements

This objectified relationship between a distribution flow element occurrence and one-to-many control element occurrences indicates that the control element(s) sense or control some aspect of the flow element. It is applied to _IfcDistributionFlowElement_ and _IfcDistributionControlElement_.<!-- end of definition -->

This relationship may be used to indicate an operational relationship such as an actuator operating a valve, damper, or switch. It may also be used to indicate a sensing relationship such as a sensor detecting conditions of fluid flow.

This relationship implies a sensing or controlling relationship; if elements are merely connected without any control relationship, then _IfcRelConnectsElements_ should be used.

> HISTORY  New entity in IFC2x.
>

## Attributes

### RelatedControlElements
References control elements which may be used to impart control on the Distribution Element.

### RelatingFlowElement
Relationship to a distribution flow element
