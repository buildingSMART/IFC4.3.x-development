# IfcDistributionSystemEnum

This enumeration identifies different types of distribution systems. It is used to designate systems by their function as well as ports of devices within such systems to restrict connectivity to compatible connections.

> HISTORY&nbsp; New enumeration in IFC4.

Ports for cable carriers may be connected using _IfcCableCarrierSegment_ and _IfcCableCarrierFitting_. Type objects for cable carrier segments and fittings (_IfcCableCarrierSegmentType_ and _IfcCableCarrierFittingType_ that are not specific to a particular system type may have ports with _PredefinedType_ of NOTDEFINED which indicates that occurrences of such objects may connect to ports of any other cable-carrier based port. Valid enumerations for cable carriers are the same as that for cables, and may be asserted if ports of the contained cables are all of the same type.
