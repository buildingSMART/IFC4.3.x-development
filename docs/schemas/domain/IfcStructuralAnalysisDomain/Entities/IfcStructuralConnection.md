An _IfcStructuralConnection_ represents a structural connection object (node connection, edge connection, or surface connection) or supports.

<!-- end of short definition -->


> HISTORY New entity in IFC2x2.

## Attributes

### AppliedCondition
Optional boundary conditions which define support conditions of this connection object, given in local coordinate directions of the connection object. If left unspecified, the connection object is assumed to have no supports besides being connected with members.

### ConnectsStructuralMembers
References to the IfcRelConnectsStructuralMembers relationship by which structural members can be associated to structural connections.
